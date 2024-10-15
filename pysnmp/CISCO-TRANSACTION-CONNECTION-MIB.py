# SNMP MIB module (CISCO-TRANSACTION-CONNECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRANSACTION-CONNECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoTransactionConnectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144)
)
ciscoTransactionConnectionMIB.setRevisions(
        ("2005-12-22 00:00",
         "1999-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTransConnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTransConnMIBObjects = _CiscoTransConnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1)
)
_CtcLicense_ObjectIdentity = ObjectIdentity
ctcLicense = _CtcLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1)
)
if mibBuilder.loadTexts:
    ctcLicense.setStatus("current")


class _CtcLicenseState_Type(Integer32):
    """Custom type ctcLicenseState based on Integer32"""
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
        *(("badKey", 3),
          ("expired", 5),
          ("licenseOK", 4),
          ("notValidatedYet", 2),
          ("unconfigured", 1))
    )


_CtcLicenseState_Type.__name__ = "Integer32"
_CtcLicenseState_Object = MibScalar
ctcLicenseState = _CtcLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1, 1),
    _CtcLicenseState_Type()
)
ctcLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcLicenseState.setStatus("current")


class _CtcLicenseKey_Type(OctetString):
    """Custom type ctcLicenseKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CtcLicenseKey_Type.__name__ = "OctetString"
_CtcLicenseKey_Object = MibScalar
ctcLicenseKey = _CtcLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1, 2),
    _CtcLicenseKey_Type()
)
ctcLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcLicenseKey.setStatus("current")
_CtcLicenseMaxConn_Type = Unsigned32
_CtcLicenseMaxConn_Object = MibScalar
ctcLicenseMaxConn = _CtcLicenseMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1, 3),
    _CtcLicenseMaxConn_Type()
)
ctcLicenseMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcLicenseMaxConn.setStatus("current")
_CtcLicenseCurrConn_Type = Unsigned32
_CtcLicenseCurrConn_Object = MibScalar
ctcLicenseCurrConn = _CtcLicenseCurrConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1, 4),
    _CtcLicenseCurrConn_Type()
)
ctcLicenseCurrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcLicenseCurrConn.setStatus("current")
_CtcLicenseExpiration_Type = DateAndTime
_CtcLicenseExpiration_Object = MibScalar
ctcLicenseExpiration = _CtcLicenseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 1, 5),
    _CtcLicenseExpiration_Type()
)
ctcLicenseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcLicenseExpiration.setStatus("current")
_CtcDestinationTable_Object = MibTable
ctcDestinationTable = _CtcDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2)
)
if mibBuilder.loadTexts:
    ctcDestinationTable.setStatus("current")
_CtcDestinationEntry_Object = MibTableRow
ctcDestinationEntry = _CtcDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2, 1)
)
ctcDestinationEntry.setIndexNames(
    (0, "CISCO-TRANSACTION-CONNECTION-MIB", "ctcDestinationName"),
)
if mibBuilder.loadTexts:
    ctcDestinationEntry.setStatus("current")


class _CtcDestinationName_Type(SnmpAdminString):
    """Custom type ctcDestinationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcDestinationName_Type.__name__ = "SnmpAdminString"
_CtcDestinationName_Object = MibTableColumn
ctcDestinationName = _CtcDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2, 1, 1),
    _CtcDestinationName_Type()
)
ctcDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcDestinationName.setStatus("current")


class _CtcDestinationRemoteLUName_Type(SnmpAdminString):
    """Custom type ctcDestinationRemoteLUName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CtcDestinationRemoteLUName_Type.__name__ = "SnmpAdminString"
_CtcDestinationRemoteLUName_Object = MibTableColumn
ctcDestinationRemoteLUName = _CtcDestinationRemoteLUName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2, 1, 2),
    _CtcDestinationRemoteLUName_Type()
)
ctcDestinationRemoteLUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcDestinationRemoteLUName.setStatus("current")


class _CtcDestinationModeName_Type(SnmpAdminString):
    """Custom type ctcDestinationModeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CtcDestinationModeName_Type.__name__ = "SnmpAdminString"
