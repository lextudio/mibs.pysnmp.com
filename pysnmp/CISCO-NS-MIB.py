# SNMP MIB module (CISCO-NS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:13 2024
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

(FcAddressId,
 FcClassOfServices,
 FcNameId,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "FcClassOfServices",
    "FcNameId",
    "FcNameIdOrZero")

(notifyVsanIndex,
 vsanIndex) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "notifyVsanIndex",
    "vsanIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoNsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293)
)
ciscoNsMIB.setRevisions(
        ("2004-08-30 00:00",
         "2004-02-19 00:00",
         "2003-03-06 00:00",
         "2002-10-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcGs3RejectReasonCode(Integer32, TextualConvention):
    status = "current"
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
        *(("cmdNotSupported", 9),
          ("invalidCmdCode", 2),
          ("invalidIUSize", 5),
          ("invalidVerLevel", 3),
          ("logicalBusy", 6),
          ("logicalError", 4),
          ("none", 1),
          ("protocolError", 7),
          ("unableToPerformCmdReq", 8),
          ("vendorError", 10))
    )



class FcNameServerRejReasonExpl(Integer32, TextualConvention):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 17),
          ("classOfServiceNotRegistered", 5),
          ("databaseEmpty", 19),
          ("fabricPortNameNotRegistered", 13),
          ("fc4DescriptorNotRegistered", 15),
          ("fc4FeaturesNotRegistered", 16),
          ("fc4TypeNotRegistered", 8),
          ("hardAddressNotRegistered", 14),
          ("ipaNotRegistered", 7),
          ("noAdditionalExplanation", 1),
          ("noObjectRegInSpecifiedScope", 20),
          ("nodeIpAddressNotRegistered", 6),
          ("nodeNameNotRegistered", 4),
          ("portIdentifierNotRegistered", 2),
          ("portIpAddressNotRegistered", 12),
          ("portNameNotRegistered", 3),
          ("portTypeNotRegistered", 11),
          ("symbolicNodeNameNotRegistered", 10),
          ("symbolicPortNameNotRegistered", 9),
          ("unacceptablePortIdentifier", 18))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoNameServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNameServerMIBObjects = _CiscoNameServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1)
)
_FcNameServerConfiguration_ObjectIdentity = ObjectIdentity
fcNameServerConfiguration = _FcNameServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1)
)
_FcNameServerProxyPortTable_Object = MibTable
fcNameServerProxyPortTable = _FcNameServerProxyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fcNameServerProxyPortTable.setStatus("current")
_FcNameServerProxyPortEntry_Object = MibTableRow
fcNameServerProxyPortEntry = _FcNameServerProxyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1, 1)
)
fcNameServerProxyPortEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcNameServerProxyPortEntry.setStatus("current")


class _FcNameServerProxyPortName_Type(FcNameIdOrZero):
    """Custom type fcNameServerProxyPortName based on FcNameIdOrZero"""
    defaultHexValue = ""


_FcNameServerProxyPortName_Object = MibTableColumn
fcNameServerProxyPortName = _FcNameServerProxyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1, 1, 1),
    _FcNameServerProxyPortName_Type()
)
fcNameServerProxyPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerProxyPortName.setStatus("current")
_FcNameServerTableLastChange_Type = TimeStamp
_FcNameServerTableLastChange_Object = MibScalar
fcNameServerTableLastChange = _FcNameServerTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 2),
    _FcNameServerTableLastChange_Type()
)
fcNameServerTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerTableLastChange.setStatus("current")


