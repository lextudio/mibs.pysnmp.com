# SNMP MIB module (CISCO-ENHANCED-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-SLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:26 2024
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

(SlbUrlString,) = mibBuilder.importSymbols(
    "CISCO-SLB-EXT-MIB",
    "SlbUrlString")

(CiscoProbeHealthMonState,
 cslbxProbeName) = mibBuilder.importSymbols(
    "CISCO-SLB-HEALTH-MON-MIB",
    "CiscoProbeHealthMonState",
    "cslbxProbeName")

(SlbRealServerState,
 SlbServerString,
 slbEntity,
 slbServerFarmName) = mibBuilder.importSymbols(
    "CISCO-SLB-MIB",
    "SlbRealServerState",
    "SlbServerString",
    "slbEntity",
    "slbServerFarmName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoHTTPResponseStatusCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoHTTPResponseStatusCode")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnhancedSlbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470)
)
ciscoEnhancedSlbMIB.setRevisions(
        ("2012-12-03 00:00",
         "2012-04-09 00:00",
         "2009-09-19 00:00",
         "2008-05-21 00:00",
         "2008-03-12 00:00",
         "2006-03-31 00:00",
         "2006-02-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoRserverAdminStatus(Integer32, TextualConvention):
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
        *(("inService", 1),
          ("inServiceStandby", 3),
          ("outOfService", 2))
    )



class SlbRserverLocalityState(Integer32, TextualConvention):
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
        *(("local", 2),
          ("remote", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEnhancedSlbMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEnhancedSlbMIBNotifs = _CiscoEnhancedSlbMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0)
)
_CiscoEnhancedSlbMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEnhancedSlbMIBObjects = _CiscoEnhancedSlbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1)
)
_CesRealServer_ObjectIdentity = ObjectIdentity
cesRealServer = _CesRealServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1)
)
_CesRserverTable_Object = MibTable
cesRserverTable = _CesRserverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cesRserverTable.setStatus("current")
_CesRserverEntry_Object = MibTableRow
cesRserverEntry = _CesRserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1)
)
cesRserverEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesRserverName"),
)
if mibBuilder.loadTexts:
    cesRserverEntry.setStatus("current")


class _CesRserverName_Type(SnmpAdminString):
    """Custom type cesRserverName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CesRserverName_Type.__name__ = "SnmpAdminString"
_CesRserverName_Object = MibTableColumn
cesRserverName = _CesRserverName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 1),
    _CesRserverName_Type()
)
cesRserverName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cesRserverName.setStatus("current")


class _CesRserverType_Type(Integer32):
    """Custom type cesRserverType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("redirect", 1))
    )


_CesRserverType_Type.__name__ = "Integer32"
_CesRserverType_Object = MibTableColumn
cesRserverType = _CesRserverType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 2),
    _CesRserverType_Type()
)
cesRserverType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverType.setStatus("current")
_CesRserverIpAddressType_Type = InetAddressType
_CesRserverIpAddressType_Object = MibTableColumn
cesRserverIpAddressType = _CesRserverIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 3),
    _CesRserverIpAddressType_Type()
)
cesRserverIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverIpAddressType.setStatus("current")
_CesRserverIpAddress_Type = InetAddress
_CesRserverIpAddress_Object = MibTableColumn
cesRserverIpAddress = _CesRserverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 4),
    _CesRserverIpAddress_Type()
)
cesRserverIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverIpAddress.setStatus("current")
_CesRserverDescription_Type = SnmpAdminString
_CesRserverDescription_Object = MibTableColumn
cesRserverDescription = _CesRserverDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 5),
    _CesRserverDescription_Type()
)
cesRserverDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverDescription.setStatus("current")


class _CesRserverMaxConns_Type(Unsigned32):
    """Custom type cesRserverMaxConns based on Unsigned32"""
    defaultValue = 4294967295


_CesRserverMaxConns_Object = MibTableColumn
cesRserverMaxConns = _CesRserverMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 6),
    _CesRserverMaxConns_Type()
)
cesRserverMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverMaxConns.setStatus("current")


class _CesRserverMinConns_Type(Unsigned32):
    """Custom type cesRserverMinConns based on Unsigned32"""
    defaultValue = 4294967295


_CesRserverMinConns_Object = MibTableColumn
cesRserverMinConns = _CesRserverMinConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 7),
    _CesRserverMinConns_Type()
)
cesRserverMinConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverMinConns.setStatus("current")


