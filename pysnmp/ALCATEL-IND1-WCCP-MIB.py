# SNMP MIB module (ALCATEL-IND1-WCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-WCCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:38 2024
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

(softentIND1Wccp,
 wccpTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Wccp",
    "wccpTraps")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1WCCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WccpServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("standard", 1),
          ("unknown", 3))
    )



class WccpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 3),
          ("version1", 1),
          ("version2", 2))
    )



class WccpServiceProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("unknown", 3))
    )



class WccpServiceMessageType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1),
          ("unknown", 3))
    )



class WccpServicePortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1),
          ("unknown", 3))
    )



class WccpOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1WCCPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBNotifications = _AlcatelIND1WCCPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBNotifications.setStatus("current")
_AlcatelIND1WCCPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBObjects = _AlcatelIND1WCCPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBObjects.setStatus("current")
_WccpFeature_ObjectIdentity = ObjectIdentity
wccpFeature = _WccpFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 1)
)
_WccpAdminEnabled_Type = TruthValue
_WccpAdminEnabled_Object = MibScalar
wccpAdminEnabled = _WccpAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 1, 1),
    _WccpAdminEnabled_Type()
)
wccpAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpAdminEnabled.setStatus("current")
_WccpServiceCount_Type = Counter32
_WccpServiceCount_Object = MibScalar
wccpServiceCount = _WccpServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 1, 2),
    _WccpServiceCount_Type()
)
wccpServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceCount.setStatus("current")


class _WccpGlobalStatsReset_Type(Integer32):
    """Custom type wccpGlobalStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_WccpGlobalStatsReset_Type.__name__ = "Integer32"
_WccpGlobalStatsReset_Object = MibScalar
wccpGlobalStatsReset = _WccpGlobalStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 1, 3),
    _WccpGlobalStatsReset_Type()
)
wccpGlobalStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpGlobalStatsReset.setStatus("current")
_WccpGlobalStatsMessageInvalid_Type = Counter32
_WccpGlobalStatsMessageInvalid_Object = MibScalar
wccpGlobalStatsMessageInvalid = _WccpGlobalStatsMessageInvalid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 1, 4),
    _WccpGlobalStatsMessageInvalid_Type()
)
wccpGlobalStatsMessageInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpGlobalStatsMessageInvalid.setStatus("current")
_WccpServices_ObjectIdentity = ObjectIdentity
wccpServices = _WccpServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2)
)
_WccpServiceTable_Object = MibTable
wccpServiceTable = _WccpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wccpServiceTable.setStatus("current")
_WccpServiceTableEntry_Object = MibTableRow
wccpServiceTableEntry = _WccpServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1)
)
wccpServiceTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpServiceId"),
)
if mibBuilder.loadTexts:
    wccpServiceTableEntry.setStatus("current")


class _WccpServiceId_Type(Integer32):
    """Custom type wccpServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpServiceId_Type.__name__ = "Integer32"
_WccpServiceId_Object = MibTableColumn
wccpServiceId = _WccpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 1),
    _WccpServiceId_Type()
)
wccpServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpServiceId.setStatus("current")
_WccpServiceProtocol_Type = WccpServiceProtocolType
_WccpServiceProtocol_Object = MibTableColumn
wccpServiceProtocol = _WccpServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 2),
    _WccpServiceProtocol_Type()
)
wccpServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceProtocol.setStatus("current")
_WccpServiceMessageType_Type = WccpServiceMessageType
_WccpServiceMessageType_Object = MibTableColumn
wccpServiceMessageType = _WccpServiceMessageType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 3),
    _WccpServiceMessageType_Type()
)
wccpServiceMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceMessageType.setStatus("current")
_WccpServicePortType_Type = WccpServicePortType
_WccpServicePortType_Object = MibTableColumn
wccpServicePortType = _WccpServicePortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 4),
    _WccpServicePortType_Type()
)
wccpServicePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServicePortType.setStatus("current")
_WccpServiceAdminEnabled_Type = TruthValue
_WccpServiceAdminEnabled_Object = MibTableColumn
wccpServiceAdminEnabled = _WccpServiceAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 5),
    _WccpServiceAdminEnabled_Type()
)
wccpServiceAdminEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpServiceAdminEnabled.setStatus("current")