class _FcNameServerNumRows_Type(Integer32):
    """Custom type fcNameServerNumRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FcNameServerNumRows_Type.__name__ = "Integer32"
_FcNameServerNumRows_Object = MibScalar
fcNameServerNumRows = _FcNameServerNumRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 3),
    _FcNameServerNumRows_Type()
)
fcNameServerNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerNumRows.setStatus("current")
_FcNameServerTable_Object = MibTable
fcNameServerTable = _FcNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fcNameServerTable.setStatus("current")
_FcNameServerEntry_Object = MibTableRow
fcNameServerEntry = _FcNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1)
)
fcNameServerEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-NS-MIB", "fcNameServerPortIdentifier"),
)
if mibBuilder.loadTexts:
    fcNameServerEntry.setStatus("current")
_FcNameServerPortIdentifier_Type = FcAddressId
_FcNameServerPortIdentifier_Object = MibTableColumn
fcNameServerPortIdentifier = _FcNameServerPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 1),
    _FcNameServerPortIdentifier_Type()
)
fcNameServerPortIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcNameServerPortIdentifier.setStatus("current")


class _FcNameServerPortName_Type(FcNameId):
    """Custom type fcNameServerPortName based on FcNameId"""
    defaultHexValue = "0000000000000000"


_FcNameServerPortName_Object = MibTableColumn
fcNameServerPortName = _FcNameServerPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 2),
    _FcNameServerPortName_Type()
)
fcNameServerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerPortName.setStatus("current")


class _FcNameServerNodeName_Type(FcNameId):
    """Custom type fcNameServerNodeName based on FcNameId"""
    defaultHexValue = "0000000000000000"


_FcNameServerNodeName_Object = MibTableColumn
fcNameServerNodeName = _FcNameServerNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 3),
    _FcNameServerNodeName_Type()
)
fcNameServerNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerNodeName.setStatus("current")
_FcNameServerClassOfSvc_Type = FcClassOfServices
_FcNameServerClassOfSvc_Object = MibTableColumn
fcNameServerClassOfSvc = _FcNameServerClassOfSvc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 4),
    _FcNameServerClassOfSvc_Type()
)
fcNameServerClassOfSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerClassOfSvc.setStatus("current")


class _FcNameServerNodeIpAddress_Type(OctetString):
    """Custom type fcNameServerNodeIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_FcNameServerNodeIpAddress_Type.__name__ = "OctetString"
_FcNameServerNodeIpAddress_Object = MibTableColumn
fcNameServerNodeIpAddress = _FcNameServerNodeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 5),
    _FcNameServerNodeIpAddress_Type()
)
fcNameServerNodeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerNodeIpAddress.setStatus("current")


class _FcNameServerProcAssoc_Type(OctetString):
    """Custom type fcNameServerProcAssoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FcNameServerProcAssoc_Type.__name__ = "OctetString"
_FcNameServerProcAssoc_Object = MibTableColumn
fcNameServerProcAssoc = _FcNameServerProcAssoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 6),
    _FcNameServerProcAssoc_Type()
)
fcNameServerProcAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerProcAssoc.setStatus("current")


class _FcNameServerFC4Type_Type(OctetString):
    """Custom type fcNameServerFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcNameServerFC4Type_Type.__name__ = "OctetString"
_FcNameServerFC4Type_Object = MibTableColumn
fcNameServerFC4Type = _FcNameServerFC4Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 7),
    _FcNameServerFC4Type_Type()
)
fcNameServerFC4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerFC4Type.setStatus("current")


class _FcNameServerPortType_Type(Integer32):
    """Custom type fcNameServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nPort", 2),
          ("nlPort", 3),
          ("unknown", 1))
    )


_FcNameServerPortType_Type.__name__ = "Integer32"
_FcNameServerPortType_Object = MibTableColumn
fcNameServerPortType = _FcNameServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 8),
    _FcNameServerPortType_Type()
)
fcNameServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerPortType.setStatus("current")


class _FcNameServerPortIpAddress_Type(OctetString):
    """Custom type fcNameServerPortIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_FcNameServerPortIpAddress_Type.__name__ = "OctetString"
_FcNameServerPortIpAddress_Object = MibTableColumn
fcNameServerPortIpAddress = _FcNameServerPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 9),
    _FcNameServerPortIpAddress_Type()
)
fcNameServerPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerPortIpAddress.setStatus("current")


class _FcNameServerFabricPortName_Type(FcNameId):
    """Custom type fcNameServerFabricPortName based on FcNameId"""
    defaultHexValue = "0000000000000000"


