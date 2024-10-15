# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:17 2024
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

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsDomainFeatureType,
 CucsDomainFunctionalState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsDomainFeatureType",
    "CucsDomainFunctionalState")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsDomainObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDomainEnvironmentFeatureTable_Object = MibTable
cucsDomainEnvironmentFeatureTable = _CucsDomainEnvironmentFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1)
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureTable.setStatus("current")
_CucsDomainEnvironmentFeatureEntry_Object = MibTableRow
cucsDomainEnvironmentFeatureEntry = _CucsDomainEnvironmentFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1)
)
cucsDomainEnvironmentFeatureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainEnvironmentFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureEntry.setStatus("current")
_CucsDomainEnvironmentFeatureInstanceId_Type = CucsManagedObjectId
_CucsDomainEnvironmentFeatureInstanceId_Object = MibTableColumn
cucsDomainEnvironmentFeatureInstanceId = _CucsDomainEnvironmentFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 1),
    _CucsDomainEnvironmentFeatureInstanceId_Type()
)
cucsDomainEnvironmentFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureInstanceId.setStatus("current")
_CucsDomainEnvironmentFeatureDn_Type = CucsManagedObjectDn
_CucsDomainEnvironmentFeatureDn_Object = MibTableColumn
cucsDomainEnvironmentFeatureDn = _CucsDomainEnvironmentFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 2),
    _CucsDomainEnvironmentFeatureDn_Type()
)
cucsDomainEnvironmentFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureDn.setStatus("current")
_CucsDomainEnvironmentFeatureRn_Type = SnmpAdminString
_CucsDomainEnvironmentFeatureRn_Object = MibTableColumn
cucsDomainEnvironmentFeatureRn = _CucsDomainEnvironmentFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 3),
    _CucsDomainEnvironmentFeatureRn_Type()
)
cucsDomainEnvironmentFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureRn.setStatus("current")
_CucsDomainEnvironmentFeatureFltAggr_Type = Unsigned64
_CucsDomainEnvironmentFeatureFltAggr_Object = MibTableColumn
cucsDomainEnvironmentFeatureFltAggr = _CucsDomainEnvironmentFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 4),
    _CucsDomainEnvironmentFeatureFltAggr_Type()
)
cucsDomainEnvironmentFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureFltAggr.setStatus("current")
_CucsDomainEnvironmentFeatureFunctionalState_Type = CucsDomainFunctionalState
_CucsDomainEnvironmentFeatureFunctionalState_Object = MibTableColumn
cucsDomainEnvironmentFeatureFunctionalState = _CucsDomainEnvironmentFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 5),
    _CucsDomainEnvironmentFeatureFunctionalState_Type()
)
cucsDomainEnvironmentFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureFunctionalState.setStatus("current")
_CucsDomainEnvironmentFeatureName_Type = SnmpAdminString
_CucsDomainEnvironmentFeatureName_Object = MibTableColumn
cucsDomainEnvironmentFeatureName = _CucsDomainEnvironmentFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 6),
    _CucsDomainEnvironmentFeatureName_Type()
)
cucsDomainEnvironmentFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureName.setStatus("current")
_CucsDomainEnvironmentFeatureType_Type = CucsDomainFeatureType
_CucsDomainEnvironmentFeatureType_Object = MibTableColumn
cucsDomainEnvironmentFeatureType = _CucsDomainEnvironmentFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 1, 1, 7),
    _CucsDomainEnvironmentFeatureType_Type()
)
cucsDomainEnvironmentFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureType.setStatus("current")
_CucsDomainEnvironmentParamTable_Object = MibTable
cucsDomainEnvironmentParamTable = _CucsDomainEnvironmentParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2)
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamTable.setStatus("current")
_CucsDomainEnvironmentParamEntry_Object = MibTableRow
cucsDomainEnvironmentParamEntry = _CucsDomainEnvironmentParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1)
)
cucsDomainEnvironmentParamEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainEnvironmentParamInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamEntry.setStatus("current")
_CucsDomainEnvironmentParamInstanceId_Type = CucsManagedObjectId
_CucsDomainEnvironmentParamInstanceId_Object = MibTableColumn
cucsDomainEnvironmentParamInstanceId = _CucsDomainEnvironmentParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 1),
    _CucsDomainEnvironmentParamInstanceId_Type()
)
cucsDomainEnvironmentParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamInstanceId.setStatus("current")
_CucsDomainEnvironmentParamDn_Type = CucsManagedObjectDn
_CucsDomainEnvironmentParamDn_Object = MibTableColumn
cucsDomainEnvironmentParamDn = _CucsDomainEnvironmentParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 2),
    _CucsDomainEnvironmentParamDn_Type()
)
cucsDomainEnvironmentParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamDn.setStatus("current")
_CucsDomainEnvironmentParamRn_Type = SnmpAdminString
_CucsDomainEnvironmentParamRn_Object = MibTableColumn
cucsDomainEnvironmentParamRn = _CucsDomainEnvironmentParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 3),
    _CucsDomainEnvironmentParamRn_Type()
)
cucsDomainEnvironmentParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamRn.setStatus("current")
_CucsDomainEnvironmentParamFltAggr_Type = Unsigned64
_CucsDomainEnvironmentParamFltAggr_Object = MibTableColumn
cucsDomainEnvironmentParamFltAggr = _CucsDomainEnvironmentParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 4),
    _CucsDomainEnvironmentParamFltAggr_Type()
)
cucsDomainEnvironmentParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamFltAggr.setStatus("current")
_CucsDomainEnvironmentParamName_Type = SnmpAdminString
_CucsDomainEnvironmentParamName_Object = MibTableColumn
cucsDomainEnvironmentParamName = _CucsDomainEnvironmentParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 5),
    _CucsDomainEnvironmentParamName_Type()
)
cucsDomainEnvironmentParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamName.setStatus("current")
_CucsDomainEnvironmentParamValue_Type = SnmpAdminString
_CucsDomainEnvironmentParamValue_Object = MibTableColumn
cucsDomainEnvironmentParamValue = _CucsDomainEnvironmentParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 2, 1, 6),
    _CucsDomainEnvironmentParamValue_Type()
)
cucsDomainEnvironmentParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentParamValue.setStatus("current")
_CucsDomainNetworkFeatureTable_Object = MibTable
cucsDomainNetworkFeatureTable = _CucsDomainNetworkFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3)
)
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureTable.setStatus("current")
_CucsDomainNetworkFeatureEntry_Object = MibTableRow
cucsDomainNetworkFeatureEntry = _CucsDomainNetworkFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1)
)
cucsDomainNetworkFeatureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainNetworkFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureEntry.setStatus("current")
_CucsDomainNetworkFeatureInstanceId_Type = CucsManagedObjectId
_CucsDomainNetworkFeatureInstanceId_Object = MibTableColumn
cucsDomainNetworkFeatureInstanceId = _CucsDomainNetworkFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 1),
    _CucsDomainNetworkFeatureInstanceId_Type()
)
cucsDomainNetworkFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureInstanceId.setStatus("current")
_CucsDomainNetworkFeatureDn_Type = CucsManagedObjectDn
_CucsDomainNetworkFeatureDn_Object = MibTableColumn
cucsDomainNetworkFeatureDn = _CucsDomainNetworkFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 2),
    _CucsDomainNetworkFeatureDn_Type()
)
cucsDomainNetworkFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureDn.setStatus("current")
_CucsDomainNetworkFeatureRn_Type = SnmpAdminString
_CucsDomainNetworkFeatureRn_Object = MibTableColumn
cucsDomainNetworkFeatureRn = _CucsDomainNetworkFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 3),
    _CucsDomainNetworkFeatureRn_Type()
)
cucsDomainNetworkFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureRn.setStatus("current")
_CucsDomainNetworkFeatureFltAggr_Type = Unsigned64
_CucsDomainNetworkFeatureFltAggr_Object = MibTableColumn
cucsDomainNetworkFeatureFltAggr = _CucsDomainNetworkFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 4),
    _CucsDomainNetworkFeatureFltAggr_Type()
)
cucsDomainNetworkFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureFltAggr.setStatus("current")
_CucsDomainNetworkFeatureFunctionalState_Type = CucsDomainFunctionalState
_CucsDomainNetworkFeatureFunctionalState_Object = MibTableColumn
cucsDomainNetworkFeatureFunctionalState = _CucsDomainNetworkFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 5),
    _CucsDomainNetworkFeatureFunctionalState_Type()
)
cucsDomainNetworkFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureFunctionalState.setStatus("current")
_CucsDomainNetworkFeatureName_Type = SnmpAdminString
_CucsDomainNetworkFeatureName_Object = MibTableColumn
cucsDomainNetworkFeatureName = _CucsDomainNetworkFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 6),
    _CucsDomainNetworkFeatureName_Type()
)
cucsDomainNetworkFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureName.setStatus("current")
_CucsDomainNetworkFeatureType_Type = CucsDomainFeatureType
_CucsDomainNetworkFeatureType_Object = MibTableColumn
cucsDomainNetworkFeatureType = _CucsDomainNetworkFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 3, 1, 7),
    _CucsDomainNetworkFeatureType_Type()
)
cucsDomainNetworkFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureType.setStatus("current")
_CucsDomainNetworkParamTable_Object = MibTable
cucsDomainNetworkParamTable = _CucsDomainNetworkParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4)
)
if mibBuilder.loadTexts:
    cucsDomainNetworkParamTable.setStatus("current")
