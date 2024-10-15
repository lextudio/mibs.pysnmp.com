# SNMP MIB module (SVRNTCLU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SVRNTCLU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:45 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ObjectType(Integer32):
    """Custom type ObjectType based on Integer32"""
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
        *(("application", 5),
          ("disk", 4),
          ("fileShare", 7),
          ("ipAddress", 6),
          ("objectOther", 2),
          ("objectUnknown", 1),
          ("share", 3))
    )





class PolicyType(Integer32):
    """Custom type PolicyType based on Integer32"""
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
        *(("inOrder", 3),
          ("leastLoad", 5),
          ("policyOther", 2),
          ("policyUnknown", 1),
          ("random", 4),
          ("roundRobin", 6))
    )





class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class DateAndTime(DisplayString):
    """Custom type DateAndTime based on DisplayString"""




class FailoverReason(Integer32):
    """Custom type FailoverReason based on Integer32"""
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
        *(("failback", 5),
          ("failure", 4),
          ("reasonOther", 2),
          ("reasonUnknown", 1),
          ("reconfiguration", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_SvrSystem_ObjectIdentity = ObjectIdentity
svrSystem = _SvrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22)
)
_SvrCluster_ObjectIdentity = ObjectIdentity
svrCluster = _SvrCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4)
)
_SvrNTClu_ObjectIdentity = ObjectIdentity
svrNTClu = _SvrNTClu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2)
)
_SvrNTCluObjects_ObjectIdentity = ObjectIdentity
svrNTCluObjects = _SvrNTCluObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1)
)
_SvrNTCluMibInfo_ObjectIdentity = ObjectIdentity
svrNTCluMibInfo = _SvrNTCluMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1)
)
_NtcExMgtMibMajorRev_Type = Integer32
_NtcExMgtMibMajorRev_Object = MibScalar
ntcExMgtMibMajorRev = _NtcExMgtMibMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1, 1),
    _NtcExMgtMibMajorRev_Type()
)
ntcExMgtMibMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExMgtMibMajorRev.setStatus("mandatory")
_NtcExMgtMibMinorRev_Type = Integer32
_NtcExMgtMibMinorRev_Object = MibScalar
ntcExMgtMibMinorRev = _NtcExMgtMibMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1, 2),
    _NtcExMgtMibMinorRev_Type()
)
ntcExMgtMibMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExMgtMibMinorRev.setStatus("mandatory")
_SvrNTCluClusterInfo_ObjectIdentity = ObjectIdentity
svrNTCluClusterInfo = _SvrNTCluClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2)
)
_NtcExAlias_Type = DisplayString
_NtcExAlias_Object = MibScalar
ntcExAlias = _NtcExAlias_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 1),
    _NtcExAlias_Type()
)
ntcExAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExAlias.setStatus("mandatory")
_NtcExGroupTable_Object = MibTable
ntcExGroupTable = _NtcExGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ntcExGroupTable.setStatus("mandatory")
_NtcExGroupEntry_Object = MibTableRow
ntcExGroupEntry = _NtcExGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1)
)
ntcExGroupEntry.setIndexNames(
    (0, "SVRNTCLU-MIB", "ntcExGroupIndex"),
)
if mibBuilder.loadTexts:
    ntcExGroupEntry.setStatus("mandatory")
_NtcExGroupIndex_Type = Integer32
_NtcExGroupIndex_Object = MibTableColumn
ntcExGroupIndex = _NtcExGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 1),
    _NtcExGroupIndex_Type()
)
ntcExGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupIndex.setStatus("mandatory")
_NtcExGroupName_Type = DisplayString
_NtcExGroupName_Object = MibTableColumn
ntcExGroupName = _NtcExGroupName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 2),
    _NtcExGroupName_Type()
)
ntcExGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupName.setStatus("mandatory")
_NtcExGroupComment_Type = DisplayString
_NtcExGroupComment_Object = MibTableColumn
ntcExGroupComment = _NtcExGroupComment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 3),
    _NtcExGroupComment_Type()
)
ntcExGroupComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupComment.setStatus("mandatory")
_NtcExGroupOnLine_Type = Integer32
_NtcExGroupOnLine_Object = MibTableColumn
ntcExGroupOnLine = _NtcExGroupOnLine_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 4),
    _NtcExGroupOnLine_Type()
)
ntcExGroupOnLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupOnLine.setStatus("mandatory")
_NtcExGroupFailedOver_Type = Boolean
_NtcExGroupFailedOver_Object = MibTableColumn
ntcExGroupFailedOver = _NtcExGroupFailedOver_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 5),
    _NtcExGroupFailedOver_Type()
)
ntcExGroupFailedOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupFailedOver.setStatus("mandatory")
_NtcExGroupPolicy_Type = PolicyType
_NtcExGroupPolicy_Object = MibTableColumn
ntcExGroupPolicy = _NtcExGroupPolicy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 6),
    _NtcExGroupPolicy_Type()
)
ntcExGroupPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupPolicy.setStatus("mandatory")
_NtcExGroupReevaluate_Type = Boolean
_NtcExGroupReevaluate_Object = MibTableColumn
ntcExGroupReevaluate = _NtcExGroupReevaluate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 7),
    _NtcExGroupReevaluate_Type()
)
ntcExGroupReevaluate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupReevaluate.setStatus("mandatory")
_NtcExGroupMembers_Type = DisplayString
_NtcExGroupMembers_Object = MibTableColumn
ntcExGroupMembers = _NtcExGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 8),
    _NtcExGroupMembers_Type()
)
ntcExGroupMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupMembers.setStatus("mandatory")
_NtcExGroupObjects_Type = DisplayString
_NtcExGroupObjects_Object = MibTableColumn
ntcExGroupObjects = _NtcExGroupObjects_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 9),
    _NtcExGroupObjects_Type()
)
ntcExGroupObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExGroupObjects.setStatus("mandatory")
_NtcExObjectTable_Object = MibTable
ntcExObjectTable = _NtcExObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ntcExObjectTable.setStatus("mandatory")
_NtcExObjectEntry_Object = MibTableRow
ntcExObjectEntry = _NtcExObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1)
)
ntcExObjectEntry.setIndexNames(
    (0, "SVRNTCLU-MIB", "ntcExObjectIndex"),
)
if mibBuilder.loadTexts:
    ntcExObjectEntry.setStatus("mandatory")
