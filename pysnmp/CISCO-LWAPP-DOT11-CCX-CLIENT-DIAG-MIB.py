# SNMP MIB module (CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:18 2024
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

(CLDot11ClientDiagAssocReason,
 CiscoLwappDot11ClientAuthMethod) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB",
    "CLDot11ClientDiagAssocReason",
    "CiscoLwappDot11ClientAuthMethod")

(ciscoLwappDot11ClientCcxMIBObjects,
 cldcClientMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "ciscoLwappDot11ClientCcxMIBObjects",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoMilliSeconds,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11CcxClientDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2)
)
ciscoLwappDot11CcxClientDiagMIB.setRevisions(
        ("2006-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoLwappCcxDiagResponseStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("incapable", 4),
          ("refused", 3),
          ("successful", 0),
          ("unknown", 5))
    )



class CiscoLwappCcxDiagTestStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 5),
          ("pending", 1),
          ("stopped", 4),
          ("successful", 0),
          ("timeout", 3))
    )



class CiscoLwappDot11ClientDot1xCredential(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("one-time-password", 4),
          ("other-cert", 3),
          ("pre-sharedkey", 0),
          ("secure-id-token", 5),
          ("username-password", 1),
          ("xdot", 2))
    )



class CiscoLwappDot11ClientAbortTestReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancelled-by-operator", 2),
          ("reserved", 0),
          ("timeout", 1))
    )



class CiscoLwappDot11ClientInitiateTest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort-test", 2),
          ("initiate-test", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11CcxClientDiagMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11CcxClientDiagMIBObjects = _CiscoLwappDot11CcxClientDiagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0)
)
_CiscoClientCcxDiagRequest_ObjectIdentity = ObjectIdentity
ciscoClientCcxDiagRequest = _CiscoClientCcxDiagRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1)
)
_CldccDiagDhcpTestReqTable_Object = MibTable
cldccDiagDhcpTestReqTable = _CldccDiagDhcpTestReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 1)
)
if mibBuilder.loadTexts:
    cldccDiagDhcpTestReqTable.setStatus("current")
_CldccDiagDhcpTestReqEntry_Object = MibTableRow
cldccDiagDhcpTestReqEntry = _CldccDiagDhcpTestReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 1, 1)
)
cldccDiagDhcpTestReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagDhcpTestReqEntry.setStatus("current")
_CldccDiagDhcpTestReqRowStatus_Type = RowStatus
_CldccDiagDhcpTestReqRowStatus_Object = MibTableColumn
cldccDiagDhcpTestReqRowStatus = _CldccDiagDhcpTestReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 1, 1, 1),
    _CldccDiagDhcpTestReqRowStatus_Type()
)
cldccDiagDhcpTestReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagDhcpTestReqRowStatus.setStatus("current")
_CldccDiagPingTestReqTable_Object = MibTable
cldccDiagPingTestReqTable = _CldccDiagPingTestReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 2)
)
if mibBuilder.loadTexts:
    cldccDiagPingTestReqTable.setStatus("current")
_CldccDiagPingTestReqEntry_Object = MibTableRow
cldccDiagPingTestReqEntry = _CldccDiagPingTestReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 2, 1)
)
cldccDiagPingTestReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagPingTestReqEntry.setStatus("current")


class _CldccDiagPingTestType_Type(Integer32):
    """Custom type cldccDiagPingTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default-gw", 2),
          ("dns-server", 1))
    )


_CldccDiagPingTestType_Type.__name__ = "Integer32"
_CldccDiagPingTestType_Object = MibTableColumn
cldccDiagPingTestType = _CldccDiagPingTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 2, 1, 1),
    _CldccDiagPingTestType_Type()
)
cldccDiagPingTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagPingTestType.setStatus("current")
_CldccDiagPingTestReqRowStatus_Type = RowStatus
_CldccDiagPingTestReqRowStatus_Object = MibTableColumn
cldccDiagPingTestReqRowStatus = _CldccDiagPingTestReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 2, 1, 2),
    _CldccDiagPingTestReqRowStatus_Type()
)
cldccDiagPingTestReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagPingTestReqRowStatus.setStatus("current")
_CldccDiagDnsNameResolTestReqTable_Object = MibTable
cldccDiagDnsNameResolTestReqTable = _CldccDiagDnsNameResolTestReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 3)
)
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestReqTable.setStatus("current")
_CldccDiagDnsNameResolTestReqEntry_Object = MibTableRow
cldccDiagDnsNameResolTestReqEntry = _CldccDiagDnsNameResolTestReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 3, 1)
)
cldccDiagDnsNameResolTestReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestReqEntry.setStatus("current")


class _CldccDiagDnsNameResolTestReqNetworkName_Type(OctetString):
    """Custom type cldccDiagDnsNameResolTestReqNetworkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CldccDiagDnsNameResolTestReqNetworkName_Type.__name__ = "OctetString"