_CtcDestinationModeName_Object = MibTableColumn
ctcDestinationModeName = _CtcDestinationModeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2, 1, 3),
    _CtcDestinationModeName_Type()
)
ctcDestinationModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcDestinationModeName.setStatus("current")
_CtcDestinationNumHits_Type = Unsigned32
_CtcDestinationNumHits_Object = MibTableColumn
ctcDestinationNumHits = _CtcDestinationNumHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 2, 1, 4),
    _CtcDestinationNumHits_Type()
)
ctcDestinationNumHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcDestinationNumHits.setStatus("current")
_CtcRouteTable_Object = MibTable
ctcRouteTable = _CtcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 3)
)
if mibBuilder.loadTexts:
    ctcRouteTable.setStatus("current")
_CtcRouteEntry_Object = MibTableRow
ctcRouteEntry = _CtcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 3, 1)
)
ctcRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctcRouteEntry.setStatus("current")
_CtcRouteOwningServer_Type = Unsigned32
_CtcRouteOwningServer_Object = MibTableColumn
ctcRouteOwningServer = _CtcRouteOwningServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 3, 1, 1),
    _CtcRouteOwningServer_Type()
)
ctcRouteOwningServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcRouteOwningServer.setStatus("current")


class _CtcRouteTransactionID_Type(SnmpAdminString):
    """Custom type ctcRouteTransactionID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcRouteTransactionID_Type.__name__ = "SnmpAdminString"
_CtcRouteTransactionID_Object = MibTableColumn
ctcRouteTransactionID = _CtcRouteTransactionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 3, 1, 2),
    _CtcRouteTransactionID_Type()
)
ctcRouteTransactionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcRouteTransactionID.setStatus("current")


class _CtcRouteDestinationName_Type(SnmpAdminString):
    """Custom type ctcRouteDestinationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcRouteDestinationName_Type.__name__ = "SnmpAdminString"
_CtcRouteDestinationName_Object = MibTableColumn
ctcRouteDestinationName = _CtcRouteDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 3, 1, 3),
    _CtcRouteDestinationName_Type()
)
ctcRouteDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcRouteDestinationName.setStatus("current")
_CtcServerTable_Object = MibTable
ctcServerTable = _CtcServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4)
)
if mibBuilder.loadTexts:
    ctcServerTable.setStatus("current")
_CtcServerEntry_Object = MibTableRow
ctcServerEntry = _CtcServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1)
)
ctcServerEntry.setIndexNames(
    (0, "CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerIndex"),
)
if mibBuilder.loadTexts:
    ctcServerEntry.setStatus("current")
_CtcServerIndex_Type = Unsigned32
_CtcServerIndex_Object = MibTableColumn
ctcServerIndex = _CtcServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 1),
    _CtcServerIndex_Type()
)
ctcServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerIndex.setStatus("current")


class _CtcServerName_Type(SnmpAdminString):
    """Custom type ctcServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcServerName_Type.__name__ = "SnmpAdminString"
_CtcServerName_Object = MibTableColumn
ctcServerName = _CtcServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 2),
    _CtcServerName_Type()
)
ctcServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerName.setStatus("current")
_CtcServerListening_Type = TruthValue
_CtcServerListening_Object = MibTableColumn
ctcServerListening = _CtcServerListening_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 3),
    _CtcServerListening_Type()
)
ctcServerListening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerListening.setStatus("current")


class _CtcServerIPAddr_Type(IpAddress):
    """Custom type ctcServerIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CtcServerIPAddr_Object = MibTableColumn
ctcServerIPAddr = _CtcServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 4),
    _CtcServerIPAddr_Type()
)
ctcServerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerIPAddr.setStatus("current")


class _CtcServerPort_Type(Unsigned32):
    """Custom type ctcServerPort based on Unsigned32"""
    defaultValue = 1435

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtcServerPort_Type.__name__ = "Unsigned32"
_CtcServerPort_Object = MibTableColumn
ctcServerPort = _CtcServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 5),
    _CtcServerPort_Type()
)
ctcServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerPort.setStatus("current")


