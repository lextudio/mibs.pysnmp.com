# SNMP MIB module (IFCP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IFCP-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:54 2024
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

(PhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero")

(FcAddressIdOrZero,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcNameIdOrZero")

(ZeroBasedCounter64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "ZeroBasedCounter64")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ifcpMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230)
)
ifcpMgmtMIB.setRevisions(
        ("2011-03-09 00:00",
         "2006-01-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IfcpIpTOVorZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class IfcpLTIorZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IfcpSessionStates(Integer32, TextualConvention):
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
        *(("down", 1),
          ("open", 3),
          ("openPending", 2))
    )



class IfcpAddressMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressTranslation", 2),
          ("addressTransparent", 1))
    )



# MIB Managed Objects in the order of their OIDs

_IfcpGatewayObjects_ObjectIdentity = ObjectIdentity
ifcpGatewayObjects = _IfcpGatewayObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 1)
)
_IfcpLclGatewayInfo_ObjectIdentity = ObjectIdentity
ifcpLclGatewayInfo = _IfcpLclGatewayInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1)
)
_IfcpLclGtwyInstTable_Object = MibTable
ifcpLclGtwyInstTable = _IfcpLclGtwyInstTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ifcpLclGtwyInstTable.setStatus("current")
_IfcpLclGtwyInstEntry_Object = MibTableRow
ifcpLclGtwyInstEntry = _IfcpLclGtwyInstEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1)
)
ifcpLclGtwyInstEntry.setIndexNames(
    (0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"),
)
if mibBuilder.loadTexts:
    ifcpLclGtwyInstEntry.setStatus("current")


class _IfcpLclGtwyInstIndex_Type(Unsigned32):
    """Custom type ifcpLclGtwyInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfcpLclGtwyInstIndex_Type.__name__ = "Unsigned32"
_IfcpLclGtwyInstIndex_Object = MibTableColumn
ifcpLclGtwyInstIndex = _IfcpLclGtwyInstIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 1),
    _IfcpLclGtwyInstIndex_Type()
)
ifcpLclGtwyInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstIndex.setStatus("current")
_IfcpLclGtwyInstPhyIndex_Type = PhysicalIndexOrZero
_IfcpLclGtwyInstPhyIndex_Object = MibTableColumn
ifcpLclGtwyInstPhyIndex = _IfcpLclGtwyInstPhyIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 2),
    _IfcpLclGtwyInstPhyIndex_Type()
)
ifcpLclGtwyInstPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstPhyIndex.setStatus("current")


class _IfcpLclGtwyInstVersionMin_Type(Unsigned32):
    """Custom type ifcpLclGtwyInstVersionMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfcpLclGtwyInstVersionMin_Type.__name__ = "Unsigned32"
_IfcpLclGtwyInstVersionMin_Object = MibTableColumn
ifcpLclGtwyInstVersionMin = _IfcpLclGtwyInstVersionMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 3),
    _IfcpLclGtwyInstVersionMin_Type()
)
ifcpLclGtwyInstVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstVersionMin.setStatus("current")