_CldccDiagDnsNameResolTestReqNetworkName_Object = MibTableColumn
cldccDiagDnsNameResolTestReqNetworkName = _CldccDiagDnsNameResolTestReqNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 3, 1, 1),
    _CldccDiagDnsNameResolTestReqNetworkName_Type()
)
cldccDiagDnsNameResolTestReqNetworkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestReqNetworkName.setStatus("current")
_CldccDiagDnsNameResolTestReqRowStatus_Type = RowStatus
_CldccDiagDnsNameResolTestReqRowStatus_Object = MibTableColumn
cldccDiagDnsNameResolTestReqRowStatus = _CldccDiagDnsNameResolTestReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 3, 1, 2),
    _CldccDiagDnsNameResolTestReqRowStatus_Type()
)
cldccDiagDnsNameResolTestReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestReqRowStatus.setStatus("current")
_CldccDiagAssociationTestReqTable_Object = MibTable
cldccDiagAssociationTestReqTable = _CldccDiagAssociationTestReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4)
)
if mibBuilder.loadTexts:
    cldccDiagAssociationTestReqTable.setStatus("current")
_CldccDiagAssociationTestReqEntry_Object = MibTableRow
cldccDiagAssociationTestReqEntry = _CldccDiagAssociationTestReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1)
)
cldccDiagAssociationTestReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagAssociationTestReqEntry.setStatus("current")
_CldccDiagAssocTestReqBssid_Type = MacAddress
_CldccDiagAssocTestReqBssid_Object = MibTableColumn
cldccDiagAssocTestReqBssid = _CldccDiagAssocTestReqBssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 1),
    _CldccDiagAssocTestReqBssid_Type()
)
cldccDiagAssocTestReqBssid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqBssid.setStatus("current")


class _CldccDiagAssocTestReqSsid_Type(OctetString):
    """Custom type cldccDiagAssocTestReqSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CldccDiagAssocTestReqSsid_Type.__name__ = "OctetString"
_CldccDiagAssocTestReqSsid_Object = MibTableColumn
cldccDiagAssocTestReqSsid = _CldccDiagAssocTestReqSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 2),
    _CldccDiagAssocTestReqSsid_Type()
)
cldccDiagAssocTestReqSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqSsid.setStatus("current")


class _CldccDiagAssocTestReqChannel_Type(Integer32):
    """Custom type cldccDiagAssocTestReqChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAssocTestReqChannel_Type.__name__ = "Integer32"
_CldccDiagAssocTestReqChannel_Object = MibTableColumn
cldccDiagAssocTestReqChannel = _CldccDiagAssocTestReqChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 3),
    _CldccDiagAssocTestReqChannel_Type()
)
cldccDiagAssocTestReqChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqChannel.setStatus("current")


class _CldccDiagAssocTestReqBand_Type(Integer32):
    """Custom type cldccDiagAssocTestReqBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAssocTestReqBand_Type.__name__ = "Integer32"
_CldccDiagAssocTestReqBand_Object = MibTableColumn
cldccDiagAssocTestReqBand = _CldccDiagAssocTestReqBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 4),
    _CldccDiagAssocTestReqBand_Type()
)
cldccDiagAssocTestReqBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqBand.setStatus("current")


class _CldccDiagAssocTestReqPhyType_Type(Integer32):
    """Custom type cldccDiagAssocTestReqPhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAssocTestReqPhyType_Type.__name__ = "Integer32"
_CldccDiagAssocTestReqPhyType_Object = MibTableColumn
cldccDiagAssocTestReqPhyType = _CldccDiagAssocTestReqPhyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 5),
    _CldccDiagAssocTestReqPhyType_Type()
)
cldccDiagAssocTestReqPhyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqPhyType.setStatus("current")
_CldccDiagAssocTestReqRowStatus_Type = RowStatus
_CldccDiagAssocTestReqRowStatus_Object = MibTableColumn
cldccDiagAssocTestReqRowStatus = _CldccDiagAssocTestReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 4, 1, 6),
    _CldccDiagAssocTestReqRowStatus_Type()
)
cldccDiagAssocTestReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAssocTestReqRowStatus.setStatus("current")
_CldccDiagAuthenticationTestReqTable_Object = MibTable
cldccDiagAuthenticationTestReqTable = _CldccDiagAuthenticationTestReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5)
)
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqTable.setStatus("current")
_CldccDiagAuthenticationTestReqEntry_Object = MibTableRow
cldccDiagAuthenticationTestReqEntry = _CldccDiagAuthenticationTestReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1)
)
cldccDiagAuthenticationTestReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqEntry.setStatus("current")
_CldccDiagAuthenticationTestReqBssid_Type = MacAddress
_CldccDiagAuthenticationTestReqBssid_Object = MibTableColumn
cldccDiagAuthenticationTestReqBssid = _CldccDiagAuthenticationTestReqBssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 1),
    _CldccDiagAuthenticationTestReqBssid_Type()
)
cldccDiagAuthenticationTestReqBssid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqBssid.setStatus("current")
_CldccDiagAuthenticationTestReqProfileId_Type = Unsigned32
_CldccDiagAuthenticationTestReqProfileId_Object = MibTableColumn
cldccDiagAuthenticationTestReqProfileId = _CldccDiagAuthenticationTestReqProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 2),
    _CldccDiagAuthenticationTestReqProfileId_Type()
)
cldccDiagAuthenticationTestReqProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqProfileId.setStatus("current")


class _CldccDiagAuthenticationTestReqChannel_Type(Integer32):
    """Custom type cldccDiagAuthenticationTestReqChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAuthenticationTestReqChannel_Type.__name__ = "Integer32"
_CldccDiagAuthenticationTestReqChannel_Object = MibTableColumn
cldccDiagAuthenticationTestReqChannel = _CldccDiagAuthenticationTestReqChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 3),
    _CldccDiagAuthenticationTestReqChannel_Type()
)
cldccDiagAuthenticationTestReqChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqChannel.setStatus("current")


class _CldccDiagAuthenticationTestReqBand_Type(Integer32):
    """Custom type cldccDiagAuthenticationTestReqBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAuthenticationTestReqBand_Type.__name__ = "Integer32"