_FcNameServerFabricPortName_Object = MibTableColumn
fcNameServerFabricPortName = _FcNameServerFabricPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 10),
    _FcNameServerFabricPortName_Type()
)
fcNameServerFabricPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerFabricPortName.setStatus("current")
_FcNameServerHardAddress_Type = FcAddressId
_FcNameServerHardAddress_Object = MibTableColumn
fcNameServerHardAddress = _FcNameServerHardAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 11),
    _FcNameServerHardAddress_Type()
)
fcNameServerHardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerHardAddress.setStatus("current")


class _FcNameServerSymbolicPortName_Type(SnmpAdminString):
    """Custom type fcNameServerSymbolicPortName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FcNameServerSymbolicPortName_Type.__name__ = "SnmpAdminString"
_FcNameServerSymbolicPortName_Object = MibTableColumn
fcNameServerSymbolicPortName = _FcNameServerSymbolicPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 12),
    _FcNameServerSymbolicPortName_Type()
)
fcNameServerSymbolicPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerSymbolicPortName.setStatus("current")


class _FcNameServerSymbolicNodeName_Type(SnmpAdminString):
    """Custom type fcNameServerSymbolicNodeName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FcNameServerSymbolicNodeName_Type.__name__ = "SnmpAdminString"
_FcNameServerSymbolicNodeName_Object = MibTableColumn
fcNameServerSymbolicNodeName = _FcNameServerSymbolicNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 13),
    _FcNameServerSymbolicNodeName_Type()
)
fcNameServerSymbolicNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerSymbolicNodeName.setStatus("current")