class _CesRserverAdminWeight_Type(Unsigned32):
    """Custom type cesRserverAdminWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesRserverAdminWeight_Type.__name__ = "Unsigned32"
_CesRserverAdminWeight_Object = MibTableColumn
cesRserverAdminWeight = _CesRserverAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 8),
    _CesRserverAdminWeight_Type()
)
cesRserverAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverAdminWeight.setStatus("current")
_CesRserverRedirectRelocationStr_Type = SlbUrlString
_CesRserverRedirectRelocationStr_Object = MibTableColumn
cesRserverRedirectRelocationStr = _CesRserverRedirectRelocationStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 9),
    _CesRserverRedirectRelocationStr_Type()
)
cesRserverRedirectRelocationStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverRedirectRelocationStr.setStatus("current")


class _CesRserverRedirectCode_Type(CiscoHTTPResponseStatusCode):
    """Custom type cesRserverRedirectCode based on CiscoHTTPResponseStatusCode"""
    defaultValue = 302

    subtypeSpec = CiscoHTTPResponseStatusCode.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 399),
    )


_CesRserverRedirectCode_Type.__name__ = "CiscoHTTPResponseStatusCode"
_CesRserverRedirectCode_Object = MibTableColumn
cesRserverRedirectCode = _CesRserverRedirectCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 10),
    _CesRserverRedirectCode_Type()
)
cesRserverRedirectCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverRedirectCode.setStatus("current")
_CesRserverRedirectPort_Type = InetPortNumber
_CesRserverRedirectPort_Object = MibTableColumn
cesRserverRedirectPort = _CesRserverRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 11),
    _CesRserverRedirectPort_Type()
)
cesRserverRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverRedirectPort.setStatus("current")


class _CesRserverAdminStatus_Type(CiscoRserverAdminStatus):
    """Custom type cesRserverAdminStatus based on CiscoRserverAdminStatus"""


_CesRserverAdminStatus_Object = MibTableColumn
cesRserverAdminStatus = _CesRserverAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 12),
    _CesRserverAdminStatus_Type()
)
cesRserverAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverAdminStatus.setStatus("current")
_CesRserverOperStatus_Type = SlbRealServerState
_CesRserverOperStatus_Object = MibTableColumn
cesRserverOperStatus = _CesRserverOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 13),
    _CesRserverOperStatus_Type()
)
cesRserverOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverOperStatus.setStatus("current")
_CesRserverStatechangeDescr_Type = SnmpAdminString
_CesRserverStatechangeDescr_Object = MibTableColumn
cesRserverStatechangeDescr = _CesRserverStatechangeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 14),
    _CesRserverStatechangeDescr_Type()
)
cesRserverStatechangeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverStatechangeDescr.setStatus("current")


class _CesRserverStorageType_Type(StorageType):
    """Custom type cesRserverStorageType based on StorageType"""


_CesRserverStorageType_Object = MibTableColumn
cesRserverStorageType = _CesRserverStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 15),
    _CesRserverStorageType_Type()
)
cesRserverStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverStorageType.setStatus("current")
_CesRserverRowStatus_Type = RowStatus
_CesRserverRowStatus_Object = MibTableColumn
cesRserverRowStatus = _CesRserverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 16),
    _CesRserverRowStatus_Type()
)
cesRserverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverRowStatus.setStatus("current")
_CesRserverTotalConns_Type = Counter64
_CesRserverTotalConns_Object = MibTableColumn
cesRserverTotalConns = _CesRserverTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 17),
    _CesRserverTotalConns_Type()
)
cesRserverTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverTotalConns.setStatus("current")
if mibBuilder.loadTexts:
    cesRserverTotalConns.setUnits("connections")
_CesRserverFailedConns_Type = Counter64
_CesRserverFailedConns_Object = MibTableColumn
cesRserverFailedConns = _CesRserverFailedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 18),
    _CesRserverFailedConns_Type()
)
cesRserverFailedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverFailedConns.setStatus("current")
if mibBuilder.loadTexts:
    cesRserverFailedConns.setUnits("connections")
_CesRserverCurrConns_Type = Counter64
_CesRserverCurrConns_Object = MibTableColumn
cesRserverCurrConns = _CesRserverCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 19),
    _CesRserverCurrConns_Type()
)
cesRserverCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverCurrConns.setStatus("current")
if mibBuilder.loadTexts:
    cesRserverCurrConns.setUnits("connections")


class _CesRserverLocality_Type(SlbRserverLocalityState):
    """Custom type cesRserverLocality based on SlbRserverLocalityState"""
    defaultValue = 1


_CesRserverLocality_Object = MibTableColumn
cesRserverLocality = _CesRserverLocality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 1, 1, 20),
    _CesRserverLocality_Type()
)
cesRserverLocality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverLocality.setStatus("current")
_CesRserverProbeTable_Object = MibTable
cesRserverProbeTable = _CesRserverProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cesRserverProbeTable.setStatus("current")
_CesRserverProbeEntry_Object = MibTableRow
cesRserverProbeEntry = _CesRserverProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1)
)
cesRserverProbeEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesRserverName"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesRserverProbeName"),
)
if mibBuilder.loadTexts:
    cesRserverProbeEntry.setStatus("current")
_CesRserverProbeName_Type = SlbServerString
_CesRserverProbeName_Object = MibTableColumn
cesRserverProbeName = _CesRserverProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 1),
    _CesRserverProbeName_Type()
)
cesRserverProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cesRserverProbeName.setStatus("current")


class _CesRserverProbeStorageType_Type(StorageType):
    """Custom type cesRserverProbeStorageType based on StorageType"""


_CesRserverProbeStorageType_Object = MibTableColumn
cesRserverProbeStorageType = _CesRserverProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 2),
    _CesRserverProbeStorageType_Type()
)
cesRserverProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverProbeStorageType.setStatus("current")
_CesRserverProbeRowStatus_Type = RowStatus
_CesRserverProbeRowStatus_Object = MibTableColumn
cesRserverProbeRowStatus = _CesRserverProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 3),
    _CesRserverProbeRowStatus_Type()
)
cesRserverProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRserverProbeRowStatus.setStatus("current")
_CesRserverProbesPassed_Type = Counter32
_CesRserverProbesPassed_Object = MibTableColumn
cesRserverProbesPassed = _CesRserverProbesPassed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 4),
    _CesRserverProbesPassed_Type()
)
cesRserverProbesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbesPassed.setStatus("current")
_CesRserverProbesFailed_Type = Counter32
_CesRserverProbesFailed_Object = MibTableColumn
cesRserverProbesFailed = _CesRserverProbesFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 5),
    _CesRserverProbesFailed_Type()
)
cesRserverProbesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbesFailed.setStatus("current")


class _CesRserverProbeHealthMonState_Type(CiscoProbeHealthMonState):
    """Custom type cesRserverProbeHealthMonState based on CiscoProbeHealthMonState"""


_CesRserverProbeHealthMonState_Object = MibTableColumn
cesRserverProbeHealthMonState = _CesRserverProbeHealthMonState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 6),
    _CesRserverProbeHealthMonState_Type()
)
cesRserverProbeHealthMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbeHealthMonState.setStatus("current")
_CesRserverProbeLastProbeTime_Type = DateAndTime
_CesRserverProbeLastProbeTime_Object = MibTableColumn
cesRserverProbeLastProbeTime = _CesRserverProbeLastProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 7),
    _CesRserverProbeLastProbeTime_Type()
)
cesRserverProbeLastProbeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbeLastProbeTime.setStatus("current")
_CesRserverProbeLastActiveTime_Type = DateAndTime
_CesRserverProbeLastActiveTime_Object = MibTableColumn
cesRserverProbeLastActiveTime = _CesRserverProbeLastActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 8),
    _CesRserverProbeLastActiveTime_Type()
)
cesRserverProbeLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbeLastActiveTime.setStatus("current")
_CesRserverProbeLastFailedTime_Type = DateAndTime
_CesRserverProbeLastFailedTime_Object = MibTableColumn
cesRserverProbeLastFailedTime = _CesRserverProbeLastFailedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 2, 1, 9),
    _CesRserverProbeLastFailedTime_Type()
)
cesRserverProbeLastFailedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesRserverProbeLastFailedTime.setStatus("current")
_CesServerFarmRserverTable_Object = MibTable
cesServerFarmRserverTable = _CesServerFarmRserverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cesServerFarmRserverTable.setStatus("current")
_CesServerFarmRserverEntry_Object = MibTableRow
cesServerFarmRserverEntry = _CesServerFarmRserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1)
)
cesServerFarmRserverEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesRserverName"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverPort"),
)
if mibBuilder.loadTexts:
    cesServerFarmRserverEntry.setStatus("current")
_CesServerFarmRserverPort_Type = InetPortNumber
_CesServerFarmRserverPort_Object = MibTableColumn
cesServerFarmRserverPort = _CesServerFarmRserverPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 1),
    _CesServerFarmRserverPort_Type()
)
cesServerFarmRserverPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cesServerFarmRserverPort.setStatus("current")


class _CesServerFarmRserverAdminWeight_Type(Unsigned32):
    """Custom type cesServerFarmRserverAdminWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesServerFarmRserverAdminWeight_Type.__name__ = "Unsigned32"