_CldccDiagAuthenticationTestReqBand_Object = MibTableColumn
cldccDiagAuthenticationTestReqBand = _CldccDiagAuthenticationTestReqBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 5),
    _CldccDiagAuthenticationTestReqBand_Type()
)
cldccDiagAuthenticationTestReqBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqBand.setStatus("current")


class _CldccDiagAuthenticationTestReqPhyType_Type(Integer32):
    """Custom type cldccDiagAuthenticationTestReqPhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAuthenticationTestReqPhyType_Type.__name__ = "Integer32"
_CldccDiagAuthenticationTestReqPhyType_Object = MibTableColumn
cldccDiagAuthenticationTestReqPhyType = _CldccDiagAuthenticationTestReqPhyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 6),
    _CldccDiagAuthenticationTestReqPhyType_Type()
)
cldccDiagAuthenticationTestReqPhyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqPhyType.setStatus("current")
_CldccDiagAuthenticationTestReqRowStatus_Type = RowStatus
_CldccDiagAuthenticationTestReqRowStatus_Object = MibTableColumn
cldccDiagAuthenticationTestReqRowStatus = _CldccDiagAuthenticationTestReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 5, 1, 9),
    _CldccDiagAuthenticationTestReqRowStatus_Type()
)
cldccDiagAuthenticationTestReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestReqRowStatus.setStatus("current")
_CldccDiagMsgDisplayReqTable_Object = MibTable
cldccDiagMsgDisplayReqTable = _CldccDiagMsgDisplayReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 6)
)
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayReqTable.setStatus("current")
_CldccDiagMsgDisplayReqEntry_Object = MibTableRow
cldccDiagMsgDisplayReqEntry = _CldccDiagMsgDisplayReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 6, 1)
)
cldccDiagMsgDisplayReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayReqEntry.setStatus("current")


class _CldccDiagMsgDisplayMsgType_Type(Integer32):
    """Custom type cldccDiagMsgDisplayMsgType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bad-credentials", 4),
          ("begining-association-test", 14),
          ("begining-dhcp-test", 15),
          ("begining-dns-ping-test", 17),
          ("begining-dot1x-test", 19),
          ("begining-name-resolution-test", 18),
          ("begining-network-connectivity-test", 16),
          ("call-support", 5),
          ("cancel-diag-channel-operation", 24),
          ("client-report-retrieval-refused", 26),
          ("invalid-network-address", 28),
          ("invalid-network-settings", 2),
          ("invalid-ssid", 1),
          ("known-problem-with-network", 29),
          ("log-retrieval-refused", 25),
          ("problem-resolved", 6),
          ("redirecting-client-to-a-profile", 20),
          ("resolution-incomplete", 7),
          ("retrieval-complete", 13),
          ("retrieving-client-logs", 12),
          ("retrieving-client-reports", 11),
          ("scheduled-maint-period", 30),
          ("test-complete", 21),
          ("test-failed", 23),
          ("test-passed", 22),
          ("test-request-refused-by-client", 27),
          ("trouble-shooting-refused-by-network", 10),
          ("try-again-later", 8),
          ("user-action-required", 9),
          ("waln-encryption-incorrect", 32),
          ("wlan-auth-incorrect", 33),
          ("wlan-capability-mismatch", 3),
          ("wlan-security-incorrect", 31))
    )


_CldccDiagMsgDisplayMsgType_Type.__name__ = "Integer32"
_CldccDiagMsgDisplayMsgType_Object = MibTableColumn
cldccDiagMsgDisplayMsgType = _CldccDiagMsgDisplayMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 6, 1, 1),
    _CldccDiagMsgDisplayMsgType_Type()
)
cldccDiagMsgDisplayMsgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayMsgType.setStatus("current")
_CldccDiagMsgDisplayReqRowStatus_Type = RowStatus
_CldccDiagMsgDisplayReqRowStatus_Object = MibTableColumn
cldccDiagMsgDisplayReqRowStatus = _CldccDiagMsgDisplayReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 6, 1, 2),
    _CldccDiagMsgDisplayReqRowStatus_Type()
)
cldccDiagMsgDisplayReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayReqRowStatus.setStatus("current")
_CldccDiagProfileRedirectReqTable_Object = MibTable
cldccDiagProfileRedirectReqTable = _CldccDiagProfileRedirectReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 7)
)
if mibBuilder.loadTexts:
    cldccDiagProfileRedirectReqTable.setStatus("current")
