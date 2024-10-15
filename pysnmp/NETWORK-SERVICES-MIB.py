# SNMP MIB module (NETWORK-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:13 2024
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

application = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 27)
)
application.setRevisions(
        ("2000-03-03 00:00",
         "1999-05-12 00:00",
         "1997-08-17 00:00",
         "1993-11-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DistinguishedName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class URLString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ApplTable_Object = MibTable
applTable = _ApplTable_Object(
    (1, 3, 6, 1, 2, 1, 27, 1)
)
if mibBuilder.loadTexts:
    applTable.setStatus("current")
_ApplEntry_Object = MibTableRow
applEntry = _ApplEntry_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1)
)
applEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    applEntry.setStatus("current")


class _ApplIndex_Type(Integer32):
    """Custom type applIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApplIndex_Type.__name__ = "Integer32"
_ApplIndex_Object = MibTableColumn
applIndex = _ApplIndex_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 1),
    _ApplIndex_Type()
)
applIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    applIndex.setStatus("current")
_ApplName_Type = SnmpAdminString
_ApplName_Object = MibTableColumn
applName = _ApplName_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 2),
    _ApplName_Type()
)
applName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applName.setStatus("current")
_ApplDirectoryName_Type = DistinguishedName
_ApplDirectoryName_Object = MibTableColumn
applDirectoryName = _ApplDirectoryName_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 3),
    _ApplDirectoryName_Type()
)
applDirectoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applDirectoryName.setStatus("current")
_ApplVersion_Type = SnmpAdminString
_ApplVersion_Object = MibTableColumn
applVersion = _ApplVersion_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 4),
    _ApplVersion_Type()
)
applVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applVersion.setStatus("current")
_ApplUptime_Type = TimeStamp
_ApplUptime_Object = MibTableColumn
applUptime = _ApplUptime_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 5),
    _ApplUptime_Type()
)
applUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applUptime.setStatus("current")


class _ApplOperStatus_Type(Integer32):
    """Custom type applOperStatus based on Integer32"""
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
        *(("congested", 4),
          ("down", 2),
          ("halted", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("up", 1))
    )


_ApplOperStatus_Type.__name__ = "Integer32"
_ApplOperStatus_Object = MibTableColumn
applOperStatus = _ApplOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 6),
    _ApplOperStatus_Type()
)
applOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOperStatus.setStatus("current")
_ApplLastChange_Type = TimeStamp
_ApplLastChange_Object = MibTableColumn
applLastChange = _ApplLastChange_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 7),
    _ApplLastChange_Type()
)
applLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applLastChange.setStatus("current")
_ApplInboundAssociations_Type = Gauge32
_ApplInboundAssociations_Object = MibTableColumn
applInboundAssociations = _ApplInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 8),
    _ApplInboundAssociations_Type()
)
applInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applInboundAssociations.setStatus("current")
_ApplOutboundAssociations_Type = Gauge32
_ApplOutboundAssociations_Object = MibTableColumn
applOutboundAssociations = _ApplOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 9),
    _ApplOutboundAssociations_Type()
)
applOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applOutboundAssociations.setStatus("current")
_ApplAccumulatedInboundAssociations_Type = Counter32
_ApplAccumulatedInboundAssociations_Object = MibTableColumn
applAccumulatedInboundAssociations = _ApplAccumulatedInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 10),
    _ApplAccumulatedInboundAssociations_Type()
)
applAccumulatedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applAccumulatedInboundAssociations.setStatus("current")
_ApplAccumulatedOutboundAssociations_Type = Counter32
_ApplAccumulatedOutboundAssociations_Object = MibTableColumn
applAccumulatedOutboundAssociations = _ApplAccumulatedOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 11),
    _ApplAccumulatedOutboundAssociations_Type()
)
applAccumulatedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applAccumulatedOutboundAssociations.setStatus("current")
_ApplLastInboundActivity_Type = TimeStamp
_ApplLastInboundActivity_Object = MibTableColumn
applLastInboundActivity = _ApplLastInboundActivity_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 12),
    _ApplLastInboundActivity_Type()
)
applLastInboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applLastInboundActivity.setStatus("current")
_ApplLastOutboundActivity_Type = TimeStamp
_ApplLastOutboundActivity_Object = MibTableColumn
applLastOutboundActivity = _ApplLastOutboundActivity_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 13),
    _ApplLastOutboundActivity_Type()
)
applLastOutboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applLastOutboundActivity.setStatus("current")
_ApplRejectedInboundAssociations_Type = Counter32
_ApplRejectedInboundAssociations_Object = MibTableColumn
applRejectedInboundAssociations = _ApplRejectedInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 14),
    _ApplRejectedInboundAssociations_Type()
)
applRejectedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applRejectedInboundAssociations.setStatus("current")
_ApplFailedOutboundAssociations_Type = Counter32
_ApplFailedOutboundAssociations_Object = MibTableColumn
applFailedOutboundAssociations = _ApplFailedOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 15),
    _ApplFailedOutboundAssociations_Type()
)
applFailedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applFailedOutboundAssociations.setStatus("current")
_ApplDescription_Type = SnmpAdminString
_ApplDescription_Object = MibTableColumn
applDescription = _ApplDescription_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 16),
    _ApplDescription_Type()
)
applDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applDescription.setStatus("current")
_ApplURL_Type = URLString
_ApplURL_Object = MibTableColumn
applURL = _ApplURL_Object(
    (1, 3, 6, 1, 2, 1, 27, 1, 1, 17),
    _ApplURL_Type()
)
applURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applURL.setStatus("current")
_AssocTable_Object = MibTable
assocTable = _AssocTable_Object(
    (1, 3, 6, 1, 2, 1, 27, 2)
)
if mibBuilder.loadTexts:
    assocTable.setStatus("current")
_AssocEntry_Object = MibTableRow
assocEntry = _AssocEntry_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1)
)
assocEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "NETWORK-SERVICES-MIB", "assocIndex"),
)
if mibBuilder.loadTexts:
    assocEntry.setStatus("current")


class _AssocIndex_Type(Integer32):
    """Custom type assocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AssocIndex_Type.__name__ = "Integer32"
