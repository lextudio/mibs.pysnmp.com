# SNMP MIB module (APACHE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APACHE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:09 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

apacheMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4)
)
apacheMIB.setRevisions(
        ("1998-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApacheServerStatusType(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dead", 1),
          ("dns", 8),
          ("graceful", 9),
          ("keepalive", 6),
          ("log", 7),
          ("read", 4),
          ("ready", 3),
          ("starting", 2),
          ("write", 5))
    )



# MIB Managed Objects in the order of their OIDs

_ApacheMIBObjects_ObjectIdentity = ObjectIdentity
apacheMIBObjects = _ApacheMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4, 1)
)
_ApScoreBoardTable_Object = MibTable
apScoreBoardTable = _ApScoreBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    apScoreBoardTable.setStatus("current")
_ApScoreBoardEntry_Object = MibTableRow
apScoreBoardEntry = _ApScoreBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1)
)
apScoreBoardEntry.setIndexNames(
    (0, "APACHE-MIB", "apScoreBoardIndex"),
)
if mibBuilder.loadTexts:
    apScoreBoardEntry.setStatus("current")
_ApScoreBoardIndex_Type = Unsigned32
_ApScoreBoardIndex_Object = MibTableColumn
apScoreBoardIndex = _ApScoreBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 1),
    _ApScoreBoardIndex_Type()
)
apScoreBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apScoreBoardIndex.setStatus("current")
_ApScoreBoardProcessId_Type = Unsigned32
_ApScoreBoardProcessId_Object = MibTableColumn
apScoreBoardProcessId = _ApScoreBoardProcessId_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 2),
    _ApScoreBoardProcessId_Type()
)
apScoreBoardProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardProcessId.setStatus("current")
_ApScoreBoardStatus_Type = ApacheServerStatusType
_ApScoreBoardStatus_Object = MibTableColumn
apScoreBoardStatus = _ApScoreBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 3),
    _ApScoreBoardStatus_Type()
)
apScoreBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardStatus.setStatus("current")
_ApScoreBoardStartTime_Type = TimeStamp
_ApScoreBoardStartTime_Object = MibTableColumn
apScoreBoardStartTime = _ApScoreBoardStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 4),
    _ApScoreBoardStartTime_Type()
)
apScoreBoardStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardStartTime.setStatus("current")
_ApScoreBoardAccessCount_Type = Unsigned32
_ApScoreBoardAccessCount_Object = MibTableColumn
apScoreBoardAccessCount = _ApScoreBoardAccessCount_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 5),
    _ApScoreBoardAccessCount_Type()
)
apScoreBoardAccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardAccessCount.setStatus("current")
_ApScoreBoardAccessBytes_Type = Unsigned32
_ApScoreBoardAccessBytes_Object = MibTableColumn
apScoreBoardAccessBytes = _ApScoreBoardAccessBytes_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 6),
    _ApScoreBoardAccessBytes_Type()
)
apScoreBoardAccessBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardAccessBytes.setStatus("current")
_ApScoreBoardClient_Type = DisplayString
_ApScoreBoardClient_Object = MibTableColumn
apScoreBoardClient = _ApScoreBoardClient_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 7),
    _ApScoreBoardClient_Type()
)
apScoreBoardClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardClient.setStatus("current")
_ApScoreBoardRequest_Type = DisplayString
_ApScoreBoardRequest_Object = MibTableColumn
apScoreBoardRequest = _ApScoreBoardRequest_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 8),
    _ApScoreBoardRequest_Type()
)
apScoreBoardRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardRequest.setStatus("current")
_ApScoreBoardVirtualHost_Type = Unsigned32
_ApScoreBoardVirtualHost_Object = MibTableColumn
apScoreBoardVirtualHost = _ApScoreBoardVirtualHost_Object(
    (1, 3, 6, 1, 4, 1, 4, 1, 1, 1, 9),
    _ApScoreBoardVirtualHost_Type()
)
apScoreBoardVirtualHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apScoreBoardVirtualHost.setStatus("current")
_ApMIBConformance_ObjectIdentity = ObjectIdentity
apMIBConformance = _ApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4, 2)
)
_ApMIBCompliances_ObjectIdentity = ObjectIdentity
apMIBCompliances = _ApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4, 2, 1)
)
_ApMIBGroups_ObjectIdentity = ObjectIdentity
apMIBGroups = _ApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4, 2, 2)
)
_JointResearchCentre_ObjectIdentity = ObjectIdentity
jointResearchCentre = _JointResearchCentre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1847)
)
_JrcMIBs_ObjectIdentity = ObjectIdentity
jrcMIBs = _JrcMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1847, 1)
)

# Managed Objects groups

apScoreBoardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4, 2, 2, 1)
)
apScoreBoardGroup.setObjects(
      *(("APACHE-MIB", "apScoreBoardProcessId"),
        ("APACHE-MIB", "apScoreBoardStatus"),
        ("APACHE-MIB", "apScoreBoardStartTime"),
        ("APACHE-MIB", "apScoreBoardAccessCount"),
        ("APACHE-MIB", "apScoreBoardAccessBytes"),
        ("APACHE-MIB", "apScoreBoardClient"),
        ("APACHE-MIB", "apScoreBoardRequest"),
        ("APACHE-MIB", "apScoreBoardVirtualHost"))
)
if mibBuilder.loadTexts:
    apScoreBoardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APACHE-MIB",
    **{"ApacheServerStatusType": ApacheServerStatusType,
       "apacheMIB": apacheMIB,
       "apacheMIBObjects": apacheMIBObjects,
       "apScoreBoardTable": apScoreBoardTable,
       "apScoreBoardEntry": apScoreBoardEntry,
       "apScoreBoardIndex": apScoreBoardIndex,
       "apScoreBoardProcessId": apScoreBoardProcessId,
       "apScoreBoardStatus": apScoreBoardStatus,
       "apScoreBoardStartTime": apScoreBoardStartTime,
       "apScoreBoardAccessCount": apScoreBoardAccessCount,
       "apScoreBoardAccessBytes": apScoreBoardAccessBytes,
       "apScoreBoardClient": apScoreBoardClient,
       "apScoreBoardRequest": apScoreBoardRequest,
       "apScoreBoardVirtualHost": apScoreBoardVirtualHost,
       "apMIBConformance": apMIBConformance,
       "apMIBCompliances": apMIBCompliances,
       "apMIBGroups": apMIBGroups,
       "apScoreBoardGroup": apScoreBoardGroup,
       "jointResearchCentre": jointResearchCentre,
       "jrcMIBs": jrcMIBs}
)