_CldccDiagProfileRedirectReqEntry_Object = MibTableRow
cldccDiagProfileRedirectReqEntry = _CldccDiagProfileRedirectReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 7, 1)
)
cldccDiagProfileRedirectReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagProfileRedirectReqEntry.setStatus("current")
_CldccDiagProfileRedirectReqProfileId_Type = Unsigned32
_CldccDiagProfileRedirectReqProfileId_Object = MibTableColumn
cldccDiagProfileRedirectReqProfileId = _CldccDiagProfileRedirectReqProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 7, 1, 1),
    _CldccDiagProfileRedirectReqProfileId_Type()
)
cldccDiagProfileRedirectReqProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagProfileRedirectReqProfileId.setStatus("current")
_CldccDiagProfileRedirectReqRowStatus_Type = RowStatus
_CldccDiagProfileRedirectReqRowStatus_Object = MibTableColumn
cldccDiagProfileRedirectReqRowStatus = _CldccDiagProfileRedirectReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 1, 7, 1, 2),
    _CldccDiagProfileRedirectReqRowStatus_Type()
)
cldccDiagProfileRedirectReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccDiagProfileRedirectReqRowStatus.setStatus("current")
_CiscoClientCcxDiagResponse_ObjectIdentity = ObjectIdentity
ciscoClientCcxDiagResponse = _CiscoClientCcxDiagResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2)
)
_CldccDiagDhcpTestRespTable_Object = MibTable
cldccDiagDhcpTestRespTable = _CldccDiagDhcpTestRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 1)
)
if mibBuilder.loadTexts:
    cldccDiagDhcpTestRespTable.setStatus("current")
_CldccDiagDhcpTestRespEntry_Object = MibTableRow
cldccDiagDhcpTestRespEntry = _CldccDiagDhcpTestRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 1, 1)
)
cldccDiagDhcpTestRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagDhcpTestRespEntry.setStatus("current")


class _CldccDiagDhcpTestRespDhcpOffer_Type(OctetString):
    """Custom type cldccDiagDhcpTestRespDhcpOffer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CldccDiagDhcpTestRespDhcpOffer_Type.__name__ = "OctetString"
_CldccDiagDhcpTestRespDhcpOffer_Object = MibTableColumn
cldccDiagDhcpTestRespDhcpOffer = _CldccDiagDhcpTestRespDhcpOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 1, 1, 1),
    _CldccDiagDhcpTestRespDhcpOffer_Type()
)
cldccDiagDhcpTestRespDhcpOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagDhcpTestRespDhcpOffer.setStatus("current")
_CldccDiagPingTestRespTable_Object = MibTable
cldccDiagPingTestRespTable = _CldccDiagPingTestRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2)
)
if mibBuilder.loadTexts:
    cldccDiagPingTestRespTable.setStatus("current")
_CldccDiagPingTestRespEntry_Object = MibTableRow
cldccDiagPingTestRespEntry = _CldccDiagPingTestRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2)
)
cldccDiagPingTestRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagPingTestRespEntry.setStatus("current")
_CldccDiagPingTestRespIPAddressType_Type = InetAddressType
_CldccDiagPingTestRespIPAddressType_Object = MibTableColumn
cldccDiagPingTestRespIPAddressType = _CldccDiagPingTestRespIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 1),
    _CldccDiagPingTestRespIPAddressType_Type()
)
cldccDiagPingTestRespIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespIPAddressType.setStatus("current")
_CldccDiagPingTestRespIPAddress_Type = InetAddress
_CldccDiagPingTestRespIPAddress_Object = MibTableColumn
cldccDiagPingTestRespIPAddress = _CldccDiagPingTestRespIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 2),
    _CldccDiagPingTestRespIPAddress_Type()
)
cldccDiagPingTestRespIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespIPAddress.setStatus("current")
_CldccDiagPingTestRespDestMacAddress_Type = MacAddress
_CldccDiagPingTestRespDestMacAddress_Object = MibTableColumn
cldccDiagPingTestRespDestMacAddress = _CldccDiagPingTestRespDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 3),
    _CldccDiagPingTestRespDestMacAddress_Type()
)
cldccDiagPingTestRespDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespDestMacAddress.setStatus("current")
_CldccDiagPingTestRespPingsSent_Type = Unsigned32
_CldccDiagPingTestRespPingsSent_Object = MibTableColumn
cldccDiagPingTestRespPingsSent = _CldccDiagPingTestRespPingsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 4),
    _CldccDiagPingTestRespPingsSent_Type()
)
cldccDiagPingTestRespPingsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespPingsSent.setStatus("current")
_CldccDiagPingTestRespPingsReceived_Type = Unsigned32
_CldccDiagPingTestRespPingsReceived_Object = MibTableColumn
cldccDiagPingTestRespPingsReceived = _CldccDiagPingTestRespPingsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 5),
    _CldccDiagPingTestRespPingsReceived_Type()
)
cldccDiagPingTestRespPingsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespPingsReceived.setStatus("current")
_CldccDiagPingTestRespMinEchoTIme_Type = CiscoMilliSeconds
_CldccDiagPingTestRespMinEchoTIme_Object = MibTableColumn
cldccDiagPingTestRespMinEchoTIme = _CldccDiagPingTestRespMinEchoTIme_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 6),
    _CldccDiagPingTestRespMinEchoTIme_Type()
)
cldccDiagPingTestRespMinEchoTIme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespMinEchoTIme.setStatus("current")
_CldccDiagPingTestRespMaxEchoTIme_Type = CiscoMilliSeconds
_CldccDiagPingTestRespMaxEchoTIme_Object = MibTableColumn
cldccDiagPingTestRespMaxEchoTIme = _CldccDiagPingTestRespMaxEchoTIme_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 2, 2, 7),
    _CldccDiagPingTestRespMaxEchoTIme_Type()
)
cldccDiagPingTestRespMaxEchoTIme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagPingTestRespMaxEchoTIme.setStatus("current")
_CldccDiagDnsNameResolTestRespTable_Object = MibTable
cldccDiagDnsNameResolTestRespTable = _CldccDiagDnsNameResolTestRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 3)
)
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestRespTable.setStatus("current")
_CldccDiagDnsNameResolTestRespEntry_Object = MibTableRow
cldccDiagDnsNameResolTestRespEntry = _CldccDiagDnsNameResolTestRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 3, 1)
)
cldccDiagDnsNameResolTestRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestRespEntry.setStatus("current")
_CldccDiagDnsNameResolTestRespIpAddressType_Type = InetAddressType
_CldccDiagDnsNameResolTestRespIpAddressType_Object = MibTableColumn
cldccDiagDnsNameResolTestRespIpAddressType = _CldccDiagDnsNameResolTestRespIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 3, 1, 1),
    _CldccDiagDnsNameResolTestRespIpAddressType_Type()
)
cldccDiagDnsNameResolTestRespIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestRespIpAddressType.setStatus("current")
_CldccDiagDnsNameResolTestRespIpAddress_Type = InetAddress
_CldccDiagDnsNameResolTestRespIpAddress_Object = MibTableColumn
cldccDiagDnsNameResolTestRespIpAddress = _CldccDiagDnsNameResolTestRespIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 3, 1, 2),
    _CldccDiagDnsNameResolTestRespIpAddress_Type()
)
cldccDiagDnsNameResolTestRespIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestRespIpAddress.setStatus("current")


class _CldccDiagDnsNameResolTestRespServerName_Type(OctetString):
    """Custom type cldccDiagDnsNameResolTestRespServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CldccDiagDnsNameResolTestRespServerName_Type.__name__ = "OctetString"