class _CtcServerDestinationName_Type(SnmpAdminString):
    """Custom type ctcServerDestinationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcServerDestinationName_Type.__name__ = "SnmpAdminString"
_CtcServerDestinationName_Object = MibTableColumn
ctcServerDestinationName = _CtcServerDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 6),
    _CtcServerDestinationName_Type()
)
ctcServerDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerDestinationName.setStatus("current")


class _CtcServerClientTimeout_Type(Unsigned32):
    """Custom type ctcServerClientTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CtcServerClientTimeout_Type.__name__ = "Unsigned32"
_CtcServerClientTimeout_Object = MibTableColumn
ctcServerClientTimeout = _CtcServerClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 7),
    _CtcServerClientTimeout_Type()
)
ctcServerClientTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ctcServerClientTimeout.setUnits("minutes")


class _CtcServerHostTimeout_Type(Unsigned32):
    """Custom type ctcServerHostTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CtcServerHostTimeout_Type.__name__ = "Unsigned32"
_CtcServerHostTimeout_Object = MibTableColumn
ctcServerHostTimeout = _CtcServerHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 8),
    _CtcServerHostTimeout_Type()
)
ctcServerHostTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerHostTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ctcServerHostTimeout.setUnits("minutes")


class _CtcServerWindowSize_Type(Unsigned32):
    """Custom type ctcServerWindowSize based on Unsigned32"""
    defaultValue = 4096


_CtcServerWindowSize_Object = MibTableColumn
ctcServerWindowSize = _CtcServerWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 9),
    _CtcServerWindowSize_Type()
)
ctcServerWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    ctcServerWindowSize.setUnits("bytes")
_CtcServerConnectionCount_Type = Unsigned32
_CtcServerConnectionCount_Object = MibTableColumn
ctcServerConnectionCount = _CtcServerConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 10),
    _CtcServerConnectionCount_Type()
)
ctcServerConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerConnectionCount.setStatus("current")


class _CtcServerProgNameUpperCase_Type(TruthValue):
    """Custom type ctcServerProgNameUpperCase based on TruthValue"""


_CtcServerProgNameUpperCase_Object = MibTableColumn
ctcServerProgNameUpperCase = _CtcServerProgNameUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 4, 1, 11),
    _CtcServerProgNameUpperCase_Type()
)
ctcServerProgNameUpperCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcServerProgNameUpperCase.setStatus("current")
_CtcConnectionTable_Object = MibTable
ctcConnectionTable = _CtcConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5)
)
if mibBuilder.loadTexts:
    ctcConnectionTable.setStatus("current")
_CtcConnectionEntry_Object = MibTableRow
ctcConnectionEntry = _CtcConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1)
)
ctcConnectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctcConnectionEntry.setStatus("current")


class _CtcConnectionId_Type(OctetString):
    """Custom type ctcConnectionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtcConnectionId_Type.__name__ = "OctetString"
_CtcConnectionId_Object = MibTableColumn
ctcConnectionId = _CtcConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 1),
    _CtcConnectionId_Type()
)
ctcConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionId.setStatus("current")
_CtcConnectionServer_Type = Unsigned32
_CtcConnectionServer_Object = MibTableColumn
ctcConnectionServer = _CtcConnectionServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 2),
    _CtcConnectionServer_Type()
)
ctcConnectionServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionServer.setStatus("current")


class _CtcConnectionState_Type(Integer32):
    """Custom type ctcConnectionState based on Integer32"""
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
        *(("closing", 2),
          ("halt", 3),
          ("receiving", 4),
          ("reset", 1))
    )