_CesServerFarmRserverAdminWeight_Object = MibTableColumn
cesServerFarmRserverAdminWeight = _CesServerFarmRserverAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 2),
    _CesServerFarmRserverAdminWeight_Type()
)
cesServerFarmRserverAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverAdminWeight.setStatus("current")


class _CesServerFarmRserverOperWeight_Type(Unsigned32):
    """Custom type cesServerFarmRserverOperWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CesServerFarmRserverOperWeight_Type.__name__ = "Unsigned32"
_CesServerFarmRserverOperWeight_Object = MibTableColumn
cesServerFarmRserverOperWeight = _CesServerFarmRserverOperWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 3),
    _CesServerFarmRserverOperWeight_Type()
)
cesServerFarmRserverOperWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverOperWeight.setStatus("current")
_CesServerFarmRserverMaxConns_Type = Unsigned32
_CesServerFarmRserverMaxConns_Object = MibTableColumn
cesServerFarmRserverMaxConns = _CesServerFarmRserverMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 4),
    _CesServerFarmRserverMaxConns_Type()
)
cesServerFarmRserverMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverMaxConns.setStatus("current")
_CesServerFarmRserverMinConns_Type = Unsigned32
_CesServerFarmRserverMinConns_Object = MibTableColumn
cesServerFarmRserverMinConns = _CesServerFarmRserverMinConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 5),
    _CesServerFarmRserverMinConns_Type()
)
cesServerFarmRserverMinConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverMinConns.setStatus("current")
_CesServerFarmRserverAdminStatus_Type = CiscoRserverAdminStatus
_CesServerFarmRserverAdminStatus_Object = MibTableColumn
cesServerFarmRserverAdminStatus = _CesServerFarmRserverAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 6),
    _CesServerFarmRserverAdminStatus_Type()
)
cesServerFarmRserverAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverAdminStatus.setStatus("current")
_CesServerFarmRserverOperStatus_Type = SlbRealServerState
_CesServerFarmRserverOperStatus_Object = MibTableColumn
cesServerFarmRserverOperStatus = _CesServerFarmRserverOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 7),
    _CesServerFarmRserverOperStatus_Type()
)
cesServerFarmRserverOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverOperStatus.setStatus("current")
_CesServerFarmRserverStateDescr_Type = SnmpAdminString
_CesServerFarmRserverStateDescr_Object = MibTableColumn
cesServerFarmRserverStateDescr = _CesServerFarmRserverStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 8),
    _CesServerFarmRserverStateDescr_Type()
)
cesServerFarmRserverStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverStateDescr.setStatus("current")


class _CesServerFarmRserverBackupName_Type(SnmpAdminString):
    """Custom type cesServerFarmRserverBackupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CesServerFarmRserverBackupName_Type.__name__ = "SnmpAdminString"
