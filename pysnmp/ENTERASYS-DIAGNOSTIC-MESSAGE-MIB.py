# SNMP MIB module (ENTERASYS-DIAGNOSTIC-MESSAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-DIAGNOSTIC-MESSAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:46 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysDiagnosticMessageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13)
)
etsysDiagnosticMessageMIB.setRevisions(
        ("2003-01-10 21:17",
         "2002-06-07 14:28",
         "2001-12-03 19:51",
         "2001-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LongAdminString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysDiagnosticMessage_ObjectIdentity = ObjectIdentity
etsysDiagnosticMessage = _EtsysDiagnosticMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1)
)
_EtsysDiagnosticMessageCount_Type = Counter32
_EtsysDiagnosticMessageCount_Object = MibScalar
etsysDiagnosticMessageCount = _EtsysDiagnosticMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 1),
    _EtsysDiagnosticMessageCount_Type()
)
etsysDiagnosticMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageCount.setStatus("current")
_EtsysDiagnosticMessageChanges_Type = Counter32
_EtsysDiagnosticMessageChanges_Object = MibScalar
etsysDiagnosticMessageChanges = _EtsysDiagnosticMessageChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 2),
    _EtsysDiagnosticMessageChanges_Type()
)
etsysDiagnosticMessageChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageChanges.setStatus("current")
_EtsysDiagnosticMessageTable_Object = MibTable
etsysDiagnosticMessageTable = _EtsysDiagnosticMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3)
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageTable.setStatus("current")
_EtsysDiagnosticMessageEntry_Object = MibTableRow
etsysDiagnosticMessageEntry = _EtsysDiagnosticMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1)
)
etsysDiagnosticMessageEntry.setIndexNames(
    (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"),
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageEntry.setStatus("current")


class _EtsysDiagnosticMessageIndex_Type(Unsigned32):
    """Custom type etsysDiagnosticMessageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysDiagnosticMessageIndex_Type.__name__ = "Unsigned32"
_EtsysDiagnosticMessageIndex_Object = MibTableColumn
etsysDiagnosticMessageIndex = _EtsysDiagnosticMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 1),
    _EtsysDiagnosticMessageIndex_Type()
)
etsysDiagnosticMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageIndex.setStatus("current")
_EtsysDiagnosticMessageTime_Type = DateAndTime
_EtsysDiagnosticMessageTime_Object = MibTableColumn
etsysDiagnosticMessageTime = _EtsysDiagnosticMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 2),
    _EtsysDiagnosticMessageTime_Type()
)
etsysDiagnosticMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageTime.setStatus("current")


class _EtsysDiagnosticMessageType_Type(SnmpAdminString):
    """Custom type etsysDiagnosticMessageType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysDiagnosticMessageType_Type.__name__ = "SnmpAdminString"
_EtsysDiagnosticMessageType_Object = MibTableColumn
etsysDiagnosticMessageType = _EtsysDiagnosticMessageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 3),
    _EtsysDiagnosticMessageType_Type()
)
etsysDiagnosticMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageType.setStatus("current")


class _EtsysDiagnosticMessageSummary_Type(SnmpAdminString):
    """Custom type etsysDiagnosticMessageSummary based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysDiagnosticMessageSummary_Type.__name__ = "SnmpAdminString"
_EtsysDiagnosticMessageSummary_Object = MibTableColumn
etsysDiagnosticMessageSummary = _EtsysDiagnosticMessageSummary_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 4),
    _EtsysDiagnosticMessageSummary_Type()
)
etsysDiagnosticMessageSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageSummary.setStatus("current")


class _EtsysDiagnosticMessageFWRevision_Type(SnmpAdminString):
    """Custom type etsysDiagnosticMessageFWRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EtsysDiagnosticMessageFWRevision_Type.__name__ = "SnmpAdminString"
_EtsysDiagnosticMessageFWRevision_Object = MibTableColumn
etsysDiagnosticMessageFWRevision = _EtsysDiagnosticMessageFWRevision_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 5),
    _EtsysDiagnosticMessageFWRevision_Type()
)
etsysDiagnosticMessageFWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageFWRevision.setStatus("current")


class _EtsysDiagnosticMessageStatus_Type(Bits):
    """Custom type etsysDiagnosticMessageStatus based on Bits"""
    namedValues = NamedValues(
        ("etsysDiagnosticMessageBadChecksum", 0)
    )

