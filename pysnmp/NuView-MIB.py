# SNMP MIB module (NuView-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NuView-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:29 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NuView_ObjectIdentity = ObjectIdentity
NuView = _NuView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427)
)
_ClusterX_ObjectIdentity = ObjectIdentity
ClusterX = _ClusterX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427, 2)
)
_ClxMibStats_ObjectIdentity = ObjectIdentity
clxMibStats = _ClxMibStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427, 2, 1)
)


class _ClxMibStatsMajRev_Type(Integer32):
    """Custom type clxMibStatsMajRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClxMibStatsMajRev_Type.__name__ = "Integer32"
_ClxMibStatsMajRev_Object = MibScalar
clxMibStatsMajRev = _ClxMibStatsMajRev_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 1, 1),
    _ClxMibStatsMajRev_Type()
)
clxMibStatsMajRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxMibStatsMajRev.setStatus("mandatory")


class _ClxMibStatsMinRev_Type(Integer32):
    """Custom type clxMibStatsMinRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClxMibStatsMinRev_Type.__name__ = "Integer32"
_ClxMibStatsMinRev_Object = MibScalar
clxMibStatsMinRev = _ClxMibStatsMinRev_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 1, 2),
    _ClxMibStatsMinRev_Type()
)
clxMibStatsMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxMibStatsMinRev.setStatus("mandatory")
_ClxMibStatsVendorName_Type = DisplayString
_ClxMibStatsVendorName_Object = MibScalar
clxMibStatsVendorName = _ClxMibStatsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 1, 3),
    _ClxMibStatsVendorName_Type()
)
clxMibStatsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxMibStatsVendorName.setStatus("mandatory")
_ClxTrapData_ObjectIdentity = ObjectIdentity
clxTrapData = _ClxTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2)
)
_ClxTrapDataString01_Type = DisplayString
_ClxTrapDataString01_Object = MibScalar
clxTrapDataString01 = _ClxTrapDataString01_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 1),
    _ClxTrapDataString01_Type()
)
clxTrapDataString01.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataString01.setStatus("mandatory")
_ClxTrapDataNodeName_Type = DisplayString
_ClxTrapDataNodeName_Object = MibScalar
clxTrapDataNodeName = _ClxTrapDataNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 2),
    _ClxTrapDataNodeName_Type()
)
clxTrapDataNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNodeName.setStatus("mandatory")
_ClxTrapDataClusterName_Type = DisplayString
_ClxTrapDataClusterName_Object = MibScalar
clxTrapDataClusterName = _ClxTrapDataClusterName_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 3),
    _ClxTrapDataClusterName_Type()
)
clxTrapDataClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataClusterName.setStatus("mandatory")
_ClxTrapDataResourceName_Type = DisplayString
_ClxTrapDataResourceName_Object = MibScalar
clxTrapDataResourceName = _ClxTrapDataResourceName_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 4),
    _ClxTrapDataResourceName_Type()
)
clxTrapDataResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataResourceName.setStatus("mandatory")
_ClxTrapDataResourceType_Type = DisplayString
_ClxTrapDataResourceType_Object = MibScalar
clxTrapDataResourceType = _ClxTrapDataResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 5),
    _ClxTrapDataResourceType_Type()
)
clxTrapDataResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataResourceType.setStatus("mandatory")