_CesServerFarmRserverBackupName_Object = MibTableColumn
cesServerFarmRserverBackupName = _CesServerFarmRserverBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 9),
    _CesServerFarmRserverBackupName_Type()
)
cesServerFarmRserverBackupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverBackupName.setStatus("current")


class _CesServerFarmRserverBackupPort_Type(InetPortNumber):
    """Custom type cesServerFarmRserverBackupPort based on InetPortNumber"""
    defaultValue = 0


_CesServerFarmRserverBackupPort_Object = MibTableColumn
cesServerFarmRserverBackupPort = _CesServerFarmRserverBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 10),
    _CesServerFarmRserverBackupPort_Type()
)
cesServerFarmRserverBackupPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverBackupPort.setStatus("current")
_CesServerFarmRserverTotalConns_Type = Counter64
_CesServerFarmRserverTotalConns_Object = MibTableColumn
cesServerFarmRserverTotalConns = _CesServerFarmRserverTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 11),
    _CesServerFarmRserverTotalConns_Type()
)
cesServerFarmRserverTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverTotalConns.setStatus("current")
_CesServerFarmRserverFailedConns_Type = Counter64
_CesServerFarmRserverFailedConns_Object = MibTableColumn
cesServerFarmRserverFailedConns = _CesServerFarmRserverFailedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 12),
    _CesServerFarmRserverFailedConns_Type()
)
cesServerFarmRserverFailedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverFailedConns.setStatus("current")
_CesServerFarmRserverDroppedConns_Type = Counter64
_CesServerFarmRserverDroppedConns_Object = MibTableColumn
cesServerFarmRserverDroppedConns = _CesServerFarmRserverDroppedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 13),
    _CesServerFarmRserverDroppedConns_Type()
)
cesServerFarmRserverDroppedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverDroppedConns.setStatus("current")
_CesServerFarmRserverCurrentConns_Type = Counter64
_CesServerFarmRserverCurrentConns_Object = MibTableColumn
cesServerFarmRserverCurrentConns = _CesServerFarmRserverCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 14),
    _CesServerFarmRserverCurrentConns_Type()
)
cesServerFarmRserverCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesServerFarmRserverCurrentConns.setStatus("current")


class _CesServerFarmRserverStorageType_Type(StorageType):
    """Custom type cesServerFarmRserverStorageType based on StorageType"""