class _IfcpLclGtwyInstVersionMax_Type(Unsigned32):
    """Custom type ifcpLclGtwyInstVersionMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfcpLclGtwyInstVersionMax_Type.__name__ = "Unsigned32"
_IfcpLclGtwyInstVersionMax_Object = MibTableColumn
ifcpLclGtwyInstVersionMax = _IfcpLclGtwyInstVersionMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 4),
    _IfcpLclGtwyInstVersionMax_Type()
)
ifcpLclGtwyInstVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstVersionMax.setStatus("current")


class _IfcpLclGtwyInstAddrTransMode_Type(IfcpAddressMode):
    """Custom type ifcpLclGtwyInstAddrTransMode based on IfcpAddressMode"""


_IfcpLclGtwyInstAddrTransMode_Object = MibTableColumn
ifcpLclGtwyInstAddrTransMode = _IfcpLclGtwyInstAddrTransMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 5),
    _IfcpLclGtwyInstAddrTransMode_Type()
)
ifcpLclGtwyInstAddrTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstAddrTransMode.setStatus("current")


class _IfcpLclGtwyInstFcBrdcstSupport_Type(TruthValue):
    """Custom type ifcpLclGtwyInstFcBrdcstSupport based on TruthValue"""


_IfcpLclGtwyInstFcBrdcstSupport_Object = MibTableColumn
ifcpLclGtwyInstFcBrdcstSupport = _IfcpLclGtwyInstFcBrdcstSupport_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 6),
    _IfcpLclGtwyInstFcBrdcstSupport_Type()
)
ifcpLclGtwyInstFcBrdcstSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstFcBrdcstSupport.setStatus("current")


class _IfcpLclGtwyInstDefaultIpTOV_Type(IfcpIpTOVorZero):
    """Custom type ifcpLclGtwyInstDefaultIpTOV based on IfcpIpTOVorZero"""
    defaultValue = 6


_IfcpLclGtwyInstDefaultIpTOV_Object = MibTableColumn
ifcpLclGtwyInstDefaultIpTOV = _IfcpLclGtwyInstDefaultIpTOV_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 7),
    _IfcpLclGtwyInstDefaultIpTOV_Type()
)
ifcpLclGtwyInstDefaultIpTOV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstDefaultIpTOV.setStatus("current")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstDefaultIpTOV.setUnits("seconds")


class _IfcpLclGtwyInstDefaultLTInterval_Type(IfcpLTIorZero):
    """Custom type ifcpLclGtwyInstDefaultLTInterval based on IfcpLTIorZero"""
    defaultValue = 10


_IfcpLclGtwyInstDefaultLTInterval_Object = MibTableColumn
ifcpLclGtwyInstDefaultLTInterval = _IfcpLclGtwyInstDefaultLTInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 8),
    _IfcpLclGtwyInstDefaultLTInterval_Type()
)
ifcpLclGtwyInstDefaultLTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstDefaultLTInterval.setStatus("current")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstDefaultLTInterval.setUnits("seconds")


class _IfcpLclGtwyInstDescr_Type(SnmpAdminString):
    """Custom type ifcpLclGtwyInstDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IfcpLclGtwyInstDescr_Type.__name__ = "SnmpAdminString"
_IfcpLclGtwyInstDescr_Object = MibTableColumn
ifcpLclGtwyInstDescr = _IfcpLclGtwyInstDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 9),
    _IfcpLclGtwyInstDescr_Type()
)
ifcpLclGtwyInstDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstDescr.setStatus("current")


class _IfcpLclGtwyInstNumActiveSessions_Type(Gauge32):
    """Custom type ifcpLclGtwyInstNumActiveSessions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfcpLclGtwyInstNumActiveSessions_Type.__name__ = "Gauge32"
_IfcpLclGtwyInstNumActiveSessions_Object = MibTableColumn
ifcpLclGtwyInstNumActiveSessions = _IfcpLclGtwyInstNumActiveSessions_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 10),
    _IfcpLclGtwyInstNumActiveSessions_Type()
)
ifcpLclGtwyInstNumActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstNumActiveSessions.setStatus("current")


class _IfcpLclGtwyInstStorageType_Type(StorageType):
    """Custom type ifcpLclGtwyInstStorageType based on StorageType"""


_IfcpLclGtwyInstStorageType_Object = MibTableColumn
ifcpLclGtwyInstStorageType = _IfcpLclGtwyInstStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 11),
    _IfcpLclGtwyInstStorageType_Type()
)
ifcpLclGtwyInstStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpLclGtwyInstStorageType.setStatus("current")
_IfcpNportSessionInfo_ObjectIdentity = ObjectIdentity
ifcpNportSessionInfo = _IfcpNportSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2)
)
_IfcpSessionAttributesTable_Object = MibTable
ifcpSessionAttributesTable = _IfcpSessionAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ifcpSessionAttributesTable.setStatus("current")
_IfcpSessionAttributesEntry_Object = MibTableRow
ifcpSessionAttributesEntry = _IfcpSessionAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1)
)
ifcpSessionAttributesEntry.setIndexNames(
    (0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"),
    (0, "IFCP-MGMT-MIB", "ifcpSessionIndex"),
)
if mibBuilder.loadTexts:
    ifcpSessionAttributesEntry.setStatus("current")


class _IfcpSessionIndex_Type(Integer32):
    """Custom type ifcpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfcpSessionIndex_Type.__name__ = "Integer32"
