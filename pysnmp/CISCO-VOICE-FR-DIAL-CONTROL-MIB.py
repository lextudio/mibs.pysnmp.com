# SNMP MIB module (CISCO-VOICE-FR-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:25 2024
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

ciscoVoiceFrDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvfrdcMIBObjects_ObjectIdentity = ObjectIdentity
cvfrdcMIBObjects = _CvfrdcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1)
)
_CvFrCallHistory_ObjectIdentity = ObjectIdentity
cvFrCallHistory = _CvFrCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1)
)
_CvFrCallHistoryTable_Object = MibTable
cvFrCallHistoryTable = _CvFrCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvFrCallHistoryTable.setStatus("current")
_CvFrCallHistoryEntry_Object = MibTableRow
cvFrCallHistoryEntry = _CvFrCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1)
)
cvFrCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvFrCallHistoryEntry.setStatus("current")
_CvFrCallHistoryConnectionId_Type = CvcGUid
_CvFrCallHistoryConnectionId_Object = MibTableColumn
cvFrCallHistoryConnectionId = _CvFrCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 1),
    _CvFrCallHistoryConnectionId_Type()
)
cvFrCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvFrCallHistoryConnectionId.setStatus("current")


class _CvFrCallHistoryDlci_Type(Integer32):
    """Custom type cvFrCallHistoryDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvFrCallHistoryDlci_Type.__name__ = "Integer32"
_CvFrCallHistoryDlci_Object = MibTableColumn
cvFrCallHistoryDlci = _CvFrCallHistoryDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 2),
    _CvFrCallHistoryDlci_Type()
)
cvFrCallHistoryDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvFrCallHistoryDlci.setStatus("current")


class _CvFrCallHistoryLowerIfName_Type(DisplayString):
    """Custom type cvFrCallHistoryLowerIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CvFrCallHistoryLowerIfName_Type.__name__ = "DisplayString"
_CvFrCallHistoryLowerIfName_Object = MibTableColumn
cvFrCallHistoryLowerIfName = _CvFrCallHistoryLowerIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 3),
    _CvFrCallHistoryLowerIfName_Type()
)
cvFrCallHistoryLowerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvFrCallHistoryLowerIfName.setStatus("current")
_CvFrCallHistorySessionTarget_Type = DisplayString
_CvFrCallHistorySessionTarget_Object = MibTableColumn
cvFrCallHistorySessionTarget = _CvFrCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 4),
    _CvFrCallHistorySessionTarget_Type()
)
cvFrCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvFrCallHistorySessionTarget.setStatus("current")
_CvfrdcMIBConformance_ObjectIdentity = ObjectIdentity
cvfrdcMIBConformance = _CvfrdcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 3)
)
_CvfrdcMIBCompliances_ObjectIdentity = ObjectIdentity
cvfrdcMIBCompliances = _CvfrdcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1)
)
_CvfrdcMIBGroups_ObjectIdentity = ObjectIdentity
cvfrdcMIBGroups = _CvfrdcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2)
)

# Managed Objects groups

cvFrCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2, 1)
)
cvFrCallHistoryGroup.setObjects(
      *(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryConnectionId"),
        ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryDlci"),
        ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryLowerIfName"),
        ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistorySessionTarget"))
)
if mibBuilder.loadTexts:
    cvFrCallHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvfrdcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvfrdcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-FR-DIAL-CONTROL-MIB",
    **{"ciscoVoiceFrDialControlMIB": ciscoVoiceFrDialControlMIB,
       "cvfrdcMIBObjects": cvfrdcMIBObjects,
       "cvFrCallHistory": cvFrCallHistory,
       "cvFrCallHistoryTable": cvFrCallHistoryTable,
       "cvFrCallHistoryEntry": cvFrCallHistoryEntry,
       "cvFrCallHistoryConnectionId": cvFrCallHistoryConnectionId,
       "cvFrCallHistoryDlci": cvFrCallHistoryDlci,
       "cvFrCallHistoryLowerIfName": cvFrCallHistoryLowerIfName,
       "cvFrCallHistorySessionTarget": cvFrCallHistorySessionTarget,
       "cvfrdcMIBConformance": cvfrdcMIBConformance,
       "cvfrdcMIBCompliances": cvfrdcMIBCompliances,
       "cvfrdcMIBCompliance": cvfrdcMIBCompliance,
       "cvfrdcMIBGroups": cvfrdcMIBGroups,
       "cvFrCallHistoryGroup": cvFrCallHistoryGroup}
)
