# SNMP MIB module (CISCO-VOICE-DNIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-DNIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:23 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVoiceDnisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnisMapname(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CvE164String(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_CvDnisMIBObjects_ObjectIdentity = ObjectIdentity
cvDnisMIBObjects = _CvDnisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1)
)
_CvDnisMap_ObjectIdentity = ObjectIdentity
cvDnisMap = _CvDnisMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1)
)
_CvDnisMappingTable_Object = MibTable
cvDnisMappingTable = _CvDnisMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvDnisMappingTable.setStatus("current")
_CvDnisMappingEntry_Object = MibTableRow
cvDnisMappingEntry = _CvDnisMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1)
)
cvDnisMappingEntry.setIndexNames(
    (1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"),
)
if mibBuilder.loadTexts:
    cvDnisMappingEntry.setStatus("current")


class _CvDnisMappingName_Type(DnisMapname):
    """Custom type cvDnisMappingName based on DnisMapname"""
    subtypeSpec = DnisMapname.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CvDnisMappingName_Type.__name__ = "DnisMapname"
_CvDnisMappingName_Object = MibTableColumn
cvDnisMappingName = _CvDnisMappingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1),
    _CvDnisMappingName_Type()
)
cvDnisMappingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvDnisMappingName.setStatus("current")
_CvDnisMappingUrl_Type = DisplayString
_CvDnisMappingUrl_Object = MibTableColumn
cvDnisMappingUrl = _CvDnisMappingUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2),
    _CvDnisMappingUrl_Type()
)
cvDnisMappingUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvDnisMappingUrl.setStatus("current")


class _CvDnisMappingRefresh_Type(Integer32):
    """Custom type cvDnisMappingRefresh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("refresh", 2))
    )


_CvDnisMappingRefresh_Type.__name__ = "Integer32"
_CvDnisMappingRefresh_Object = MibTableColumn
cvDnisMappingRefresh = _CvDnisMappingRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3),
    _CvDnisMappingRefresh_Type()
)
cvDnisMappingRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvDnisMappingRefresh.setStatus("current")
_CvDnisMappingUrlAccessError_Type = DisplayString
_CvDnisMappingUrlAccessError_Object = MibTableColumn
cvDnisMappingUrlAccessError = _CvDnisMappingUrlAccessError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4),
    _CvDnisMappingUrlAccessError_Type()
)
cvDnisMappingUrlAccessError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvDnisMappingUrlAccessError.setStatus("current")
_CvDnisMappingStatus_Type = RowStatus
_CvDnisMappingStatus_Object = MibTableColumn
cvDnisMappingStatus = _CvDnisMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5),
    _CvDnisMappingStatus_Type()
)
cvDnisMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvDnisMappingStatus.setStatus("current")
_CvDnisNodeTable_Object = MibTable
cvDnisNodeTable = _CvDnisNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvDnisNodeTable.setStatus("current")
_CvDnisNodeEntry_Object = MibTableRow
cvDnisNodeEntry = _CvDnisNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1)
)
cvDnisNodeEntry.setIndexNames(
    (0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"),
    (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"),
)
if mibBuilder.loadTexts:
    cvDnisNodeEntry.setStatus("current")
_CvDnisNumber_Type = CvE164String
_CvDnisNumber_Object = MibTableColumn
cvDnisNumber = _CvDnisNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1),
    _CvDnisNumber_Type()
)
cvDnisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvDnisNumber.setStatus("current")
_CvDnisNodeUrl_Type = DisplayString
_CvDnisNodeUrl_Object = MibTableColumn
cvDnisNodeUrl = _CvDnisNodeUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2),
    _CvDnisNodeUrl_Type()
)
cvDnisNodeUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvDnisNodeUrl.setStatus("current")
_CvDnisNodeModifiable_Type = TruthValue
_CvDnisNodeModifiable_Object = MibTableColumn
cvDnisNodeModifiable = _CvDnisNodeModifiable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3),
    _CvDnisNodeModifiable_Type()
)
cvDnisNodeModifiable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvDnisNodeModifiable.setStatus("current")
_CvDnisNodeStatus_Type = RowStatus
_CvDnisNodeStatus_Object = MibTableColumn
cvDnisNodeStatus = _CvDnisNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4),
    _CvDnisNodeStatus_Type()
)
cvDnisNodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvDnisNodeStatus.setStatus("current")
_CvDnisMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cvDnisMIBNotificationPrefix = _CvDnisMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 2)
)
_CvDnisMIBNotifications_ObjectIdentity = ObjectIdentity
cvDnisMIBNotifications = _CvDnisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0)
)
_CvDnisMIBConformance_ObjectIdentity = ObjectIdentity
cvDnisMIBConformance = _CvDnisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3)
)
_CvDnisMIBCompliances_ObjectIdentity = ObjectIdentity
cvDnisMIBCompliances = _CvDnisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1)
)
_CvDnisMIBGroups_ObjectIdentity = ObjectIdentity
cvDnisMIBGroups = _CvDnisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2)
)

# Managed Objects groups

cvDnisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)
)
cvDnisGroup.setObjects(
      *(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
)
if mibBuilder.loadTexts:
    cvDnisGroup.setStatus("current")


# Notification objects

cvDnisMappingUrlInaccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)
)
cvDnisMappingUrlInaccessible.setObjects(
      *(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"),
        ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
)
if mibBuilder.loadTexts:
    cvDnisMappingUrlInaccessible.setStatus(
        "current"
    )


# Notifications groups

cvDnisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)
)
cvDnisNotificationGroup.setObjects(
    ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible")
)
if mibBuilder.loadTexts:
    cvDnisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvDnisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvDnisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-DNIS-MIB",
    **{"DnisMapname": DnisMapname,
       "CvE164String": CvE164String,
       "ciscoVoiceDnisMIB": ciscoVoiceDnisMIB,
       "cvDnisMIBObjects": cvDnisMIBObjects,
       "cvDnisMap": cvDnisMap,
       "cvDnisMappingTable": cvDnisMappingTable,
       "cvDnisMappingEntry": cvDnisMappingEntry,
       "cvDnisMappingName": cvDnisMappingName,
       "cvDnisMappingUrl": cvDnisMappingUrl,
       "cvDnisMappingRefresh": cvDnisMappingRefresh,
       "cvDnisMappingUrlAccessError": cvDnisMappingUrlAccessError,
       "cvDnisMappingStatus": cvDnisMappingStatus,
       "cvDnisNodeTable": cvDnisNodeTable,
       "cvDnisNodeEntry": cvDnisNodeEntry,
       "cvDnisNumber": cvDnisNumber,
       "cvDnisNodeUrl": cvDnisNodeUrl,
       "cvDnisNodeModifiable": cvDnisNodeModifiable,
       "cvDnisNodeStatus": cvDnisNodeStatus,
       "cvDnisMIBNotificationPrefix": cvDnisMIBNotificationPrefix,
       "cvDnisMIBNotifications": cvDnisMIBNotifications,
       "cvDnisMappingUrlInaccessible": cvDnisMappingUrlInaccessible,
       "cvDnisMIBConformance": cvDnisMIBConformance,
       "cvDnisMIBCompliances": cvDnisMIBCompliances,
       "cvDnisMIBCompliance": cvDnisMIBCompliance,
       "cvDnisMIBGroups": cvDnisMIBGroups,
       "cvDnisGroup": cvDnisGroup,
       "cvDnisNotificationGroup": cvDnisNotificationGroup}
)