_IfcpSessionIndex_Object = MibTableColumn
ifcpSessionIndex = _IfcpSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 1),
    _IfcpSessionIndex_Type()
)
ifcpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifcpSessionIndex.setStatus("current")
_IfcpSessionLclPrtlIfIndex_Type = InterfaceIndexOrZero
_IfcpSessionLclPrtlIfIndex_Object = MibTableColumn
ifcpSessionLclPrtlIfIndex = _IfcpSessionLclPrtlIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 2),
    _IfcpSessionLclPrtlIfIndex_Type()
)
ifcpSessionLclPrtlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclPrtlIfIndex.setStatus("current")
_IfcpSessionLclPrtlAddrType_Type = InetAddressType
_IfcpSessionLclPrtlAddrType_Object = MibTableColumn
ifcpSessionLclPrtlAddrType = _IfcpSessionLclPrtlAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 3),
    _IfcpSessionLclPrtlAddrType_Type()
)
ifcpSessionLclPrtlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclPrtlAddrType.setStatus("current")
_IfcpSessionLclPrtlAddr_Type = InetAddress
_IfcpSessionLclPrtlAddr_Object = MibTableColumn
ifcpSessionLclPrtlAddr = _IfcpSessionLclPrtlAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 4),
    _IfcpSessionLclPrtlAddr_Type()
)
ifcpSessionLclPrtlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclPrtlAddr.setStatus("current")
_IfcpSessionLclPrtlTcpPort_Type = InetPortNumber
_IfcpSessionLclPrtlTcpPort_Object = MibTableColumn
ifcpSessionLclPrtlTcpPort = _IfcpSessionLclPrtlTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 5),
    _IfcpSessionLclPrtlTcpPort_Type()
)
ifcpSessionLclPrtlTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclPrtlTcpPort.setStatus("current")
_IfcpSessionLclNpWwun_Type = FcNameIdOrZero
_IfcpSessionLclNpWwun_Object = MibTableColumn
ifcpSessionLclNpWwun = _IfcpSessionLclNpWwun_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 6),
    _IfcpSessionLclNpWwun_Type()
)
ifcpSessionLclNpWwun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclNpWwun.setStatus("current")
_IfcpSessionLclNpFcid_Type = FcAddressIdOrZero
_IfcpSessionLclNpFcid_Object = MibTableColumn
ifcpSessionLclNpFcid = _IfcpSessionLclNpFcid_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 7),
    _IfcpSessionLclNpFcid_Type()
)
ifcpSessionLclNpFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclNpFcid.setStatus("current")
_IfcpSessionRmtNpWwun_Type = FcNameIdOrZero
_IfcpSessionRmtNpWwun_Object = MibTableColumn
ifcpSessionRmtNpWwun = _IfcpSessionRmtNpWwun_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 8),
    _IfcpSessionRmtNpWwun_Type()
)
ifcpSessionRmtNpWwun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtNpWwun.setStatus("current")
_IfcpSessionRmtPrtlIfAddrType_Type = InetAddressType
_IfcpSessionRmtPrtlIfAddrType_Object = MibTableColumn
ifcpSessionRmtPrtlIfAddrType = _IfcpSessionRmtPrtlIfAddrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 9),
    _IfcpSessionRmtPrtlIfAddrType_Type()
)
ifcpSessionRmtPrtlIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtPrtlIfAddrType.setStatus("current")
_IfcpSessionRmtPrtlIfAddr_Type = InetAddress
_IfcpSessionRmtPrtlIfAddr_Object = MibTableColumn
ifcpSessionRmtPrtlIfAddr = _IfcpSessionRmtPrtlIfAddr_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 10),
    _IfcpSessionRmtPrtlIfAddr_Type()
)
ifcpSessionRmtPrtlIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtPrtlIfAddr.setStatus("current")


class _IfcpSessionRmtPrtlTcpPort_Type(InetPortNumber):
    """Custom type ifcpSessionRmtPrtlTcpPort based on InetPortNumber"""
    defaultValue = 3420