_CucsDomainNetworkParamEntry_Object = MibTableRow
cucsDomainNetworkParamEntry = _CucsDomainNetworkParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1)
)
cucsDomainNetworkParamEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainNetworkParamInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainNetworkParamEntry.setStatus("current")
_CucsDomainNetworkParamInstanceId_Type = CucsManagedObjectId
_CucsDomainNetworkParamInstanceId_Object = MibTableColumn
cucsDomainNetworkParamInstanceId = _CucsDomainNetworkParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 1),
    _CucsDomainNetworkParamInstanceId_Type()
)
cucsDomainNetworkParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamInstanceId.setStatus("current")
_CucsDomainNetworkParamDn_Type = CucsManagedObjectDn
_CucsDomainNetworkParamDn_Object = MibTableColumn
cucsDomainNetworkParamDn = _CucsDomainNetworkParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 2),
    _CucsDomainNetworkParamDn_Type()
)
cucsDomainNetworkParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamDn.setStatus("current")
_CucsDomainNetworkParamRn_Type = SnmpAdminString
_CucsDomainNetworkParamRn_Object = MibTableColumn
cucsDomainNetworkParamRn = _CucsDomainNetworkParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 3),
    _CucsDomainNetworkParamRn_Type()
)
cucsDomainNetworkParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamRn.setStatus("current")
_CucsDomainNetworkParamFltAggr_Type = Unsigned64
_CucsDomainNetworkParamFltAggr_Object = MibTableColumn
cucsDomainNetworkParamFltAggr = _CucsDomainNetworkParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 4),
    _CucsDomainNetworkParamFltAggr_Type()
)
cucsDomainNetworkParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamFltAggr.setStatus("current")
_CucsDomainNetworkParamName_Type = SnmpAdminString
_CucsDomainNetworkParamName_Object = MibTableColumn
cucsDomainNetworkParamName = _CucsDomainNetworkParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 5),
    _CucsDomainNetworkParamName_Type()
)
cucsDomainNetworkParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamName.setStatus("current")
_CucsDomainNetworkParamValue_Type = SnmpAdminString
_CucsDomainNetworkParamValue_Object = MibTableColumn
cucsDomainNetworkParamValue = _CucsDomainNetworkParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 4, 1, 6),
    _CucsDomainNetworkParamValue_Type()
)
cucsDomainNetworkParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkParamValue.setStatus("current")
_CucsDomainServerFeatureTable_Object = MibTable
cucsDomainServerFeatureTable = _CucsDomainServerFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5)
)
if mibBuilder.loadTexts:
    cucsDomainServerFeatureTable.setStatus("current")
