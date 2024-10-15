# SNMP MIB module (QUANTA-OPENFLOW-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QUANTA-OPENFLOW-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:05 2024
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

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

openFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200)
)
openFlow.setRevisions(
        ("2011-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentOpenFlowGroup_ObjectIdentity = ObjectIdentity
agentOpenFlowGroup = _AgentOpenFlowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1)
)
_AgentOpenFlowGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalConfigGroup = _AgentOpenFlowGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 1)
)


class _AgentOpenFlowAdminMode_Type(Integer32):
    """Custom type agentOpenFlowAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentOpenFlowAdminMode_Type.__name__ = "Integer32"
_AgentOpenFlowAdminMode_Object = MibScalar
agentOpenFlowAdminMode = _AgentOpenFlowAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 1, 1),
    _AgentOpenFlowAdminMode_Type()
)
agentOpenFlowAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowAdminMode.setStatus("current")


class _AgentOpenFlowVariant_Type(Integer32):
    """Custom type agentOpenFlowVariant based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("openFlow10Mode", 2),
          ("openFlow11Mode", 3),
          ("openFlow12Mode", 4),
          ("openFlow13Mode", 5))
    )


_AgentOpenFlowVariant_Type.__name__ = "Integer32"
_AgentOpenFlowVariant_Object = MibScalar
agentOpenFlowVariant = _AgentOpenFlowVariant_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 1, 2),
    _AgentOpenFlowVariant_Type()
)
agentOpenFlowVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowVariant.setStatus("current")
_AgentOpenFlowCfgControllerTable_Object = MibTable
agentOpenFlowCfgControllerTable = _AgentOpenFlowCfgControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3)
)
if mibBuilder.loadTexts:
    agentOpenFlowCfgControllerTable.setStatus("current")
_AgentOpenFlowCfgControllerEntry_Object = MibTableRow
agentOpenFlowCfgControllerEntry = _AgentOpenFlowCfgControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3, 1)
)
agentOpenFlowCfgControllerEntry.setIndexNames(
    (0, "QUANTA-OPENFLOW-PRIVATE-MIB", "agentOpenFlowCfgCtrlIPAddress"),
    (0, "QUANTA-OPENFLOW-PRIVATE-MIB", "agentOpenFlowCfgCtrlIPPort"),
)
if mibBuilder.loadTexts:
    agentOpenFlowCfgControllerEntry.setStatus("current")
_AgentOpenFlowCfgCtrlIPAddress_Type = IpAddress
_AgentOpenFlowCfgCtrlIPAddress_Object = MibTableColumn
agentOpenFlowCfgCtrlIPAddress = _AgentOpenFlowCfgCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3, 1, 1),
    _AgentOpenFlowCfgCtrlIPAddress_Type()
)
agentOpenFlowCfgCtrlIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlIPAddress.setStatus("current")


class _AgentOpenFlowCfgCtrlIPPort_Type(Unsigned32):
    """Custom type agentOpenFlowCfgCtrlIPPort based on Unsigned32"""
    defaultValue = 6632

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentOpenFlowCfgCtrlIPPort_Type.__name__ = "Unsigned32"
_AgentOpenFlowCfgCtrlIPPort_Object = MibTableColumn
agentOpenFlowCfgCtrlIPPort = _AgentOpenFlowCfgCtrlIPPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3, 1, 2),
    _AgentOpenFlowCfgCtrlIPPort_Type()
)
agentOpenFlowCfgCtrlIPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlIPPort.setStatus("current")


class _AgentOpenFlowCfgCtrlConnectionMode_Type(Integer32):
    """Custom type agentOpenFlowCfgCtrlConnectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssl", 1),
          ("tcp", 2))
    )


_AgentOpenFlowCfgCtrlConnectionMode_Type.__name__ = "Integer32"
_AgentOpenFlowCfgCtrlConnectionMode_Object = MibTableColumn
agentOpenFlowCfgCtrlConnectionMode = _AgentOpenFlowCfgCtrlConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3, 1, 3),
    _AgentOpenFlowCfgCtrlConnectionMode_Type()
)
agentOpenFlowCfgCtrlConnectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlConnectionMode.setStatus("current")
_AgentOpenFlowCfgCtrlStatus_Type = RowStatus
_AgentOpenFlowCfgCtrlStatus_Object = MibTableColumn
agentOpenFlowCfgCtrlStatus = _AgentOpenFlowCfgCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 3, 1, 4),
    _AgentOpenFlowCfgCtrlStatus_Type()
)
agentOpenFlowCfgCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlStatus.setStatus("current")
_AgentOpenFlowGlobalStatusParameters_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalStatusParameters = _AgentOpenFlowGlobalStatusParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 6)
)


class _AgentOpenFlowOperationalStatus_Type(Integer32):
    """Custom type agentOpenFlowOperationalStatus based on Integer32"""
    defaultValue = 2

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
        *(("disable", 2),
          ("disablePending", 4),
          ("enable", 1),
          ("enablePending", 3))
    )


_AgentOpenFlowOperationalStatus_Type.__name__ = "Integer32"
_AgentOpenFlowOperationalStatus_Object = MibScalar
agentOpenFlowOperationalStatus = _AgentOpenFlowOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 6, 1),
    _AgentOpenFlowOperationalStatus_Type()
)
agentOpenFlowOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowOperationalStatus.setStatus("current")


class _AgentOpenFlowDisableReason_Type(Integer32):
    """Custom type agentOpenFlowDisableReason based on Integer32"""
    defaultValue = 2

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
        *(("administrativelyDisabled", 2),
          ("noSSLCertificates", 4),
          ("noSuitableIPInterface", 3),
          ("none", 1))
    )


_AgentOpenFlowDisableReason_Type.__name__ = "Integer32"
_AgentOpenFlowDisableReason_Object = MibScalar
agentOpenFlowDisableReason = _AgentOpenFlowDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 6, 2),
    _AgentOpenFlowDisableReason_Type()
)
agentOpenFlowDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowDisableReason.setStatus("current")
_AgentOpenFlowGlobalCommands_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalCommands = _AgentOpenFlowGlobalCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 7)
)


class _AgentOpenFlowEraseOpenFlowManagerCertificates_Type(Integer32):
    """Custom type agentOpenFlowEraseOpenFlowManagerCertificates based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysReturnedOnRead", 1),
          ("eraseCertificates", 2))
    )


