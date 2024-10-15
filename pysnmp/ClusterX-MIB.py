# SNMP MIB module (ClusterX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ClusterX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:47 2024
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

_Veritassoftware_ObjectIdentity = ObjectIdentity
veritassoftware = _Veritassoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302)
)
_Veritasproducts_ObjectIdentity = ObjectIdentity
veritasproducts = _Veritasproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3)
)
_ClusterX_ObjectIdentity = ObjectIdentity
clusterX = _ClusterX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7)
)
_ClxMibStats_ObjectIdentity = ObjectIdentity
clxMibStats = _ClxMibStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 1)
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
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 2),
    _ClxMibStatsMinRev_Type()
)
clxMibStatsMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxMibStatsMinRev.setStatus("mandatory")
_ClxMibStatsVendorName_Type = DisplayString
_ClxMibStatsVendorName_Object = MibScalar
clxMibStatsVendorName = _ClxMibStatsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 1, 3),
    _ClxMibStatsVendorName_Type()
)
clxMibStatsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxMibStatsVendorName.setStatus("mandatory")
_ClxTrapData_ObjectIdentity = ObjectIdentity
clxTrapData = _ClxTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2)
)
_ClxTrapDataString01_Type = DisplayString
_ClxTrapDataString01_Object = MibScalar
clxTrapDataString01 = _ClxTrapDataString01_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 1),
    _ClxTrapDataString01_Type()
)
clxTrapDataString01.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataString01.setStatus("mandatory")
_ClxTrapDataNodeName_Type = DisplayString
_ClxTrapDataNodeName_Object = MibScalar
clxTrapDataNodeName = _ClxTrapDataNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 2),
    _ClxTrapDataNodeName_Type()
)
clxTrapDataNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNodeName.setStatus("mandatory")
_ClxTrapDataClusterName_Type = DisplayString
_ClxTrapDataClusterName_Object = MibScalar
clxTrapDataClusterName = _ClxTrapDataClusterName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 3),
    _ClxTrapDataClusterName_Type()
)
clxTrapDataClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataClusterName.setStatus("mandatory")
_ClxTrapDataResourceName_Type = DisplayString
_ClxTrapDataResourceName_Object = MibScalar
clxTrapDataResourceName = _ClxTrapDataResourceName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 4),
    _ClxTrapDataResourceName_Type()
)
clxTrapDataResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataResourceName.setStatus("mandatory")
_ClxTrapDataResourceType_Type = DisplayString
_ClxTrapDataResourceType_Object = MibScalar
clxTrapDataResourceType = _ClxTrapDataResourceType_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 6),
    _ClxTrapDataSeverityValue_Type()
)
clxTrapDataSeverityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clxTrapDataSeverityValue.setStatus("mandatory")
_ClxTrapDataNetwork_Type = DisplayString
_ClxTrapDataNetwork_Object = MibScalar
clxTrapDataNetwork = _ClxTrapDataNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 7),
    _ClxTrapDataNetwork_Type()
)
clxTrapDataNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNetwork.setStatus("mandatory")
_ClxTrapEventDate_Type = DisplayString
_ClxTrapEventDate_Object = MibScalar
clxTrapEventDate = _ClxTrapEventDate_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 8),
    _ClxTrapEventDate_Type()
)
clxTrapEventDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventDate.setStatus("mandatory")
_ClxTrapEventTime_Type = DisplayString
_ClxTrapEventTime_Object = MibScalar
clxTrapEventTime = _ClxTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 9),
    _ClxTrapEventTime_Type()
)
clxTrapEventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventTime.setStatus("mandatory")
_ClxTrapEventSource_Type = DisplayString
_ClxTrapEventSource_Object = MibScalar
clxTrapEventSource = _ClxTrapEventSource_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 10),
    _ClxTrapEventSource_Type()
)
clxTrapEventSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventSource.setStatus("mandatory")
_ClxTrapEventCategory_Type = DisplayString
_ClxTrapEventCategory_Object = MibScalar
clxTrapEventCategory = _ClxTrapEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 11),
    _ClxTrapEventCategory_Type()
)
clxTrapEventCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventCategory.setStatus("mandatory")
_ClxTrapEventID_Type = DisplayString
_ClxTrapEventID_Object = MibScalar
clxTrapEventID = _ClxTrapEventID_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 12),
    _ClxTrapEventID_Type()
)
clxTrapEventID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventID.setStatus("mandatory")
_ClxTrapEventUser_Type = DisplayString
_ClxTrapEventUser_Object = MibScalar
clxTrapEventUser = _ClxTrapEventUser_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 13),
    _ClxTrapEventUser_Type()
)
clxTrapEventUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventUser.setStatus("mandatory")
_ClxTrapEventComputer_Type = DisplayString
_ClxTrapEventComputer_Object = MibScalar
clxTrapEventComputer = _ClxTrapEventComputer_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 14),
    _ClxTrapEventComputer_Type()
)
clxTrapEventComputer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapEventComputer.setStatus("mandatory")
_ClxTrapDataNetworkName_Type = DisplayString
_ClxTrapDataNetworkName_Object = MibScalar
clxTrapDataNetworkName = _ClxTrapDataNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 15),
    _ClxTrapDataNetworkName_Type()
)
clxTrapDataNetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataNetworkName.setStatus("mandatory")
_ClxTrapDataWLBSNodeName_Type = DisplayString
_ClxTrapDataWLBSNodeName_Object = MibScalar
clxTrapDataWLBSNodeName = _ClxTrapDataWLBSNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 16),
    _ClxTrapDataWLBSNodeName_Type()
)
clxTrapDataWLBSNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataWLBSNodeName.setStatus("mandatory")
_ClxTrapDataWLBSClusterName_Type = DisplayString
_ClxTrapDataWLBSClusterName_Object = MibScalar
clxTrapDataWLBSClusterName = _ClxTrapDataWLBSClusterName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 17),
    _ClxTrapDataWLBSClusterName_Type()
)
clxTrapDataWLBSClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataWLBSClusterName.setStatus("mandatory")
_ClxTrapDataWLBSHostID_Type = DisplayString
_ClxTrapDataWLBSHostID_Object = MibScalar
clxTrapDataWLBSHostID = _ClxTrapDataWLBSHostID_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 18),
    _ClxTrapDataWLBSHostID_Type()
)
clxTrapDataWLBSHostID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataWLBSHostID.setStatus("mandatory")
_ClxTrapDataPortNumber_Type = DisplayString
_ClxTrapDataPortNumber_Object = MibScalar
clxTrapDataPortNumber = _ClxTrapDataPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 19),
    _ClxTrapDataPortNumber_Type()
)
clxTrapDataPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataPortNumber.setStatus("mandatory")
_ClxTrapDataApplicationName_Type = DisplayString
_ClxTrapDataApplicationName_Object = MibScalar
clxTrapDataApplicationName = _ClxTrapDataApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 20),
    _ClxTrapDataApplicationName_Type()
)
clxTrapDataApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataApplicationName.setStatus("mandatory")
_ClxTrapDataApplicationFailureReason_Type = DisplayString
_ClxTrapDataApplicationFailureReason_Object = MibScalar
clxTrapDataApplicationFailureReason = _ClxTrapDataApplicationFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 21),
    _ClxTrapDataApplicationFailureReason_Type()
)
clxTrapDataApplicationFailureReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataApplicationFailureReason.setStatus("mandatory")
_ClxTrapDataApplicationFailureAction_Type = DisplayString
_ClxTrapDataApplicationFailureAction_Object = MibScalar
clxTrapDataApplicationFailureAction = _ClxTrapDataApplicationFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 22),
    _ClxTrapDataApplicationFailureAction_Type()
)
clxTrapDataApplicationFailureAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataApplicationFailureAction.setStatus("mandatory")
_ClxTrapDataApplicationOnLineAction_Type = DisplayString
_ClxTrapDataApplicationOnLineAction_Object = MibScalar
clxTrapDataApplicationOnLineAction = _ClxTrapDataApplicationOnLineAction_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 2, 23),
    _ClxTrapDataApplicationOnLineAction_Type()
)
clxTrapDataApplicationOnLineAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clxTrapDataApplicationOnLineAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects

clusterXTrapStr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 1)
)
clusterXTrapStr.setObjects(
    ("ClusterX-MIB", "clxTrapDataString01")
)
if mibBuilder.loadTexts:
    clusterXTrapStr.setStatus(
        ""
    )

clusterXTrapNodeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 2)
)
clusterXTrapNodeFail.setObjects(
      *(("ClusterX-MIB", "clxTrapDataClusterName"),
        ("ClusterX-MIB", "clxTrapDataNodeName"))
)
if mibBuilder.loadTexts:
    clusterXTrapNodeFail.setStatus(
        ""
    )

clusterXTrapClusterFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 3)
)
clusterXTrapClusterFail.setObjects(
    ("ClusterX-MIB", "clxTrapDataClusterName")
)
if mibBuilder.loadTexts:
    clusterXTrapClusterFail.setStatus(
        ""
    )

clusterXTrapResourceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 4)
)
clusterXTrapResourceFail.setObjects(
      *(("ClusterX-MIB", "clxTrapDataClusterName"),
        ("ClusterX-MIB", "clxTrapDataNodeName"),
        ("ClusterX-MIB", "clxTrapDataResourceName"))
)
if mibBuilder.loadTexts:
    clusterXTrapResourceFail.setStatus(
        ""
    )

clusterXTrapNodeJoins = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 5)
)
clusterXTrapNodeJoins.setObjects(
      *(("ClusterX-MIB", "clxTrapDataClusterName"),
        ("ClusterX-MIB", "clxTrapDataNodeName"))
)
if mibBuilder.loadTexts:
    clusterXTrapNodeJoins.setStatus(
        ""
    )

clusterXTrapNetworkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 6)
)
clusterXTrapNetworkFail.setObjects(
      *(("ClusterX-MIB", "clxTrapDataString01"),
        ("ClusterX-MIB", "clxTrapDataNetworkName"))
)
if mibBuilder.loadTexts:
    clusterXTrapNetworkFail.setStatus(
        ""
    )

clusterXTrapNormalClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 7)
)
clusterXTrapNormalClusterServiceLog.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXTrapNormalClusterServiceLog.setStatus(
        ""
    )

clusterXTrapWarningClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 8)
)
clusterXTrapWarningClusterServiceLog.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXTrapWarningClusterServiceLog.setStatus(
        ""
    )

clusterXTrapCriticalClusterServiceLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 9)
)
clusterXTrapCriticalClusterServiceLog.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXTrapCriticalClusterServiceLog.setStatus(
        ""
    )

clusterXWLBSTrapApplicationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 10)
)
clusterXWLBSTrapApplicationFail.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"),
        ("ClusterX-MIB", "clxTrapDataApplicationName"),
        ("ClusterX-MIB", "clxTrapDataApplicationFailureReason"),
        ("ClusterX-MIB", "clxTrapDataApplicationFailureAction"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapApplicationFail.setStatus(
        ""
    )

clusterXWLBSTrapEventLogNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 11)
)
clusterXWLBSTrapEventLogNormal.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapEventLogNormal.setStatus(
        ""
    )

clusterXWLBSTrapEventLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 12)
)
clusterXWLBSTrapEventLogWarning.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapEventLogWarning.setStatus(
        ""
    )

clusterXWLBSTrapEventLogCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 13)
)
clusterXWLBSTrapEventLogCritical.setObjects(
      *(("ClusterX-MIB", "clxTrapEventDate"),
        ("ClusterX-MIB", "clxTrapEventTime"),
        ("ClusterX-MIB", "clxTrapEventSource"),
        ("ClusterX-MIB", "clxTrapEventCategory"),
        ("ClusterX-MIB", "clxTrapEventID"),
        ("ClusterX-MIB", "clxTrapEventUser"),
        ("ClusterX-MIB", "clxTrapEventComputer"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapEventLogCritical.setStatus(
        ""
    )

clusterXWLBSTrapSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 14)
)
clusterXWLBSTrapSuspended.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapSuspended.setStatus(
        ""
    )

clusterXWLBSTrapResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 15)
)
clusterXWLBSTrapResumed.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapResumed.setStatus(
        ""
    )

clusterXWLBSTrapStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 16)
)
clusterXWLBSTrapStarted.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapStarted.setStatus(
        ""
    )

clusterXWLBSTrapStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 17)
)
clusterXWLBSTrapStopped.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapStopped.setStatus(
        ""
    )

clusterXWLBSTrapDrainStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 18)
)
clusterXWLBSTrapDrainStopped.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapDrainStopped.setStatus(
        ""
    )

clusterXWLBSTrapConverged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 19)
)
clusterXWLBSTrapConverged.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapConverged.setStatus(
        ""
    )

clusterXWLBSTrapEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 20)
)
clusterXWLBSTrapEnabled.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"),
        ("ClusterX-MIB", "clxTrapDataPortNumber"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapEnabled.setStatus(
        ""
    )

clusterXWLBSTrapDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 21)
)
clusterXWLBSTrapDisabled.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"),
        ("ClusterX-MIB", "clxTrapDataPortNumber"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapDisabled.setStatus(
        ""
    )

clusterXWLBSTrapDrained = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 22)
)
clusterXWLBSTrapDrained.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"),
        ("ClusterX-MIB", "clxTrapDataPortNumber"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapDrained.setStatus(
        ""
    )

clusterXWLBSTrapApplicationOnLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 23)
)
clusterXWLBSTrapApplicationOnLine.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"),
        ("ClusterX-MIB", "clxTrapDataApplicationName"),
        ("ClusterX-MIB", "clxTrapDataApplicationOnLineAction"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapApplicationOnLine.setStatus(
        ""
    )

clusterXWLBSTrapReloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 7, 0, 24)
)
clusterXWLBSTrapReloaded.setObjects(
      *(("ClusterX-MIB", "clxTrapDataWLBSClusterName"),
        ("ClusterX-MIB", "clxTrapDataWLBSNodeName"))
)
if mibBuilder.loadTexts:
    clusterXWLBSTrapReloaded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ClusterX-MIB",
    **{"veritassoftware": veritassoftware,
       "veritasproducts": veritasproducts,
       "clusterX": clusterX,
       "clusterXTrapStr": clusterXTrapStr,
       "clusterXTrapNodeFail": clusterXTrapNodeFail,
       "clusterXTrapClusterFail": clusterXTrapClusterFail,
       "clusterXTrapResourceFail": clusterXTrapResourceFail,
       "clusterXTrapNodeJoins": clusterXTrapNodeJoins,
       "clusterXTrapNetworkFail": clusterXTrapNetworkFail,
       "clusterXTrapNormalClusterServiceLog": clusterXTrapNormalClusterServiceLog,
       "clusterXTrapWarningClusterServiceLog": clusterXTrapWarningClusterServiceLog,
       "clusterXTrapCriticalClusterServiceLog": clusterXTrapCriticalClusterServiceLog,
       "clusterXWLBSTrapApplicationFail": clusterXWLBSTrapApplicationFail,
       "clusterXWLBSTrapEventLogNormal": clusterXWLBSTrapEventLogNormal,
       "clusterXWLBSTrapEventLogWarning": clusterXWLBSTrapEventLogWarning,
       "clusterXWLBSTrapEventLogCritical": clusterXWLBSTrapEventLogCritical,
       "clusterXWLBSTrapSuspended": clusterXWLBSTrapSuspended,
       "clusterXWLBSTrapResumed": clusterXWLBSTrapResumed,
       "clusterXWLBSTrapStarted": clusterXWLBSTrapStarted,
       "clusterXWLBSTrapStopped": clusterXWLBSTrapStopped,
       "clusterXWLBSTrapDrainStopped": clusterXWLBSTrapDrainStopped,
       "clusterXWLBSTrapConverged": clusterXWLBSTrapConverged,
       "clusterXWLBSTrapEnabled": clusterXWLBSTrapEnabled,
       "clusterXWLBSTrapDisabled": clusterXWLBSTrapDisabled,
       "clusterXWLBSTrapDrained": clusterXWLBSTrapDrained,
       "clusterXWLBSTrapApplicationOnLine": clusterXWLBSTrapApplicationOnLine,
       "clusterXWLBSTrapReloaded": clusterXWLBSTrapReloaded,
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
       "clxTrapDataNetworkName": clxTrapDataNetworkName,
       "clxTrapDataWLBSNodeName": clxTrapDataWLBSNodeName,
       "clxTrapDataWLBSClusterName": clxTrapDataWLBSClusterName,
       "clxTrapDataWLBSHostID": clxTrapDataWLBSHostID,
       "clxTrapDataPortNumber": clxTrapDataPortNumber,
       "clxTrapDataApplicationName": clxTrapDataApplicationName,
       "clxTrapDataApplicationFailureReason": clxTrapDataApplicationFailureReason,
       "clxTrapDataApplicationFailureAction": clxTrapDataApplicationFailureAction,
       "clxTrapDataApplicationOnLineAction": clxTrapDataApplicationOnLineAction}
)