_CtcConnectionState_Type.__name__ = "Integer32"
_CtcConnectionState_Object = MibTableColumn
ctcConnectionState = _CtcConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 3),
    _CtcConnectionState_Type()
)
ctcConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionState.setStatus("current")
_CtcConnectionSessionCount_Type = Unsigned32
_CtcConnectionSessionCount_Object = MibTableColumn
ctcConnectionSessionCount = _CtcConnectionSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 4),
    _CtcConnectionSessionCount_Type()
)
ctcConnectionSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionSessionCount.setStatus("current")
_CtcConnectionClientIPAddr_Type = IpAddress
_CtcConnectionClientIPAddr_Object = MibTableColumn
ctcConnectionClientIPAddr = _CtcConnectionClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 5),
    _CtcConnectionClientIPAddr_Type()
)
ctcConnectionClientIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionClientIPAddr.setStatus("current")


class _CtcConnectionClientPort_Type(Unsigned32):
    """Custom type ctcConnectionClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtcConnectionClientPort_Type.__name__ = "Unsigned32"
_CtcConnectionClientPort_Object = MibTableColumn
ctcConnectionClientPort = _CtcConnectionClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 6),
    _CtcConnectionClientPort_Type()
)
ctcConnectionClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionClientPort.setStatus("current")
_CtcConnectionTotalConversations_Type = Unsigned32
_CtcConnectionTotalConversations_Object = MibTableColumn
ctcConnectionTotalConversations = _CtcConnectionTotalConversations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 7),
    _CtcConnectionTotalConversations_Type()
)
ctcConnectionTotalConversations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionTotalConversations.setStatus("current")
_CtcConnectionConnectTime_Type = DateAndTime
_CtcConnectionConnectTime_Object = MibTableColumn
ctcConnectionConnectTime = _CtcConnectionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 8),
    _CtcConnectionConnectTime_Type()
)
ctcConnectionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionConnectTime.setStatus("current")
_CtcConnectionIdleTime_Type = TimeInterval
_CtcConnectionIdleTime_Object = MibTableColumn
ctcConnectionIdleTime = _CtcConnectionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 9),
    _CtcConnectionIdleTime_Type()
)
ctcConnectionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionIdleTime.setStatus("current")
_CtcConnectionTotalBytesRecvd_Type = Unsigned32
_CtcConnectionTotalBytesRecvd_Object = MibTableColumn
ctcConnectionTotalBytesRecvd = _CtcConnectionTotalBytesRecvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 5, 1, 10),
    _CtcConnectionTotalBytesRecvd_Type()
)
ctcConnectionTotalBytesRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcConnectionTotalBytesRecvd.setStatus("current")
_CtcTransactionTable_Object = MibTable
ctcTransactionTable = _CtcTransactionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6)
)
if mibBuilder.loadTexts:
    ctcTransactionTable.setStatus("current")
_CtcTransactionEntry_Object = MibTableRow
ctcTransactionEntry = _CtcTransactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1)
)
ctcTransactionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctcTransactionEntry.setStatus("current")


class _CtcTransactionSessionId_Type(OctetString):
    """Custom type ctcTransactionSessionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtcTransactionSessionId_Type.__name__ = "OctetString"
_CtcTransactionSessionId_Object = MibTableColumn
ctcTransactionSessionId = _CtcTransactionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 1),
    _CtcTransactionSessionId_Type()
)
ctcTransactionSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionSessionId.setStatus("current")
_CtcTransactionServer_Type = Unsigned32
_CtcTransactionServer_Object = MibTableColumn
ctcTransactionServer = _CtcTransactionServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 2),
    _CtcTransactionServer_Type()
)
ctcTransactionServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionServer.setStatus("current")