_CesServerFarmRserverStorageType_Object = MibTableColumn
cesServerFarmRserverStorageType = _CesServerFarmRserverStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 15),
    _CesServerFarmRserverStorageType_Type()
)
cesServerFarmRserverStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverStorageType.setStatus("current")
_CesServerFarmRserverRowStatus_Type = RowStatus
_CesServerFarmRserverRowStatus_Object = MibTableColumn
cesServerFarmRserverRowStatus = _CesServerFarmRserverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 16),
    _CesServerFarmRserverRowStatus_Type()
)
cesServerFarmRserverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverRowStatus.setStatus("current")
_CesServerFarmRserverDescr_Type = SnmpAdminString
_CesServerFarmRserverDescr_Object = MibTableColumn
cesServerFarmRserverDescr = _CesServerFarmRserverDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 17),
    _CesServerFarmRserverDescr_Type()
)
cesServerFarmRserverDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverDescr.setStatus("current")
_CesServerFarmRserverBuddyGroup_Type = SnmpAdminString
_CesServerFarmRserverBuddyGroup_Object = MibTableColumn
cesServerFarmRserverBuddyGroup = _CesServerFarmRserverBuddyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 3, 1, 18),
    _CesServerFarmRserverBuddyGroup_Type()
)
cesServerFarmRserverBuddyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesServerFarmRserverBuddyGroup.setStatus("current")
_CesRealServerProbeTable_Object = MibTable
cesRealServerProbeTable = _CesRealServerProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cesRealServerProbeTable.setStatus("current")
_CesRealServerProbeEntry_Object = MibTableRow
cesRealServerProbeEntry = _CesRealServerProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 4, 1)
)
cesRealServerProbeEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-HEALTH-MON-MIB", "cslbxProbeName"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesRserverName"),
    (0, "CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverPort"),
)
if mibBuilder.loadTexts:
    cesRealServerProbeEntry.setStatus("current")


class _CesRealServerProbeStorageType_Type(StorageType):
    """Custom type cesRealServerProbeStorageType based on StorageType"""


_CesRealServerProbeStorageType_Object = MibTableColumn
cesRealServerProbeStorageType = _CesRealServerProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 4, 1, 1),
    _CesRealServerProbeStorageType_Type()
)
cesRealServerProbeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRealServerProbeStorageType.setStatus("current")
_CesRealServerProbeRowStatus_Type = RowStatus
_CesRealServerProbeRowStatus_Object = MibTableColumn
cesRealServerProbeRowStatus = _CesRealServerProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 1, 4, 1, 2),
    _CesRealServerProbeRowStatus_Type()
)
cesRealServerProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cesRealServerProbeRowStatus.setStatus("current")
_CesDfpAgent_ObjectIdentity = ObjectIdentity
cesDfpAgent = _CesDfpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 2)
)
_CesStickyConfig_ObjectIdentity = ObjectIdentity
cesStickyConfig = _CesStickyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 3)
)
_CesNotifControl_ObjectIdentity = ObjectIdentity
cesNotifControl = _CesNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 4)
)
_CesRealServerNotifEnable_Type = TruthValue
_CesRealServerNotifEnable_Object = MibScalar
cesRealServerNotifEnable = _CesRealServerNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 4, 1),
    _CesRealServerNotifEnable_Type()
)
cesRealServerNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesRealServerNotifEnable.setStatus("current")
_CesNotificationObjects_ObjectIdentity = ObjectIdentity
cesNotificationObjects = _CesNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 5)
)


class _CesRealServerName_Type(SnmpAdminString):
    """Custom type cesRealServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CesRealServerName_Type.__name__ = "SnmpAdminString"
_CesRealServerName_Object = MibScalar
cesRealServerName = _CesRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 5, 1),
    _CesRealServerName_Type()
)
cesRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cesRealServerName.setStatus("current")


class _CesProbeName_Type(SnmpAdminString):
    """Custom type cesProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CesProbeName_Type.__name__ = "SnmpAdminString"
_CesProbeName_Object = MibScalar
cesProbeName = _CesProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 5, 2),
    _CesProbeName_Type()
)
cesProbeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cesProbeName.setStatus("current")