_IfcpSessionRmtPrtlTcpPort_Object = MibTableColumn
ifcpSessionRmtPrtlTcpPort = _IfcpSessionRmtPrtlTcpPort_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 11),
    _IfcpSessionRmtPrtlTcpPort_Type()
)
ifcpSessionRmtPrtlTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtPrtlTcpPort.setStatus("current")
_IfcpSessionRmtNpFcid_Type = FcAddressIdOrZero
_IfcpSessionRmtNpFcid_Object = MibTableColumn
ifcpSessionRmtNpFcid = _IfcpSessionRmtNpFcid_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 12),
    _IfcpSessionRmtNpFcid_Type()
)
ifcpSessionRmtNpFcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtNpFcid.setStatus("current")
_IfcpSessionRmtNpFcidAlias_Type = FcAddressIdOrZero
_IfcpSessionRmtNpFcidAlias_Object = MibTableColumn
ifcpSessionRmtNpFcidAlias = _IfcpSessionRmtNpFcidAlias_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 13),
    _IfcpSessionRmtNpFcidAlias_Type()
)
ifcpSessionRmtNpFcidAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtNpFcidAlias.setStatus("current")
_IfcpSessionIpTOV_Type = IfcpIpTOVorZero
_IfcpSessionIpTOV_Object = MibTableColumn
ifcpSessionIpTOV = _IfcpSessionIpTOV_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 14),
    _IfcpSessionIpTOV_Type()
)
ifcpSessionIpTOV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifcpSessionIpTOV.setStatus("current")
if mibBuilder.loadTexts:
    ifcpSessionIpTOV.setUnits("seconds")
_IfcpSessionLclLTIntvl_Type = IfcpLTIorZero
_IfcpSessionLclLTIntvl_Object = MibTableColumn
ifcpSessionLclLTIntvl = _IfcpSessionLclLTIntvl_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 15),
    _IfcpSessionLclLTIntvl_Type()
)
ifcpSessionLclLTIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLclLTIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ifcpSessionLclLTIntvl.setUnits("seconds")
_IfcpSessionRmtLTIntvl_Type = IfcpLTIorZero
_IfcpSessionRmtLTIntvl_Object = MibTableColumn
ifcpSessionRmtLTIntvl = _IfcpSessionRmtLTIntvl_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 16),
    _IfcpSessionRmtLTIntvl_Type()
)
ifcpSessionRmtLTIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRmtLTIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ifcpSessionRmtLTIntvl.setUnits("seconds")
_IfcpSessionBound_Type = TruthValue
_IfcpSessionBound_Object = MibTableColumn
ifcpSessionBound = _IfcpSessionBound_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 17),
    _IfcpSessionBound_Type()
)
ifcpSessionBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionBound.setStatus("current")


class _IfcpSessionStorageType_Type(StorageType):
    """Custom type ifcpSessionStorageType based on StorageType"""


_IfcpSessionStorageType_Object = MibTableColumn
ifcpSessionStorageType = _IfcpSessionStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 18),
    _IfcpSessionStorageType_Type()
)
ifcpSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionStorageType.setStatus("current")
_IfcpSessionStatsTable_Object = MibTable
ifcpSessionStatsTable = _IfcpSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifcpSessionStatsTable.setStatus("current")
_IfcpSessionStatsEntry_Object = MibTableRow
ifcpSessionStatsEntry = _IfcpSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifcpSessionStatsEntry.setStatus("current")
_IfcpSessionState_Type = IfcpSessionStates
_IfcpSessionState_Object = MibTableColumn
ifcpSessionState = _IfcpSessionState_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 1),
    _IfcpSessionState_Type()
)
ifcpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionState.setStatus("current")


