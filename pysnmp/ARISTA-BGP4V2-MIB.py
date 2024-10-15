# SNMP MIB module (ARISTA-BGP4V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-BGP4V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:16 2024
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

(AristaBgp4V2AddressFamilyIdentifierTC,
 AristaBgp4V2IdentifierTC,
 AristaBgp4V2SubsequentAddressFamilyIdentifierTC) = mibBuilder.importSymbols(
    "ARISTA-BGP4V2-TC-MIB",
    "AristaBgp4V2AddressFamilyIdentifierTC",
    "AristaBgp4V2IdentifierTC",
    "AristaBgp4V2SubsequentAddressFamilyIdentifierTC")

(aristaExperiment,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaExperiment")

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

aristaBgp4V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1)
)
aristaBgp4V2.setRevisions(
        ("2014-08-15 00:00",
         "2012-10-19 00:00",
         "2012-03-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaBgp4V2Notifications_ObjectIdentity = ObjectIdentity
aristaBgp4V2Notifications = _AristaBgp4V2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 0)
)
_AristaBgp4V2Objects_ObjectIdentity = ObjectIdentity
aristaBgp4V2Objects = _AristaBgp4V2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1)
)
_AristaBgp4V2DiscontinuityTable_Object = MibTable
aristaBgp4V2DiscontinuityTable = _AristaBgp4V2DiscontinuityTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2DiscontinuityTable.setStatus("current")
_AristaBgp4V2DiscontinuityEntry_Object = MibTableRow
aristaBgp4V2DiscontinuityEntry = _AristaBgp4V2DiscontinuityEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1)
)
aristaBgp4V2DiscontinuityEntry.setIndexNames(
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"),
)
if mibBuilder.loadTexts:
    aristaBgp4V2DiscontinuityEntry.setStatus("current")
_AristaBgp4V2DiscontinuityTime_Type = TimeStamp
_AristaBgp4V2DiscontinuityTime_Object = MibTableColumn
aristaBgp4V2DiscontinuityTime = _AristaBgp4V2DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1, 1),
    _AristaBgp4V2DiscontinuityTime_Type()
)
aristaBgp4V2DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2DiscontinuityTime.setStatus("current")
_AristaBgp4V2PeerTable_Object = MibTable
aristaBgp4V2PeerTable = _AristaBgp4V2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerTable.setStatus("current")
_AristaBgp4V2PeerEntry_Object = MibTableRow
aristaBgp4V2PeerEntry = _AristaBgp4V2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1)
)
aristaBgp4V2PeerEntry.setIndexNames(
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerEntry.setStatus("current")


class _AristaBgp4V2PeerInstance_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AristaBgp4V2PeerInstance_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerInstance_Object = MibTableColumn
aristaBgp4V2PeerInstance = _AristaBgp4V2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 1),
    _AristaBgp4V2PeerInstance_Type()
)
aristaBgp4V2PeerInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerInstance.setStatus("current")
_AristaBgp4V2PeerLocalAddrType_Type = InetAddressType
_AristaBgp4V2PeerLocalAddrType_Object = MibTableColumn
aristaBgp4V2PeerLocalAddrType = _AristaBgp4V2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 2),
    _AristaBgp4V2PeerLocalAddrType_Type()
)
aristaBgp4V2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLocalAddrType.setStatus("current")
_AristaBgp4V2PeerLocalAddr_Type = InetAddress
_AristaBgp4V2PeerLocalAddr_Object = MibTableColumn
aristaBgp4V2PeerLocalAddr = _AristaBgp4V2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 3),
    _AristaBgp4V2PeerLocalAddr_Type()
)
aristaBgp4V2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLocalAddr.setStatus("current")
_AristaBgp4V2PeerRemoteAddrType_Type = InetAddressType
_AristaBgp4V2PeerRemoteAddrType_Object = MibTableColumn
aristaBgp4V2PeerRemoteAddrType = _AristaBgp4V2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 4),
    _AristaBgp4V2PeerRemoteAddrType_Type()
)
aristaBgp4V2PeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerRemoteAddrType.setStatus("current")
_AristaBgp4V2PeerRemoteAddr_Type = InetAddress
_AristaBgp4V2PeerRemoteAddr_Object = MibTableColumn
aristaBgp4V2PeerRemoteAddr = _AristaBgp4V2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 5),
    _AristaBgp4V2PeerRemoteAddr_Type()
)
aristaBgp4V2PeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerRemoteAddr.setStatus("current")
_AristaBgp4V2PeerLocalPort_Type = InetPortNumber
_AristaBgp4V2PeerLocalPort_Object = MibTableColumn
aristaBgp4V2PeerLocalPort = _AristaBgp4V2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 6),
    _AristaBgp4V2PeerLocalPort_Type()
)
aristaBgp4V2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLocalPort.setStatus("current")
_AristaBgp4V2PeerLocalAs_Type = InetAutonomousSystemNumber
_AristaBgp4V2PeerLocalAs_Object = MibTableColumn
aristaBgp4V2PeerLocalAs = _AristaBgp4V2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 7),
    _AristaBgp4V2PeerLocalAs_Type()
)
aristaBgp4V2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLocalAs.setStatus("current")
_AristaBgp4V2PeerLocalIdentifier_Type = AristaBgp4V2IdentifierTC
_AristaBgp4V2PeerLocalIdentifier_Object = MibTableColumn
aristaBgp4V2PeerLocalIdentifier = _AristaBgp4V2PeerLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 8),
    _AristaBgp4V2PeerLocalIdentifier_Type()
)
aristaBgp4V2PeerLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLocalIdentifier.setStatus("current")
_AristaBgp4V2PeerRemotePort_Type = InetPortNumber
_AristaBgp4V2PeerRemotePort_Object = MibTableColumn
aristaBgp4V2PeerRemotePort = _AristaBgp4V2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 9),
    _AristaBgp4V2PeerRemotePort_Type()
)
aristaBgp4V2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerRemotePort.setStatus("current")
_AristaBgp4V2PeerRemoteAs_Type = InetAutonomousSystemNumber
_AristaBgp4V2PeerRemoteAs_Object = MibTableColumn
aristaBgp4V2PeerRemoteAs = _AristaBgp4V2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 10),
    _AristaBgp4V2PeerRemoteAs_Type()
)
aristaBgp4V2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerRemoteAs.setStatus("current")
_AristaBgp4V2PeerRemoteIdentifier_Type = AristaBgp4V2IdentifierTC
_AristaBgp4V2PeerRemoteIdentifier_Object = MibTableColumn
aristaBgp4V2PeerRemoteIdentifier = _AristaBgp4V2PeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 11),
    _AristaBgp4V2PeerRemoteIdentifier_Type()
)
aristaBgp4V2PeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerRemoteIdentifier.setStatus("current")