_CldccDiagDnsNameResolTestRespServerName_Object = MibTableColumn
cldccDiagDnsNameResolTestRespServerName = _CldccDiagDnsNameResolTestRespServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 3, 1, 3),
    _CldccDiagDnsNameResolTestRespServerName_Type()
)
cldccDiagDnsNameResolTestRespServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagDnsNameResolTestRespServerName.setStatus("current")
_CldccDiagAssociationTestRespTable_Object = MibTable
cldccDiagAssociationTestRespTable = _CldccDiagAssociationTestRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 4)
)
if mibBuilder.loadTexts:
    cldccDiagAssociationTestRespTable.setStatus("current")
_CldccDiagAssociationTestRespEntry_Object = MibTableRow
cldccDiagAssociationTestRespEntry = _CldccDiagAssociationTestRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 4, 4)
)
cldccDiagAssociationTestRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagAssociationTestRespEntry.setStatus("current")
_CldccDiagAssociationTestRespIsAssocComplete_Type = TruthValue
_CldccDiagAssociationTestRespIsAssocComplete_Object = MibTableColumn
cldccDiagAssociationTestRespIsAssocComplete = _CldccDiagAssociationTestRespIsAssocComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 4, 4, 1),
    _CldccDiagAssociationTestRespIsAssocComplete_Type()
)
cldccDiagAssociationTestRespIsAssocComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagAssociationTestRespIsAssocComplete.setStatus("current")
_CldccDiagAssocTestRespReturnedStatus_Type = Unsigned32
_CldccDiagAssocTestRespReturnedStatus_Object = MibTableColumn
cldccDiagAssocTestRespReturnedStatus = _CldccDiagAssocTestRespReturnedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 4, 4, 2),
    _CldccDiagAssocTestRespReturnedStatus_Type()
)
cldccDiagAssocTestRespReturnedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagAssocTestRespReturnedStatus.setStatus("current")
_CldccDiagAuthenticationTestRespTable_Object = MibTable
cldccDiagAuthenticationTestRespTable = _CldccDiagAuthenticationTestRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 5)
)
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestRespTable.setStatus("current")
_CldccDiagAuthenticationTestRespEntry_Object = MibTableRow
cldccDiagAuthenticationTestRespEntry = _CldccDiagAuthenticationTestRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 5, 5)
)
cldccDiagAuthenticationTestRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestRespEntry.setStatus("current")
_CldccDiagAuthenticationTestRespIsCompleted_Type = TruthValue
_CldccDiagAuthenticationTestRespIsCompleted_Object = MibTableColumn
cldccDiagAuthenticationTestRespIsCompleted = _CldccDiagAuthenticationTestRespIsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 5, 5, 1),
    _CldccDiagAuthenticationTestRespIsCompleted_Type()
)
cldccDiagAuthenticationTestRespIsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestRespIsCompleted.setStatus("current")


class _CldccDiagAuthenticationTestRespReturnedStatus_Type(Integer32):
    """Custom type cldccDiagAuthenticationTestRespReturnedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccDiagAuthenticationTestRespReturnedStatus_Type.__name__ = "Integer32"
_CldccDiagAuthenticationTestRespReturnedStatus_Object = MibTableColumn
cldccDiagAuthenticationTestRespReturnedStatus = _CldccDiagAuthenticationTestRespReturnedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 5, 5, 2),
    _CldccDiagAuthenticationTestRespReturnedStatus_Type()
)
cldccDiagAuthenticationTestRespReturnedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestRespReturnedStatus.setStatus("current")


class _CldccDiagAuthenticationTestRespEAPMethod_Type(OctetString):
    """Custom type cldccDiagAuthenticationTestRespEAPMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CldccDiagAuthenticationTestRespEAPMethod_Type.__name__ = "OctetString"
