# SNMP MIB module (CISCO-VOICE-HDLC-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:26 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CvcGUid,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcGUid")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVoiceHdlcDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvhdlcdcMIBObjects_ObjectIdentity = ObjectIdentity
cvhdlcdcMIBObjects = _CvhdlcdcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1)
)
_CvHdlcCallHistory_ObjectIdentity = ObjectIdentity
cvHdlcCallHistory = _CvHdlcCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1)
)
_CvHdlcCallHistoryTable_Object = MibTable
cvHdlcCallHistoryTable = _CvHdlcCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvHdlcCallHistoryTable.setStatus("current")
_CvHdlcCallHistoryEntry_Object = MibTableRow
cvHdlcCallHistoryEntry = _CvHdlcCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1)
)
cvHdlcCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvHdlcCallHistoryEntry.setStatus("current")
_CvHdlcCallHistoryConnectionId_Type = CvcGUid
_CvHdlcCallHistoryConnectionId_Object = MibTableColumn
cvHdlcCallHistoryConnectionId = _CvHdlcCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 1),
    _CvHdlcCallHistoryConnectionId_Type()
)
cvHdlcCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvHdlcCallHistoryConnectionId.setStatus("current")


class _CvHdlcCallHistoryLowerIfName_Type(DisplayString):
    """Custom type cvHdlcCallHistoryLowerIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CvHdlcCallHistoryLowerIfName_Type.__name__ = "DisplayString"
_CvHdlcCallHistoryLowerIfName_Object = MibTableColumn
cvHdlcCallHistoryLowerIfName = _CvHdlcCallHistoryLowerIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 2),
    _CvHdlcCallHistoryLowerIfName_Type()
)
cvHdlcCallHistoryLowerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvHdlcCallHistoryLowerIfName.setStatus("current")
_CvHdlcCallHistorySessionTarget_Type = DisplayString
_CvHdlcCallHistorySessionTarget_Object = MibTableColumn
cvHdlcCallHistorySessionTarget = _CvHdlcCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 3),
    _CvHdlcCallHistorySessionTarget_Type()
)
cvHdlcCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvHdlcCallHistorySessionTarget.setStatus("current")
_CvhdlcdcMIBConformance_ObjectIdentity = ObjectIdentity
cvhdlcdcMIBConformance = _CvhdlcdcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 3)
)
_CvhdlcdcMIBCompliances_ObjectIdentity = ObjectIdentity
cvhdlcdcMIBCompliances = _CvhdlcdcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1)
)
_CvhdlcdcMIBGroups_ObjectIdentity = ObjectIdentity
cvhdlcdcMIBGroups = _CvhdlcdcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2)
)

# Managed Objects groups

cvHdlcCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2, 1)
)
cvHdlcCallHistoryGroup.setObjects(
      *(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryConnectionId"),
        ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryLowerIfName"),
        ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistorySessionTarget"))
)
if mibBuilder.loadTexts:
    cvHdlcCallHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvhdlcdcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvhdlcdcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-HDLC-DIAL-CONTROL-MIB",
    **{"ciscoVoiceHdlcDialControlMIB": ciscoVoiceHdlcDialControlMIB,
       "cvhdlcdcMIBObjects": cvhdlcdcMIBObjects,
       "cvHdlcCallHistory": cvHdlcCallHistory,
       "cvHdlcCallHistoryTable": cvHdlcCallHistoryTable,
       "cvHdlcCallHistoryEntry": cvHdlcCallHistoryEntry,
       "cvHdlcCallHistoryConnectionId": cvHdlcCallHistoryConnectionId,
       "cvHdlcCallHistoryLowerIfName": cvHdlcCallHistoryLowerIfName,
       "cvHdlcCallHistorySessionTarget": cvHdlcCallHistorySessionTarget,
       "cvhdlcdcMIBConformance": cvhdlcdcMIBConformance,
       "cvhdlcdcMIBCompliances": cvhdlcdcMIBCompliances,
       "cvhdlcdcMIBCompliance": cvhdlcdcMIBCompliance,
       "cvhdlcdcMIBGroups": cvhdlcdcMIBGroups,
       "cvHdlcCallHistoryGroup": cvHdlcCallHistoryGroup}
)