_AgentOpenFlowEraseOpenFlowManagerCertificates_Type.__name__ = "Integer32"
_AgentOpenFlowEraseOpenFlowManagerCertificates_Object = MibScalar
agentOpenFlowEraseOpenFlowManagerCertificates = _AgentOpenFlowEraseOpenFlowManagerCertificates_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 7, 1),
    _AgentOpenFlowEraseOpenFlowManagerCertificates_Type()
)
agentOpenFlowEraseOpenFlowManagerCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowEraseOpenFlowManagerCertificates.setStatus("current")
_AgentOpenFlowFlowTableStatusTable_Object = MibTable
agentOpenFlowFlowTableStatusTable = _AgentOpenFlowFlowTableStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8)
)
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableStatusTable.setStatus("current")
_AgentOpenFlowFlowTableStatusEntry_Object = MibTableRow
agentOpenFlowFlowTableStatusEntry = _AgentOpenFlowFlowTableStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1)
)
agentOpenFlowFlowTableStatusEntry.setIndexNames(
    (0, "QUANTA-OPENFLOW-PRIVATE-MIB", "agentOpenFlowFlowTable"),
)
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableStatusEntry.setStatus("current")


class _AgentOpenFlowFlowTable_Type(Unsigned32):
    """Custom type agentOpenFlowFlowTable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowFlowTable_Type.__name__ = "Unsigned32"
_AgentOpenFlowFlowTable_Object = MibTableColumn
agentOpenFlowFlowTable = _AgentOpenFlowFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 1),
    _AgentOpenFlowFlowTable_Type()
)
agentOpenFlowFlowTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTable.setStatus("current")


class _AgentOpenFlowFlowTableName_Type(OctetString):
    """Custom type agentOpenFlowFlowTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentOpenFlowFlowTableName_Type.__name__ = "OctetString"
_AgentOpenFlowFlowTableName_Object = MibTableColumn
agentOpenFlowFlowTableName = _AgentOpenFlowFlowTableName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 2),
    _AgentOpenFlowFlowTableName_Type()
)
agentOpenFlowFlowTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableName.setStatus("current")