_CldccDiagAuthenticationTestRespEAPMethod_Object = MibTableColumn
cldccDiagAuthenticationTestRespEAPMethod = _CldccDiagAuthenticationTestRespEAPMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 5, 5, 3),
    _CldccDiagAuthenticationTestRespEAPMethod_Type()
)
cldccDiagAuthenticationTestRespEAPMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagAuthenticationTestRespEAPMethod.setStatus("current")
_CldccDiagMsgDisplayRespTable_Object = MibTable
cldccDiagMsgDisplayRespTable = _CldccDiagMsgDisplayRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 6)
)
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayRespTable.setStatus("current")
_CldccDiagMsgDisplayRespEntry_Object = MibTableRow
cldccDiagMsgDisplayRespEntry = _CldccDiagMsgDisplayRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 6, 1)
)
cldccDiagMsgDisplayRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayRespEntry.setStatus("current")


class _CldccDiagMsgDisplayRespString_Type(OctetString):
    """Custom type cldccDiagMsgDisplayRespString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CldccDiagMsgDisplayRespString_Type.__name__ = "OctetString"
_CldccDiagMsgDisplayRespString_Object = MibTableColumn
cldccDiagMsgDisplayRespString = _CldccDiagMsgDisplayRespString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 6, 1, 1),
    _CldccDiagMsgDisplayRespString_Type()
)
cldccDiagMsgDisplayRespString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagMsgDisplayRespString.setStatus("current")
_CldccDiagTestLoggedFrameTable_Object = MibTable
cldccDiagTestLoggedFrameTable = _CldccDiagTestLoggedFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8)
)
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameTable.setStatus("current")
_CldccDiagTestLoggedFrameEntry_Object = MibTableRow
cldccDiagTestLoggedFrameEntry = _CldccDiagTestLoggedFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8, 1)
)
cldccDiagTestLoggedFrameEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB", "cldccDiagTestLoggedFrameIndex"),
)
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameEntry.setStatus("current")
_CldccDiagTestLoggedFrameIndex_Type = Unsigned32
_CldccDiagTestLoggedFrameIndex_Object = MibTableColumn
cldccDiagTestLoggedFrameIndex = _CldccDiagTestLoggedFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8, 1, 1),
    _CldccDiagTestLoggedFrameIndex_Type()
)
cldccDiagTestLoggedFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameIndex.setStatus("current")


class _CldccDiagTestLoggedFrameDirection_Type(Integer32):
    """Custom type cldccDiagTestLoggedFrameDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 0))
    )


_CldccDiagTestLoggedFrameDirection_Type.__name__ = "Integer32"
_CldccDiagTestLoggedFrameDirection_Object = MibTableColumn
cldccDiagTestLoggedFrameDirection = _CldccDiagTestLoggedFrameDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8, 1, 2),
    _CldccDiagTestLoggedFrameDirection_Type()
)
cldccDiagTestLoggedFrameDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameDirection.setStatus("current")
_CldccDiagTestLoggedFrameTimeStamp_Type = TimeStamp
_CldccDiagTestLoggedFrameTimeStamp_Object = MibTableColumn
cldccDiagTestLoggedFrameTimeStamp = _CldccDiagTestLoggedFrameTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8, 1, 3),
    _CldccDiagTestLoggedFrameTimeStamp_Type()
)
cldccDiagTestLoggedFrameTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameTimeStamp.setStatus("current")