class _CtcTransactionConnectionId_Type(OctetString):
    """Custom type ctcTransactionConnectionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtcTransactionConnectionId_Type.__name__ = "OctetString"
_CtcTransactionConnectionId_Object = MibTableColumn
ctcTransactionConnectionId = _CtcTransactionConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 3),
    _CtcTransactionConnectionId_Type()
)
ctcTransactionConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionConnectionId.setStatus("current")


class _CtcTransactionState_Type(Integer32):
    """Custom type ctcTransactionState based on Integer32"""
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
        *(("closing", 7),
          ("exception", 5),
          ("exceptionresponse", 6),
          ("opening", 2),
          ("receiving", 4),
          ("reset", 1),
          ("sending", 3))
    )


_CtcTransactionState_Type.__name__ = "Integer32"
_CtcTransactionState_Object = MibTableColumn
ctcTransactionState = _CtcTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 4),
    _CtcTransactionState_Type()
)
ctcTransactionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionState.setStatus("current")


class _CtcTransactionTPName_Type(SnmpAdminString):
    """Custom type ctcTransactionTPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CtcTransactionTPName_Type.__name__ = "SnmpAdminString"
_CtcTransactionTPName_Object = MibTableColumn
ctcTransactionTPName = _CtcTransactionTPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 5),
    _CtcTransactionTPName_Type()
)
ctcTransactionTPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionTPName.setStatus("current")