class _ClxTrapDataSeverityValue_Type(Integer32):
    """Custom type clxTrapDataSeverityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("info", 0),
          ("warning", 1))
    )


_ClxTrapDataSeverityValue_Type.__name__ = "Integer32"
_ClxTrapDataSeverityValue_Object = MibScalar
clxTrapDataSeverityValue = _ClxTrapDataSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 6),
    _ClxTrapDataSeverityValue_Type()
)
clxTrapDataSeverityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxTrapDataSeverityValue.setStatus("mandatory")
_ClxTrapDataNetwork_Type = DisplayString
_ClxTrapDataNetwork_Object = MibScalar
clxTrapDataNetwork = _ClxTrapDataNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 7),
    _ClxTrapDataNetwork_Type()
)
clxTrapDataNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNetwork.setStatus("mandatory")
_ClxTrapEventDate_Type = DisplayString
_ClxTrapEventDate_Object = MibScalar
clxTrapEventDate = _ClxTrapEventDate_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 8),
    _ClxTrapEventDate_Type()
)
clxTrapEventDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventDate.setStatus("mandatory")
_ClxTrapEventTime_Type = DisplayString
_ClxTrapEventTime_Object = MibScalar
clxTrapEventTime = _ClxTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 9),
    _ClxTrapEventTime_Type()
)
clxTrapEventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventTime.setStatus("mandatory")
_ClxTrapEventSource_Type = DisplayString
_ClxTrapEventSource_Object = MibScalar
clxTrapEventSource = _ClxTrapEventSource_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 10),
    _ClxTrapEventSource_Type()
)
clxTrapEventSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventSource.setStatus("mandatory")
_ClxTrapEventCategory_Type = DisplayString
_ClxTrapEventCategory_Object = MibScalar
clxTrapEventCategory = _ClxTrapEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 11),
    _ClxTrapEventCategory_Type()
)
clxTrapEventCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventCategory.setStatus("mandatory")
_ClxTrapEventID_Type = DisplayString
_ClxTrapEventID_Object = MibScalar
clxTrapEventID = _ClxTrapEventID_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 12),
    _ClxTrapEventID_Type()
)
clxTrapEventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventID.setStatus("mandatory")
_ClxTrapEventUser_Type = DisplayString
_ClxTrapEventUser_Object = MibScalar
clxTrapEventUser = _ClxTrapEventUser_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 13),
    _ClxTrapEventUser_Type()
)
clxTrapEventUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventUser.setStatus("mandatory")
_ClxTrapEventComputer_Type = DisplayString
_ClxTrapEventComputer_Object = MibScalar
clxTrapEventComputer = _ClxTrapEventComputer_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 14),
    _ClxTrapEventComputer_Type()
)
clxTrapEventComputer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventComputer.setStatus("mandatory")
_ClxTrapDataNetworkName_Type = DisplayString
_ClxTrapDataNetworkName_Object = MibScalar
clxTrapDataNetworkName = _ClxTrapDataNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 2427, 2, 2, 15),
    _ClxTrapDataNetworkName_Type()
)
clxTrapDataNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNetworkName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

NuViewTrapStr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 0, 1)
)
NuViewTrapStr.setObjects(
    ("NuView-MIB", "clxTrapDataString01")
)
if mibBuilder.loadTexts:
    NuViewTrapStr.setStatus(
        ""
    )

ClusterXTrapStr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 1)
)
ClusterXTrapStr.setObjects(
    ("NuView-MIB", "clxTrapDataString01")
)
if mibBuilder.loadTexts:
    ClusterXTrapStr.setStatus(
        ""
    )

ClusterXTrapNodeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 2)
)
ClusterXTrapNodeFail.setObjects(
      *(("NuView-MIB", "clxTrapDataClusterName"),
        ("NuView-MIB", "clxTrapDataNodeName"))
)
if mibBuilder.loadTexts:
    ClusterXTrapNodeFail.setStatus(
        ""
    )

ClusterXTrapClusterFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 3)
)
ClusterXTrapClusterFail.setObjects(
    ("NuView-MIB", "clxTrapDataClusterName")
)
if mibBuilder.loadTexts:
    ClusterXTrapClusterFail.setStatus(
        ""
    )

ClusterXTrapResourceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 4)
)
ClusterXTrapResourceFail.setObjects(
      *(("NuView-MIB", "clxTrapDataClusterName"),
        ("NuView-MIB", "clxTrapDataNodeName"),
        ("NuView-MIB", "clxTrapDataResourceName"))
)
if mibBuilder.loadTexts:
    ClusterXTrapResourceFail.setStatus(
        ""
    )

ClusterXTrapNodeJoins = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 5)
)
ClusterXTrapNodeJoins.setObjects(
      *(("NuView-MIB", "clxTrapDataClusterName"),
        ("NuView-MIB", "clxTrapDataNodeName"))
)
if mibBuilder.loadTexts:
    ClusterXTrapNodeJoins.setStatus(
        ""
    )

ClusterXTrapNetworkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 6)
)
ClusterXTrapNetworkFail.setObjects(
      *(("NuView-MIB", "clxTrapDataClusterName"),
        ("NuView-MIB", "clxTrapDataNetworkName"))
)
if mibBuilder.loadTexts:
    ClusterXTrapNetworkFail.setStatus(
        ""
    )

ClusterXTrapNormalClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 7)
)
ClusterXTrapNormalClusterServiceLog.setObjects(
      *(("NuView-MIB", "clxTrapEventDate"),
        ("NuView-MIB", "clxTrapEventTime"),
        ("NuView-MIB", "clxTrapEventSource"),
        ("NuView-MIB", "clxTrapEventCategory"),
        ("NuView-MIB", "clxTrapEventID"),
        ("NuView-MIB", "clxTrapEventUser"),
        ("NuView-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    ClusterXTrapNormalClusterServiceLog.setStatus(
        ""
    )

ClusterXTrapWarningClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 8)
)
ClusterXTrapWarningClusterServiceLog.setObjects(
      *(("NuView-MIB", "clxTrapEventDate"),
        ("NuView-MIB", "clxTrapEventTime"),
        ("NuView-MIB", "clxTrapEventSource"),
        ("NuView-MIB", "clxTrapEventCategory"),
        ("NuView-MIB", "clxTrapEventID"),
        ("NuView-MIB", "clxTrapEventUser"),
        ("NuView-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    ClusterXTrapWarningClusterServiceLog.setStatus(
        ""
    )

ClusterXTrapCriticalClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2427, 2, 0, 9)
)
ClusterXTrapCriticalClusterServiceLog.setObjects(
      *(("NuView-MIB", "clxTrapEventDate"),
        ("NuView-MIB", "clxTrapEventTime"),
        ("NuView-MIB", "clxTrapEventSource"),
        ("NuView-MIB", "clxTrapEventCategory"),
        ("NuView-MIB", "clxTrapEventID"),
        ("NuView-MIB", "clxTrapEventUser"),
        ("NuView-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    ClusterXTrapCriticalClusterServiceLog.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NuView-MIB",
    **{"NuView": NuView,
       "NuViewTrapStr": NuViewTrapStr,
       "ClusterX": ClusterX,
       "ClusterXTrapStr": ClusterXTrapStr,
       "ClusterXTrapNodeFail": ClusterXTrapNodeFail,
       "ClusterXTrapClusterFail": ClusterXTrapClusterFail,
       "ClusterXTrapResourceFail": ClusterXTrapResourceFail,
       "ClusterXTrapNodeJoins": ClusterXTrapNodeJoins,
       "ClusterXTrapNetworkFail": ClusterXTrapNetworkFail,
       "ClusterXTrapNormalClusterServiceLog": ClusterXTrapNormalClusterServiceLog,
       "ClusterXTrapWarningClusterServiceLog": ClusterXTrapWarningClusterServiceLog,
       "ClusterXTrapCriticalClusterServiceLog": ClusterXTrapCriticalClusterServiceLog,
       "clxMibStats": clxMibStats,
       "clxMibStatsMajRev": clxMibStatsMajRev,
       "clxMibStatsMinRev": clxMibStatsMinRev,
       "clxMibStatsVendorName": clxMibStatsVendorName,
       "clxTrapData": clxTrapData,
       "clxTrapDataString01": clxTrapDataString01,
       "clxTrapDataNodeName": clxTrapDataNodeName,
       "clxTrapDataClusterName": clxTrapDataClusterName,
       "clxTrapDataResourceName": clxTrapDataResourceName,
       "clxTrapDataResourceType": clxTrapDataResourceType,
       "clxTrapDataSeverityValue": clxTrapDataSeverityValue,
       "clxTrapDataNetwork": clxTrapDataNetwork,
       "clxTrapEventDate": clxTrapEventDate,
       "clxTrapEventTime": clxTrapEventTime,
       "clxTrapEventSource": clxTrapEventSource,
       "clxTrapEventCategory": clxTrapEventCategory,
       "clxTrapEventID": clxTrapEventID,
       "clxTrapEventUser": clxTrapEventUser,
       "clxTrapEventComputer": clxTrapEventComputer,
       "clxTrapDataNetworkName": clxTrapDataNetworkName}
)