class _AristaBgp4V2PeerAdminStatus_Type(Integer32):
    """Custom type aristaBgp4V2PeerAdminStatus based on Integer32"""
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


_AristaBgp4V2PeerAdminStatus_Type.__name__ = "Integer32"
_AristaBgp4V2PeerAdminStatus_Object = MibTableColumn
aristaBgp4V2PeerAdminStatus = _AristaBgp4V2PeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 12),
    _AristaBgp4V2PeerAdminStatus_Type()
)
aristaBgp4V2PeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerAdminStatus.setStatus("current")


class _AristaBgp4V2PeerState_Type(Integer32):
    """Custom type aristaBgp4V2PeerState based on Integer32"""
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


_AristaBgp4V2PeerState_Type.__name__ = "Integer32"
_AristaBgp4V2PeerState_Object = MibTableColumn
aristaBgp4V2PeerState = _AristaBgp4V2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 13),
    _AristaBgp4V2PeerState_Type()
)
aristaBgp4V2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerState.setStatus("current")
_AristaBgp4V2PeerDescription_Type = SnmpAdminString
_AristaBgp4V2PeerDescription_Object = MibTableColumn
aristaBgp4V2PeerDescription = _AristaBgp4V2PeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 14),
    _AristaBgp4V2PeerDescription_Type()
)
aristaBgp4V2PeerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerDescription.setStatus("current")
_AristaBgp4V2PeerErrorsTable_Object = MibTable
aristaBgp4V2PeerErrorsTable = _AristaBgp4V2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerErrorsTable.setStatus("current")
_AristaBgp4V2PeerErrorsEntry_Object = MibTableRow
aristaBgp4V2PeerErrorsEntry = _AristaBgp4V2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerErrorsEntry.setStatus("current")


class _AristaBgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerLastErrorCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaBgp4V2PeerLastErrorCodeReceived_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerLastErrorCodeReceived_Object = MibTableColumn
aristaBgp4V2PeerLastErrorCodeReceived = _AristaBgp4V2PeerLastErrorCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 1),
    _AristaBgp4V2PeerLastErrorCodeReceived_Type()
)
aristaBgp4V2PeerLastErrorCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorCodeReceived.setStatus("current")


class _AristaBgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerLastErrorSubCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaBgp4V2PeerLastErrorSubCodeReceived_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerLastErrorSubCodeReceived_Object = MibTableColumn
aristaBgp4V2PeerLastErrorSubCodeReceived = _AristaBgp4V2PeerLastErrorSubCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 2),
    _AristaBgp4V2PeerLastErrorSubCodeReceived_Type()
)
aristaBgp4V2PeerLastErrorSubCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorSubCodeReceived.setStatus("current")
_AristaBgp4V2PeerLastErrorReceivedTime_Type = TimeStamp
_AristaBgp4V2PeerLastErrorReceivedTime_Object = MibTableColumn
aristaBgp4V2PeerLastErrorReceivedTime = _AristaBgp4V2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 3),
    _AristaBgp4V2PeerLastErrorReceivedTime_Type()
)
aristaBgp4V2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorReceivedTime.setStatus("current")
_AristaBgp4V2PeerLastErrorReceivedText_Type = SnmpAdminString
_AristaBgp4V2PeerLastErrorReceivedText_Object = MibTableColumn
aristaBgp4V2PeerLastErrorReceivedText = _AristaBgp4V2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 4),
    _AristaBgp4V2PeerLastErrorReceivedText_Type()
)
aristaBgp4V2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorReceivedText.setStatus("current")


class _AristaBgp4V2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type aristaBgp4V2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_AristaBgp4V2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_AristaBgp4V2PeerLastErrorReceivedData_Object = MibTableColumn
aristaBgp4V2PeerLastErrorReceivedData = _AristaBgp4V2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 5),
    _AristaBgp4V2PeerLastErrorReceivedData_Type()
)
aristaBgp4V2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorReceivedData.setStatus("current")


class _AristaBgp4V2PeerLastErrorCodeSent_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerLastErrorCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaBgp4V2PeerLastErrorCodeSent_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerLastErrorCodeSent_Object = MibTableColumn
aristaBgp4V2PeerLastErrorCodeSent = _AristaBgp4V2PeerLastErrorCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 6),
    _AristaBgp4V2PeerLastErrorCodeSent_Type()
)
aristaBgp4V2PeerLastErrorCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorCodeSent.setStatus("current")


class _AristaBgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerLastErrorSubCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AristaBgp4V2PeerLastErrorSubCodeSent_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerLastErrorSubCodeSent_Object = MibTableColumn
aristaBgp4V2PeerLastErrorSubCodeSent = _AristaBgp4V2PeerLastErrorSubCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 7),
    _AristaBgp4V2PeerLastErrorSubCodeSent_Type()
)
aristaBgp4V2PeerLastErrorSubCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorSubCodeSent.setStatus("current")
_AristaBgp4V2PeerLastErrorSentTime_Type = TimeStamp
_AristaBgp4V2PeerLastErrorSentTime_Object = MibTableColumn
aristaBgp4V2PeerLastErrorSentTime = _AristaBgp4V2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 8),
    _AristaBgp4V2PeerLastErrorSentTime_Type()
)
aristaBgp4V2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorSentTime.setStatus("current")
_AristaBgp4V2PeerLastErrorSentText_Type = SnmpAdminString
_AristaBgp4V2PeerLastErrorSentText_Object = MibTableColumn
aristaBgp4V2PeerLastErrorSentText = _AristaBgp4V2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 9),
    _AristaBgp4V2PeerLastErrorSentText_Type()
)
aristaBgp4V2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorSentText.setStatus("current")