class _WccpServicePassword_Type(SnmpAdminString):
    """Custom type wccpServicePassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WccpServicePassword_Type.__name__ = "SnmpAdminString"
_WccpServicePassword_Object = MibTableColumn
wccpServicePassword = _WccpServicePassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 6),
    _WccpServicePassword_Type()
)
wccpServicePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpServicePassword.setStatus("current")
_WccpServiceType_Type = WccpServiceType
_WccpServiceType_Object = MibTableColumn
wccpServiceType = _WccpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 7),
    _WccpServiceType_Type()
)
wccpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceType.setStatus("current")
_WccpServiceVersion_Type = WccpVersion
_WccpServiceVersion_Object = MibTableColumn
wccpServiceVersion = _WccpServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 8),
    _WccpServiceVersion_Type()
)
wccpServiceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceVersion.setStatus("current")
_WccpServiceWebCacheCount_Type = Counter32
_WccpServiceWebCacheCount_Object = MibTableColumn
wccpServiceWebCacheCount = _WccpServiceWebCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 9),
    _WccpServiceWebCacheCount_Type()
)
wccpServiceWebCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceWebCacheCount.setStatus("current")
_WccpServiceReceiveId_Type = Counter32
_WccpServiceReceiveId_Object = MibTableColumn
wccpServiceReceiveId = _WccpServiceReceiveId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 10),
    _WccpServiceReceiveId_Type()
)
wccpServiceReceiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceReceiveId.setStatus("current")
_WccpServiceChangeNumber_Type = Counter32
_WccpServiceChangeNumber_Object = MibTableColumn
wccpServiceChangeNumber = _WccpServiceChangeNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 11),
    _WccpServiceChangeNumber_Type()
)
wccpServiceChangeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServiceChangeNumber.setStatus("current")


class _WccpServicePrecedence_Type(Integer32):
    """Custom type wccpServicePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpServicePrecedence_Type.__name__ = "Integer32"
_WccpServicePrecedence_Object = MibTableColumn
wccpServicePrecedence = _WccpServicePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 12),
    _WccpServicePrecedence_Type()
)
wccpServicePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServicePrecedence.setStatus("current")
_WccpServiceRowStatus_Type = RowStatus
_WccpServiceRowStatus_Object = MibTableColumn
wccpServiceRowStatus = _WccpServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 1, 1, 13),
    _WccpServiceRowStatus_Type()
)
wccpServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpServiceRowStatus.setStatus("current")
_WccpServicePortTable_Object = MibTable
wccpServicePortTable = _WccpServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wccpServicePortTable.setStatus("current")
_WccpServicePortTableEntry_Object = MibTableRow
wccpServicePortTableEntry = _WccpServicePortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 2, 1)
)
wccpServicePortTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpServicePortServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpServicePortPortId"),
)
if mibBuilder.loadTexts:
    wccpServicePortTableEntry.setStatus("current")


class _WccpServicePortServiceId_Type(Integer32):
    """Custom type wccpServicePortServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpServicePortServiceId_Type.__name__ = "Integer32"
_WccpServicePortServiceId_Object = MibTableColumn
wccpServicePortServiceId = _WccpServicePortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 2, 1, 1),
    _WccpServicePortServiceId_Type()
)
wccpServicePortServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpServicePortServiceId.setStatus("current")


class _WccpServicePortPortId_Type(Integer32):
    """Custom type wccpServicePortPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WccpServicePortPortId_Type.__name__ = "Integer32"
_WccpServicePortPortId_Object = MibTableColumn
wccpServicePortPortId = _WccpServicePortPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 2, 1, 2),
    _WccpServicePortPortId_Type()
)
wccpServicePortPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpServicePortPortId.setStatus("current")
_WccpServicePortPortNum_Type = Integer32
_WccpServicePortPortNum_Object = MibTableColumn
wccpServicePortPortNum = _WccpServicePortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 2, 2, 1, 3),
    _WccpServicePortPortNum_Type()
)
wccpServicePortPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpServicePortPortNum.setStatus("current")
_WccpWebCaches_ObjectIdentity = ObjectIdentity
wccpWebCaches = _WccpWebCaches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3)
)
_WccpWebCacheTable_Object = MibTable
wccpWebCacheTable = _WccpWebCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wccpWebCacheTable.setStatus("current")
_WccpWebCacheTableEntry_Object = MibTableRow
wccpWebCacheTableEntry = _WccpWebCacheTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1)
)
wccpWebCacheTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpWebCacheServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpWebCacheIpAddressType"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpWebCacheIpAddress"),
)
if mibBuilder.loadTexts:
    wccpWebCacheTableEntry.setStatus("current")


class _WccpWebCacheServiceId_Type(Integer32):
    """Custom type wccpWebCacheServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpWebCacheServiceId_Type.__name__ = "Integer32"
_WccpWebCacheServiceId_Object = MibTableColumn
wccpWebCacheServiceId = _WccpWebCacheServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 1),
    _WccpWebCacheServiceId_Type()
)
wccpWebCacheServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpWebCacheServiceId.setStatus("current")


class _WccpWebCacheIpAddressType_Type(InetAddressType):
    """Custom type wccpWebCacheIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WccpWebCacheIpAddressType_Type.__name__ = "InetAddressType"
_WccpWebCacheIpAddressType_Object = MibTableColumn
wccpWebCacheIpAddressType = _WccpWebCacheIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 2),
    _WccpWebCacheIpAddressType_Type()
)
wccpWebCacheIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpWebCacheIpAddressType.setStatus("current")