class _FcNameServerFC4Features_Type(OctetString):
    """Custom type fcNameServerFC4Features based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FcNameServerFC4Features_Type.__name__ = "OctetString"
_FcNameServerFC4Features_Object = MibTableColumn
fcNameServerFC4Features = _FcNameServerFC4Features_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 14),
    _FcNameServerFC4Features_Type()
)
fcNameServerFC4Features.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerFC4Features.setStatus("current")


class _FcNameServerPortFunction_Type(Bits):
    """Custom type fcNameServerPortFunction based on Bits"""
    namedValues = NamedValues(
        *(("intPort", 4),
          ("ipfcPort", 3),
          ("trapPort", 0),
          ("vep", 1),
          ("volOwner", 2))
    )

_FcNameServerPortFunction_Type.__name__ = "Bits"
_FcNameServerPortFunction_Object = MibTableColumn
fcNameServerPortFunction = _FcNameServerPortFunction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 15),
    _FcNameServerPortFunction_Type()
)
fcNameServerPortFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerPortFunction.setStatus("deprecated")
_FcNameServerPermanentPortName_Type = FcNameId
_FcNameServerPermanentPortName_Object = MibTableColumn
fcNameServerPermanentPortName = _FcNameServerPermanentPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 16),
    _FcNameServerPermanentPortName_Type()
)
fcNameServerPermanentPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerPermanentPortName.setStatus("current")


class _FcNameServerRejReqNotifyEnable_Type(TruthValue):
    """Custom type fcNameServerRejReqNotifyEnable based on TruthValue"""


_FcNameServerRejReqNotifyEnable_Object = MibScalar
fcNameServerRejReqNotifyEnable = _FcNameServerRejReqNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 5),
    _FcNameServerRejReqNotifyEnable_Type()
)
fcNameServerRejReqNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNameServerRejReqNotifyEnable.setStatus("current")
_FcNameServerStats_ObjectIdentity = ObjectIdentity
fcNameServerStats = _FcNameServerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2)
)
_FcNameServerTotalRejects_Type = Counter32
_FcNameServerTotalRejects_Object = MibScalar
fcNameServerTotalRejects = _FcNameServerTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 1),
    _FcNameServerTotalRejects_Type()
)
fcNameServerTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerTotalRejects.setStatus("current")
_FcNameServerStatsTable_Object = MibTable
fcNameServerStatsTable = _FcNameServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fcNameServerStatsTable.setStatus("current")
_FcNameServerStatsEntry_Object = MibTableRow
fcNameServerStatsEntry = _FcNameServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1)
)
fcNameServerStatsEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    fcNameServerStatsEntry.setStatus("current")
_FcNameServerInGetReqs_Type = Counter32
_FcNameServerInGetReqs_Object = MibTableColumn
fcNameServerInGetReqs = _FcNameServerInGetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 1),
    _FcNameServerInGetReqs_Type()
)
fcNameServerInGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerInGetReqs.setStatus("current")
_FcNameServerOutGetReqs_Type = Counter32
_FcNameServerOutGetReqs_Object = MibTableColumn
fcNameServerOutGetReqs = _FcNameServerOutGetReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 2),
    _FcNameServerOutGetReqs_Type()
)
fcNameServerOutGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerOutGetReqs.setStatus("current")
_FcNameServerInRegReqs_Type = Counter32
_FcNameServerInRegReqs_Object = MibTableColumn
fcNameServerInRegReqs = _FcNameServerInRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 3),
    _FcNameServerInRegReqs_Type()
)
fcNameServerInRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerInRegReqs.setStatus("current")
_FcNameServerInDeRegReqs_Type = Counter32
_FcNameServerInDeRegReqs_Object = MibTableColumn
fcNameServerInDeRegReqs = _FcNameServerInDeRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 4),
    _FcNameServerInDeRegReqs_Type()
)
fcNameServerInDeRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerInDeRegReqs.setStatus("current")
_FcNameServerInRscns_Type = Counter32
_FcNameServerInRscns_Object = MibTableColumn
fcNameServerInRscns = _FcNameServerInRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 5),
    _FcNameServerInRscns_Type()
)
fcNameServerInRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerInRscns.setStatus("current")
_FcNameServerOutRscns_Type = Counter32
_FcNameServerOutRscns_Object = MibTableColumn
fcNameServerOutRscns = _FcNameServerOutRscns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 6),
    _FcNameServerOutRscns_Type()
)
fcNameServerOutRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerOutRscns.setStatus("current")
_FcNameServerRejects_Type = Counter32
_FcNameServerRejects_Object = MibTableColumn
fcNameServerRejects = _FcNameServerRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 7),
    _FcNameServerRejects_Type()
)
fcNameServerRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerRejects.setStatus("current")
_FcNameServerInformation_ObjectIdentity = ObjectIdentity
fcNameServerInformation = _FcNameServerInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3)
)
_FcNameServerRejectReasonCode_Type = FcGs3RejectReasonCode
_FcNameServerRejectReasonCode_Object = MibScalar
fcNameServerRejectReasonCode = _FcNameServerRejectReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3, 1),
    _FcNameServerRejectReasonCode_Type()
)
fcNameServerRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerRejectReasonCode.setStatus("current")
_FcNameServerRejReasonCodeExp_Type = FcNameServerRejReasonExpl
_FcNameServerRejReasonCodeExp_Object = MibScalar
fcNameServerRejReasonCodeExp = _FcNameServerRejReasonCodeExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3, 2),
    _FcNameServerRejReasonCodeExp_Type()
)
fcNameServerRejReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNameServerRejReasonCodeExp.setStatus("current")
_FcNameServerNotification_ObjectIdentity = ObjectIdentity
fcNameServerNotification = _FcNameServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4)
)
_FcNameServerNotifications_ObjectIdentity = ObjectIdentity
fcNameServerNotifications = _FcNameServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0)
)
_FcNameServerMIBConformance_ObjectIdentity = ObjectIdentity
fcNameServerMIBConformance = _FcNameServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2)
)
_FcNameServerMIBCompliances_ObjectIdentity = ObjectIdentity
fcNameServerMIBCompliances = _FcNameServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1)
)
_FcNameServerMIBGroups_ObjectIdentity = ObjectIdentity
fcNameServerMIBGroups = _FcNameServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2)
)

# Managed Objects groups

fcNameServerDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 1)
)
fcNameServerDBGroup.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerProxyPortName"),
        ("CISCO-NS-MIB", "fcNameServerNumRows"),
        ("CISCO-NS-MIB", "fcNameServerTableLastChange"),
        ("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerNodeName"),
        ("CISCO-NS-MIB", "fcNameServerClassOfSvc"),
        ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerProcAssoc"),
        ("CISCO-NS-MIB", "fcNameServerFC4Type"),
        ("CISCO-NS-MIB", "fcNameServerPortType"),
        ("CISCO-NS-MIB", "fcNameServerPortIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerFabricPortName"),
        ("CISCO-NS-MIB", "fcNameServerHardAddress"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"),
        ("CISCO-NS-MIB", "fcNameServerFC4Features"))
)
if mibBuilder.loadTexts:
    fcNameServerDBGroup.setStatus("deprecated")

fcNameServerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 2)
)
fcNameServerStatsGroup.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerTotalRejects"),
        ("CISCO-NS-MIB", "fcNameServerInGetReqs"),
        ("CISCO-NS-MIB", "fcNameServerOutGetReqs"),
        ("CISCO-NS-MIB", "fcNameServerInRegReqs"),
        ("CISCO-NS-MIB", "fcNameServerInDeRegReqs"),
        ("CISCO-NS-MIB", "fcNameServerInRscns"),
        ("CISCO-NS-MIB", "fcNameServerOutRscns"),
        ("CISCO-NS-MIB", "fcNameServerRejects"))
)
if mibBuilder.loadTexts:
    fcNameServerStatsGroup.setStatus("current")

fcNameServerNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 3)
)
fcNameServerNotifyControlGroup.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerRejectReasonCode"),
        ("CISCO-NS-MIB", "fcNameServerRejReasonCodeExp"),
        ("CISCO-NS-MIB", "fcNameServerRejReqNotifyEnable"))
)
if mibBuilder.loadTexts:
    fcNameServerNotifyControlGroup.setStatus("current")

fcNameServerDBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 5)
)
fcNameServerDBGroup1.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerProxyPortName"),
        ("CISCO-NS-MIB", "fcNameServerNumRows"),
        ("CISCO-NS-MIB", "fcNameServerTableLastChange"),
        ("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerNodeName"),
        ("CISCO-NS-MIB", "fcNameServerClassOfSvc"),
        ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerProcAssoc"),
        ("CISCO-NS-MIB", "fcNameServerFC4Type"),
        ("CISCO-NS-MIB", "fcNameServerPortType"),
        ("CISCO-NS-MIB", "fcNameServerPortIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerFabricPortName"),
        ("CISCO-NS-MIB", "fcNameServerHardAddress"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"),
        ("CISCO-NS-MIB", "fcNameServerFC4Features"),
        ("CISCO-NS-MIB", "fcNameServerPortFunction"))
)
if mibBuilder.loadTexts:
    fcNameServerDBGroup1.setStatus("deprecated")

fcNameServerDBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 7)
)
fcNameServerDBGroup2.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerProxyPortName"),
        ("CISCO-NS-MIB", "fcNameServerNumRows"),
        ("CISCO-NS-MIB", "fcNameServerTableLastChange"),
        ("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerNodeName"),
        ("CISCO-NS-MIB", "fcNameServerClassOfSvc"),
        ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerProcAssoc"),
        ("CISCO-NS-MIB", "fcNameServerFC4Type"),
        ("CISCO-NS-MIB", "fcNameServerPortType"),
        ("CISCO-NS-MIB", "fcNameServerPortIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerFabricPortName"),
        ("CISCO-NS-MIB", "fcNameServerHardAddress"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"),
        ("CISCO-NS-MIB", "fcNameServerFC4Features"))
)
if mibBuilder.loadTexts:
    fcNameServerDBGroup2.setStatus("current")

fcNameServerDBGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 8)
)
fcNameServerDBGroup3.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerProxyPortName"),
        ("CISCO-NS-MIB", "fcNameServerNumRows"),
        ("CISCO-NS-MIB", "fcNameServerTableLastChange"),
        ("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerNodeName"),
        ("CISCO-NS-MIB", "fcNameServerClassOfSvc"),
        ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerProcAssoc"),
        ("CISCO-NS-MIB", "fcNameServerFC4Type"),
        ("CISCO-NS-MIB", "fcNameServerPortType"),
        ("CISCO-NS-MIB", "fcNameServerPortIpAddress"),
        ("CISCO-NS-MIB", "fcNameServerFabricPortName"),
        ("CISCO-NS-MIB", "fcNameServerHardAddress"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"),
        ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"),
        ("CISCO-NS-MIB", "fcNameServerFC4Features"),
        ("CISCO-NS-MIB", "fcNameServerPermanentPortName"))
)
if mibBuilder.loadTexts:
    fcNameServerDBGroup3.setStatus("current")


# Notification objects

fcNameServerRejectRegNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 1)
)
fcNameServerRejectRegNotify.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerRejectReasonCode"),
        ("CISCO-NS-MIB", "fcNameServerRejReasonCodeExp"))
)
if mibBuilder.loadTexts:
    fcNameServerRejectRegNotify.setStatus(
        "current"
    )

fcNameServerDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 2)
)
fcNameServerDatabaseFull.setObjects(
    ("CISCO-VSAN-MIB", "notifyVsanIndex")
)
if mibBuilder.loadTexts:
    fcNameServerDatabaseFull.setStatus(
        "current"
    )

fcNameServerEntryAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 3)
)
fcNameServerEntryAdd.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerPortType"))
)
if mibBuilder.loadTexts:
    fcNameServerEntryAdd.setStatus(
        "current"
    )

fcNameServerEntryDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 4)
)
fcNameServerEntryDelete.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerPortName"),
        ("CISCO-NS-MIB", "fcNameServerPortType"))
)
if mibBuilder.loadTexts:
    fcNameServerEntryDelete.setStatus(
        "current"
    )


# Notifications groups

fcNameServerNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 4)
)
fcNameServerNotifyGroup.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerRejectRegNotify"),
        ("CISCO-NS-MIB", "fcNameServerDatabaseFull"))
)
if mibBuilder.loadTexts:
    fcNameServerNotifyGroup.setStatus(
        "deprecated"
    )

fcNameServerNotifyGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 6)
)
fcNameServerNotifyGroupRev1.setObjects(
      *(("CISCO-NS-MIB", "fcNameServerRejectRegNotify"),
        ("CISCO-NS-MIB", "fcNameServerDatabaseFull"),
        ("CISCO-NS-MIB", "fcNameServerEntryAdd"),
        ("CISCO-NS-MIB", "fcNameServerEntryDelete"))
)
if mibBuilder.loadTexts:
    fcNameServerNotifyGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fcNameServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcNameServerMIBCompliance.setStatus(
        "deprecated"
    )

fcNameServerMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fcNameServerMIBCompliance1.setStatus(
        "deprecated"
    )

fcNameServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fcNameServerMIBCompliance2.setStatus(
        "deprecated"
    )

fcNameServerMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 4)
)
if mibBuilder.loadTexts:
    fcNameServerMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NS-MIB",
    **{"FcGs3RejectReasonCode": FcGs3RejectReasonCode,
       "FcNameServerRejReasonExpl": FcNameServerRejReasonExpl,
       "ciscoNsMIB": ciscoNsMIB,
       "ciscoNameServerMIBObjects": ciscoNameServerMIBObjects,
       "fcNameServerConfiguration": fcNameServerConfiguration,
       "fcNameServerProxyPortTable": fcNameServerProxyPortTable,
       "fcNameServerProxyPortEntry": fcNameServerProxyPortEntry,
       "fcNameServerProxyPortName": fcNameServerProxyPortName,
       "fcNameServerTableLastChange": fcNameServerTableLastChange,
       "fcNameServerNumRows": fcNameServerNumRows,
       "fcNameServerTable": fcNameServerTable,
       "fcNameServerEntry": fcNameServerEntry,
       "fcNameServerPortIdentifier": fcNameServerPortIdentifier,
       "fcNameServerPortName": fcNameServerPortName,
       "fcNameServerNodeName": fcNameServerNodeName,
       "fcNameServerClassOfSvc": fcNameServerClassOfSvc,
       "fcNameServerNodeIpAddress": fcNameServerNodeIpAddress,
       "fcNameServerProcAssoc": fcNameServerProcAssoc,
       "fcNameServerFC4Type": fcNameServerFC4Type,
       "fcNameServerPortType": fcNameServerPortType,
       "fcNameServerPortIpAddress": fcNameServerPortIpAddress,
       "fcNameServerFabricPortName": fcNameServerFabricPortName,
       "fcNameServerHardAddress": fcNameServerHardAddress,
       "fcNameServerSymbolicPortName": fcNameServerSymbolicPortName,
       "fcNameServerSymbolicNodeName": fcNameServerSymbolicNodeName,
       "fcNameServerFC4Features": fcNameServerFC4Features,
       "fcNameServerPortFunction": fcNameServerPortFunction,
       "fcNameServerPermanentPortName": fcNameServerPermanentPortName,
       "fcNameServerRejReqNotifyEnable": fcNameServerRejReqNotifyEnable,
       "fcNameServerStats": fcNameServerStats,
       "fcNameServerTotalRejects": fcNameServerTotalRejects,
       "fcNameServerStatsTable": fcNameServerStatsTable,
       "fcNameServerStatsEntry": fcNameServerStatsEntry,
       "fcNameServerInGetReqs": fcNameServerInGetReqs,
       "fcNameServerOutGetReqs": fcNameServerOutGetReqs,
       "fcNameServerInRegReqs": fcNameServerInRegReqs,
       "fcNameServerInDeRegReqs": fcNameServerInDeRegReqs,
       "fcNameServerInRscns": fcNameServerInRscns,
       "fcNameServerOutRscns": fcNameServerOutRscns,
       "fcNameServerRejects": fcNameServerRejects,
       "fcNameServerInformation": fcNameServerInformation,
       "fcNameServerRejectReasonCode": fcNameServerRejectReasonCode,
       "fcNameServerRejReasonCodeExp": fcNameServerRejReasonCodeExp,
       "fcNameServerNotification": fcNameServerNotification,
       "fcNameServerNotifications": fcNameServerNotifications,
       "fcNameServerRejectRegNotify": fcNameServerRejectRegNotify,
       "fcNameServerDatabaseFull": fcNameServerDatabaseFull,
       "fcNameServerEntryAdd": fcNameServerEntryAdd,
       "fcNameServerEntryDelete": fcNameServerEntryDelete,
       "fcNameServerMIBConformance": fcNameServerMIBConformance,
       "fcNameServerMIBCompliances": fcNameServerMIBCompliances,
       "fcNameServerMIBCompliance": fcNameServerMIBCompliance,
       "fcNameServerMIBCompliance1": fcNameServerMIBCompliance1,
       "fcNameServerMIBCompliance2": fcNameServerMIBCompliance2,
       "fcNameServerMIBCompliance3": fcNameServerMIBCompliance3,
       "fcNameServerMIBGroups": fcNameServerMIBGroups,
       "fcNameServerDBGroup": fcNameServerDBGroup,
       "fcNameServerStatsGroup": fcNameServerStatsGroup,
       "fcNameServerNotifyControlGroup": fcNameServerNotifyControlGroup,
       "fcNameServerNotifyGroup": fcNameServerNotifyGroup,
       "fcNameServerDBGroup1": fcNameServerDBGroup1,
       "fcNameServerNotifyGroupRev1": fcNameServerNotifyGroupRev1,
       "fcNameServerDBGroup2": fcNameServerDBGroup2,
       "fcNameServerDBGroup3": fcNameServerDBGroup3}
)