_CucsDomainServerFeatureEntry_Object = MibTableRow
cucsDomainServerFeatureEntry = _CucsDomainServerFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1)
)
cucsDomainServerFeatureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainServerFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainServerFeatureEntry.setStatus("current")
_CucsDomainServerFeatureInstanceId_Type = CucsManagedObjectId
_CucsDomainServerFeatureInstanceId_Object = MibTableColumn
cucsDomainServerFeatureInstanceId = _CucsDomainServerFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 1),
    _CucsDomainServerFeatureInstanceId_Type()
)
cucsDomainServerFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureInstanceId.setStatus("current")
_CucsDomainServerFeatureDn_Type = CucsManagedObjectDn
_CucsDomainServerFeatureDn_Object = MibTableColumn
cucsDomainServerFeatureDn = _CucsDomainServerFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 2),
    _CucsDomainServerFeatureDn_Type()
)
cucsDomainServerFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureDn.setStatus("current")
_CucsDomainServerFeatureRn_Type = SnmpAdminString
_CucsDomainServerFeatureRn_Object = MibTableColumn
cucsDomainServerFeatureRn = _CucsDomainServerFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 3),
    _CucsDomainServerFeatureRn_Type()
)
cucsDomainServerFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureRn.setStatus("current")
_CucsDomainServerFeatureFltAggr_Type = Unsigned64
_CucsDomainServerFeatureFltAggr_Object = MibTableColumn
cucsDomainServerFeatureFltAggr = _CucsDomainServerFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 4),
    _CucsDomainServerFeatureFltAggr_Type()
)
cucsDomainServerFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureFltAggr.setStatus("current")
_CucsDomainServerFeatureFunctionalState_Type = CucsDomainFunctionalState
_CucsDomainServerFeatureFunctionalState_Object = MibTableColumn
cucsDomainServerFeatureFunctionalState = _CucsDomainServerFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 5),
    _CucsDomainServerFeatureFunctionalState_Type()
)
cucsDomainServerFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureFunctionalState.setStatus("current")
_CucsDomainServerFeatureName_Type = SnmpAdminString
_CucsDomainServerFeatureName_Object = MibTableColumn
cucsDomainServerFeatureName = _CucsDomainServerFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 6),
    _CucsDomainServerFeatureName_Type()
)
cucsDomainServerFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureName.setStatus("current")
_CucsDomainServerFeatureType_Type = CucsDomainFeatureType
_CucsDomainServerFeatureType_Object = MibTableColumn
cucsDomainServerFeatureType = _CucsDomainServerFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 5, 1, 7),
    _CucsDomainServerFeatureType_Type()
)
cucsDomainServerFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureType.setStatus("current")
_CucsDomainServerParamTable_Object = MibTable
cucsDomainServerParamTable = _CucsDomainServerParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6)
)
if mibBuilder.loadTexts:
    cucsDomainServerParamTable.setStatus("current")