class _WccpWebCacheIpAddress_Type(InetAddress):
    """Custom type wccpWebCacheIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_WccpWebCacheIpAddress_Type.__name__ = "InetAddress"
_WccpWebCacheIpAddress_Object = MibTableColumn
wccpWebCacheIpAddress = _WccpWebCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 3),
    _WccpWebCacheIpAddress_Type()
)
wccpWebCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpWebCacheIpAddress.setStatus("current")
_WccpWebCacheProtoVersion_Type = WccpVersion
_WccpWebCacheProtoVersion_Object = MibTableColumn
wccpWebCacheProtoVersion = _WccpWebCacheProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 4),
    _WccpWebCacheProtoVersion_Type()
)
wccpWebCacheProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheProtoVersion.setStatus("current")
_WccpWebCacheReceiveId_Type = Counter32
_WccpWebCacheReceiveId_Object = MibTableColumn
wccpWebCacheReceiveId = _WccpWebCacheReceiveId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 5),
    _WccpWebCacheReceiveId_Type()
)
wccpWebCacheReceiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheReceiveId.setStatus("current")
_WccpWebCacheChangeNum_Type = Counter32
_WccpWebCacheChangeNum_Object = MibTableColumn
wccpWebCacheChangeNum = _WccpWebCacheChangeNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 6),
    _WccpWebCacheChangeNum_Type()
)
wccpWebCacheChangeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheChangeNum.setStatus("current")
_WccpWebCacheNumberOfRouters_Type = Counter32
_WccpWebCacheNumberOfRouters_Object = MibTableColumn
wccpWebCacheNumberOfRouters = _WccpWebCacheNumberOfRouters_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 7),
    _WccpWebCacheNumberOfRouters_Type()
)
wccpWebCacheNumberOfRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheNumberOfRouters.setStatus("current")
_WccpWebCacheNumberOfWebCaches_Type = Counter32
_WccpWebCacheNumberOfWebCaches_Object = MibTableColumn
wccpWebCacheNumberOfWebCaches = _WccpWebCacheNumberOfWebCaches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 8),
    _WccpWebCacheNumberOfWebCaches_Type()
)
wccpWebCacheNumberOfWebCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheNumberOfWebCaches.setStatus("current")
_WccpWebCacheState_Type = WccpOperState
_WccpWebCacheState_Object = MibTableColumn
wccpWebCacheState = _WccpWebCacheState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 9),
    _WccpWebCacheState_Type()
)
wccpWebCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheState.setStatus("current")
_WccpWebCacheConnectTime_Type = DateAndTime
_WccpWebCacheConnectTime_Object = MibTableColumn
wccpWebCacheConnectTime = _WccpWebCacheConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 3, 1, 1, 10),
    _WccpWebCacheConnectTime_Type()
)
wccpWebCacheConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpWebCacheConnectTime.setStatus("current")
_WccpRouters_ObjectIdentity = ObjectIdentity
wccpRouters = _WccpRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4)
)
_WccpRouterTable_Object = MibTable
wccpRouterTable = _WccpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wccpRouterTable.setStatus("current")
_WccpRouterTableEntry_Object = MibTableRow
wccpRouterTableEntry = _WccpRouterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1, 1)
)
wccpRouterTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRouterServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRouterIpAddressType"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRouterIpAddress"),
)
if mibBuilder.loadTexts:
    wccpRouterTableEntry.setStatus("current")


class _WccpRouterServiceId_Type(Integer32):
    """Custom type wccpRouterServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpRouterServiceId_Type.__name__ = "Integer32"
_WccpRouterServiceId_Object = MibTableColumn
wccpRouterServiceId = _WccpRouterServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1, 1, 1),
    _WccpRouterServiceId_Type()
)
wccpRouterServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRouterServiceId.setStatus("current")


class _WccpRouterIpAddressType_Type(InetAddressType):
    """Custom type wccpRouterIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WccpRouterIpAddressType_Type.__name__ = "InetAddressType"
_WccpRouterIpAddressType_Object = MibTableColumn
wccpRouterIpAddressType = _WccpRouterIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1, 1, 2),
    _WccpRouterIpAddressType_Type()
)
wccpRouterIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRouterIpAddressType.setStatus("current")


class _WccpRouterIpAddress_Type(InetAddress):
    """Custom type wccpRouterIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_WccpRouterIpAddress_Type.__name__ = "InetAddress"