class _AristaBgp4V2PeerLastErrorSentData_Type(OctetString):
    """Custom type aristaBgp4V2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_AristaBgp4V2PeerLastErrorSentData_Type.__name__ = "OctetString"
_AristaBgp4V2PeerLastErrorSentData_Object = MibTableColumn
aristaBgp4V2PeerLastErrorSentData = _AristaBgp4V2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 10),
    _AristaBgp4V2PeerLastErrorSentData_Type()
)
aristaBgp4V2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerLastErrorSentData.setStatus("current")
_AristaBgp4V2PeerEventTimesTable_Object = MibTable
aristaBgp4V2PeerEventTimesTable = _AristaBgp4V2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerEventTimesTable.setStatus("current")
_AristaBgp4V2PeerEventTimesEntry_Object = MibTableRow
aristaBgp4V2PeerEventTimesEntry = _AristaBgp4V2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerEventTimesEntry.setStatus("current")
_AristaBgp4V2PeerFsmEstablishedTime_Type = Gauge32
_AristaBgp4V2PeerFsmEstablishedTime_Object = MibTableColumn
aristaBgp4V2PeerFsmEstablishedTime = _AristaBgp4V2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1, 1),
    _AristaBgp4V2PeerFsmEstablishedTime_Type()
)
aristaBgp4V2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerFsmEstablishedTime.setUnits("seconds")
_AristaBgp4V2PeerInUpdatesElapsedTime_Type = Gauge32
_AristaBgp4V2PeerInUpdatesElapsedTime_Object = MibTableColumn
aristaBgp4V2PeerInUpdatesElapsedTime = _AristaBgp4V2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1, 2),
    _AristaBgp4V2PeerInUpdatesElapsedTime_Type()
)
aristaBgp4V2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerInUpdatesElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerInUpdatesElapsedTime.setUnits("seconds")
_AristaBgp4V2PeerConfiguredTimersTable_Object = MibTable
aristaBgp4V2PeerConfiguredTimersTable = _AristaBgp4V2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerConfiguredTimersTable.setStatus("current")
_AristaBgp4V2PeerConfiguredTimersEntry_Object = MibTableRow
aristaBgp4V2PeerConfiguredTimersEntry = _AristaBgp4V2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerConfiguredTimersEntry.setStatus("current")


class _AristaBgp4V2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AristaBgp4V2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerConnectRetryInterval_Object = MibTableColumn
aristaBgp4V2PeerConnectRetryInterval = _AristaBgp4V2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 1),
    _AristaBgp4V2PeerConnectRetryInterval_Type()
)
aristaBgp4V2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerConnectRetryInterval.setUnits("seconds")


class _AristaBgp4V2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AristaBgp4V2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerHoldTimeConfigured_Object = MibTableColumn
aristaBgp4V2PeerHoldTimeConfigured = _AristaBgp4V2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 2),
    _AristaBgp4V2PeerHoldTimeConfigured_Type()
)
aristaBgp4V2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerHoldTimeConfigured.setUnits("seconds")


class _AristaBgp4V2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AristaBgp4V2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerKeepAliveConfigured_Object = MibTableColumn
aristaBgp4V2PeerKeepAliveConfigured = _AristaBgp4V2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 3),
    _AristaBgp4V2PeerKeepAliveConfigured_Type()
)
aristaBgp4V2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerKeepAliveConfigured.setUnits("seconds")


class _AristaBgp4V2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaBgp4V2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerMinASOrigInterval_Object = MibTableColumn
aristaBgp4V2PeerMinASOrigInterval = _AristaBgp4V2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 4),
    _AristaBgp4V2PeerMinASOrigInterval_Type()
)
aristaBgp4V2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerMinASOrigInterval.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerMinASOrigInterval.setUnits("seconds")


class _AristaBgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AristaBgp4V2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerMinRouteAdverInterval_Object = MibTableColumn
aristaBgp4V2PeerMinRouteAdverInterval = _AristaBgp4V2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 5),
    _AristaBgp4V2PeerMinRouteAdverInterval_Type()
)
aristaBgp4V2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerMinRouteAdverInterval.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerMinRouteAdverInterval.setUnits("seconds")
_AristaBgp4V2PeerNegotiatedTimersTable_Object = MibTable
aristaBgp4V2PeerNegotiatedTimersTable = _AristaBgp4V2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerNegotiatedTimersTable.setStatus("current")
_AristaBgp4V2PeerNegotiatedTimersEntry_Object = MibTableRow
aristaBgp4V2PeerNegotiatedTimersEntry = _AristaBgp4V2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerNegotiatedTimersEntry.setStatus("current")


class _AristaBgp4V2PeerHoldTime_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_AristaBgp4V2PeerHoldTime_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerHoldTime_Object = MibTableColumn
aristaBgp4V2PeerHoldTime = _AristaBgp4V2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1, 1),
    _AristaBgp4V2PeerHoldTime_Type()
)
aristaBgp4V2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerHoldTime.setUnits("seconds")


class _AristaBgp4V2PeerKeepAlive_Type(Unsigned32):
    """Custom type aristaBgp4V2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_AristaBgp4V2PeerKeepAlive_Type.__name__ = "Unsigned32"