_NtcExObjectIndex_Type = Integer32
_NtcExObjectIndex_Object = MibTableColumn
ntcExObjectIndex = _NtcExObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 1),
    _NtcExObjectIndex_Type()
)
ntcExObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectIndex.setStatus("mandatory")
_NtcExObjectName_Type = DisplayString
_NtcExObjectName_Object = MibTableColumn
ntcExObjectName = _NtcExObjectName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 2),
    _NtcExObjectName_Type()
)
ntcExObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectName.setStatus("mandatory")
_NtcExObjectComment_Type = DisplayString
_NtcExObjectComment_Object = MibTableColumn
ntcExObjectComment = _NtcExObjectComment_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 3),
    _NtcExObjectComment_Type()
)
ntcExObjectComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectComment.setStatus("mandatory")
_NtcExObjectType_Type = ObjectType
_NtcExObjectType_Object = MibTableColumn
ntcExObjectType = _NtcExObjectType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 4),
    _NtcExObjectType_Type()
)
ntcExObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectType.setStatus("mandatory")
_NtcExObjectDrives_Type = DisplayString
_NtcExObjectDrives_Object = MibTableColumn
ntcExObjectDrives = _NtcExObjectDrives_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 5),
    _NtcExObjectDrives_Type()
)
ntcExObjectDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectDrives.setStatus("mandatory")
_NtcExObjectIpAddress_Type = IpAddress
_NtcExObjectIpAddress_Object = MibTableColumn
ntcExObjectIpAddress = _NtcExObjectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 6),
    _NtcExObjectIpAddress_Type()
)
ntcExObjectIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcExObjectIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SVRNTCLU-MIB",
    **{"ObjectType": ObjectType,
       "PolicyType": PolicyType,
       "Boolean": Boolean,
       "DateAndTime": DateAndTime,
       "FailoverReason": FailoverReason,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "svrSystem": svrSystem,
       "svrCluster": svrCluster,
       "svrNTClu": svrNTClu,
       "svrNTCluObjects": svrNTCluObjects,
       "svrNTCluMibInfo": svrNTCluMibInfo,
       "ntcExMgtMibMajorRev": ntcExMgtMibMajorRev,
       "ntcExMgtMibMinorRev": ntcExMgtMibMinorRev,
       "svrNTCluClusterInfo": svrNTCluClusterInfo,
       "ntcExAlias": ntcExAlias,
       "ntcExGroupTable": ntcExGroupTable,
       "ntcExGroupEntry": ntcExGroupEntry,
       "ntcExGroupIndex": ntcExGroupIndex,
       "ntcExGroupName": ntcExGroupName,
       "ntcExGroupComment": ntcExGroupComment,
       "ntcExGroupOnLine": ntcExGroupOnLine,
       "ntcExGroupFailedOver": ntcExGroupFailedOver,
       "ntcExGroupPolicy": ntcExGroupPolicy,
       "ntcExGroupReevaluate": ntcExGroupReevaluate,
       "ntcExGroupMembers": ntcExGroupMembers,
       "ntcExGroupObjects": ntcExGroupObjects,
       "ntcExObjectTable": ntcExObjectTable,
       "ntcExObjectEntry": ntcExObjectEntry,
       "ntcExObjectIndex": ntcExObjectIndex,
       "ntcExObjectName": ntcExObjectName,
       "ntcExObjectComment": ntcExObjectComment,
       "ntcExObjectType": ntcExObjectType,
       "ntcExObjectDrives": ntcExObjectDrives,
       "ntcExObjectIpAddress": ntcExObjectIpAddress}
)