class _CtcTransactionUserId_Type(SnmpAdminString):
    """Custom type ctcTransactionUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtcTransactionUserId_Type.__name__ = "SnmpAdminString"
_CtcTransactionUserId_Object = MibTableColumn
ctcTransactionUserId = _CtcTransactionUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 1, 6, 1, 6),
    _CtcTransactionUserId_Type()
)
ctcTransactionUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcTransactionUserId.setStatus("current")
_CiscoTransConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTransConnMIBConformance = _CiscoTransConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3)
)
_CiscoTransConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTransConnMIBCompliances = _CiscoTransConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 1)
)
_CiscoTransConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTransConnMIBGroups = _CiscoTransConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2)
)

# Managed Objects groups

ciscoTransConnLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 1)
)
ciscoTransConnLicenseGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcLicenseState"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcLicenseKey"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcLicenseMaxConn"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcLicenseCurrConn"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcLicenseExpiration"))
)
if mibBuilder.loadTexts:
    ciscoTransConnLicenseGroup.setStatus("current")

ciscoTransConnDestinationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 2)
)
ciscoTransConnDestinationGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcDestinationName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcDestinationRemoteLUName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcDestinationModeName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcDestinationNumHits"))
)
if mibBuilder.loadTexts:
    ciscoTransConnDestinationGroup.setStatus("current")

ciscoTransConnRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 3)
)
ciscoTransConnRouteGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcRouteOwningServer"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcRouteTransactionID"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcRouteDestinationName"))
)
if mibBuilder.loadTexts:
    ciscoTransConnRouteGroup.setStatus("current")

ciscoTransConnServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 4)
)
ciscoTransConnServerGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerIndex"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerListening"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerIPAddr"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerPort"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerDestinationName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerClientTimeout"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerHostTimeout"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerWindowSize"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerConnectionCount"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcServerProgNameUpperCase"))
)
if mibBuilder.loadTexts:
    ciscoTransConnServerGroup.setStatus("current")

ciscoTransConnConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 5)
)
ciscoTransConnConnectionGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionId"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionServer"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionState"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionSessionCount"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionClientIPAddr"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionClientPort"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionTotalConversations"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionConnectTime"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionIdleTime"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcConnectionTotalBytesRecvd"))
)
if mibBuilder.loadTexts:
    ciscoTransConnConnectionGroup.setStatus("current")

ciscoTransConnTransactionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 2, 6)
)
ciscoTransConnTransactionGroup.setObjects(
      *(("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionSessionId"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionServer"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionConnectionId"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionState"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionTPName"),
        ("CISCO-TRANSACTION-CONNECTION-MIB", "ctcTransactionUserId"))
)
if mibBuilder.loadTexts:
    ciscoTransConnTransactionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTransConnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 144, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTransConnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRANSACTION-CONNECTION-MIB",
    **{"ciscoTransactionConnectionMIB": ciscoTransactionConnectionMIB,
       "ciscoTransConnMIBObjects": ciscoTransConnMIBObjects,
       "ctcLicense": ctcLicense,
       "ctcLicenseState": ctcLicenseState,
       "ctcLicenseKey": ctcLicenseKey,
       "ctcLicenseMaxConn": ctcLicenseMaxConn,
       "ctcLicenseCurrConn": ctcLicenseCurrConn,
       "ctcLicenseExpiration": ctcLicenseExpiration,
       "ctcDestinationTable": ctcDestinationTable,
       "ctcDestinationEntry": ctcDestinationEntry,
       "ctcDestinationName": ctcDestinationName,
       "ctcDestinationRemoteLUName": ctcDestinationRemoteLUName,
       "ctcDestinationModeName": ctcDestinationModeName,
       "ctcDestinationNumHits": ctcDestinationNumHits,
       "ctcRouteTable": ctcRouteTable,
       "ctcRouteEntry": ctcRouteEntry,
       "ctcRouteOwningServer": ctcRouteOwningServer,
       "ctcRouteTransactionID": ctcRouteTransactionID,
       "ctcRouteDestinationName": ctcRouteDestinationName,
       "ctcServerTable": ctcServerTable,
       "ctcServerEntry": ctcServerEntry,
       "ctcServerIndex": ctcServerIndex,
       "ctcServerName": ctcServerName,
       "ctcServerListening": ctcServerListening,
       "ctcServerIPAddr": ctcServerIPAddr,
       "ctcServerPort": ctcServerPort,
       "ctcServerDestinationName": ctcServerDestinationName,
       "ctcServerClientTimeout": ctcServerClientTimeout,
       "ctcServerHostTimeout": ctcServerHostTimeout,
       "ctcServerWindowSize": ctcServerWindowSize,
       "ctcServerConnectionCount": ctcServerConnectionCount,
       "ctcServerProgNameUpperCase": ctcServerProgNameUpperCase,
       "ctcConnectionTable": ctcConnectionTable,
       "ctcConnectionEntry": ctcConnectionEntry,
       "ctcConnectionId": ctcConnectionId,
       "ctcConnectionServer": ctcConnectionServer,
       "ctcConnectionState": ctcConnectionState,
       "ctcConnectionSessionCount": ctcConnectionSessionCount,
       "ctcConnectionClientIPAddr": ctcConnectionClientIPAddr,
       "ctcConnectionClientPort": ctcConnectionClientPort,
       "ctcConnectionTotalConversations": ctcConnectionTotalConversations,
       "ctcConnectionConnectTime": ctcConnectionConnectTime,
       "ctcConnectionIdleTime": ctcConnectionIdleTime,
       "ctcConnectionTotalBytesRecvd": ctcConnectionTotalBytesRecvd,
       "ctcTransactionTable": ctcTransactionTable,
       "ctcTransactionEntry": ctcTransactionEntry,
       "ctcTransactionSessionId": ctcTransactionSessionId,
       "ctcTransactionServer": ctcTransactionServer,
       "ctcTransactionConnectionId": ctcTransactionConnectionId,
       "ctcTransactionState": ctcTransactionState,
       "ctcTransactionTPName": ctcTransactionTPName,
       "ctcTransactionUserId": ctcTransactionUserId,
       "ciscoTransConnMIBConformance": ciscoTransConnMIBConformance,
       "ciscoTransConnMIBCompliances": ciscoTransConnMIBCompliances,
       "ciscoTransConnMIBCompliance": ciscoTransConnMIBCompliance,
       "ciscoTransConnMIBGroups": ciscoTransConnMIBGroups,
       "ciscoTransConnLicenseGroup": ciscoTransConnLicenseGroup,
       "ciscoTransConnDestinationGroup": ciscoTransConnDestinationGroup,
       "ciscoTransConnRouteGroup": ciscoTransConnRouteGroup,
       "ciscoTransConnServerGroup": ciscoTransConnServerGroup,
       "ciscoTransConnConnectionGroup": ciscoTransConnConnectionGroup,
       "ciscoTransConnTransactionGroup": ciscoTransConnTransactionGroup}
)