_AristaBgp4V2PeerKeepAlive_Object = MibTableColumn
aristaBgp4V2PeerKeepAlive = _AristaBgp4V2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1, 2),
    _AristaBgp4V2PeerKeepAlive_Type()
)
aristaBgp4V2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerKeepAlive.setUnits("seconds")
_AristaBgp4V2PeerCountersTable_Object = MibTable
aristaBgp4V2PeerCountersTable = _AristaBgp4V2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerCountersTable.setStatus("current")
_AristaBgp4V2PeerCountersEntry_Object = MibTableRow
aristaBgp4V2PeerCountersEntry = _AristaBgp4V2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PeerCountersEntry.setStatus("current")
_AristaBgp4V2PeerInUpdates_Type = Counter32
_AristaBgp4V2PeerInUpdates_Object = MibTableColumn
aristaBgp4V2PeerInUpdates = _AristaBgp4V2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 1),
    _AristaBgp4V2PeerInUpdates_Type()
)
aristaBgp4V2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerInUpdates.setStatus("current")
_AristaBgp4V2PeerOutUpdates_Type = Counter32
_AristaBgp4V2PeerOutUpdates_Object = MibTableColumn
aristaBgp4V2PeerOutUpdates = _AristaBgp4V2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 2),
    _AristaBgp4V2PeerOutUpdates_Type()
)
aristaBgp4V2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerOutUpdates.setStatus("current")
_AristaBgp4V2PeerInTotalMessages_Type = Counter32
_AristaBgp4V2PeerInTotalMessages_Object = MibTableColumn
aristaBgp4V2PeerInTotalMessages = _AristaBgp4V2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 3),
    _AristaBgp4V2PeerInTotalMessages_Type()
)
aristaBgp4V2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerInTotalMessages.setStatus("current")
_AristaBgp4V2PeerOutTotalMessages_Type = Counter32
_AristaBgp4V2PeerOutTotalMessages_Object = MibTableColumn
aristaBgp4V2PeerOutTotalMessages = _AristaBgp4V2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 4),
    _AristaBgp4V2PeerOutTotalMessages_Type()
)
aristaBgp4V2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerOutTotalMessages.setStatus("current")
_AristaBgp4V2PeerFsmEstablishedTransitions_Type = Counter32
_AristaBgp4V2PeerFsmEstablishedTransitions_Object = MibTableColumn
aristaBgp4V2PeerFsmEstablishedTransitions = _AristaBgp4V2PeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 5),
    _AristaBgp4V2PeerFsmEstablishedTransitions_Type()
)
aristaBgp4V2PeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PeerFsmEstablishedTransitions.setStatus("current")
_AristaBgp4V2PrefixGaugesTable_Object = MibTable
aristaBgp4V2PrefixGaugesTable = _AristaBgp4V2PrefixGaugesTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixGaugesTable.setStatus("current")
_AristaBgp4V2PrefixGaugesEntry_Object = MibTableRow
aristaBgp4V2PrefixGaugesEntry = _AristaBgp4V2PrefixGaugesEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1)
)
aristaBgp4V2PrefixGaugesEntry.setIndexNames(
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixGaugesAfi"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixGaugesSafi"),
)
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixGaugesEntry.setStatus("current")
_AristaBgp4V2PrefixGaugesAfi_Type = AristaBgp4V2AddressFamilyIdentifierTC
_AristaBgp4V2PrefixGaugesAfi_Object = MibTableColumn
aristaBgp4V2PrefixGaugesAfi = _AristaBgp4V2PrefixGaugesAfi_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 1),
    _AristaBgp4V2PrefixGaugesAfi_Type()
)
aristaBgp4V2PrefixGaugesAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixGaugesAfi.setStatus("current")
_AristaBgp4V2PrefixGaugesSafi_Type = AristaBgp4V2SubsequentAddressFamilyIdentifierTC
_AristaBgp4V2PrefixGaugesSafi_Object = MibTableColumn
aristaBgp4V2PrefixGaugesSafi = _AristaBgp4V2PrefixGaugesSafi_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 2),
    _AristaBgp4V2PrefixGaugesSafi_Type()
)
aristaBgp4V2PrefixGaugesSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixGaugesSafi.setStatus("current")
_AristaBgp4V2PrefixInPrefixes_Type = Gauge32
_AristaBgp4V2PrefixInPrefixes_Object = MibTableColumn
aristaBgp4V2PrefixInPrefixes = _AristaBgp4V2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 3),
    _AristaBgp4V2PrefixInPrefixes_Type()
)
aristaBgp4V2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixInPrefixes.setStatus("current")
_AristaBgp4V2PrefixInPrefixesAccepted_Type = Gauge32
_AristaBgp4V2PrefixInPrefixesAccepted_Object = MibTableColumn
aristaBgp4V2PrefixInPrefixesAccepted = _AristaBgp4V2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 4),
    _AristaBgp4V2PrefixInPrefixesAccepted_Type()
)
aristaBgp4V2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixInPrefixesAccepted.setStatus("current")
_AristaBgp4V2PrefixOutPrefixes_Type = Gauge32
_AristaBgp4V2PrefixOutPrefixes_Object = MibTableColumn
aristaBgp4V2PrefixOutPrefixes = _AristaBgp4V2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 5),
    _AristaBgp4V2PrefixOutPrefixes_Type()
)
aristaBgp4V2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2PrefixOutPrefixes.setStatus("current")
_AristaBgp4V2NlriTable_Object = MibTable
aristaBgp4V2NlriTable = _AristaBgp4V2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    aristaBgp4V2NlriTable.setStatus("current")
_AristaBgp4V2NlriEntry_Object = MibTableRow
aristaBgp4V2NlriEntry = _AristaBgp4V2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1)
)
aristaBgp4V2NlriEntry.setIndexNames(
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAfi"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriSafi"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefix"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixLen"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriIndex"),
)
if mibBuilder.loadTexts:
    aristaBgp4V2NlriEntry.setStatus("current")


class _AristaBgp4V2NlriIndex_Type(Unsigned32):
    """Custom type aristaBgp4V2NlriIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AristaBgp4V2NlriIndex_Type.__name__ = "Unsigned32"
_AristaBgp4V2NlriIndex_Object = MibTableColumn
aristaBgp4V2NlriIndex = _AristaBgp4V2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 1),
    _AristaBgp4V2NlriIndex_Type()
)
aristaBgp4V2NlriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriIndex.setStatus("current")
_AristaBgp4V2NlriAfi_Type = AristaBgp4V2AddressFamilyIdentifierTC
_AristaBgp4V2NlriAfi_Object = MibTableColumn
aristaBgp4V2NlriAfi = _AristaBgp4V2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 2),
    _AristaBgp4V2NlriAfi_Type()
)
aristaBgp4V2NlriAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAfi.setStatus("current")
_AristaBgp4V2NlriSafi_Type = AristaBgp4V2SubsequentAddressFamilyIdentifierTC
_AristaBgp4V2NlriSafi_Object = MibTableColumn
aristaBgp4V2NlriSafi = _AristaBgp4V2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 3),
    _AristaBgp4V2NlriSafi_Type()
)
aristaBgp4V2NlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriSafi.setStatus("current")
_AristaBgp4V2NlriPrefixType_Type = InetAddressType
_AristaBgp4V2NlriPrefixType_Object = MibTableColumn
aristaBgp4V2NlriPrefixType = _AristaBgp4V2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 4),
    _AristaBgp4V2NlriPrefixType_Type()
)
aristaBgp4V2NlriPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriPrefixType.setStatus("current")
_AristaBgp4V2NlriPrefix_Type = InetAddress
_AristaBgp4V2NlriPrefix_Object = MibTableColumn
aristaBgp4V2NlriPrefix = _AristaBgp4V2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 5),
    _AristaBgp4V2NlriPrefix_Type()
)
aristaBgp4V2NlriPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriPrefix.setStatus("current")
_AristaBgp4V2NlriPrefixLen_Type = InetAddressPrefixLength
_AristaBgp4V2NlriPrefixLen_Object = MibTableColumn
aristaBgp4V2NlriPrefixLen = _AristaBgp4V2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 6),
    _AristaBgp4V2NlriPrefixLen_Type()
)
aristaBgp4V2NlriPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriPrefixLen.setStatus("current")
_AristaBgp4V2NlriBest_Type = TruthValue
_AristaBgp4V2NlriBest_Object = MibTableColumn
aristaBgp4V2NlriBest = _AristaBgp4V2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 7),
    _AristaBgp4V2NlriBest_Type()
)
aristaBgp4V2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriBest.setStatus("current")
_AristaBgp4V2NlriCalcLocalPref_Type = Unsigned32
_AristaBgp4V2NlriCalcLocalPref_Object = MibTableColumn
aristaBgp4V2NlriCalcLocalPref = _AristaBgp4V2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 8),
    _AristaBgp4V2NlriCalcLocalPref_Type()
)
aristaBgp4V2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriCalcLocalPref.setStatus("current")


class _AristaBgp4V2NlriOrigin_Type(Integer32):
    """Custom type aristaBgp4V2NlriOrigin based on Integer32"""
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


_AristaBgp4V2NlriOrigin_Type.__name__ = "Integer32"
_AristaBgp4V2NlriOrigin_Object = MibTableColumn
aristaBgp4V2NlriOrigin = _AristaBgp4V2NlriOrigin_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 9),
    _AristaBgp4V2NlriOrigin_Type()
)
aristaBgp4V2NlriOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriOrigin.setStatus("current")
_AristaBgp4V2NlriNextHopAddrType_Type = InetAddressType
_AristaBgp4V2NlriNextHopAddrType_Object = MibTableColumn
aristaBgp4V2NlriNextHopAddrType = _AristaBgp4V2NlriNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 10),
    _AristaBgp4V2NlriNextHopAddrType_Type()
)
aristaBgp4V2NlriNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriNextHopAddrType.setStatus("current")


class _AristaBgp4V2NlriNextHopAddr_Type(InetAddress):
    """Custom type aristaBgp4V2NlriNextHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_AristaBgp4V2NlriNextHopAddr_Type.__name__ = "InetAddress"