class _CldccDiagTestLoggedFrameData_Type(OctetString):
    """Custom type cldccDiagTestLoggedFrameData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_CldccDiagTestLoggedFrameData_Type.__name__ = "OctetString"
_CldccDiagTestLoggedFrameData_Object = MibTableColumn
cldccDiagTestLoggedFrameData = _CldccDiagTestLoggedFrameData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 2, 8, 1, 4),
    _CldccDiagTestLoggedFrameData_Type()
)
cldccDiagTestLoggedFrameData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLoggedFrameData.setStatus("current")
_CiscoClientCcxDiagStatus_ObjectIdentity = ObjectIdentity
ciscoClientCcxDiagStatus = _CiscoClientCcxDiagStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 3)
)
_CldccDiagTestStatusTable_Object = MibTable
cldccDiagTestStatusTable = _CldccDiagTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 3, 1)
)
if mibBuilder.loadTexts:
    cldccDiagTestStatusTable.setStatus("current")
_CldccDiagTestStatusEntry_Object = MibTableRow
cldccDiagTestStatusEntry = _CldccDiagTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 3, 1, 1)
)
cldccDiagTestStatusEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccDiagTestStatusEntry.setStatus("current")
_CldccDiagTestLastTestStatus_Type = CiscoLwappCcxDiagTestStatus
_CldccDiagTestLastTestStatus_Object = MibTableColumn
cldccDiagTestLastTestStatus = _CldccDiagTestLastTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 3, 1, 1, 1),
    _CldccDiagTestLastTestStatus_Type()
)
cldccDiagTestLastTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLastTestStatus.setStatus("current")
_CldccDiagTestLastResponseStatus_Type = CiscoLwappCcxDiagResponseStatus
_CldccDiagTestLastResponseStatus_Object = MibTableColumn
cldccDiagTestLastResponseStatus = _CldccDiagTestLastResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 0, 3, 1, 1, 2),
    _CldccDiagTestLastResponseStatus_Type()
)
cldccDiagTestLastResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccDiagTestLastResponseStatus.setStatus("current")
_CiscoLwappDot11CcxClientDiagMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11CcxClientDiagMIBNotifs = _CiscoLwappDot11CcxClientDiagMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 1)
)
_CiscoLwappDot11CcxClientDiagMIBNotifObjs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11CcxClientDiagMIBNotifObjs = _CiscoLwappDot11CcxClientDiagMIBNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 2)
)
_CldccDiagClientMacAddress_Type = MacAddress
_CldccDiagClientMacAddress_Object = MibScalar
cldccDiagClientMacAddress = _CldccDiagClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 2, 1),
    _CldccDiagClientMacAddress_Type()
)
cldccDiagClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldccDiagClientMacAddress.setStatus("current")
_CldccDiagAssocReasonCode_Type = CLDot11ClientDiagAssocReason
_CldccDiagAssocReasonCode_Object = MibScalar
cldccDiagAssocReasonCode = _CldccDiagAssocReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 2, 2),
    _CldccDiagAssocReasonCode_Type()
)
cldccDiagAssocReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cldccDiagAssocReasonCode.setStatus("current")

# Managed Objects groups


# Notification objects

cldccDiagClientAssociatedToDiagWlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 2, 1, 1)
)
cldccDiagClientAssociatedToDiagWlan.setObjects(
      *(("CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB", "cldccDiagClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB", "cldccDiagAssocReasonCode"))
)
if mibBuilder.loadTexts:
    cldccDiagClientAssociatedToDiagWlan.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CCX-CLIENT-DIAG-MIB",
    **{"CiscoLwappCcxDiagResponseStatus": CiscoLwappCcxDiagResponseStatus,
       "CiscoLwappCcxDiagTestStatus": CiscoLwappCcxDiagTestStatus,
       "CiscoLwappDot11ClientDot1xCredential": CiscoLwappDot11ClientDot1xCredential,
       "CiscoLwappDot11ClientAbortTestReason": CiscoLwappDot11ClientAbortTestReason,
       "CiscoLwappDot11ClientInitiateTest": CiscoLwappDot11ClientInitiateTest,
       "ciscoLwappDot11CcxClientDiagMIB": ciscoLwappDot11CcxClientDiagMIB,
       "ciscoLwappDot11CcxClientDiagMIBObjects": ciscoLwappDot11CcxClientDiagMIBObjects,
       "ciscoClientCcxDiagRequest": ciscoClientCcxDiagRequest,
       "cldccDiagDhcpTestReqTable": cldccDiagDhcpTestReqTable,
       "cldccDiagDhcpTestReqEntry": cldccDiagDhcpTestReqEntry,
       "cldccDiagDhcpTestReqRowStatus": cldccDiagDhcpTestReqRowStatus,
       "cldccDiagPingTestReqTable": cldccDiagPingTestReqTable,
       "cldccDiagPingTestReqEntry": cldccDiagPingTestReqEntry,
       "cldccDiagPingTestType": cldccDiagPingTestType,
       "cldccDiagPingTestReqRowStatus": cldccDiagPingTestReqRowStatus,
       "cldccDiagDnsNameResolTestReqTable": cldccDiagDnsNameResolTestReqTable,
       "cldccDiagDnsNameResolTestReqEntry": cldccDiagDnsNameResolTestReqEntry,
       "cldccDiagDnsNameResolTestReqNetworkName": cldccDiagDnsNameResolTestReqNetworkName,
       "cldccDiagDnsNameResolTestReqRowStatus": cldccDiagDnsNameResolTestReqRowStatus,
       "cldccDiagAssociationTestReqTable": cldccDiagAssociationTestReqTable,
       "cldccDiagAssociationTestReqEntry": cldccDiagAssociationTestReqEntry,
       "cldccDiagAssocTestReqBssid": cldccDiagAssocTestReqBssid,
       "cldccDiagAssocTestReqSsid": cldccDiagAssocTestReqSsid,
       "cldccDiagAssocTestReqChannel": cldccDiagAssocTestReqChannel,
       "cldccDiagAssocTestReqBand": cldccDiagAssocTestReqBand,
       "cldccDiagAssocTestReqPhyType": cldccDiagAssocTestReqPhyType,
       "cldccDiagAssocTestReqRowStatus": cldccDiagAssocTestReqRowStatus,
       "cldccDiagAuthenticationTestReqTable": cldccDiagAuthenticationTestReqTable,
       "cldccDiagAuthenticationTestReqEntry": cldccDiagAuthenticationTestReqEntry,
       "cldccDiagAuthenticationTestReqBssid": cldccDiagAuthenticationTestReqBssid,
       "cldccDiagAuthenticationTestReqProfileId": cldccDiagAuthenticationTestReqProfileId,
       "cldccDiagAuthenticationTestReqChannel": cldccDiagAuthenticationTestReqChannel,
       "cldccDiagAuthenticationTestReqBand": cldccDiagAuthenticationTestReqBand,
       "cldccDiagAuthenticationTestReqPhyType": cldccDiagAuthenticationTestReqPhyType,
       "cldccDiagAuthenticationTestReqRowStatus": cldccDiagAuthenticationTestReqRowStatus,
       "cldccDiagMsgDisplayReqTable": cldccDiagMsgDisplayReqTable,
       "cldccDiagMsgDisplayReqEntry": cldccDiagMsgDisplayReqEntry,
       "cldccDiagMsgDisplayMsgType": cldccDiagMsgDisplayMsgType,
       "cldccDiagMsgDisplayReqRowStatus": cldccDiagMsgDisplayReqRowStatus,
       "cldccDiagProfileRedirectReqTable": cldccDiagProfileRedirectReqTable,
       "cldccDiagProfileRedirectReqEntry": cldccDiagProfileRedirectReqEntry,
       "cldccDiagProfileRedirectReqProfileId": cldccDiagProfileRedirectReqProfileId,
       "cldccDiagProfileRedirectReqRowStatus": cldccDiagProfileRedirectReqRowStatus,
       "ciscoClientCcxDiagResponse": ciscoClientCcxDiagResponse,
       "cldccDiagDhcpTestRespTable": cldccDiagDhcpTestRespTable,
       "cldccDiagDhcpTestRespEntry": cldccDiagDhcpTestRespEntry,
       "cldccDiagDhcpTestRespDhcpOffer": cldccDiagDhcpTestRespDhcpOffer,
       "cldccDiagPingTestRespTable": cldccDiagPingTestRespTable,
       "cldccDiagPingTestRespEntry": cldccDiagPingTestRespEntry,
       "cldccDiagPingTestRespIPAddressType": cldccDiagPingTestRespIPAddressType,
       "cldccDiagPingTestRespIPAddress": cldccDiagPingTestRespIPAddress,
       "cldccDiagPingTestRespDestMacAddress": cldccDiagPingTestRespDestMacAddress,
       "cldccDiagPingTestRespPingsSent": cldccDiagPingTestRespPingsSent,
       "cldccDiagPingTestRespPingsReceived": cldccDiagPingTestRespPingsReceived,
       "cldccDiagPingTestRespMinEchoTIme": cldccDiagPingTestRespMinEchoTIme,
       "cldccDiagPingTestRespMaxEchoTIme": cldccDiagPingTestRespMaxEchoTIme,
       "cldccDiagDnsNameResolTestRespTable": cldccDiagDnsNameResolTestRespTable,
       "cldccDiagDnsNameResolTestRespEntry": cldccDiagDnsNameResolTestRespEntry,
       "cldccDiagDnsNameResolTestRespIpAddressType": cldccDiagDnsNameResolTestRespIpAddressType,
       "cldccDiagDnsNameResolTestRespIpAddress": cldccDiagDnsNameResolTestRespIpAddress,
       "cldccDiagDnsNameResolTestRespServerName": cldccDiagDnsNameResolTestRespServerName,
       "cldccDiagAssociationTestRespTable": cldccDiagAssociationTestRespTable,
       "cldccDiagAssociationTestRespEntry": cldccDiagAssociationTestRespEntry,
       "cldccDiagAssociationTestRespIsAssocComplete": cldccDiagAssociationTestRespIsAssocComplete,
       "cldccDiagAssocTestRespReturnedStatus": cldccDiagAssocTestRespReturnedStatus,
       "cldccDiagAuthenticationTestRespTable": cldccDiagAuthenticationTestRespTable,
       "cldccDiagAuthenticationTestRespEntry": cldccDiagAuthenticationTestRespEntry,
       "cldccDiagAuthenticationTestRespIsCompleted": cldccDiagAuthenticationTestRespIsCompleted,
       "cldccDiagAuthenticationTestRespReturnedStatus": cldccDiagAuthenticationTestRespReturnedStatus,
       "cldccDiagAuthenticationTestRespEAPMethod": cldccDiagAuthenticationTestRespEAPMethod,
       "cldccDiagMsgDisplayRespTable": cldccDiagMsgDisplayRespTable,
       "cldccDiagMsgDisplayRespEntry": cldccDiagMsgDisplayRespEntry,
       "cldccDiagMsgDisplayRespString": cldccDiagMsgDisplayRespString,
       "cldccDiagTestLoggedFrameTable": cldccDiagTestLoggedFrameTable,
       "cldccDiagTestLoggedFrameEntry": cldccDiagTestLoggedFrameEntry,
       "cldccDiagTestLoggedFrameIndex": cldccDiagTestLoggedFrameIndex,
       "cldccDiagTestLoggedFrameDirection": cldccDiagTestLoggedFrameDirection,
       "cldccDiagTestLoggedFrameTimeStamp": cldccDiagTestLoggedFrameTimeStamp,
       "cldccDiagTestLoggedFrameData": cldccDiagTestLoggedFrameData,
       "ciscoClientCcxDiagStatus": ciscoClientCcxDiagStatus,
       "cldccDiagTestStatusTable": cldccDiagTestStatusTable,
       "cldccDiagTestStatusEntry": cldccDiagTestStatusEntry,
       "cldccDiagTestLastTestStatus": cldccDiagTestLastTestStatus,
       "cldccDiagTestLastResponseStatus": cldccDiagTestLastResponseStatus,
       "ciscoLwappDot11CcxClientDiagMIBNotifs": ciscoLwappDot11CcxClientDiagMIBNotifs,
       "cldccDiagClientAssociatedToDiagWlan": cldccDiagClientAssociatedToDiagWlan,
       "ciscoLwappDot11CcxClientDiagMIBNotifObjs": ciscoLwappDot11CcxClientDiagMIBNotifObjs,
       "cldccDiagClientMacAddress": cldccDiagClientMacAddress,
       "cldccDiagAssocReasonCode": cldccDiagAssocReasonCode}
)