_CucsDomainServerParamEntry_Object = MibTableRow
cucsDomainServerParamEntry = _CucsDomainServerParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1)
)
cucsDomainServerParamEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainServerParamInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainServerParamEntry.setStatus("current")
_CucsDomainServerParamInstanceId_Type = CucsManagedObjectId
_CucsDomainServerParamInstanceId_Object = MibTableColumn
cucsDomainServerParamInstanceId = _CucsDomainServerParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 1),
    _CucsDomainServerParamInstanceId_Type()
)
cucsDomainServerParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainServerParamInstanceId.setStatus("current")
_CucsDomainServerParamDn_Type = CucsManagedObjectDn
_CucsDomainServerParamDn_Object = MibTableColumn
cucsDomainServerParamDn = _CucsDomainServerParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 2),
    _CucsDomainServerParamDn_Type()
)
cucsDomainServerParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerParamDn.setStatus("current")
_CucsDomainServerParamRn_Type = SnmpAdminString
_CucsDomainServerParamRn_Object = MibTableColumn
cucsDomainServerParamRn = _CucsDomainServerParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 3),
    _CucsDomainServerParamRn_Type()
)
cucsDomainServerParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerParamRn.setStatus("current")
_CucsDomainServerParamFltAggr_Type = Unsigned64
_CucsDomainServerParamFltAggr_Object = MibTableColumn
cucsDomainServerParamFltAggr = _CucsDomainServerParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 4),
    _CucsDomainServerParamFltAggr_Type()
)
cucsDomainServerParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerParamFltAggr.setStatus("current")
_CucsDomainServerParamName_Type = SnmpAdminString
_CucsDomainServerParamName_Object = MibTableColumn
cucsDomainServerParamName = _CucsDomainServerParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 5),
    _CucsDomainServerParamName_Type()
)
cucsDomainServerParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerParamName.setStatus("current")
_CucsDomainServerParamValue_Type = SnmpAdminString
_CucsDomainServerParamValue_Object = MibTableColumn
cucsDomainServerParamValue = _CucsDomainServerParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 6, 1, 6),
    _CucsDomainServerParamValue_Type()
)
cucsDomainServerParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerParamValue.setStatus("current")
_CucsDomainStorageFeatureTable_Object = MibTable
cucsDomainStorageFeatureTable = _CucsDomainStorageFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7)
)
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureTable.setStatus("current")
_CucsDomainStorageFeatureEntry_Object = MibTableRow
cucsDomainStorageFeatureEntry = _CucsDomainStorageFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1)
)
cucsDomainStorageFeatureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainStorageFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureEntry.setStatus("current")
_CucsDomainStorageFeatureInstanceId_Type = CucsManagedObjectId
_CucsDomainStorageFeatureInstanceId_Object = MibTableColumn
cucsDomainStorageFeatureInstanceId = _CucsDomainStorageFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 1),
    _CucsDomainStorageFeatureInstanceId_Type()
)
cucsDomainStorageFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureInstanceId.setStatus("current")
_CucsDomainStorageFeatureDn_Type = CucsManagedObjectDn
_CucsDomainStorageFeatureDn_Object = MibTableColumn
cucsDomainStorageFeatureDn = _CucsDomainStorageFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 2),
    _CucsDomainStorageFeatureDn_Type()
)
cucsDomainStorageFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureDn.setStatus("current")
_CucsDomainStorageFeatureRn_Type = SnmpAdminString
_CucsDomainStorageFeatureRn_Object = MibTableColumn
cucsDomainStorageFeatureRn = _CucsDomainStorageFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 3),
    _CucsDomainStorageFeatureRn_Type()
)
cucsDomainStorageFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureRn.setStatus("current")
_CucsDomainStorageFeatureFltAggr_Type = Unsigned64
_CucsDomainStorageFeatureFltAggr_Object = MibTableColumn
cucsDomainStorageFeatureFltAggr = _CucsDomainStorageFeatureFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 4),
    _CucsDomainStorageFeatureFltAggr_Type()
)
cucsDomainStorageFeatureFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureFltAggr.setStatus("current")
_CucsDomainStorageFeatureFunctionalState_Type = CucsDomainFunctionalState
_CucsDomainStorageFeatureFunctionalState_Object = MibTableColumn
cucsDomainStorageFeatureFunctionalState = _CucsDomainStorageFeatureFunctionalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 5),
    _CucsDomainStorageFeatureFunctionalState_Type()
)
cucsDomainStorageFeatureFunctionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureFunctionalState.setStatus("current")
_CucsDomainStorageFeatureName_Type = SnmpAdminString
_CucsDomainStorageFeatureName_Object = MibTableColumn
cucsDomainStorageFeatureName = _CucsDomainStorageFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 6),
    _CucsDomainStorageFeatureName_Type()
)
cucsDomainStorageFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureName.setStatus("current")
_CucsDomainStorageFeatureType_Type = CucsDomainFeatureType
_CucsDomainStorageFeatureType_Object = MibTableColumn
cucsDomainStorageFeatureType = _CucsDomainStorageFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 7, 1, 7),
    _CucsDomainStorageFeatureType_Type()
)
cucsDomainStorageFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureType.setStatus("current")
_CucsDomainStorageParamTable_Object = MibTable
cucsDomainStorageParamTable = _CucsDomainStorageParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8)
)
if mibBuilder.loadTexts:
    cucsDomainStorageParamTable.setStatus("current")