_AristaBgp4V2NlriNextHopAddr_Object = MibTableColumn
aristaBgp4V2NlriNextHopAddr = _AristaBgp4V2NlriNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 11),
    _AristaBgp4V2NlriNextHopAddr_Type()
)
aristaBgp4V2NlriNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriNextHopAddr.setStatus("current")
_AristaBgp4V2NlriLinkLocalNextHopAddrType_Type = InetAddressType
_AristaBgp4V2NlriLinkLocalNextHopAddrType_Object = MibTableColumn
aristaBgp4V2NlriLinkLocalNextHopAddrType = _AristaBgp4V2NlriLinkLocalNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 12),
    _AristaBgp4V2NlriLinkLocalNextHopAddrType_Type()
)
aristaBgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriLinkLocalNextHopAddrType.setStatus("current")
_AristaBgp4V2NlriLinkLocalNextHopAddr_Type = InetAddress
_AristaBgp4V2NlriLinkLocalNextHopAddr_Object = MibTableColumn
aristaBgp4V2NlriLinkLocalNextHopAddr = _AristaBgp4V2NlriLinkLocalNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 13),
    _AristaBgp4V2NlriLinkLocalNextHopAddr_Type()
)
aristaBgp4V2NlriLinkLocalNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriLinkLocalNextHopAddr.setStatus("current")
_AristaBgp4V2NlriLocalPrefPresent_Type = TruthValue
_AristaBgp4V2NlriLocalPrefPresent_Object = MibTableColumn
aristaBgp4V2NlriLocalPrefPresent = _AristaBgp4V2NlriLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 14),
    _AristaBgp4V2NlriLocalPrefPresent_Type()
)
aristaBgp4V2NlriLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriLocalPrefPresent.setStatus("current")
_AristaBgp4V2NlriLocalPref_Type = Unsigned32
_AristaBgp4V2NlriLocalPref_Object = MibTableColumn
aristaBgp4V2NlriLocalPref = _AristaBgp4V2NlriLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 15),
    _AristaBgp4V2NlriLocalPref_Type()
)
aristaBgp4V2NlriLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriLocalPref.setStatus("current")
_AristaBgp4V2NlriMedPresent_Type = TruthValue
_AristaBgp4V2NlriMedPresent_Object = MibTableColumn
aristaBgp4V2NlriMedPresent = _AristaBgp4V2NlriMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 16),
    _AristaBgp4V2NlriMedPresent_Type()
)
aristaBgp4V2NlriMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriMedPresent.setStatus("current")
_AristaBgp4V2NlriMed_Type = Unsigned32
_AristaBgp4V2NlriMed_Object = MibTableColumn
aristaBgp4V2NlriMed = _AristaBgp4V2NlriMed_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 17),
    _AristaBgp4V2NlriMed_Type()
)
aristaBgp4V2NlriMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriMed.setStatus("current")
_AristaBgp4V2NlriAtomicAggregate_Type = TruthValue
_AristaBgp4V2NlriAtomicAggregate_Object = MibTableColumn
aristaBgp4V2NlriAtomicAggregate = _AristaBgp4V2NlriAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 18),
    _AristaBgp4V2NlriAtomicAggregate_Type()
)
aristaBgp4V2NlriAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAtomicAggregate.setStatus("current")
_AristaBgp4V2NlriAggregatorPresent_Type = TruthValue
_AristaBgp4V2NlriAggregatorPresent_Object = MibTableColumn
aristaBgp4V2NlriAggregatorPresent = _AristaBgp4V2NlriAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 19),
    _AristaBgp4V2NlriAggregatorPresent_Type()
)
aristaBgp4V2NlriAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAggregatorPresent.setStatus("current")
_AristaBgp4V2NlriAggregatorAS_Type = InetAutonomousSystemNumber
_AristaBgp4V2NlriAggregatorAS_Object = MibTableColumn
aristaBgp4V2NlriAggregatorAS = _AristaBgp4V2NlriAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 20),
    _AristaBgp4V2NlriAggregatorAS_Type()
)
aristaBgp4V2NlriAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAggregatorAS.setStatus("current")
_AristaBgp4V2NlriAggregatorAddr_Type = AristaBgp4V2IdentifierTC
_AristaBgp4V2NlriAggregatorAddr_Object = MibTableColumn
aristaBgp4V2NlriAggregatorAddr = _AristaBgp4V2NlriAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 21),
    _AristaBgp4V2NlriAggregatorAddr_Type()
)
aristaBgp4V2NlriAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAggregatorAddr.setStatus("current")
_AristaBgp4V2NlriAsPathCalcLength_Type = Unsigned32
_AristaBgp4V2NlriAsPathCalcLength_Object = MibTableColumn
aristaBgp4V2NlriAsPathCalcLength = _AristaBgp4V2NlriAsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 22),
    _AristaBgp4V2NlriAsPathCalcLength_Type()
)
aristaBgp4V2NlriAsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAsPathCalcLength.setStatus("current")
_AristaBgp4V2NlriAsPathString_Type = SnmpAdminString
_AristaBgp4V2NlriAsPathString_Object = MibTableColumn
aristaBgp4V2NlriAsPathString = _AristaBgp4V2NlriAsPathString_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 23),
    _AristaBgp4V2NlriAsPathString_Type()
)
aristaBgp4V2NlriAsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAsPathString.setStatus("current")