class _AgentOpenFlowFlowTableDescription_Type(OctetString):
    """Custom type agentOpenFlowFlowTableDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AgentOpenFlowFlowTableDescription_Type.__name__ = "OctetString"
_AgentOpenFlowFlowTableDescription_Object = MibTableColumn
agentOpenFlowFlowTableDescription = _AgentOpenFlowFlowTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 3),
    _AgentOpenFlowFlowTableDescription_Type()
)
agentOpenFlowFlowTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableDescription.setStatus("current")
_AgentOpenFlowMaximumSize_Type = Unsigned32
_AgentOpenFlowMaximumSize_Object = MibTableColumn
agentOpenFlowMaximumSize = _AgentOpenFlowMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 4),
    _AgentOpenFlowMaximumSize_Type()
)
agentOpenFlowMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowMaximumSize.setStatus("current")
_AgentOpenFlowNumberOfEntries_Type = Unsigned32
_AgentOpenFlowNumberOfEntries_Object = MibTableColumn
agentOpenFlowNumberOfEntries = _AgentOpenFlowNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 5),
    _AgentOpenFlowNumberOfEntries_Type()
)
agentOpenFlowNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowNumberOfEntries.setStatus("current")
_AgentOpenFlowHardwareEntries_Type = Unsigned32
_AgentOpenFlowHardwareEntries_Object = MibTableColumn
agentOpenFlowHardwareEntries = _AgentOpenFlowHardwareEntries_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 6),
    _AgentOpenFlowHardwareEntries_Type()
)
agentOpenFlowHardwareEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowHardwareEntries.setStatus("current")
_AgentOpenFlowSoftwareOnlyEntries_Type = Unsigned32
_AgentOpenFlowSoftwareOnlyEntries_Object = MibTableColumn
agentOpenFlowSoftwareOnlyEntries = _AgentOpenFlowSoftwareOnlyEntries_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 7),
    _AgentOpenFlowSoftwareOnlyEntries_Type()
)
agentOpenFlowSoftwareOnlyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowSoftwareOnlyEntries.setStatus("current")
_AgentOpenFlowWaitingForSpaceEntries_Type = Unsigned32
_AgentOpenFlowWaitingForSpaceEntries_Object = MibTableColumn
agentOpenFlowWaitingForSpaceEntries = _AgentOpenFlowWaitingForSpaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 8),
    _AgentOpenFlowWaitingForSpaceEntries_Type()
)
agentOpenFlowWaitingForSpaceEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowWaitingForSpaceEntries.setStatus("current")
_AgentOpenFlowFlowInsertionCount_Type = Unsigned32
_AgentOpenFlowFlowInsertionCount_Object = MibTableColumn
agentOpenFlowFlowInsertionCount = _AgentOpenFlowFlowInsertionCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 9),
    _AgentOpenFlowFlowInsertionCount_Type()
)
agentOpenFlowFlowInsertionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowInsertionCount.setStatus("current")
_AgentOpenFlowFlowDeletionCount_Type = Unsigned32
_AgentOpenFlowFlowDeletionCount_Object = MibTableColumn
agentOpenFlowFlowDeletionCount = _AgentOpenFlowFlowDeletionCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 10),
    _AgentOpenFlowFlowDeletionCount_Type()
)
agentOpenFlowFlowDeletionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowDeletionCount.setStatus("current")
_AgentOpenFlowInsertionFailureCount_Type = Unsigned32
_AgentOpenFlowInsertionFailureCount_Object = MibTableColumn
agentOpenFlowInsertionFailureCount = _AgentOpenFlowInsertionFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 200, 1, 8, 1, 11),
    _AgentOpenFlowInsertionFailureCount_Type()
)
agentOpenFlowInsertionFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowInsertionFailureCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QUANTA-OPENFLOW-PRIVATE-MIB",
    **{"openFlow": openFlow,
       "agentOpenFlowGroup": agentOpenFlowGroup,
       "agentOpenFlowGlobalConfigGroup": agentOpenFlowGlobalConfigGroup,
       "agentOpenFlowAdminMode": agentOpenFlowAdminMode,
       "agentOpenFlowVariant": agentOpenFlowVariant,
       "agentOpenFlowCfgControllerTable": agentOpenFlowCfgControllerTable,
       "agentOpenFlowCfgControllerEntry": agentOpenFlowCfgControllerEntry,
       "agentOpenFlowCfgCtrlIPAddress": agentOpenFlowCfgCtrlIPAddress,
       "agentOpenFlowCfgCtrlIPPort": agentOpenFlowCfgCtrlIPPort,
       "agentOpenFlowCfgCtrlConnectionMode": agentOpenFlowCfgCtrlConnectionMode,
       "agentOpenFlowCfgCtrlStatus": agentOpenFlowCfgCtrlStatus,
       "agentOpenFlowGlobalStatusParameters": agentOpenFlowGlobalStatusParameters,
       "agentOpenFlowOperationalStatus": agentOpenFlowOperationalStatus,
       "agentOpenFlowDisableReason": agentOpenFlowDisableReason,
       "agentOpenFlowGlobalCommands": agentOpenFlowGlobalCommands,
       "agentOpenFlowEraseOpenFlowManagerCertificates": agentOpenFlowEraseOpenFlowManagerCertificates,
       "agentOpenFlowFlowTableStatusTable": agentOpenFlowFlowTableStatusTable,
       "agentOpenFlowFlowTableStatusEntry": agentOpenFlowFlowTableStatusEntry,
       "agentOpenFlowFlowTable": agentOpenFlowFlowTable,
       "agentOpenFlowFlowTableName": agentOpenFlowFlowTableName,
       "agentOpenFlowFlowTableDescription": agentOpenFlowFlowTableDescription,
       "agentOpenFlowMaximumSize": agentOpenFlowMaximumSize,
       "agentOpenFlowNumberOfEntries": agentOpenFlowNumberOfEntries,
       "agentOpenFlowHardwareEntries": agentOpenFlowHardwareEntries,
       "agentOpenFlowSoftwareOnlyEntries": agentOpenFlowSoftwareOnlyEntries,
       "agentOpenFlowWaitingForSpaceEntries": agentOpenFlowWaitingForSpaceEntries,
       "agentOpenFlowFlowInsertionCount": agentOpenFlowFlowInsertionCount,
       "agentOpenFlowFlowDeletionCount": agentOpenFlowFlowDeletionCount,
       "agentOpenFlowInsertionFailureCount": agentOpenFlowInsertionFailureCount}
)