class _CesServerFarmName_Type(SnmpAdminString):
    """Custom type cesServerFarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CesServerFarmName_Type.__name__ = "SnmpAdminString"
_CesServerFarmName_Object = MibScalar
cesServerFarmName = _CesServerFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 1, 5, 3),
    _CesServerFarmName_Type()
)
cesServerFarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cesServerFarmName.setStatus("current")
_CiscoEnhancedSlbMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEnhancedSlbMIBConformance = _CiscoEnhancedSlbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2)
)
_CiscoEnhancedSlbMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEnhancedSlbMIBCompliances = _CiscoEnhancedSlbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1)
)
_CiscoEnhancedSlbMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEnhancedSlbMIBGroups = _CiscoEnhancedSlbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2)
)

# Managed Objects groups

cesRealServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 1)
)
cesRealServerGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverDescription"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverMaxConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverMinConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectRelocationStr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectCode"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStatechangeDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRowStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeRowStatus"))
)
if mibBuilder.loadTexts:
    cesRealServerGroup.setStatus("deprecated")

cesRealServerFarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 3)
)
cesRealServerFarmGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverMaxConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverMinConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverTotalConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverFailedConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDroppedConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverCurrentConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverRowStatus"))
)
if mibBuilder.loadTexts:
    cesRealServerFarmGroup.setStatus("deprecated")

cesNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 9)
)
cesNotificationObjectGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesProbeName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerNotifEnable"))
)
if mibBuilder.loadTexts:
    cesNotificationObjectGroup.setStatus("current")

cesRealServerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 12)
)
cesRealServerGroupRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverDescription"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverMaxConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverMinConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectRelocationStr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectCode"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRedirectPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStatechangeDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverRowStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverTotalConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverFailedConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverCurrConns"))
)
if mibBuilder.loadTexts:
    cesRealServerGroupRev1.setStatus("current")

cesRserverProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 13)
)
cesRserverProbeGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeRowStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbesPassed"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbesFailed"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeHealthMonState"))
)
if mibBuilder.loadTexts:
    cesRserverProbeGroup.setStatus("deprecated")

cesRealserverProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 14)
)
cesRealserverProbeGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerProbeStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerProbeRowStatus"))
)
if mibBuilder.loadTexts:
    cesRealserverProbeGroup.setStatus("current")

cesRserverProbeGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 15)
)
cesRserverProbeGroupRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeRowStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbesPassed"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbesFailed"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeHealthMonState"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeLastProbeTime"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeLastActiveTime"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverProbeLastFailedTime"))
)
if mibBuilder.loadTexts:
    cesRserverProbeGroupRev1.setStatus("current")

cesRealServerFarmGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 19)
)
cesRealServerFarmGroupRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperWeight"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverMaxConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverMinConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverTotalConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverFailedConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDroppedConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverCurrentConns"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStorageType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverRowStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDescr"))
)
if mibBuilder.loadTexts:
    cesRealServerFarmGroupRev1.setStatus("deprecated")

cesRealServerFarmBuddyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 22)
)
cesRealServerFarmBuddyGroup.setObjects(
    ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBuddyGroup")
)
if mibBuilder.loadTexts:
    cesRealServerFarmBuddyGroup.setStatus("current")

cesRealServerGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 23)
)
cesRealServerGroupRev2.setObjects(
    ("CISCO-ENHANCED-SLB-MIB", "cesRserverLocality")
)
if mibBuilder.loadTexts:
    cesRealServerGroupRev2.setStatus("current")


# Notification objects

cesRealServerStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 1)
)
cesRealServerStateUp.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"))
)
if mibBuilder.loadTexts:
    cesRealServerStateUp.setStatus(
        "deprecated"
    )

cesRealServerStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 2)
)
cesRealServerStateDown.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"))
)
if mibBuilder.loadTexts:
    cesRealServerStateDown.setStatus(
        "deprecated"
    )

cesRealServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 3)
)
cesRealServerStateChange.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesProbeName"))
)
if mibBuilder.loadTexts:
    cesRealServerStateChange.setStatus(
        "deprecated"
    )

cesRserverStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 4)
)
cesRserverStateUp.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"))
)
if mibBuilder.loadTexts:
    cesRserverStateUp.setStatus(
        "current"
    )

cesRserverStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 5)
)
cesRserverStateDown.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"))
)
if mibBuilder.loadTexts:
    cesRserverStateDown.setStatus(
        "current"
    )

cesRserverStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 6)
)
cesRserverStateChange.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStatechangeDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesProbeName"))
)
if mibBuilder.loadTexts:
    cesRserverStateChange.setStatus(
        "current"
    )

cesRealServerStateUpRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 7)
)
cesRealServerStateUpRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDescr"))
)
if mibBuilder.loadTexts:
    cesRealServerStateUpRev1.setStatus(
        "current"
    )

cesRealServerStateDownRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 8)
)
cesRealServerStateDownRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDescr"))
)
if mibBuilder.loadTexts:
    cesRealServerStateDownRev1.setStatus(
        "current"
    )

cesRealServerStateChangeRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 9)
)
cesRealServerStateChangeRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverBackupPort"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverAdminStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverOperStatus"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverStateDescr"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddressType"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverIpAddress"),
        ("CISCO-ENHANCED-SLB-MIB", "cesProbeName"),
        ("CISCO-ENHANCED-SLB-MIB", "cesServerFarmRserverDescr"))
)
if mibBuilder.loadTexts:
    cesRealServerStateChangeRev1.setStatus(
        "current"
    )

cesRserverLocalityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 0, 10)
)
cesRserverLocalityChange.setObjects(
    ("CISCO-ENHANCED-SLB-MIB", "cesRserverLocality")
)
if mibBuilder.loadTexts:
    cesRserverLocalityChange.setStatus(
        "current"
    )


# Notifications groups

cesRealServerNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 10)
)
cesRealServerNotifGroup.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateUp"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateDown"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateChange"))
)
if mibBuilder.loadTexts:
    cesRealServerNotifGroup.setStatus(
        "deprecated"
    )

cesRealServerNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 11)
)
cesRealServerNotifGroupRev1.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateUp"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateDown"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateChange"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateUp"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateDown"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateChange"))
)
if mibBuilder.loadTexts:
    cesRealServerNotifGroupRev1.setStatus(
        "current"
    )

cesRealServerNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 21)
)
cesRealServerNotifGroupRev2.setObjects(
      *(("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateUpRev1"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateDownRev1"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRealServerStateChangeRev1"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateUp"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateDown"),
        ("CISCO-ENHANCED-SLB-MIB", "cesRserverStateChange"))
)
if mibBuilder.loadTexts:
    cesRealServerNotifGroupRev2.setStatus(
        "current"
    )

cesRealServerNotifGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 2, 24)
)
cesRealServerNotifGroupRev3.setObjects(
    ("CISCO-ENHANCED-SLB-MIB", "cesRserverLocalityChange")
)
if mibBuilder.loadTexts:
    cesRealServerNotifGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEnhancedSlbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoEnhancedSlbMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 470, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoEnhancedSlbMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-SLB-MIB",
    **{"CiscoRserverAdminStatus": CiscoRserverAdminStatus,
       "SlbRserverLocalityState": SlbRserverLocalityState,
       "ciscoEnhancedSlbMIB": ciscoEnhancedSlbMIB,
       "ciscoEnhancedSlbMIBNotifs": ciscoEnhancedSlbMIBNotifs,
       "cesRealServerStateUp": cesRealServerStateUp,
       "cesRealServerStateDown": cesRealServerStateDown,
       "cesRealServerStateChange": cesRealServerStateChange,
       "cesRserverStateUp": cesRserverStateUp,
       "cesRserverStateDown": cesRserverStateDown,
       "cesRserverStateChange": cesRserverStateChange,
       "cesRealServerStateUpRev1": cesRealServerStateUpRev1,
       "cesRealServerStateDownRev1": cesRealServerStateDownRev1,
       "cesRealServerStateChangeRev1": cesRealServerStateChangeRev1,
       "cesRserverLocalityChange": cesRserverLocalityChange,
       "ciscoEnhancedSlbMIBObjects": ciscoEnhancedSlbMIBObjects,
       "cesRealServer": cesRealServer,
       "cesRserverTable": cesRserverTable,
       "cesRserverEntry": cesRserverEntry,
       "cesRserverName": cesRserverName,
       "cesRserverType": cesRserverType,
       "cesRserverIpAddressType": cesRserverIpAddressType,
       "cesRserverIpAddress": cesRserverIpAddress,
       "cesRserverDescription": cesRserverDescription,
       "cesRserverMaxConns": cesRserverMaxConns,
       "cesRserverMinConns": cesRserverMinConns,
       "cesRserverAdminWeight": cesRserverAdminWeight,
       "cesRserverRedirectRelocationStr": cesRserverRedirectRelocationStr,
       "cesRserverRedirectCode": cesRserverRedirectCode,
       "cesRserverRedirectPort": cesRserverRedirectPort,
       "cesRserverAdminStatus": cesRserverAdminStatus,
       "cesRserverOperStatus": cesRserverOperStatus,
       "cesRserverStatechangeDescr": cesRserverStatechangeDescr,
       "cesRserverStorageType": cesRserverStorageType,
       "cesRserverRowStatus": cesRserverRowStatus,
       "cesRserverTotalConns": cesRserverTotalConns,
       "cesRserverFailedConns": cesRserverFailedConns,
       "cesRserverCurrConns": cesRserverCurrConns,
       "cesRserverLocality": cesRserverLocality,
       "cesRserverProbeTable": cesRserverProbeTable,
       "cesRserverProbeEntry": cesRserverProbeEntry,
       "cesRserverProbeName": cesRserverProbeName,
       "cesRserverProbeStorageType": cesRserverProbeStorageType,
       "cesRserverProbeRowStatus": cesRserverProbeRowStatus,
       "cesRserverProbesPassed": cesRserverProbesPassed,
       "cesRserverProbesFailed": cesRserverProbesFailed,
       "cesRserverProbeHealthMonState": cesRserverProbeHealthMonState,
       "cesRserverProbeLastProbeTime": cesRserverProbeLastProbeTime,
       "cesRserverProbeLastActiveTime": cesRserverProbeLastActiveTime,
       "cesRserverProbeLastFailedTime": cesRserverProbeLastFailedTime,
       "cesServerFarmRserverTable": cesServerFarmRserverTable,
       "cesServerFarmRserverEntry": cesServerFarmRserverEntry,
       "cesServerFarmRserverPort": cesServerFarmRserverPort,
       "cesServerFarmRserverAdminWeight": cesServerFarmRserverAdminWeight,
       "cesServerFarmRserverOperWeight": cesServerFarmRserverOperWeight,
       "cesServerFarmRserverMaxConns": cesServerFarmRserverMaxConns,
       "cesServerFarmRserverMinConns": cesServerFarmRserverMinConns,
       "cesServerFarmRserverAdminStatus": cesServerFarmRserverAdminStatus,
       "cesServerFarmRserverOperStatus": cesServerFarmRserverOperStatus,
       "cesServerFarmRserverStateDescr": cesServerFarmRserverStateDescr,
       "cesServerFarmRserverBackupName": cesServerFarmRserverBackupName,
       "cesServerFarmRserverBackupPort": cesServerFarmRserverBackupPort,
       "cesServerFarmRserverTotalConns": cesServerFarmRserverTotalConns,
       "cesServerFarmRserverFailedConns": cesServerFarmRserverFailedConns,
       "cesServerFarmRserverDroppedConns": cesServerFarmRserverDroppedConns,
       "cesServerFarmRserverCurrentConns": cesServerFarmRserverCurrentConns,
       "cesServerFarmRserverStorageType": cesServerFarmRserverStorageType,
       "cesServerFarmRserverRowStatus": cesServerFarmRserverRowStatus,
       "cesServerFarmRserverDescr": cesServerFarmRserverDescr,
       "cesServerFarmRserverBuddyGroup": cesServerFarmRserverBuddyGroup,
       "cesRealServerProbeTable": cesRealServerProbeTable,
       "cesRealServerProbeEntry": cesRealServerProbeEntry,
       "cesRealServerProbeStorageType": cesRealServerProbeStorageType,
       "cesRealServerProbeRowStatus": cesRealServerProbeRowStatus,
       "cesDfpAgent": cesDfpAgent,
       "cesStickyConfig": cesStickyConfig,
       "cesNotifControl": cesNotifControl,
       "cesRealServerNotifEnable": cesRealServerNotifEnable,
       "cesNotificationObjects": cesNotificationObjects,
       "cesRealServerName": cesRealServerName,
       "cesProbeName": cesProbeName,
       "cesServerFarmName": cesServerFarmName,
       "ciscoEnhancedSlbMIBConformance": ciscoEnhancedSlbMIBConformance,
       "ciscoEnhancedSlbMIBCompliances": ciscoEnhancedSlbMIBCompliances,
       "ciscoEnhancedSlbMIBCompliance": ciscoEnhancedSlbMIBCompliance,
       "ciscoEnhancedSlbMIBComplianceRev1": ciscoEnhancedSlbMIBComplianceRev1,
       "ciscoEnhancedSlbMIBComplianceRev2": ciscoEnhancedSlbMIBComplianceRev2,
       "ciscoEnhancedSlbMIBComplianceRev3": ciscoEnhancedSlbMIBComplianceRev3,
       "ciscoEnhancedSlbMIBComplianceRev4": ciscoEnhancedSlbMIBComplianceRev4,
       "ciscoEnhancedSlbMIBComplianceRev5": ciscoEnhancedSlbMIBComplianceRev5,
       "ciscoEnhancedSlbMIBComplianceRev6": ciscoEnhancedSlbMIBComplianceRev6,
       "ciscoEnhancedSlbMIBGroups": ciscoEnhancedSlbMIBGroups,
       "cesRealServerGroup": cesRealServerGroup,
       "cesRealServerFarmGroup": cesRealServerFarmGroup,
       "cesNotificationObjectGroup": cesNotificationObjectGroup,
       "cesRealServerNotifGroup": cesRealServerNotifGroup,
       "cesRealServerNotifGroupRev1": cesRealServerNotifGroupRev1,
       "cesRealServerGroupRev1": cesRealServerGroupRev1,
       "cesRserverProbeGroup": cesRserverProbeGroup,
       "cesRealserverProbeGroup": cesRealserverProbeGroup,
       "cesRserverProbeGroupRev1": cesRserverProbeGroupRev1,
       "cesRealServerFarmGroupRev1": cesRealServerFarmGroupRev1,
       "cesRealServerNotifGroupRev2": cesRealServerNotifGroupRev2,
       "cesRealServerFarmBuddyGroup": cesRealServerFarmBuddyGroup,
       "cesRealServerGroupRev2": cesRealServerGroupRev2,
       "cesRealServerNotifGroupRev3": cesRealServerNotifGroupRev3}
)