_WccpRouterIpAddress_Object = MibTableColumn
wccpRouterIpAddress = _WccpRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1, 1, 3),
    _WccpRouterIpAddress_Type()
)
wccpRouterIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRouterIpAddress.setStatus("current")
_WccpRouterProtoVersion_Type = WccpVersion
_WccpRouterProtoVersion_Object = MibTableColumn
wccpRouterProtoVersion = _WccpRouterProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 4, 1, 1, 4),
    _WccpRouterProtoVersion_Type()
)
wccpRouterProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpRouterProtoVersion.setStatus("current")
_WccpRestrictVlan_ObjectIdentity = ObjectIdentity
wccpRestrictVlan = _WccpRestrictVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5)
)
_WccpRestrictVlanTable_Object = MibTable
wccpRestrictVlanTable = _WccpRestrictVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wccpRestrictVlanTable.setStatus("current")
_WccpRestrictVlanTableEntry_Object = MibTableRow
wccpRestrictVlanTableEntry = _WccpRestrictVlanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5, 1, 1)
)
wccpRestrictVlanTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanVlanId"),
)
if mibBuilder.loadTexts:
    wccpRestrictVlanTableEntry.setStatus("current")


class _WccpRestrictVlanServiceId_Type(Integer32):
    """Custom type wccpRestrictVlanServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpRestrictVlanServiceId_Type.__name__ = "Integer32"
_WccpRestrictVlanServiceId_Object = MibTableColumn
wccpRestrictVlanServiceId = _WccpRestrictVlanServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5, 1, 1, 1),
    _WccpRestrictVlanServiceId_Type()
)
wccpRestrictVlanServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictVlanServiceId.setStatus("current")


class _WccpRestrictVlanVlanId_Type(Integer32):
    """Custom type wccpRestrictVlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WccpRestrictVlanVlanId_Type.__name__ = "Integer32"
_WccpRestrictVlanVlanId_Object = MibTableColumn
wccpRestrictVlanVlanId = _WccpRestrictVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5, 1, 1, 2),
    _WccpRestrictVlanVlanId_Type()
)
wccpRestrictVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictVlanVlanId.setStatus("current")
_WccpRestrictVlanRowStatus_Type = RowStatus
_WccpRestrictVlanRowStatus_Object = MibTableColumn
wccpRestrictVlanRowStatus = _WccpRestrictVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 5, 1, 1, 3),
    _WccpRestrictVlanRowStatus_Type()
)
wccpRestrictVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpRestrictVlanRowStatus.setStatus("current")
_WccpRestrictWebCache_ObjectIdentity = ObjectIdentity
wccpRestrictWebCache = _WccpRestrictWebCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6)
)
_WccpRestrictWebCacheTable_Object = MibTable
wccpRestrictWebCacheTable = _WccpRestrictWebCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheTable.setStatus("current")
_WccpRestrictWebCacheTableEntry_Object = MibTableRow
wccpRestrictWebCacheTableEntry = _WccpRestrictWebCacheTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1)
)
wccpRestrictWebCacheTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpAddressType"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpAddress"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpMaskAddressType"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheIpMask"),
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheTableEntry.setStatus("current")


class _WccpRestrictWebCacheServiceId_Type(Integer32):
    """Custom type wccpRestrictWebCacheServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpRestrictWebCacheServiceId_Type.__name__ = "Integer32"
_WccpRestrictWebCacheServiceId_Object = MibTableColumn
wccpRestrictWebCacheServiceId = _WccpRestrictWebCacheServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 1),
    _WccpRestrictWebCacheServiceId_Type()
)
wccpRestrictWebCacheServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheServiceId.setStatus("current")


class _WccpRestrictWebCacheIpAddressType_Type(InetAddressType):
    """Custom type wccpRestrictWebCacheIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WccpRestrictWebCacheIpAddressType_Type.__name__ = "InetAddressType"
_WccpRestrictWebCacheIpAddressType_Object = MibTableColumn
wccpRestrictWebCacheIpAddressType = _WccpRestrictWebCacheIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 2),
    _WccpRestrictWebCacheIpAddressType_Type()
)
wccpRestrictWebCacheIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpAddressType.setStatus("current")


class _WccpRestrictWebCacheIpAddress_Type(InetAddress):
    """Custom type wccpRestrictWebCacheIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_WccpRestrictWebCacheIpAddress_Type.__name__ = "InetAddress"
_WccpRestrictWebCacheIpAddress_Object = MibTableColumn
wccpRestrictWebCacheIpAddress = _WccpRestrictWebCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 3),
    _WccpRestrictWebCacheIpAddress_Type()
)
wccpRestrictWebCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpAddress.setStatus("current")


class _WccpRestrictWebCacheIpMaskAddressType_Type(InetAddressType):
    """Custom type wccpRestrictWebCacheIpMaskAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WccpRestrictWebCacheIpMaskAddressType_Type.__name__ = "InetAddressType"
_WccpRestrictWebCacheIpMaskAddressType_Object = MibTableColumn
wccpRestrictWebCacheIpMaskAddressType = _WccpRestrictWebCacheIpMaskAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 4),
    _WccpRestrictWebCacheIpMaskAddressType_Type()
)
wccpRestrictWebCacheIpMaskAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpMaskAddressType.setStatus("current")