class _IfcpSessionDuration_Type(Unsigned32):
    """Custom type ifcpSessionDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfcpSessionDuration_Type.__name__ = "Unsigned32"
_IfcpSessionDuration_Object = MibTableColumn
ifcpSessionDuration = _IfcpSessionDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 2),
    _IfcpSessionDuration_Type()
)
ifcpSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionDuration.setStatus("current")
_IfcpSessionTxOctets_Type = ZeroBasedCounter64
_IfcpSessionTxOctets_Object = MibTableColumn
ifcpSessionTxOctets = _IfcpSessionTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 3),
    _IfcpSessionTxOctets_Type()
)
ifcpSessionTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionTxOctets.setStatus("current")
_IfcpSessionRxOctets_Type = ZeroBasedCounter64
_IfcpSessionRxOctets_Object = MibTableColumn
ifcpSessionRxOctets = _IfcpSessionRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 4),
    _IfcpSessionRxOctets_Type()
)
ifcpSessionRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRxOctets.setStatus("current")
_IfcpSessionTxFrames_Type = ZeroBasedCounter64
_IfcpSessionTxFrames_Object = MibTableColumn
ifcpSessionTxFrames = _IfcpSessionTxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 5),
    _IfcpSessionTxFrames_Type()
)
ifcpSessionTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionTxFrames.setStatus("current")
_IfcpSessionRxFrames_Type = ZeroBasedCounter64
_IfcpSessionRxFrames_Object = MibTableColumn
ifcpSessionRxFrames = _IfcpSessionRxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 6),
    _IfcpSessionRxFrames_Type()
)
ifcpSessionRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionRxFrames.setStatus("current")
_IfcpSessionStaleFrames_Type = ZeroBasedCounter64
_IfcpSessionStaleFrames_Object = MibTableColumn
ifcpSessionStaleFrames = _IfcpSessionStaleFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 7),
    _IfcpSessionStaleFrames_Type()
)
ifcpSessionStaleFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionStaleFrames.setStatus("current")
_IfcpSessionHeaderCRCErrors_Type = ZeroBasedCounter64
_IfcpSessionHeaderCRCErrors_Object = MibTableColumn
ifcpSessionHeaderCRCErrors = _IfcpSessionHeaderCRCErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 8),
    _IfcpSessionHeaderCRCErrors_Type()
)
ifcpSessionHeaderCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionHeaderCRCErrors.setStatus("current")
_IfcpSessionFcPayloadCRCErrors_Type = ZeroBasedCounter64
_IfcpSessionFcPayloadCRCErrors_Object = MibTableColumn
ifcpSessionFcPayloadCRCErrors = _IfcpSessionFcPayloadCRCErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 9),
    _IfcpSessionFcPayloadCRCErrors_Type()
)
ifcpSessionFcPayloadCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionFcPayloadCRCErrors.setStatus("current")
_IfcpSessionOtherErrors_Type = ZeroBasedCounter64
_IfcpSessionOtherErrors_Object = MibTableColumn
ifcpSessionOtherErrors = _IfcpSessionOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 10),
    _IfcpSessionOtherErrors_Type()
)
ifcpSessionOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionOtherErrors.setStatus("current")
_IfcpSessionDiscontinuityTime_Type = TimeStamp
_IfcpSessionDiscontinuityTime_Object = MibTableColumn
ifcpSessionDiscontinuityTime = _IfcpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 11),
    _IfcpSessionDiscontinuityTime_Type()
)
ifcpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionDiscontinuityTime.setStatus("current")
_IfcpSessionLcStatsTable_Object = MibTable
ifcpSessionLcStatsTable = _IfcpSessionLcStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ifcpSessionLcStatsTable.setStatus("current")
_IfcpSessionLcStatsEntry_Object = MibTableRow
ifcpSessionLcStatsEntry = _IfcpSessionLcStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifcpSessionLcStatsEntry.setStatus("current")
_IfcpSessionLcTxOctets_Type = ZeroBasedCounter32
_IfcpSessionLcTxOctets_Object = MibTableColumn
ifcpSessionLcTxOctets = _IfcpSessionLcTxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 1),
    _IfcpSessionLcTxOctets_Type()
)
ifcpSessionLcTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcTxOctets.setStatus("current")
_IfcpSessionLcRxOctets_Type = ZeroBasedCounter32
_IfcpSessionLcRxOctets_Object = MibTableColumn
ifcpSessionLcRxOctets = _IfcpSessionLcRxOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 2),
    _IfcpSessionLcRxOctets_Type()
)
ifcpSessionLcRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcRxOctets.setStatus("current")
_IfcpSessionLcTxFrames_Type = ZeroBasedCounter32
_IfcpSessionLcTxFrames_Object = MibTableColumn
ifcpSessionLcTxFrames = _IfcpSessionLcTxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 3),
    _IfcpSessionLcTxFrames_Type()
)
ifcpSessionLcTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcTxFrames.setStatus("current")
_IfcpSessionLcRxFrames_Type = ZeroBasedCounter32
_IfcpSessionLcRxFrames_Object = MibTableColumn
ifcpSessionLcRxFrames = _IfcpSessionLcRxFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 4),
    _IfcpSessionLcRxFrames_Type()
)
ifcpSessionLcRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcRxFrames.setStatus("current")
_IfcpSessionLcStaleFrames_Type = ZeroBasedCounter32
_IfcpSessionLcStaleFrames_Object = MibTableColumn
ifcpSessionLcStaleFrames = _IfcpSessionLcStaleFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 5),
    _IfcpSessionLcStaleFrames_Type()
)
ifcpSessionLcStaleFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcStaleFrames.setStatus("current")
_IfcpSessionLcHeaderCRCErrors_Type = ZeroBasedCounter32
_IfcpSessionLcHeaderCRCErrors_Object = MibTableColumn
ifcpSessionLcHeaderCRCErrors = _IfcpSessionLcHeaderCRCErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 6),
    _IfcpSessionLcHeaderCRCErrors_Type()
)
ifcpSessionLcHeaderCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcHeaderCRCErrors.setStatus("current")
_IfcpSessionLcFcPayloadCRCErrors_Type = ZeroBasedCounter32
_IfcpSessionLcFcPayloadCRCErrors_Object = MibTableColumn
ifcpSessionLcFcPayloadCRCErrors = _IfcpSessionLcFcPayloadCRCErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 7),
    _IfcpSessionLcFcPayloadCRCErrors_Type()
)
ifcpSessionLcFcPayloadCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcFcPayloadCRCErrors.setStatus("current")
_IfcpSessionLcOtherErrors_Type = ZeroBasedCounter32
_IfcpSessionLcOtherErrors_Object = MibTableColumn
ifcpSessionLcOtherErrors = _IfcpSessionLcOtherErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 8),
    _IfcpSessionLcOtherErrors_Type()
)
ifcpSessionLcOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifcpSessionLcOtherErrors.setStatus("current")
_IfcpGatewayConformance_ObjectIdentity = ObjectIdentity
ifcpGatewayConformance = _IfcpGatewayConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 2)
)
_IfcpCompliances_ObjectIdentity = ObjectIdentity
ifcpCompliances = _IfcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 1)
)
_IfcpGroups_ObjectIdentity = ObjectIdentity
ifcpGroups = _IfcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2)
)
ifcpSessionAttributesEntry.registerAugmentions(
    ("IFCP-MGMT-MIB",
     "ifcpSessionStatsEntry")
)
ifcpSessionStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())
ifcpSessionAttributesEntry.registerAugmentions(
    ("IFCP-MGMT-MIB",
     "ifcpSessionLcStatsEntry")
)
ifcpSessionLcStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())

# Managed Objects groups

ifcpLclGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 1)
)
ifcpLclGatewayGroup.setObjects(
      *(("IFCP-MGMT-MIB", "ifcpLclGtwyInstPhyIndex"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMin"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMax"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstAddrTransMode"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstFcBrdcstSupport"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultIpTOV"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultLTInterval"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDescr"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstNumActiveSessions"),
        ("IFCP-MGMT-MIB", "ifcpLclGtwyInstStorageType"))
)
if mibBuilder.loadTexts:
    ifcpLclGatewayGroup.setStatus("current")

ifcpLclGatewaySessionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 4)
)
ifcpLclGatewaySessionGroup.setObjects(
      *(("IFCP-MGMT-MIB", "ifcpSessionLclPrtlIfIndex"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddrType"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddr"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlTcpPort"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclNpWwun"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclNpFcid"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtNpWwun"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddrType"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddr"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlTcpPort"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcid"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcidAlias"),
        ("IFCP-MGMT-MIB", "ifcpSessionIpTOV"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclLTIntvl"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtLTIntvl"),
        ("IFCP-MGMT-MIB", "ifcpSessionBound"),
        ("IFCP-MGMT-MIB", "ifcpSessionStorageType"))
)
if mibBuilder.loadTexts:
    ifcpLclGatewaySessionGroup.setStatus("deprecated")

ifcpLclGatewaySessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 5)
)
ifcpLclGatewaySessionStatsGroup.setObjects(
      *(("IFCP-MGMT-MIB", "ifcpSessionState"),
        ("IFCP-MGMT-MIB", "ifcpSessionDuration"),
        ("IFCP-MGMT-MIB", "ifcpSessionTxOctets"),
        ("IFCP-MGMT-MIB", "ifcpSessionRxOctets"),
        ("IFCP-MGMT-MIB", "ifcpSessionTxFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionRxFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionStaleFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionHeaderCRCErrors"),
        ("IFCP-MGMT-MIB", "ifcpSessionFcPayloadCRCErrors"),
        ("IFCP-MGMT-MIB", "ifcpSessionOtherErrors"),
        ("IFCP-MGMT-MIB", "ifcpSessionDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ifcpLclGatewaySessionStatsGroup.setStatus("current")

ifcpLclGatewaySessionLcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 6)
)
ifcpLclGatewaySessionLcStatsGroup.setObjects(
      *(("IFCP-MGMT-MIB", "ifcpSessionLcTxOctets"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcRxOctets"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcTxFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcRxFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcStaleFrames"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcHeaderCRCErrors"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcFcPayloadCRCErrors"),
        ("IFCP-MGMT-MIB", "ifcpSessionLcOtherErrors"))
)
if mibBuilder.loadTexts:
    ifcpLclGatewaySessionLcStatsGroup.setStatus("current")

ifcpLclGatewaySessionGroupNoTranslation = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 7)
)
ifcpLclGatewaySessionGroupNoTranslation.setObjects(
      *(("IFCP-MGMT-MIB", "ifcpSessionLclPrtlIfIndex"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddrType"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddr"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlTcpPort"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclNpWwun"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclNpFcid"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtNpWwun"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddrType"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddr"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlTcpPort"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcid"),
        ("IFCP-MGMT-MIB", "ifcpSessionIpTOV"),
        ("IFCP-MGMT-MIB", "ifcpSessionLclLTIntvl"),
        ("IFCP-MGMT-MIB", "ifcpSessionRmtLTIntvl"),
        ("IFCP-MGMT-MIB", "ifcpSessionBound"),
        ("IFCP-MGMT-MIB", "ifcpSessionStorageType"))
)
if mibBuilder.loadTexts:
    ifcpLclGatewaySessionGroupNoTranslation.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ifcpGatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ifcpGatewayCompliance.setStatus(
        "deprecated"
    )

ifcpGatewayComplianceNoTranslation = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 230, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ifcpGatewayComplianceNoTranslation.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IFCP-MGMT-MIB",
    **{"IfcpIpTOVorZero": IfcpIpTOVorZero,
       "IfcpLTIorZero": IfcpLTIorZero,
       "IfcpSessionStates": IfcpSessionStates,
       "IfcpAddressMode": IfcpAddressMode,
       "ifcpMgmtMIB": ifcpMgmtMIB,
       "ifcpGatewayObjects": ifcpGatewayObjects,
       "ifcpLclGatewayInfo": ifcpLclGatewayInfo,
       "ifcpLclGtwyInstTable": ifcpLclGtwyInstTable,
       "ifcpLclGtwyInstEntry": ifcpLclGtwyInstEntry,
       "ifcpLclGtwyInstIndex": ifcpLclGtwyInstIndex,
       "ifcpLclGtwyInstPhyIndex": ifcpLclGtwyInstPhyIndex,
       "ifcpLclGtwyInstVersionMin": ifcpLclGtwyInstVersionMin,
       "ifcpLclGtwyInstVersionMax": ifcpLclGtwyInstVersionMax,
       "ifcpLclGtwyInstAddrTransMode": ifcpLclGtwyInstAddrTransMode,
       "ifcpLclGtwyInstFcBrdcstSupport": ifcpLclGtwyInstFcBrdcstSupport,
       "ifcpLclGtwyInstDefaultIpTOV": ifcpLclGtwyInstDefaultIpTOV,
       "ifcpLclGtwyInstDefaultLTInterval": ifcpLclGtwyInstDefaultLTInterval,
       "ifcpLclGtwyInstDescr": ifcpLclGtwyInstDescr,
       "ifcpLclGtwyInstNumActiveSessions": ifcpLclGtwyInstNumActiveSessions,
       "ifcpLclGtwyInstStorageType": ifcpLclGtwyInstStorageType,
       "ifcpNportSessionInfo": ifcpNportSessionInfo,
       "ifcpSessionAttributesTable": ifcpSessionAttributesTable,
       "ifcpSessionAttributesEntry": ifcpSessionAttributesEntry,
       "ifcpSessionIndex": ifcpSessionIndex,
       "ifcpSessionLclPrtlIfIndex": ifcpSessionLclPrtlIfIndex,
       "ifcpSessionLclPrtlAddrType": ifcpSessionLclPrtlAddrType,
       "ifcpSessionLclPrtlAddr": ifcpSessionLclPrtlAddr,
       "ifcpSessionLclPrtlTcpPort": ifcpSessionLclPrtlTcpPort,
       "ifcpSessionLclNpWwun": ifcpSessionLclNpWwun,
       "ifcpSessionLclNpFcid": ifcpSessionLclNpFcid,
       "ifcpSessionRmtNpWwun": ifcpSessionRmtNpWwun,
       "ifcpSessionRmtPrtlIfAddrType": ifcpSessionRmtPrtlIfAddrType,
       "ifcpSessionRmtPrtlIfAddr": ifcpSessionRmtPrtlIfAddr,
       "ifcpSessionRmtPrtlTcpPort": ifcpSessionRmtPrtlTcpPort,
       "ifcpSessionRmtNpFcid": ifcpSessionRmtNpFcid,
       "ifcpSessionRmtNpFcidAlias": ifcpSessionRmtNpFcidAlias,
       "ifcpSessionIpTOV": ifcpSessionIpTOV,
       "ifcpSessionLclLTIntvl": ifcpSessionLclLTIntvl,
       "ifcpSessionRmtLTIntvl": ifcpSessionRmtLTIntvl,
       "ifcpSessionBound": ifcpSessionBound,
       "ifcpSessionStorageType": ifcpSessionStorageType,
       "ifcpSessionStatsTable": ifcpSessionStatsTable,
       "ifcpSessionStatsEntry": ifcpSessionStatsEntry,
       "ifcpSessionState": ifcpSessionState,
       "ifcpSessionDuration": ifcpSessionDuration,
       "ifcpSessionTxOctets": ifcpSessionTxOctets,
       "ifcpSessionRxOctets": ifcpSessionRxOctets,
       "ifcpSessionTxFrames": ifcpSessionTxFrames,
       "ifcpSessionRxFrames": ifcpSessionRxFrames,
       "ifcpSessionStaleFrames": ifcpSessionStaleFrames,
       "ifcpSessionHeaderCRCErrors": ifcpSessionHeaderCRCErrors,
       "ifcpSessionFcPayloadCRCErrors": ifcpSessionFcPayloadCRCErrors,
       "ifcpSessionOtherErrors": ifcpSessionOtherErrors,
       "ifcpSessionDiscontinuityTime": ifcpSessionDiscontinuityTime,
       "ifcpSessionLcStatsTable": ifcpSessionLcStatsTable,
       "ifcpSessionLcStatsEntry": ifcpSessionLcStatsEntry,
       "ifcpSessionLcTxOctets": ifcpSessionLcTxOctets,
       "ifcpSessionLcRxOctets": ifcpSessionLcRxOctets,
       "ifcpSessionLcTxFrames": ifcpSessionLcTxFrames,
       "ifcpSessionLcRxFrames": ifcpSessionLcRxFrames,
       "ifcpSessionLcStaleFrames": ifcpSessionLcStaleFrames,
       "ifcpSessionLcHeaderCRCErrors": ifcpSessionLcHeaderCRCErrors,
       "ifcpSessionLcFcPayloadCRCErrors": ifcpSessionLcFcPayloadCRCErrors,
       "ifcpSessionLcOtherErrors": ifcpSessionLcOtherErrors,
       "ifcpGatewayConformance": ifcpGatewayConformance,
       "ifcpCompliances": ifcpCompliances,
       "ifcpGatewayCompliance": ifcpGatewayCompliance,
       "ifcpGatewayComplianceNoTranslation": ifcpGatewayComplianceNoTranslation,
       "ifcpGroups": ifcpGroups,
       "ifcpLclGatewayGroup": ifcpLclGatewayGroup,
       "ifcpLclGatewaySessionGroup": ifcpLclGatewaySessionGroup,
       "ifcpLclGatewaySessionStatsGroup": ifcpLclGatewaySessionStatsGroup,
       "ifcpLclGatewaySessionLcStatsGroup": ifcpLclGatewaySessionLcStatsGroup,
       "ifcpLclGatewaySessionGroupNoTranslation": ifcpLclGatewaySessionGroupNoTranslation}
)