_EtsysDiagnosticMessageStatus_Type.__name__ = "Bits"
_EtsysDiagnosticMessageStatus_Object = MibTableColumn
etsysDiagnosticMessageStatus = _EtsysDiagnosticMessageStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 6),
    _EtsysDiagnosticMessageStatus_Type()
)
etsysDiagnosticMessageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageStatus.setStatus("current")
_EtsysDiagnosticMessageDetails_ObjectIdentity = ObjectIdentity
etsysDiagnosticMessageDetails = _EtsysDiagnosticMessageDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2)
)
_EtsysDiagnosticMessageDetailsTable_Object = MibTable
etsysDiagnosticMessageDetailsTable = _EtsysDiagnosticMessageDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageDetailsTable.setStatus("current")
_EtsysDiagnosticMessageDetailsEntry_Object = MibTableRow
etsysDiagnosticMessageDetailsEntry = _EtsysDiagnosticMessageDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1)
)
etsysDiagnosticMessageDetailsEntry.setIndexNames(
    (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"),
    (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsIndex"),
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageDetailsEntry.setStatus("current")


class _EtsysDiagnosticMessageDetailsIndex_Type(Unsigned32):
    """Custom type etsysDiagnosticMessageDetailsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_EtsysDiagnosticMessageDetailsIndex_Type.__name__ = "Unsigned32"
_EtsysDiagnosticMessageDetailsIndex_Object = MibTableColumn
etsysDiagnosticMessageDetailsIndex = _EtsysDiagnosticMessageDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 1),
    _EtsysDiagnosticMessageDetailsIndex_Type()
)
etsysDiagnosticMessageDetailsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageDetailsIndex.setStatus("current")
_EtsysDiagnosticMessageDetailsText_Type = LongAdminString
_EtsysDiagnosticMessageDetailsText_Object = MibTableColumn
etsysDiagnosticMessageDetailsText = _EtsysDiagnosticMessageDetailsText_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 2),
    _EtsysDiagnosticMessageDetailsText_Type()
)
etsysDiagnosticMessageDetailsText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageDetailsText.setStatus("current")


class _EtsysDiagnosticMessageDetailsStatus_Type(Bits):
    """Custom type etsysDiagnosticMessageDetailsStatus based on Bits"""
    namedValues = NamedValues(
        ("etsysDiagnosticMessageLastSegment", 0)
    )

_EtsysDiagnosticMessageDetailsStatus_Type.__name__ = "Bits"
_EtsysDiagnosticMessageDetailsStatus_Object = MibTableColumn
etsysDiagnosticMessageDetailsStatus = _EtsysDiagnosticMessageDetailsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 3),
    _EtsysDiagnosticMessageDetailsStatus_Type()
)
etsysDiagnosticMessageDetailsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDiagnosticMessageDetailsStatus.setStatus("current")
_EtsysDiagnosticMessageConformance_ObjectIdentity = ObjectIdentity
etsysDiagnosticMessageConformance = _EtsysDiagnosticMessageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3)
)
_EtsysDiagnosticMessageGroups_ObjectIdentity = ObjectIdentity
etsysDiagnosticMessageGroups = _EtsysDiagnosticMessageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1)
)
_EtsysDiagnosticMessageCompliances_ObjectIdentity = ObjectIdentity
etsysDiagnosticMessageCompliances = _EtsysDiagnosticMessageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2)
)

# Managed Objects groups

etsysDiagnosticMessageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1, 1)
)
etsysDiagnosticMessageGroup.setObjects(
      *(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageCount"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageChanges"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageTime"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageType"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageSummary"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageFWRevision"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageStatus"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsText"),
        ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsStatus"))
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDiagnosticMessageCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDiagnosticMessageCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB",
    **{"LongAdminString": LongAdminString,
       "etsysDiagnosticMessageMIB": etsysDiagnosticMessageMIB,
       "etsysDiagnosticMessage": etsysDiagnosticMessage,
       "etsysDiagnosticMessageCount": etsysDiagnosticMessageCount,
       "etsysDiagnosticMessageChanges": etsysDiagnosticMessageChanges,
       "etsysDiagnosticMessageTable": etsysDiagnosticMessageTable,
       "etsysDiagnosticMessageEntry": etsysDiagnosticMessageEntry,
       "etsysDiagnosticMessageIndex": etsysDiagnosticMessageIndex,
       "etsysDiagnosticMessageTime": etsysDiagnosticMessageTime,
       "etsysDiagnosticMessageType": etsysDiagnosticMessageType,
       "etsysDiagnosticMessageSummary": etsysDiagnosticMessageSummary,
       "etsysDiagnosticMessageFWRevision": etsysDiagnosticMessageFWRevision,
       "etsysDiagnosticMessageStatus": etsysDiagnosticMessageStatus,
       "etsysDiagnosticMessageDetails": etsysDiagnosticMessageDetails,
       "etsysDiagnosticMessageDetailsTable": etsysDiagnosticMessageDetailsTable,
       "etsysDiagnosticMessageDetailsEntry": etsysDiagnosticMessageDetailsEntry,
       "etsysDiagnosticMessageDetailsIndex": etsysDiagnosticMessageDetailsIndex,
       "etsysDiagnosticMessageDetailsText": etsysDiagnosticMessageDetailsText,
       "etsysDiagnosticMessageDetailsStatus": etsysDiagnosticMessageDetailsStatus,
       "etsysDiagnosticMessageConformance": etsysDiagnosticMessageConformance,
       "etsysDiagnosticMessageGroups": etsysDiagnosticMessageGroups,
       "etsysDiagnosticMessageGroup": etsysDiagnosticMessageGroup,
       "etsysDiagnosticMessageCompliances": etsysDiagnosticMessageCompliances,
       "etsysDiagnosticMessageCompliance": etsysDiagnosticMessageCompliance}
)