class _WccpRestrictWebCacheIpMask_Type(InetAddress):
    """Custom type wccpRestrictWebCacheIpMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_WccpRestrictWebCacheIpMask_Type.__name__ = "InetAddress"
_WccpRestrictWebCacheIpMask_Object = MibTableColumn
wccpRestrictWebCacheIpMask = _WccpRestrictWebCacheIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 5),
    _WccpRestrictWebCacheIpMask_Type()
)
wccpRestrictWebCacheIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheIpMask.setStatus("current")
_WccpRestrictWebCacheRowStatus_Type = RowStatus
_WccpRestrictWebCacheRowStatus_Object = MibTableColumn
wccpRestrictWebCacheRowStatus = _WccpRestrictWebCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 6, 1, 1, 6),
    _WccpRestrictWebCacheRowStatus_Type()
)
wccpRestrictWebCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpRestrictWebCacheRowStatus.setStatus("current")
_WccpRestrictPort_ObjectIdentity = ObjectIdentity
wccpRestrictPort = _WccpRestrictPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7)
)
_WccpRestrictPortTable_Object = MibTable
wccpRestrictPortTable = _WccpRestrictPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    wccpRestrictPortTable.setStatus("current")
_WccpRestrictPortTableEntry_Object = MibTableRow
wccpRestrictPortTableEntry = _WccpRestrictPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7, 1, 1)
)
wccpRestrictPortTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictPortServiceId"),
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpRestrictPortIndex"),
)
if mibBuilder.loadTexts:
    wccpRestrictPortTableEntry.setStatus("current")


class _WccpRestrictPortServiceId_Type(Integer32):
    """Custom type wccpRestrictPortServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpRestrictPortServiceId_Type.__name__ = "Integer32"
_WccpRestrictPortServiceId_Object = MibTableColumn
wccpRestrictPortServiceId = _WccpRestrictPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7, 1, 1, 1),
    _WccpRestrictPortServiceId_Type()
)
wccpRestrictPortServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictPortServiceId.setStatus("current")
_WccpRestrictPortIndex_Type = InterfaceIndex
_WccpRestrictPortIndex_Object = MibTableColumn
wccpRestrictPortIndex = _WccpRestrictPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7, 1, 1, 2),
    _WccpRestrictPortIndex_Type()
)
wccpRestrictPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpRestrictPortIndex.setStatus("current")
_WccpRestrictPortRowStatus_Type = RowStatus
_WccpRestrictPortRowStatus_Object = MibTableColumn
wccpRestrictPortRowStatus = _WccpRestrictPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 7, 1, 1, 3),
    _WccpRestrictPortRowStatus_Type()
)
wccpRestrictPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wccpRestrictPortRowStatus.setStatus("current")
_WccpStatistics_ObjectIdentity = ObjectIdentity
wccpStatistics = _WccpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8)
)
_WccpStatisticsTable_Object = MibTable
wccpStatisticsTable = _WccpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    wccpStatisticsTable.setStatus("current")
_WccpStatisticsTableEntry_Object = MibTableRow
wccpStatisticsTableEntry = _WccpStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1)
)
wccpStatisticsTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-WCCP-MIB", "wccpStatsServiceId"),
)
if mibBuilder.loadTexts:
    wccpStatisticsTableEntry.setStatus("current")


class _WccpStatsServiceId_Type(Integer32):
    """Custom type wccpStatsServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WccpStatsServiceId_Type.__name__ = "Integer32"
_WccpStatsServiceId_Object = MibTableColumn
wccpStatsServiceId = _WccpStatsServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 1),
    _WccpStatsServiceId_Type()
)
wccpStatsServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wccpStatsServiceId.setStatus("current")
_WccpStatsMessagesReceived_Type = Counter32
_WccpStatsMessagesReceived_Object = MibTableColumn
wccpStatsMessagesReceived = _WccpStatsMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 2),
    _WccpStatsMessagesReceived_Type()
)
wccpStatsMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsMessagesReceived.setStatus("current")
_WccpStatsMessagesTransmitted_Type = Counter32
_WccpStatsMessagesTransmitted_Object = MibTableColumn
wccpStatsMessagesTransmitted = _WccpStatsMessagesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 3),
    _WccpStatsMessagesTransmitted_Type()
)
wccpStatsMessagesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsMessagesTransmitted.setStatus("current")
_WccpStatsMessagesDropped_Type = Counter32
_WccpStatsMessagesDropped_Object = MibTableColumn
wccpStatsMessagesDropped = _WccpStatsMessagesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 4),
    _WccpStatsMessagesDropped_Type()
)
wccpStatsMessagesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsMessagesDropped.setStatus("current")
_WccpStatsPacketsRedir_Type = Counter32
_WccpStatsPacketsRedir_Object = MibTableColumn
wccpStatsPacketsRedir = _WccpStatsPacketsRedir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 5),
    _WccpStatsPacketsRedir_Type()
)
wccpStatsPacketsRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsPacketsRedir.setStatus("current")
_WccpStatsPacketsLowRedir_Type = Counter32
_WccpStatsPacketsLowRedir_Object = MibTableColumn
wccpStatsPacketsLowRedir = _WccpStatsPacketsLowRedir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 6),
    _WccpStatsPacketsLowRedir_Type()
)
wccpStatsPacketsLowRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsPacketsLowRedir.setStatus("current")
_WccpStatsPacketsDeniedRedir_Type = Counter32
_WccpStatsPacketsDeniedRedir_Object = MibTableColumn
wccpStatsPacketsDeniedRedir = _WccpStatsPacketsDeniedRedir_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 7),
    _WccpStatsPacketsDeniedRedir_Type()
)
wccpStatsPacketsDeniedRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsPacketsDeniedRedir.setStatus("current")
_WccpStatsAuthFailures_Type = Counter32
_WccpStatsAuthFailures_Object = MibTableColumn
wccpStatsAuthFailures = _WccpStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 8),
    _WccpStatsAuthFailures_Type()
)
wccpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpStatsAuthFailures.setStatus("current")


class _WccpStatsReset_Type(Integer32):
    """Custom type wccpStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_WccpStatsReset_Type.__name__ = "Integer32"