_CucsDomainStorageParamEntry_Object = MibTableRow
cucsDomainStorageParamEntry = _CucsDomainStorageParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1)
)
cucsDomainStorageParamEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainStorageParamInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainStorageParamEntry.setStatus("current")
_CucsDomainStorageParamInstanceId_Type = CucsManagedObjectId
_CucsDomainStorageParamInstanceId_Object = MibTableColumn
cucsDomainStorageParamInstanceId = _CucsDomainStorageParamInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 1),
    _CucsDomainStorageParamInstanceId_Type()
)
cucsDomainStorageParamInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainStorageParamInstanceId.setStatus("current")
_CucsDomainStorageParamDn_Type = CucsManagedObjectDn
_CucsDomainStorageParamDn_Object = MibTableColumn
cucsDomainStorageParamDn = _CucsDomainStorageParamDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 2),
    _CucsDomainStorageParamDn_Type()
)
cucsDomainStorageParamDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageParamDn.setStatus("current")
_CucsDomainStorageParamRn_Type = SnmpAdminString
_CucsDomainStorageParamRn_Object = MibTableColumn
cucsDomainStorageParamRn = _CucsDomainStorageParamRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 3),
    _CucsDomainStorageParamRn_Type()
)
cucsDomainStorageParamRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageParamRn.setStatus("current")
_CucsDomainStorageParamFltAggr_Type = Unsigned64
_CucsDomainStorageParamFltAggr_Object = MibTableColumn
cucsDomainStorageParamFltAggr = _CucsDomainStorageParamFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 4),
    _CucsDomainStorageParamFltAggr_Type()
)
cucsDomainStorageParamFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageParamFltAggr.setStatus("current")
_CucsDomainStorageParamName_Type = SnmpAdminString
_CucsDomainStorageParamName_Object = MibTableColumn
cucsDomainStorageParamName = _CucsDomainStorageParamName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 5),
    _CucsDomainStorageParamName_Type()
)
cucsDomainStorageParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageParamName.setStatus("current")
_CucsDomainStorageParamValue_Type = SnmpAdminString
_CucsDomainStorageParamValue_Object = MibTableColumn
cucsDomainStorageParamValue = _CucsDomainStorageParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 8, 1, 6),
    _CucsDomainStorageParamValue_Type()
)
cucsDomainStorageParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageParamValue.setStatus("current")
_CucsDomainEnvironmentFeatureContTable_Object = MibTable
cucsDomainEnvironmentFeatureContTable = _CucsDomainEnvironmentFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9)
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContTable.setStatus("current")
_CucsDomainEnvironmentFeatureContEntry_Object = MibTableRow
cucsDomainEnvironmentFeatureContEntry = _CucsDomainEnvironmentFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9, 1)
)
cucsDomainEnvironmentFeatureContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainEnvironmentFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContEntry.setStatus("current")
_CucsDomainEnvironmentFeatureContInstanceId_Type = CucsManagedObjectId
_CucsDomainEnvironmentFeatureContInstanceId_Object = MibTableColumn
cucsDomainEnvironmentFeatureContInstanceId = _CucsDomainEnvironmentFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9, 1, 1),
    _CucsDomainEnvironmentFeatureContInstanceId_Type()
)
cucsDomainEnvironmentFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContInstanceId.setStatus("current")
_CucsDomainEnvironmentFeatureContDn_Type = CucsManagedObjectDn
_CucsDomainEnvironmentFeatureContDn_Object = MibTableColumn
cucsDomainEnvironmentFeatureContDn = _CucsDomainEnvironmentFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9, 1, 2),
    _CucsDomainEnvironmentFeatureContDn_Type()
)
cucsDomainEnvironmentFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContDn.setStatus("current")
_CucsDomainEnvironmentFeatureContRn_Type = SnmpAdminString
_CucsDomainEnvironmentFeatureContRn_Object = MibTableColumn
cucsDomainEnvironmentFeatureContRn = _CucsDomainEnvironmentFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9, 1, 3),
    _CucsDomainEnvironmentFeatureContRn_Type()
)
cucsDomainEnvironmentFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContRn.setStatus("current")
_CucsDomainEnvironmentFeatureContFltAggr_Type = Unsigned64
_CucsDomainEnvironmentFeatureContFltAggr_Object = MibTableColumn
cucsDomainEnvironmentFeatureContFltAggr = _CucsDomainEnvironmentFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 9, 1, 4),
    _CucsDomainEnvironmentFeatureContFltAggr_Type()
)
cucsDomainEnvironmentFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainEnvironmentFeatureContFltAggr.setStatus("current")
_CucsDomainNetworkFeatureContTable_Object = MibTable
cucsDomainNetworkFeatureContTable = _CucsDomainNetworkFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10)
)
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContTable.setStatus("current")
_CucsDomainNetworkFeatureContEntry_Object = MibTableRow
cucsDomainNetworkFeatureContEntry = _CucsDomainNetworkFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10, 1)
)
cucsDomainNetworkFeatureContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainNetworkFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContEntry.setStatus("current")
_CucsDomainNetworkFeatureContInstanceId_Type = CucsManagedObjectId
_CucsDomainNetworkFeatureContInstanceId_Object = MibTableColumn
cucsDomainNetworkFeatureContInstanceId = _CucsDomainNetworkFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10, 1, 1),
    _CucsDomainNetworkFeatureContInstanceId_Type()
)
cucsDomainNetworkFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContInstanceId.setStatus("current")
_CucsDomainNetworkFeatureContDn_Type = CucsManagedObjectDn
_CucsDomainNetworkFeatureContDn_Object = MibTableColumn
cucsDomainNetworkFeatureContDn = _CucsDomainNetworkFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10, 1, 2),
    _CucsDomainNetworkFeatureContDn_Type()
)
cucsDomainNetworkFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContDn.setStatus("current")
_CucsDomainNetworkFeatureContRn_Type = SnmpAdminString
_CucsDomainNetworkFeatureContRn_Object = MibTableColumn
cucsDomainNetworkFeatureContRn = _CucsDomainNetworkFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10, 1, 3),
    _CucsDomainNetworkFeatureContRn_Type()
)
cucsDomainNetworkFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContRn.setStatus("current")
_CucsDomainNetworkFeatureContFltAggr_Type = Unsigned64
_CucsDomainNetworkFeatureContFltAggr_Object = MibTableColumn
cucsDomainNetworkFeatureContFltAggr = _CucsDomainNetworkFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 10, 1, 4),
    _CucsDomainNetworkFeatureContFltAggr_Type()
)
cucsDomainNetworkFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainNetworkFeatureContFltAggr.setStatus("current")
_CucsDomainServerFeatureContTable_Object = MibTable
cucsDomainServerFeatureContTable = _CucsDomainServerFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11)
)
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContTable.setStatus("current")
_CucsDomainServerFeatureContEntry_Object = MibTableRow
cucsDomainServerFeatureContEntry = _CucsDomainServerFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11, 1)
)
cucsDomainServerFeatureContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainServerFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContEntry.setStatus("current")
_CucsDomainServerFeatureContInstanceId_Type = CucsManagedObjectId
_CucsDomainServerFeatureContInstanceId_Object = MibTableColumn
cucsDomainServerFeatureContInstanceId = _CucsDomainServerFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11, 1, 1),
    _CucsDomainServerFeatureContInstanceId_Type()
)
cucsDomainServerFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContInstanceId.setStatus("current")
_CucsDomainServerFeatureContDn_Type = CucsManagedObjectDn
_CucsDomainServerFeatureContDn_Object = MibTableColumn
cucsDomainServerFeatureContDn = _CucsDomainServerFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11, 1, 2),
    _CucsDomainServerFeatureContDn_Type()
)
cucsDomainServerFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContDn.setStatus("current")
_CucsDomainServerFeatureContRn_Type = SnmpAdminString
_CucsDomainServerFeatureContRn_Object = MibTableColumn
cucsDomainServerFeatureContRn = _CucsDomainServerFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11, 1, 3),
    _CucsDomainServerFeatureContRn_Type()
)
cucsDomainServerFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContRn.setStatus("current")
_CucsDomainServerFeatureContFltAggr_Type = Unsigned64
_CucsDomainServerFeatureContFltAggr_Object = MibTableColumn
cucsDomainServerFeatureContFltAggr = _CucsDomainServerFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 11, 1, 4),
    _CucsDomainServerFeatureContFltAggr_Type()
)
cucsDomainServerFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainServerFeatureContFltAggr.setStatus("current")
_CucsDomainStorageFeatureContTable_Object = MibTable
cucsDomainStorageFeatureContTable = _CucsDomainStorageFeatureContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12)
)
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContTable.setStatus("current")
_CucsDomainStorageFeatureContEntry_Object = MibTableRow
cucsDomainStorageFeatureContEntry = _CucsDomainStorageFeatureContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12, 1)
)
cucsDomainStorageFeatureContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB", "cucsDomainStorageFeatureContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContEntry.setStatus("current")
_CucsDomainStorageFeatureContInstanceId_Type = CucsManagedObjectId
_CucsDomainStorageFeatureContInstanceId_Object = MibTableColumn
cucsDomainStorageFeatureContInstanceId = _CucsDomainStorageFeatureContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12, 1, 1),
    _CucsDomainStorageFeatureContInstanceId_Type()
)
cucsDomainStorageFeatureContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContInstanceId.setStatus("current")
_CucsDomainStorageFeatureContDn_Type = CucsManagedObjectDn
_CucsDomainStorageFeatureContDn_Object = MibTableColumn
cucsDomainStorageFeatureContDn = _CucsDomainStorageFeatureContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12, 1, 2),
    _CucsDomainStorageFeatureContDn_Type()
)
cucsDomainStorageFeatureContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContDn.setStatus("current")
_CucsDomainStorageFeatureContRn_Type = SnmpAdminString
_CucsDomainStorageFeatureContRn_Object = MibTableColumn
cucsDomainStorageFeatureContRn = _CucsDomainStorageFeatureContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12, 1, 3),
    _CucsDomainStorageFeatureContRn_Type()
)
cucsDomainStorageFeatureContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContRn.setStatus("current")
_CucsDomainStorageFeatureContFltAggr_Type = Unsigned64
_CucsDomainStorageFeatureContFltAggr_Object = MibTableColumn
cucsDomainStorageFeatureContFltAggr = _CucsDomainStorageFeatureContFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 74, 12, 1, 4),
    _CucsDomainStorageFeatureContFltAggr_Type()
)
cucsDomainStorageFeatureContFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDomainStorageFeatureContFltAggr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DOMAIN-MIB",
    **{"cucsDomainObjects": cucsDomainObjects,
       "cucsDomainEnvironmentFeatureTable": cucsDomainEnvironmentFeatureTable,
       "cucsDomainEnvironmentFeatureEntry": cucsDomainEnvironmentFeatureEntry,
       "cucsDomainEnvironmentFeatureInstanceId": cucsDomainEnvironmentFeatureInstanceId,
       "cucsDomainEnvironmentFeatureDn": cucsDomainEnvironmentFeatureDn,
       "cucsDomainEnvironmentFeatureRn": cucsDomainEnvironmentFeatureRn,
       "cucsDomainEnvironmentFeatureFltAggr": cucsDomainEnvironmentFeatureFltAggr,
       "cucsDomainEnvironmentFeatureFunctionalState": cucsDomainEnvironmentFeatureFunctionalState,
       "cucsDomainEnvironmentFeatureName": cucsDomainEnvironmentFeatureName,
       "cucsDomainEnvironmentFeatureType": cucsDomainEnvironmentFeatureType,
       "cucsDomainEnvironmentParamTable": cucsDomainEnvironmentParamTable,
       "cucsDomainEnvironmentParamEntry": cucsDomainEnvironmentParamEntry,
       "cucsDomainEnvironmentParamInstanceId": cucsDomainEnvironmentParamInstanceId,
       "cucsDomainEnvironmentParamDn": cucsDomainEnvironmentParamDn,
       "cucsDomainEnvironmentParamRn": cucsDomainEnvironmentParamRn,
       "cucsDomainEnvironmentParamFltAggr": cucsDomainEnvironmentParamFltAggr,
       "cucsDomainEnvironmentParamName": cucsDomainEnvironmentParamName,
       "cucsDomainEnvironmentParamValue": cucsDomainEnvironmentParamValue,
       "cucsDomainNetworkFeatureTable": cucsDomainNetworkFeatureTable,
       "cucsDomainNetworkFeatureEntry": cucsDomainNetworkFeatureEntry,
       "cucsDomainNetworkFeatureInstanceId": cucsDomainNetworkFeatureInstanceId,
       "cucsDomainNetworkFeatureDn": cucsDomainNetworkFeatureDn,
       "cucsDomainNetworkFeatureRn": cucsDomainNetworkFeatureRn,
       "cucsDomainNetworkFeatureFltAggr": cucsDomainNetworkFeatureFltAggr,
       "cucsDomainNetworkFeatureFunctionalState": cucsDomainNetworkFeatureFunctionalState,
       "cucsDomainNetworkFeatureName": cucsDomainNetworkFeatureName,
       "cucsDomainNetworkFeatureType": cucsDomainNetworkFeatureType,
       "cucsDomainNetworkParamTable": cucsDomainNetworkParamTable,
       "cucsDomainNetworkParamEntry": cucsDomainNetworkParamEntry,
       "cucsDomainNetworkParamInstanceId": cucsDomainNetworkParamInstanceId,
       "cucsDomainNetworkParamDn": cucsDomainNetworkParamDn,
       "cucsDomainNetworkParamRn": cucsDomainNetworkParamRn,
       "cucsDomainNetworkParamFltAggr": cucsDomainNetworkParamFltAggr,
       "cucsDomainNetworkParamName": cucsDomainNetworkParamName,
       "cucsDomainNetworkParamValue": cucsDomainNetworkParamValue,
       "cucsDomainServerFeatureTable": cucsDomainServerFeatureTable,
       "cucsDomainServerFeatureEntry": cucsDomainServerFeatureEntry,
       "cucsDomainServerFeatureInstanceId": cucsDomainServerFeatureInstanceId,
       "cucsDomainServerFeatureDn": cucsDomainServerFeatureDn,
       "cucsDomainServerFeatureRn": cucsDomainServerFeatureRn,
       "cucsDomainServerFeatureFltAggr": cucsDomainServerFeatureFltAggr,
       "cucsDomainServerFeatureFunctionalState": cucsDomainServerFeatureFunctionalState,
       "cucsDomainServerFeatureName": cucsDomainServerFeatureName,
       "cucsDomainServerFeatureType": cucsDomainServerFeatureType,
       "cucsDomainServerParamTable": cucsDomainServerParamTable,
       "cucsDomainServerParamEntry": cucsDomainServerParamEntry,
       "cucsDomainServerParamInstanceId": cucsDomainServerParamInstanceId,
       "cucsDomainServerParamDn": cucsDomainServerParamDn,
       "cucsDomainServerParamRn": cucsDomainServerParamRn,
       "cucsDomainServerParamFltAggr": cucsDomainServerParamFltAggr,
       "cucsDomainServerParamName": cucsDomainServerParamName,
       "cucsDomainServerParamValue": cucsDomainServerParamValue,
       "cucsDomainStorageFeatureTable": cucsDomainStorageFeatureTable,
       "cucsDomainStorageFeatureEntry": cucsDomainStorageFeatureEntry,
       "cucsDomainStorageFeatureInstanceId": cucsDomainStorageFeatureInstanceId,
       "cucsDomainStorageFeatureDn": cucsDomainStorageFeatureDn,
       "cucsDomainStorageFeatureRn": cucsDomainStorageFeatureRn,
       "cucsDomainStorageFeatureFltAggr": cucsDomainStorageFeatureFltAggr,
       "cucsDomainStorageFeatureFunctionalState": cucsDomainStorageFeatureFunctionalState,
       "cucsDomainStorageFeatureName": cucsDomainStorageFeatureName,
       "cucsDomainStorageFeatureType": cucsDomainStorageFeatureType,
       "cucsDomainStorageParamTable": cucsDomainStorageParamTable,
       "cucsDomainStorageParamEntry": cucsDomainStorageParamEntry,
       "cucsDomainStorageParamInstanceId": cucsDomainStorageParamInstanceId,
       "cucsDomainStorageParamDn": cucsDomainStorageParamDn,
       "cucsDomainStorageParamRn": cucsDomainStorageParamRn,
       "cucsDomainStorageParamFltAggr": cucsDomainStorageParamFltAggr,
       "cucsDomainStorageParamName": cucsDomainStorageParamName,
       "cucsDomainStorageParamValue": cucsDomainStorageParamValue,
       "cucsDomainEnvironmentFeatureContTable": cucsDomainEnvironmentFeatureContTable,
       "cucsDomainEnvironmentFeatureContEntry": cucsDomainEnvironmentFeatureContEntry,
       "cucsDomainEnvironmentFeatureContInstanceId": cucsDomainEnvironmentFeatureContInstanceId,
       "cucsDomainEnvironmentFeatureContDn": cucsDomainEnvironmentFeatureContDn,
       "cucsDomainEnvironmentFeatureContRn": cucsDomainEnvironmentFeatureContRn,
       "cucsDomainEnvironmentFeatureContFltAggr": cucsDomainEnvironmentFeatureContFltAggr,
       "cucsDomainNetworkFeatureContTable": cucsDomainNetworkFeatureContTable,
       "cucsDomainNetworkFeatureContEntry": cucsDomainNetworkFeatureContEntry,
       "cucsDomainNetworkFeatureContInstanceId": cucsDomainNetworkFeatureContInstanceId,
       "cucsDomainNetworkFeatureContDn": cucsDomainNetworkFeatureContDn,
       "cucsDomainNetworkFeatureContRn": cucsDomainNetworkFeatureContRn,
       "cucsDomainNetworkFeatureContFltAggr": cucsDomainNetworkFeatureContFltAggr,
       "cucsDomainServerFeatureContTable": cucsDomainServerFeatureContTable,
       "cucsDomainServerFeatureContEntry": cucsDomainServerFeatureContEntry,
       "cucsDomainServerFeatureContInstanceId": cucsDomainServerFeatureContInstanceId,
       "cucsDomainServerFeatureContDn": cucsDomainServerFeatureContDn,
       "cucsDomainServerFeatureContRn": cucsDomainServerFeatureContRn,
       "cucsDomainServerFeatureContFltAggr": cucsDomainServerFeatureContFltAggr,
       "cucsDomainStorageFeatureContTable": cucsDomainStorageFeatureContTable,
       "cucsDomainStorageFeatureContEntry": cucsDomainStorageFeatureContEntry,
       "cucsDomainStorageFeatureContInstanceId": cucsDomainStorageFeatureContInstanceId,
       "cucsDomainStorageFeatureContDn": cucsDomainStorageFeatureContDn,
       "cucsDomainStorageFeatureContRn": cucsDomainStorageFeatureContRn,
       "cucsDomainStorageFeatureContFltAggr": cucsDomainStorageFeatureContFltAggr}
)