_AssocIndex_Object = MibTableColumn
assocIndex = _AssocIndex_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1, 1),
    _AssocIndex_Type()
)
assocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    assocIndex.setStatus("current")
_AssocRemoteApplication_Type = SnmpAdminString
_AssocRemoteApplication_Object = MibTableColumn
assocRemoteApplication = _AssocRemoteApplication_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1, 2),
    _AssocRemoteApplication_Type()
)
assocRemoteApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRemoteApplication.setStatus("current")
_AssocApplicationProtocol_Type = ObjectIdentifier
_AssocApplicationProtocol_Object = MibTableColumn
assocApplicationProtocol = _AssocApplicationProtocol_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1, 3),
    _AssocApplicationProtocol_Type()
)
assocApplicationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocApplicationProtocol.setStatus("current")


class _AssocApplicationType_Type(Integer32):
    """Custom type assocApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("peerinitiator", 3),
          ("peerresponder", 4),
          ("uainitiator", 1),
          ("uaresponder", 2))
    )


_AssocApplicationType_Type.__name__ = "Integer32"
_AssocApplicationType_Object = MibTableColumn
assocApplicationType = _AssocApplicationType_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1, 4),
    _AssocApplicationType_Type()
)
assocApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocApplicationType.setStatus("current")
_AssocDuration_Type = TimeStamp
_AssocDuration_Object = MibTableColumn
assocDuration = _AssocDuration_Object(
    (1, 3, 6, 1, 2, 1, 27, 2, 1, 5),
    _AssocDuration_Type()
)
assocDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocDuration.setStatus("current")
_ApplConformance_ObjectIdentity = ObjectIdentity
applConformance = _ApplConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 27, 3)
)
_ApplGroups_ObjectIdentity = ObjectIdentity
applGroups = _ApplGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 27, 3, 1)
)
_ApplCompliances_ObjectIdentity = ObjectIdentity
applCompliances = _ApplCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 27, 3, 2)
)
_ApplTCPProtoID_ObjectIdentity = ObjectIdentity
applTCPProtoID = _ApplTCPProtoID_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 27, 4)
)
_ApplUDPProtoID_ObjectIdentity = ObjectIdentity
applUDPProtoID = _ApplUDPProtoID_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 27, 5)
)

# Managed Objects groups

assocRFC1565Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 2)
)
assocRFC1565Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "assocRemoteApplication"),
        ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"),
        ("NETWORK-SERVICES-MIB", "assocApplicationType"),
        ("NETWORK-SERVICES-MIB", "assocDuration"))
)
if mibBuilder.loadTexts:
    assocRFC1565Group.setStatus("obsolete")

applRFC2248Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 3)
)
applRFC2248Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "applName"),
        ("NETWORK-SERVICES-MIB", "applVersion"),
        ("NETWORK-SERVICES-MIB", "applUptime"),
        ("NETWORK-SERVICES-MIB", "applOperStatus"),
        ("NETWORK-SERVICES-MIB", "applLastChange"),
        ("NETWORK-SERVICES-MIB", "applInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applLastInboundActivity"),
        ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"),
        ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applDescription"),
        ("NETWORK-SERVICES-MIB", "applURL"))
)
if mibBuilder.loadTexts:
    applRFC2248Group.setStatus("deprecated")

assocRFC2248Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 4)
)
assocRFC2248Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "assocRemoteApplication"),
        ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"),
        ("NETWORK-SERVICES-MIB", "assocApplicationType"),
        ("NETWORK-SERVICES-MIB", "assocDuration"))
)
if mibBuilder.loadTexts:
    assocRFC2248Group.setStatus("deprecated")

applRFC2788Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 5)
)
applRFC2788Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "applName"),
        ("NETWORK-SERVICES-MIB", "applDirectoryName"),
        ("NETWORK-SERVICES-MIB", "applVersion"),
        ("NETWORK-SERVICES-MIB", "applUptime"),
        ("NETWORK-SERVICES-MIB", "applOperStatus"),
        ("NETWORK-SERVICES-MIB", "applLastChange"),
        ("NETWORK-SERVICES-MIB", "applInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applLastInboundActivity"),
        ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"),
        ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applDescription"),
        ("NETWORK-SERVICES-MIB", "applURL"))
)
if mibBuilder.loadTexts:
    applRFC2788Group.setStatus("current")

assocRFC2788Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 6)
)
assocRFC2788Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "assocRemoteApplication"),
        ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"),
        ("NETWORK-SERVICES-MIB", "assocApplicationType"),
        ("NETWORK-SERVICES-MIB", "assocDuration"))
)
if mibBuilder.loadTexts:
    assocRFC2788Group.setStatus("current")

applRFC1565Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 27, 3, 1, 7)
)
applRFC1565Group.setObjects(
      *(("NETWORK-SERVICES-MIB", "applName"),
        ("NETWORK-SERVICES-MIB", "applVersion"),
        ("NETWORK-SERVICES-MIB", "applUptime"),
        ("NETWORK-SERVICES-MIB", "applOperStatus"),
        ("NETWORK-SERVICES-MIB", "applLastChange"),
        ("NETWORK-SERVICES-MIB", "applInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applLastInboundActivity"),
        ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"),
        ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"),
        ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"))
)
if mibBuilder.loadTexts:
    applRFC1565Group.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

applCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 1)
)
if mibBuilder.loadTexts:
    applCompliance.setStatus(
        "obsolete"
    )

assocCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 2)
)
if mibBuilder.loadTexts:
    assocCompliance.setStatus(
        "obsolete"
    )

applRFC2248Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 3)
)
if mibBuilder.loadTexts:
    applRFC2248Compliance.setStatus(
        "deprecated"
    )

assocRFC2248Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 4)
)
if mibBuilder.loadTexts:
    assocRFC2248Compliance.setStatus(
        "deprecated"
    )

applRFC2788Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 5)
)
if mibBuilder.loadTexts:
    applRFC2788Compliance.setStatus(
        "current"
    )

assocRFC2788Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 27, 3, 2, 6)
)
if mibBuilder.loadTexts:
    assocRFC2788Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-SERVICES-MIB",
    **{"DistinguishedName": DistinguishedName,
       "URLString": URLString,
       "application": application,
       "applTable": applTable,
       "applEntry": applEntry,
       "applIndex": applIndex,
       "applName": applName,
       "applDirectoryName": applDirectoryName,
       "applVersion": applVersion,
       "applUptime": applUptime,
       "applOperStatus": applOperStatus,
       "applLastChange": applLastChange,
       "applInboundAssociations": applInboundAssociations,
       "applOutboundAssociations": applOutboundAssociations,
       "applAccumulatedInboundAssociations": applAccumulatedInboundAssociations,
       "applAccumulatedOutboundAssociations": applAccumulatedOutboundAssociations,
       "applLastInboundActivity": applLastInboundActivity,
       "applLastOutboundActivity": applLastOutboundActivity,
       "applRejectedInboundAssociations": applRejectedInboundAssociations,
       "applFailedOutboundAssociations": applFailedOutboundAssociations,
       "applDescription": applDescription,
       "applURL": applURL,
       "assocTable": assocTable,
       "assocEntry": assocEntry,
       "assocIndex": assocIndex,
       "assocRemoteApplication": assocRemoteApplication,
       "assocApplicationProtocol": assocApplicationProtocol,
       "assocApplicationType": assocApplicationType,
       "assocDuration": assocDuration,
       "applConformance": applConformance,
       "applGroups": applGroups,
       "assocRFC1565Group": assocRFC1565Group,
       "applRFC2248Group": applRFC2248Group,
       "assocRFC2248Group": assocRFC2248Group,
       "applRFC2788Group": applRFC2788Group,
       "assocRFC2788Group": assocRFC2788Group,
       "applRFC1565Group": applRFC1565Group,
       "applCompliances": applCompliances,
       "applCompliance": applCompliance,
       "assocCompliance": assocCompliance,
       "applRFC2248Compliance": applRFC2248Compliance,
       "assocRFC2248Compliance": assocRFC2248Compliance,
       "applRFC2788Compliance": applRFC2788Compliance,
       "assocRFC2788Compliance": assocRFC2788Compliance,
       "applTCPProtoID": applTCPProtoID,
       "applUDPProtoID": applUDPProtoID}
)