_WccpStatsReset_Object = MibTableColumn
wccpStatsReset = _WccpStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 8, 1, 1, 9),
    _WccpStatsReset_Type()
)
wccpStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wccpStatsReset.setStatus("current")
_WccpTrapsObj_ObjectIdentity = ObjectIdentity
wccpTrapsObj = _WccpTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 9)
)
_WccpTrapInfoServiceId_Type = Integer32
_WccpTrapInfoServiceId_Object = MibScalar
wccpTrapInfoServiceId = _WccpTrapInfoServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 9, 1),
    _WccpTrapInfoServiceId_Type()
)
wccpTrapInfoServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoServiceId.setStatus("current")
_WccpTrapInfoOperStatus_Type = WccpOperState
_WccpTrapInfoOperStatus_Object = MibScalar
wccpTrapInfoOperStatus = _WccpTrapInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 9, 2),
    _WccpTrapInfoOperStatus_Type()
)
wccpTrapInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoOperStatus.setStatus("current")
_WccpTrapInfoWebCacheIpAddr_Type = IpAddress
_WccpTrapInfoWebCacheIpAddr_Object = MibScalar
wccpTrapInfoWebCacheIpAddr = _WccpTrapInfoWebCacheIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 9, 3),
    _WccpTrapInfoWebCacheIpAddr_Type()
)
wccpTrapInfoWebCacheIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoWebCacheIpAddr.setStatus("current")