class _AristaBgp4V2NlriAsPath_Type(OctetString):
    """Custom type aristaBgp4V2NlriAsPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4072),
    )


_AristaBgp4V2NlriAsPath_Type.__name__ = "OctetString"
_AristaBgp4V2NlriAsPath_Object = MibTableColumn
aristaBgp4V2NlriAsPath = _AristaBgp4V2NlriAsPath_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 24),
    _AristaBgp4V2NlriAsPath_Type()
)
aristaBgp4V2NlriAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriAsPath.setStatus("current")


class _AristaBgp4V2NlriPathAttrUnknown_Type(OctetString):
    """Custom type aristaBgp4V2NlriPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4072),
    )


_AristaBgp4V2NlriPathAttrUnknown_Type.__name__ = "OctetString"
_AristaBgp4V2NlriPathAttrUnknown_Object = MibTableColumn
aristaBgp4V2NlriPathAttrUnknown = _AristaBgp4V2NlriPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 25),
    _AristaBgp4V2NlriPathAttrUnknown_Type()
)
aristaBgp4V2NlriPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2NlriPathAttrUnknown.setStatus("current")
_AristaBgp4V2AdjRibsOutTable_Object = MibTable
aristaBgp4V2AdjRibsOutTable = _AristaBgp4V2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    aristaBgp4V2AdjRibsOutTable.setStatus("current")
_AristaBgp4V2AdjRibsOutEntry_Object = MibTableRow
aristaBgp4V2AdjRibsOutEntry = _AristaBgp4V2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1)
)
aristaBgp4V2AdjRibsOutEntry.setIndexNames(
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAfi"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriSafi"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefix"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixLen"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"),
    (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    aristaBgp4V2AdjRibsOutEntry.setStatus("current")


class _AristaBgp4V2AdjRibsOutIndex_Type(Unsigned32):
    """Custom type aristaBgp4V2AdjRibsOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AristaBgp4V2AdjRibsOutIndex_Type.__name__ = "Unsigned32"
_AristaBgp4V2AdjRibsOutIndex_Object = MibTableColumn
aristaBgp4V2AdjRibsOutIndex = _AristaBgp4V2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1, 1),
    _AristaBgp4V2AdjRibsOutIndex_Type()
)
aristaBgp4V2AdjRibsOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaBgp4V2AdjRibsOutIndex.setStatus("current")
_AristaBgp4V2AdjRibsOutRoute_Type = RowPointer
_AristaBgp4V2AdjRibsOutRoute_Object = MibTableColumn
aristaBgp4V2AdjRibsOutRoute = _AristaBgp4V2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1, 2),
    _AristaBgp4V2AdjRibsOutRoute_Type()
)
aristaBgp4V2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaBgp4V2AdjRibsOutRoute.setStatus("current")
_AristaBgp4V2Conformance_ObjectIdentity = ObjectIdentity
aristaBgp4V2Conformance = _AristaBgp4V2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2)
)
_AristaBgp4V2Compliances_ObjectIdentity = ObjectIdentity
aristaBgp4V2Compliances = _AristaBgp4V2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 1)
)
_AristaBgp4V2Groups_ObjectIdentity = ObjectIdentity
aristaBgp4V2Groups = _AristaBgp4V2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2)
)
aristaBgp4V2PeerEntry.registerAugmentions(
    ("ARISTA-BGP4V2-MIB",
     "aristaBgp4V2PeerErrorsEntry")
)
aristaBgp4V2PeerErrorsEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions(
    ("ARISTA-BGP4V2-MIB",
     "aristaBgp4V2PeerEventTimesEntry")
)
aristaBgp4V2PeerEventTimesEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions(
    ("ARISTA-BGP4V2-MIB",
     "aristaBgp4V2PeerConfiguredTimersEntry")
)
aristaBgp4V2PeerConfiguredTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions(
    ("ARISTA-BGP4V2-MIB",
     "aristaBgp4V2PeerNegotiatedTimersEntry")
)
aristaBgp4V2PeerNegotiatedTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions(
    ("ARISTA-BGP4V2-MIB",
     "aristaBgp4V2PeerCountersEntry")
)
aristaBgp4V2PeerCountersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())

# Managed Objects groups

aristaBgp4V2GlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 1)
)
aristaBgp4V2GlobalsGroup.setObjects(
    ("ARISTA-BGP4V2-MIB", "aristaBgp4V2DiscontinuityTime")
)
if mibBuilder.loadTexts:
    aristaBgp4V2GlobalsGroup.setStatus("current")

aristaBgp4V2StdMIBTimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 2)
)
aristaBgp4V2StdMIBTimersGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerFsmEstablishedTime"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInUpdatesElapsedTime"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerConnectRetryInterval"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerHoldTimeConfigured"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerKeepAliveConfigured"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerMinASOrigInterval"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerMinRouteAdverInterval"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerHoldTime"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBTimersGroup.setStatus("current")

aristaBgp4V2StdMIBCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 3)
)
aristaBgp4V2StdMIBCountersGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInUpdates"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerOutUpdates"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInTotalMessages"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerOutTotalMessages"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerFsmEstablishedTransitions"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixInPrefixes"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixInPrefixesAccepted"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixOutPrefixes"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBCountersGroup.setStatus("current")

aristaBgp4V2StdMIBErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 5)
)
aristaBgp4V2StdMIBErrorsGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeReceived"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeReceived"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedData"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedTime"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedText"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeSent"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeSent"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentData"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentTime"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBErrorsGroup.setStatus("current")

aristaBgp4V2StdMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 6)
)
aristaBgp4V2StdMIBPeerGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerAdminStatus"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAddrType"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAddr"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAs"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAs"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalIdentifier"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteIdentifier"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerDescription"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBPeerGroup.setStatus("current")

aristaBgp4V2StdMIBNlriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 7)
)
aristaBgp4V2StdMIBNlriGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPathCalcLength"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPathString"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriBest"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriCalcLocalPref"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2AdjRibsOutRoute"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorPresent"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorAS"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorAddr"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAtomicAggregate"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLocalPref"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLocalPrefPresent"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriMed"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriMedPresent"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriNextHopAddr"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriNextHopAddrType"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLinkLocalNextHopAddrType"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLinkLocalNextHopAddr"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriOrigin"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPath"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPathAttrUnknown"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBNlriGroup.setStatus("current")


# Notification objects

aristaBgp4V2EstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 0, 1)
)
aristaBgp4V2EstablishedNotification.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2EstablishedNotification.setStatus(
        "current"
    )

aristaBgp4V2BackwardTransitionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 0, 2)
)
aristaBgp4V2BackwardTransitionNotification.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeReceived"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeReceived"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedText"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2BackwardTransitionNotification.setStatus(
        "current"
    )


# Notifications groups

aristaBgp4V2StdMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 8)
)
aristaBgp4V2StdMIBNotificationGroup.setObjects(
      *(("ARISTA-BGP4V2-MIB", "aristaBgp4V2EstablishedNotification"),
        ("ARISTA-BGP4V2-MIB", "aristaBgp4V2BackwardTransitionNotification"))
)
if mibBuilder.loadTexts:
    aristaBgp4V2StdMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aristaBgp4V2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    aristaBgp4V2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-BGP4V2-MIB",
    **{"aristaBgp4V2": aristaBgp4V2,
       "aristaBgp4V2Notifications": aristaBgp4V2Notifications,
       "aristaBgp4V2EstablishedNotification": aristaBgp4V2EstablishedNotification,
       "aristaBgp4V2BackwardTransitionNotification": aristaBgp4V2BackwardTransitionNotification,
       "aristaBgp4V2Objects": aristaBgp4V2Objects,
       "aristaBgp4V2DiscontinuityTable": aristaBgp4V2DiscontinuityTable,
       "aristaBgp4V2DiscontinuityEntry": aristaBgp4V2DiscontinuityEntry,
       "aristaBgp4V2DiscontinuityTime": aristaBgp4V2DiscontinuityTime,
       "aristaBgp4V2PeerTable": aristaBgp4V2PeerTable,
       "aristaBgp4V2PeerEntry": aristaBgp4V2PeerEntry,
       "aristaBgp4V2PeerInstance": aristaBgp4V2PeerInstance,
       "aristaBgp4V2PeerLocalAddrType": aristaBgp4V2PeerLocalAddrType,
       "aristaBgp4V2PeerLocalAddr": aristaBgp4V2PeerLocalAddr,
       "aristaBgp4V2PeerRemoteAddrType": aristaBgp4V2PeerRemoteAddrType,
       "aristaBgp4V2PeerRemoteAddr": aristaBgp4V2PeerRemoteAddr,
       "aristaBgp4V2PeerLocalPort": aristaBgp4V2PeerLocalPort,
       "aristaBgp4V2PeerLocalAs": aristaBgp4V2PeerLocalAs,
       "aristaBgp4V2PeerLocalIdentifier": aristaBgp4V2PeerLocalIdentifier,
       "aristaBgp4V2PeerRemotePort": aristaBgp4V2PeerRemotePort,
       "aristaBgp4V2PeerRemoteAs": aristaBgp4V2PeerRemoteAs,
       "aristaBgp4V2PeerRemoteIdentifier": aristaBgp4V2PeerRemoteIdentifier,
       "aristaBgp4V2PeerAdminStatus": aristaBgp4V2PeerAdminStatus,
       "aristaBgp4V2PeerState": aristaBgp4V2PeerState,
       "aristaBgp4V2PeerDescription": aristaBgp4V2PeerDescription,
       "aristaBgp4V2PeerErrorsTable": aristaBgp4V2PeerErrorsTable,
       "aristaBgp4V2PeerErrorsEntry": aristaBgp4V2PeerErrorsEntry,
       "aristaBgp4V2PeerLastErrorCodeReceived": aristaBgp4V2PeerLastErrorCodeReceived,
       "aristaBgp4V2PeerLastErrorSubCodeReceived": aristaBgp4V2PeerLastErrorSubCodeReceived,
       "aristaBgp4V2PeerLastErrorReceivedTime": aristaBgp4V2PeerLastErrorReceivedTime,
       "aristaBgp4V2PeerLastErrorReceivedText": aristaBgp4V2PeerLastErrorReceivedText,
       "aristaBgp4V2PeerLastErrorReceivedData": aristaBgp4V2PeerLastErrorReceivedData,
       "aristaBgp4V2PeerLastErrorCodeSent": aristaBgp4V2PeerLastErrorCodeSent,
       "aristaBgp4V2PeerLastErrorSubCodeSent": aristaBgp4V2PeerLastErrorSubCodeSent,
       "aristaBgp4V2PeerLastErrorSentTime": aristaBgp4V2PeerLastErrorSentTime,
       "aristaBgp4V2PeerLastErrorSentText": aristaBgp4V2PeerLastErrorSentText,
       "aristaBgp4V2PeerLastErrorSentData": aristaBgp4V2PeerLastErrorSentData,
       "aristaBgp4V2PeerEventTimesTable": aristaBgp4V2PeerEventTimesTable,
       "aristaBgp4V2PeerEventTimesEntry": aristaBgp4V2PeerEventTimesEntry,
       "aristaBgp4V2PeerFsmEstablishedTime": aristaBgp4V2PeerFsmEstablishedTime,
       "aristaBgp4V2PeerInUpdatesElapsedTime": aristaBgp4V2PeerInUpdatesElapsedTime,
       "aristaBgp4V2PeerConfiguredTimersTable": aristaBgp4V2PeerConfiguredTimersTable,
       "aristaBgp4V2PeerConfiguredTimersEntry": aristaBgp4V2PeerConfiguredTimersEntry,
       "aristaBgp4V2PeerConnectRetryInterval": aristaBgp4V2PeerConnectRetryInterval,
       "aristaBgp4V2PeerHoldTimeConfigured": aristaBgp4V2PeerHoldTimeConfigured,
       "aristaBgp4V2PeerKeepAliveConfigured": aristaBgp4V2PeerKeepAliveConfigured,
       "aristaBgp4V2PeerMinASOrigInterval": aristaBgp4V2PeerMinASOrigInterval,
       "aristaBgp4V2PeerMinRouteAdverInterval": aristaBgp4V2PeerMinRouteAdverInterval,
       "aristaBgp4V2PeerNegotiatedTimersTable": aristaBgp4V2PeerNegotiatedTimersTable,
       "aristaBgp4V2PeerNegotiatedTimersEntry": aristaBgp4V2PeerNegotiatedTimersEntry,
       "aristaBgp4V2PeerHoldTime": aristaBgp4V2PeerHoldTime,
       "aristaBgp4V2PeerKeepAlive": aristaBgp4V2PeerKeepAlive,
       "aristaBgp4V2PeerCountersTable": aristaBgp4V2PeerCountersTable,
       "aristaBgp4V2PeerCountersEntry": aristaBgp4V2PeerCountersEntry,
       "aristaBgp4V2PeerInUpdates": aristaBgp4V2PeerInUpdates,
       "aristaBgp4V2PeerOutUpdates": aristaBgp4V2PeerOutUpdates,
       "aristaBgp4V2PeerInTotalMessages": aristaBgp4V2PeerInTotalMessages,
       "aristaBgp4V2PeerOutTotalMessages": aristaBgp4V2PeerOutTotalMessages,
       "aristaBgp4V2PeerFsmEstablishedTransitions": aristaBgp4V2PeerFsmEstablishedTransitions,
       "aristaBgp4V2PrefixGaugesTable": aristaBgp4V2PrefixGaugesTable,
       "aristaBgp4V2PrefixGaugesEntry": aristaBgp4V2PrefixGaugesEntry,
       "aristaBgp4V2PrefixGaugesAfi": aristaBgp4V2PrefixGaugesAfi,
       "aristaBgp4V2PrefixGaugesSafi": aristaBgp4V2PrefixGaugesSafi,
       "aristaBgp4V2PrefixInPrefixes": aristaBgp4V2PrefixInPrefixes,
       "aristaBgp4V2PrefixInPrefixesAccepted": aristaBgp4V2PrefixInPrefixesAccepted,
       "aristaBgp4V2PrefixOutPrefixes": aristaBgp4V2PrefixOutPrefixes,
       "aristaBgp4V2NlriTable": aristaBgp4V2NlriTable,
       "aristaBgp4V2NlriEntry": aristaBgp4V2NlriEntry,
       "aristaBgp4V2NlriIndex": aristaBgp4V2NlriIndex,
       "aristaBgp4V2NlriAfi": aristaBgp4V2NlriAfi,
       "aristaBgp4V2NlriSafi": aristaBgp4V2NlriSafi,
       "aristaBgp4V2NlriPrefixType": aristaBgp4V2NlriPrefixType,
       "aristaBgp4V2NlriPrefix": aristaBgp4V2NlriPrefix,
       "aristaBgp4V2NlriPrefixLen": aristaBgp4V2NlriPrefixLen,
       "aristaBgp4V2NlriBest": aristaBgp4V2NlriBest,
       "aristaBgp4V2NlriCalcLocalPref": aristaBgp4V2NlriCalcLocalPref,
       "aristaBgp4V2NlriOrigin": aristaBgp4V2NlriOrigin,
       "aristaBgp4V2NlriNextHopAddrType": aristaBgp4V2NlriNextHopAddrType,
       "aristaBgp4V2NlriNextHopAddr": aristaBgp4V2NlriNextHopAddr,
       "aristaBgp4V2NlriLinkLocalNextHopAddrType": aristaBgp4V2NlriLinkLocalNextHopAddrType,
       "aristaBgp4V2NlriLinkLocalNextHopAddr": aristaBgp4V2NlriLinkLocalNextHopAddr,
       "aristaBgp4V2NlriLocalPrefPresent": aristaBgp4V2NlriLocalPrefPresent,
       "aristaBgp4V2NlriLocalPref": aristaBgp4V2NlriLocalPref,
       "aristaBgp4V2NlriMedPresent": aristaBgp4V2NlriMedPresent,
       "aristaBgp4V2NlriMed": aristaBgp4V2NlriMed,
       "aristaBgp4V2NlriAtomicAggregate": aristaBgp4V2NlriAtomicAggregate,
       "aristaBgp4V2NlriAggregatorPresent": aristaBgp4V2NlriAggregatorPresent,
       "aristaBgp4V2NlriAggregatorAS": aristaBgp4V2NlriAggregatorAS,
       "aristaBgp4V2NlriAggregatorAddr": aristaBgp4V2NlriAggregatorAddr,
       "aristaBgp4V2NlriAsPathCalcLength": aristaBgp4V2NlriAsPathCalcLength,
       "aristaBgp4V2NlriAsPathString": aristaBgp4V2NlriAsPathString,
       "aristaBgp4V2NlriAsPath": aristaBgp4V2NlriAsPath,
       "aristaBgp4V2NlriPathAttrUnknown": aristaBgp4V2NlriPathAttrUnknown,
       "aristaBgp4V2AdjRibsOutTable": aristaBgp4V2AdjRibsOutTable,
       "aristaBgp4V2AdjRibsOutEntry": aristaBgp4V2AdjRibsOutEntry,
       "aristaBgp4V2AdjRibsOutIndex": aristaBgp4V2AdjRibsOutIndex,
       "aristaBgp4V2AdjRibsOutRoute": aristaBgp4V2AdjRibsOutRoute,
       "aristaBgp4V2Conformance": aristaBgp4V2Conformance,
       "aristaBgp4V2Compliances": aristaBgp4V2Compliances,
       "aristaBgp4V2Compliance": aristaBgp4V2Compliance,
       "aristaBgp4V2Groups": aristaBgp4V2Groups,
       "aristaBgp4V2GlobalsGroup": aristaBgp4V2GlobalsGroup,
       "aristaBgp4V2StdMIBTimersGroup": aristaBgp4V2StdMIBTimersGroup,
       "aristaBgp4V2StdMIBCountersGroup": aristaBgp4V2StdMIBCountersGroup,
       "aristaBgp4V2StdMIBErrorsGroup": aristaBgp4V2StdMIBErrorsGroup,
       "aristaBgp4V2StdMIBPeerGroup": aristaBgp4V2StdMIBPeerGroup,
       "aristaBgp4V2StdMIBNlriGroup": aristaBgp4V2StdMIBNlriGroup,
       "aristaBgp4V2StdMIBNotificationGroup": aristaBgp4V2StdMIBNotificationGroup}
)
