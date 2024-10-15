# SNMP MIB module (ONEACCESS-CONFIGMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-CONFIGMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:50 2024
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

(oacExpIMManagement,
 oacMIBModules,
 oacRequirements) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement",
    "oacMIBModules",
    "oacRequirements")

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

oacConfigMgmtMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2001)
)
oacConfigMgmtMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacCMConformance_ObjectIdentity = ObjectIdentity
oacCMConformance = _OacCMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2001)
)
_OacCMGroups_ObjectIdentity = ObjectIdentity
oacCMGroups = _OacCMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2001, 1)
)
_OacCMCompliances_ObjectIdentity = ObjectIdentity
oacCMCompliances = _OacCMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2001, 2)
)
_OacExpIMConfigMgmt_ObjectIdentity = ObjectIdentity
oacExpIMConfigMgmt = _OacExpIMConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6)
)
_OacConfigMgmtObjects_ObjectIdentity = ObjectIdentity
oacConfigMgmtObjects = _OacConfigMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1)
)
_OacCMHistory_ObjectIdentity = ObjectIdentity
oacCMHistory = _OacCMHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 1)
)
_OacCMHistoryRunningLastChanged_Type = DateAndTime
_OacCMHistoryRunningLastChanged_Object = MibScalar
oacCMHistoryRunningLastChanged = _OacCMHistoryRunningLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 1, 1),
    _OacCMHistoryRunningLastChanged_Type()
)
oacCMHistoryRunningLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCMHistoryRunningLastChanged.setStatus("current")
_OacCMHistoryRunningLastSaved_Type = DateAndTime
_OacCMHistoryRunningLastSaved_Object = MibScalar
oacCMHistoryRunningLastSaved = _OacCMHistoryRunningLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 1, 2),
    _OacCMHistoryRunningLastSaved_Type()
)
oacCMHistoryRunningLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCMHistoryRunningLastSaved.setStatus("current")
_OacCMHistoryStartupLastChanged_Type = DateAndTime
_OacCMHistoryStartupLastChanged_Object = MibScalar
oacCMHistoryStartupLastChanged = _OacCMHistoryStartupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 1, 3),
    _OacCMHistoryStartupLastChanged_Type()
)
oacCMHistoryStartupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacCMHistoryStartupLastChanged.setStatus("current")
_OacCMCopy_ObjectIdentity = ObjectIdentity
oacCMCopy = _OacCMCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2)
)
_OacCMCopyIndex_Type = IpAddress
_OacCMCopyIndex_Object = MibScalar
oacCMCopyIndex = _OacCMCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 1),
    _OacCMCopyIndex_Type()
)
oacCMCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacCMCopyIndex.setStatus("current")
_OacCMCopyTftpRunTable_Object = MibTable
oacCMCopyTftpRunTable = _OacCMCopyTftpRunTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    oacCMCopyTftpRunTable.setStatus("current")
_OacCMCopyTftpRunEntry_Object = MibTableRow
oacCMCopyTftpRunEntry = _OacCMCopyTftpRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 2, 1)
)
oacCMCopyTftpRunEntry.setIndexNames(
    (0, "ONEACCESS-CONFIGMGMT-MIB", "oacCMCopyIndex"),
)
if mibBuilder.loadTexts:
    oacCMCopyTftpRunEntry.setStatus("current")
_OacCMCopyTftpRun_Type = DisplayString
_OacCMCopyTftpRun_Object = MibTableColumn
oacCMCopyTftpRun = _OacCMCopyTftpRun_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 2, 1, 1),
    _OacCMCopyTftpRun_Type()
)
oacCMCopyTftpRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacCMCopyTftpRun.setStatus("current")
_OacCMCopyRunTftpTable_Object = MibTable
oacCMCopyRunTftpTable = _OacCMCopyRunTftpTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    oacCMCopyRunTftpTable.setStatus("current")
_OacCMCopyRunTftpEntry_Object = MibTableRow
oacCMCopyRunTftpEntry = _OacCMCopyRunTftpEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 3, 1)
)
oacCMCopyRunTftpEntry.setIndexNames(
    (0, "ONEACCESS-CONFIGMGMT-MIB", "oacCMCopyIndex"),
)
if mibBuilder.loadTexts:
    oacCMCopyRunTftpEntry.setStatus("current")
_OacCMCopyRunTftp_Type = DisplayString
_OacCMCopyRunTftp_Object = MibTableColumn
oacCMCopyRunTftp = _OacCMCopyRunTftp_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 2, 3, 1, 1),
    _OacCMCopyRunTftp_Type()
)
oacCMCopyRunTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacCMCopyRunTftp.setStatus("current")
_OacConfigMgmtNotifications_ObjectIdentity = ObjectIdentity
oacConfigMgmtNotifications = _OacConfigMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 3)
)

# Managed Objects groups

oacCMGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2001, 1, 1)
)
oacCMGeneralGroup.setObjects(
      *(("ONEACCESS-CONFIGMGMT-MIB", "oacCMHistoryRunningLastChanged"),
        ("ONEACCESS-CONFIGMGMT-MIB", "oacCMHistoryRunningLastSaved"),
        ("ONEACCESS-CONFIGMGMT-MIB", "oacCMHistoryStartupLastChanged"))
)
if mibBuilder.loadTexts:
    oacCMGeneralGroup.setStatus("current")


# Notification objects

oacCMRunningConfigSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacCMRunningConfigSaved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

oacCMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2001, 2, 1)
)
if mibBuilder.loadTexts:
    oacCMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-CONFIGMGMT-MIB",
    **{"oacConfigMgmtMIBModule": oacConfigMgmtMIBModule,
       "oacCMConformance": oacCMConformance,
       "oacCMGroups": oacCMGroups,
       "oacCMGeneralGroup": oacCMGeneralGroup,
       "oacCMCompliances": oacCMCompliances,
       "oacCMCompliance": oacCMCompliance,
       "oacExpIMConfigMgmt": oacExpIMConfigMgmt,
       "oacConfigMgmtObjects": oacConfigMgmtObjects,
       "oacCMHistory": oacCMHistory,
       "oacCMHistoryRunningLastChanged": oacCMHistoryRunningLastChanged,
       "oacCMHistoryRunningLastSaved": oacCMHistoryRunningLastSaved,
       "oacCMHistoryStartupLastChanged": oacCMHistoryStartupLastChanged,
       "oacCMCopy": oacCMCopy,
       "oacCMCopyIndex": oacCMCopyIndex,
       "oacCMCopyTftpRunTable": oacCMCopyTftpRunTable,
       "oacCMCopyTftpRunEntry": oacCMCopyTftpRunEntry,
       "oacCMCopyTftpRun": oacCMCopyTftpRun,
       "oacCMCopyRunTftpTable": oacCMCopyRunTftpTable,
       "oacCMCopyRunTftpEntry": oacCMCopyRunTftpEntry,
       "oacCMCopyRunTftp": oacCMCopyRunTftp,
       "oacConfigMgmtNotifications": oacConfigMgmtNotifications,
       "oacCMRunningConfigSaved": oacCMRunningConfigSaved}
)