class _WccpTrapInfoEntityGroup_Type(Integer32):
    """Custom type wccpTrapInfoEntityGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("service", 2),
          ("wccp", 1),
          ("webcache", 3))
    )


_WccpTrapInfoEntityGroup_Type.__name__ = "Integer32"
_WccpTrapInfoEntityGroup_Object = MibScalar
wccpTrapInfoEntityGroup = _WccpTrapInfoEntityGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 1, 9, 4),
    _WccpTrapInfoEntityGroup_Type()
)
wccpTrapInfoEntityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wccpTrapInfoEntityGroup.setStatus("current")
_AlcatelIND1WCCPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBConformance = _AlcatelIND1WCCPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBConformance.setStatus("current")
_AlcatelIND1WCCPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBGroups = _AlcatelIND1WCCPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBGroups.setStatus("current")
_AlcatelIND1WCCPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1WCCPMIBCompliances = _AlcatelIND1WCCPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBCompliances.setStatus("current")

# Managed Objects groups

wccpFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 1)
)
wccpFeatureGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpAdminEnabled"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceCount"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpGlobalStatsMessageInvalid"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpGlobalStatsReset"))
)
if mibBuilder.loadTexts:
    wccpFeatureGroup.setStatus("current")

wccpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 2)
)
wccpServiceGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpServiceProtocol"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceMessageType"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePortType"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceAdminEnabled"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePassword"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceType"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceVersion"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceWebCacheCount"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceReceiveId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceChangeNumber"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePrecedence"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServiceRowStatus"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpServicePortPortNum"))
)
if mibBuilder.loadTexts:
    wccpServiceGroup.setStatus("current")

wccpWebCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 3)
)
wccpWebCacheGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheProtoVersion"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheReceiveId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheChangeNum"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheNumberOfRouters"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheNumberOfWebCaches"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheConnectTime"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpWebCacheState"))
)
if mibBuilder.loadTexts:
    wccpWebCacheGroup.setStatus("current")

wccpRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 4)
)
wccpRouterGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpRouterProtoVersion")
)
if mibBuilder.loadTexts:
    wccpRouterGroup.setStatus("current")

wccpRestrictVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 5)
)
wccpRestrictVlanGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictVlanRowStatus")
)
if mibBuilder.loadTexts:
    wccpRestrictVlanGroup.setStatus("current")

wccpRestrictWebCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 6)
)
wccpRestrictWebCacheGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictWebCacheRowStatus")
)
if mibBuilder.loadTexts:
    wccpRestrictWebCacheGroup.setStatus("current")

wccpRestrictPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 7)
)
wccpRestrictPortGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpRestrictPortRowStatus")
)
if mibBuilder.loadTexts:
    wccpRestrictPortGroup.setStatus("current")

wccpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 8)
)
wccpStatisticsGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpStatsMessagesReceived"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsMessagesTransmitted"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsMessagesDropped"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsPacketsRedir"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsPacketsLowRedir"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsPacketsDeniedRedir"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsAuthFailures"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpStatsReset"))
)
if mibBuilder.loadTexts:
    wccpStatisticsGroup.setStatus("current")

wccpOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 10)
)
wccpOperStatusGroup.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoEntityGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoOperStatus"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoServiceId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoWebCacheIpAddr"))
)
if mibBuilder.loadTexts:
    wccpOperStatusGroup.setStatus("current")


# Notification objects

wccpTrapOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 0, 1)
)
wccpTrapOperStatus.setObjects(
      *(("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoEntityGroup"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoOperStatus"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoServiceId"),
        ("ALCATEL-IND1-WCCP-MIB", "wccpTrapInfoWebCacheIpAddr"))
)
if mibBuilder.loadTexts:
    wccpTrapOperStatus.setStatus(
        "current"
    )


# Notifications groups

wccpTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 1, 9)
)
wccpTrapsGroup.setObjects(
    ("ALCATEL-IND1-WCCP-MIB", "wccpTrapOperStatus")
)
if mibBuilder.loadTexts:
    wccpTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1WCCPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 38, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1WCCPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-WCCP-MIB",
    **{"WccpServiceType": WccpServiceType,
       "WccpVersion": WccpVersion,
       "WccpServiceProtocolType": WccpServiceProtocolType,
       "WccpServiceMessageType": WccpServiceMessageType,
       "WccpServicePortType": WccpServicePortType,
       "WccpOperState": WccpOperState,
       "alcatelIND1WCCPMIB": alcatelIND1WCCPMIB,
       "alcatelIND1WCCPMIBNotifications": alcatelIND1WCCPMIBNotifications,
       "wccpTrapOperStatus": wccpTrapOperStatus,
       "alcatelIND1WCCPMIBObjects": alcatelIND1WCCPMIBObjects,
       "wccpFeature": wccpFeature,
       "wccpAdminEnabled": wccpAdminEnabled,
       "wccpServiceCount": wccpServiceCount,
       "wccpGlobalStatsReset": wccpGlobalStatsReset,
       "wccpGlobalStatsMessageInvalid": wccpGlobalStatsMessageInvalid,
       "wccpServices": wccpServices,
       "wccpServiceTable": wccpServiceTable,
       "wccpServiceTableEntry": wccpServiceTableEntry,
       "wccpServiceId": wccpServiceId,
       "wccpServiceProtocol": wccpServiceProtocol,
       "wccpServiceMessageType": wccpServiceMessageType,
       "wccpServicePortType": wccpServicePortType,
       "wccpServiceAdminEnabled": wccpServiceAdminEnabled,
       "wccpServicePassword": wccpServicePassword,
       "wccpServiceType": wccpServiceType,
       "wccpServiceVersion": wccpServiceVersion,
       "wccpServiceWebCacheCount": wccpServiceWebCacheCount,
       "wccpServiceReceiveId": wccpServiceReceiveId,
       "wccpServiceChangeNumber": wccpServiceChangeNumber,
       "wccpServicePrecedence": wccpServicePrecedence,
       "wccpServiceRowStatus": wccpServiceRowStatus,
       "wccpServicePortTable": wccpServicePortTable,
       "wccpServicePortTableEntry": wccpServicePortTableEntry,
       "wccpServicePortServiceId": wccpServicePortServiceId,
       "wccpServicePortPortId": wccpServicePortPortId,
       "wccpServicePortPortNum": wccpServicePortPortNum,
       "wccpWebCaches": wccpWebCaches,
       "wccpWebCacheTable": wccpWebCacheTable,
       "wccpWebCacheTableEntry": wccpWebCacheTableEntry,
       "wccpWebCacheServiceId": wccpWebCacheServiceId,
       "wccpWebCacheIpAddressType": wccpWebCacheIpAddressType,
       "wccpWebCacheIpAddress": wccpWebCacheIpAddress,
       "wccpWebCacheProtoVersion": wccpWebCacheProtoVersion,
       "wccpWebCacheReceiveId": wccpWebCacheReceiveId,
       "wccpWebCacheChangeNum": wccpWebCacheChangeNum,
       "wccpWebCacheNumberOfRouters": wccpWebCacheNumberOfRouters,
       "wccpWebCacheNumberOfWebCaches": wccpWebCacheNumberOfWebCaches,
       "wccpWebCacheState": wccpWebCacheState,
       "wccpWebCacheConnectTime": wccpWebCacheConnectTime,
       "wccpRouters": wccpRouters,
       "wccpRouterTable": wccpRouterTable,
       "wccpRouterTableEntry": wccpRouterTableEntry,
       "wccpRouterServiceId": wccpRouterServiceId,
       "wccpRouterIpAddressType": wccpRouterIpAddressType,
       "wccpRouterIpAddress": wccpRouterIpAddress,
       "wccpRouterProtoVersion": wccpRouterProtoVersion,
       "wccpRestrictVlan": wccpRestrictVlan,
       "wccpRestrictVlanTable": wccpRestrictVlanTable,
       "wccpRestrictVlanTableEntry": wccpRestrictVlanTableEntry,
       "wccpRestrictVlanServiceId": wccpRestrictVlanServiceId,
       "wccpRestrictVlanVlanId": wccpRestrictVlanVlanId,
       "wccpRestrictVlanRowStatus": wccpRestrictVlanRowStatus,
       "wccpRestrictWebCache": wccpRestrictWebCache,
       "wccpRestrictWebCacheTable": wccpRestrictWebCacheTable,
       "wccpRestrictWebCacheTableEntry": wccpRestrictWebCacheTableEntry,
       "wccpRestrictWebCacheServiceId": wccpRestrictWebCacheServiceId,
       "wccpRestrictWebCacheIpAddressType": wccpRestrictWebCacheIpAddressType,
       "wccpRestrictWebCacheIpAddress": wccpRestrictWebCacheIpAddress,
       "wccpRestrictWebCacheIpMaskAddressType": wccpRestrictWebCacheIpMaskAddressType,
       "wccpRestrictWebCacheIpMask": wccpRestrictWebCacheIpMask,
       "wccpRestrictWebCacheRowStatus": wccpRestrictWebCacheRowStatus,
       "wccpRestrictPort": wccpRestrictPort,
       "wccpRestrictPortTable": wccpRestrictPortTable,
       "wccpRestrictPortTableEntry": wccpRestrictPortTableEntry,
       "wccpRestrictPortServiceId": wccpRestrictPortServiceId,
       "wccpRestrictPortIndex": wccpRestrictPortIndex,
       "wccpRestrictPortRowStatus": wccpRestrictPortRowStatus,
       "wccpStatistics": wccpStatistics,
       "wccpStatisticsTable": wccpStatisticsTable,
       "wccpStatisticsTableEntry": wccpStatisticsTableEntry,
       "wccpStatsServiceId": wccpStatsServiceId,
       "wccpStatsMessagesReceived": wccpStatsMessagesReceived,
       "wccpStatsMessagesTransmitted": wccpStatsMessagesTransmitted,
       "wccpStatsMessagesDropped": wccpStatsMessagesDropped,
       "wccpStatsPacketsRedir": wccpStatsPacketsRedir,
       "wccpStatsPacketsLowRedir": wccpStatsPacketsLowRedir,
       "wccpStatsPacketsDeniedRedir": wccpStatsPacketsDeniedRedir,
       "wccpStatsAuthFailures": wccpStatsAuthFailures,
       "wccpStatsReset": wccpStatsReset,
       "wccpTrapsObj": wccpTrapsObj,
       "wccpTrapInfoServiceId": wccpTrapInfoServiceId,
       "wccpTrapInfoOperStatus": wccpTrapInfoOperStatus,
       "wccpTrapInfoWebCacheIpAddr": wccpTrapInfoWebCacheIpAddr,
       "wccpTrapInfoEntityGroup": wccpTrapInfoEntityGroup,
       "alcatelIND1WCCPMIBConformance": alcatelIND1WCCPMIBConformance,
       "alcatelIND1WCCPMIBGroups": alcatelIND1WCCPMIBGroups,
       "wccpFeatureGroup": wccpFeatureGroup,
       "wccpServiceGroup": wccpServiceGroup,
       "wccpWebCacheGroup": wccpWebCacheGroup,
       "wccpRouterGroup": wccpRouterGroup,
       "wccpRestrictVlanGroup": wccpRestrictVlanGroup,
       "wccpRestrictWebCacheGroup": wccpRestrictWebCacheGroup,
       "wccpRestrictPortGroup": wccpRestrictPortGroup,
       "wccpStatisticsGroup": wccpStatisticsGroup,
       "wccpTrapsGroup": wccpTrapsGroup,
       "wccpOperStatusGroup": wccpOperStatusGroup,
       "alcatelIND1WCCPMIBCompliances": alcatelIND1WCCPMIBCompliances,
       "alcatelIND1WCCPMIBCompliance": alcatelIND1WCCPMIBCompliance}
)
