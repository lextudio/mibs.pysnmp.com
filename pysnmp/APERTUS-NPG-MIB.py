# SNMP MIB module (APERTUS-NPG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-NPG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:16 2024
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

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Apertus_ObjectIdentity = ObjectIdentity
apertus = _Apertus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543)
)
_Isg_ObjectIdentity = ObjectIdentity
isg = _Isg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3)
)
_Npg_ObjectIdentity = ObjectIdentity
npg = _Npg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 5)
)
_NpgMib_ObjectIdentity = ObjectIdentity
npgMib = _NpgMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1)
)
_NpgMibVersionNumber_Type = Integer32
_NpgMibVersionNumber_Object = MibScalar
npgMibVersionNumber = _NpgMibVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 1),
    _NpgMibVersionNumber_Type()
)
npgMibVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgMibVersionNumber.setStatus("mandatory")
_NpgVersionNumber_Type = DisplayString
_NpgVersionNumber_Object = MibScalar
npgVersionNumber = _NpgVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 2),
    _NpgVersionNumber_Type()
)
npgVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgVersionNumber.setStatus("mandatory")
_NpgSessionTable_Object = MibTable
npgSessionTable = _NpgSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    npgSessionTable.setStatus("mandatory")
_NpgSessionEntry_Object = MibTableRow
npgSessionEntry = _NpgSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1)
)
npgSessionEntry.setIndexNames(
    (0, "APERTUS-NPG-MIB", "npgSessionName"),
)
if mibBuilder.loadTexts:
    npgSessionEntry.setStatus("mandatory")
_NpgSessionName_Type = DisplayString
_NpgSessionName_Object = MibTableColumn
npgSessionName = _NpgSessionName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 1),
    _NpgSessionName_Type()
)
npgSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionName.setStatus("mandatory")
_NpgSessionCorrectState_Type = DisplayString
_NpgSessionCorrectState_Object = MibTableColumn
npgSessionCorrectState = _NpgSessionCorrectState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 2),
    _NpgSessionCorrectState_Type()
)
npgSessionCorrectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCorrectState.setStatus("mandatory")
_NpgSessionCurrentState_Type = DisplayString
_NpgSessionCurrentState_Object = MibTableColumn
npgSessionCurrentState = _NpgSessionCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 3),
    _NpgSessionCurrentState_Type()
)
npgSessionCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCurrentState.setStatus("mandatory")
_NpgSessionWhenLastUp_Type = DisplayString
_NpgSessionWhenLastUp_Object = MibTableColumn
npgSessionWhenLastUp = _NpgSessionWhenLastUp_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 4),
    _NpgSessionWhenLastUp_Type()
)
npgSessionWhenLastUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionWhenLastUp.setStatus("mandatory")
_NpgSessionWhenLastDown_Type = DisplayString
_NpgSessionWhenLastDown_Object = MibTableColumn
npgSessionWhenLastDown = _NpgSessionWhenLastDown_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 5),
    _NpgSessionWhenLastDown_Type()
)
npgSessionWhenLastDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionWhenLastDown.setStatus("mandatory")
_NpgSessionLastErrorCode_Type = Integer32
_NpgSessionLastErrorCode_Object = MibTableColumn
npgSessionLastErrorCode = _NpgSessionLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 6),
    _NpgSessionLastErrorCode_Type()
)
npgSessionLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionLastErrorCode.setStatus("mandatory")
_NpgSessionLastErrorMessage_Type = DisplayString
_NpgSessionLastErrorMessage_Object = MibTableColumn
npgSessionLastErrorMessage = _NpgSessionLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 7),
    _NpgSessionLastErrorMessage_Type()
)
npgSessionLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionLastErrorMessage.setStatus("mandatory")
_NpgSessionTimeOfNextRetry_Type = DisplayString
_NpgSessionTimeOfNextRetry_Object = MibTableColumn
npgSessionTimeOfNextRetry = _NpgSessionTimeOfNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 8),
    _NpgSessionTimeOfNextRetry_Type()
)
npgSessionTimeOfNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionTimeOfNextRetry.setStatus("mandatory")
_NpgSessionCurrentRetryValue_Type = Integer32
_NpgSessionCurrentRetryValue_Object = MibTableColumn
npgSessionCurrentRetryValue = _NpgSessionCurrentRetryValue_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 9),
    _NpgSessionCurrentRetryValue_Type()
)
npgSessionCurrentRetryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCurrentRetryValue.setStatus("mandatory")
_NpgSessionRetryCount_Type = Integer32
_NpgSessionRetryCount_Object = MibTableColumn
npgSessionRetryCount = _NpgSessionRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 10),
    _NpgSessionRetryCount_Type()
)
npgSessionRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionRetryCount.setStatus("mandatory")
_NpgSessionTimeOfActiveReset_Type = DisplayString
_NpgSessionTimeOfActiveReset_Object = MibTableColumn
npgSessionTimeOfActiveReset = _NpgSessionTimeOfActiveReset_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 11),
    _NpgSessionTimeOfActiveReset_Type()
)
npgSessionTimeOfActiveReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionTimeOfActiveReset.setStatus("mandatory")
_NpgSessionActiveStatsProcessingTime_Type = Integer32
_NpgSessionActiveStatsProcessingTime_Object = MibTableColumn
npgSessionActiveStatsProcessingTime = _NpgSessionActiveStatsProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 12),
    _NpgSessionActiveStatsProcessingTime_Type()
)
npgSessionActiveStatsProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionActiveStatsProcessingTime.setStatus("mandatory")
_NpgSessionActiveStatsBytesPrinted_Type = Integer32
_NpgSessionActiveStatsBytesPrinted_Object = MibTableColumn
npgSessionActiveStatsBytesPrinted = _NpgSessionActiveStatsBytesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 13),
    _NpgSessionActiveStatsBytesPrinted_Type()
)
npgSessionActiveStatsBytesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionActiveStatsBytesPrinted.setStatus("mandatory")
_NpgSessionActiveStatsLinesPrinted_Type = Integer32
_NpgSessionActiveStatsLinesPrinted_Object = MibTableColumn
npgSessionActiveStatsLinesPrinted = _NpgSessionActiveStatsLinesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 14),
    _NpgSessionActiveStatsLinesPrinted_Type()
)
npgSessionActiveStatsLinesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionActiveStatsLinesPrinted.setStatus("mandatory")
_NpgSessionActiveStatsPagesPrinted_Type = Integer32
_NpgSessionActiveStatsPagesPrinted_Object = MibTableColumn
npgSessionActiveStatsPagesPrinted = _NpgSessionActiveStatsPagesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 15),
    _NpgSessionActiveStatsPagesPrinted_Type()
)
npgSessionActiveStatsPagesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionActiveStatsPagesPrinted.setStatus("mandatory")
_NpgSessionActiveStatsJobsPrinted_Type = Integer32
_NpgSessionActiveStatsJobsPrinted_Object = MibTableColumn
npgSessionActiveStatsJobsPrinted = _NpgSessionActiveStatsJobsPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 16),
    _NpgSessionActiveStatsJobsPrinted_Type()
)
npgSessionActiveStatsJobsPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionActiveStatsJobsPrinted.setStatus("mandatory")
_NpgSessionCumulativeStatsProcessingTime_Type = Integer32
_NpgSessionCumulativeStatsProcessingTime_Object = MibTableColumn
npgSessionCumulativeStatsProcessingTime = _NpgSessionCumulativeStatsProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 17),
    _NpgSessionCumulativeStatsProcessingTime_Type()
)
npgSessionCumulativeStatsProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCumulativeStatsProcessingTime.setStatus("mandatory")
_NpgSessionCumulativeStatsBytesPrinted_Type = Integer32
_NpgSessionCumulativeStatsBytesPrinted_Object = MibTableColumn
npgSessionCumulativeStatsBytesPrinted = _NpgSessionCumulativeStatsBytesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 18),
    _NpgSessionCumulativeStatsBytesPrinted_Type()
)
npgSessionCumulativeStatsBytesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCumulativeStatsBytesPrinted.setStatus("mandatory")
_NpgSessionCumulativeStatsLinesPrinted_Type = Integer32
_NpgSessionCumulativeStatsLinesPrinted_Object = MibTableColumn
npgSessionCumulativeStatsLinesPrinted = _NpgSessionCumulativeStatsLinesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 19),
    _NpgSessionCumulativeStatsLinesPrinted_Type()
)
npgSessionCumulativeStatsLinesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCumulativeStatsLinesPrinted.setStatus("mandatory")
_NpgSessionCumulativeStatsPagesPrinted_Type = Integer32
_NpgSessionCumulativeStatsPagesPrinted_Object = MibTableColumn
npgSessionCumulativeStatsPagesPrinted = _NpgSessionCumulativeStatsPagesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 20),
    _NpgSessionCumulativeStatsPagesPrinted_Type()
)
npgSessionCumulativeStatsPagesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCumulativeStatsPagesPrinted.setStatus("mandatory")
_NpgSessionCumulativeStatsJobsPrinted_Type = Integer32
_NpgSessionCumulativeStatsJobsPrinted_Object = MibTableColumn
npgSessionCumulativeStatsJobsPrinted = _NpgSessionCumulativeStatsJobsPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 21),
    _NpgSessionCumulativeStatsJobsPrinted_Type()
)
npgSessionCumulativeStatsJobsPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionCumulativeStatsJobsPrinted.setStatus("mandatory")
_NpgSessionConfigTn3270eServer_Type = DisplayString
_NpgSessionConfigTn3270eServer_Object = MibTableColumn
npgSessionConfigTn3270eServer = _NpgSessionConfigTn3270eServer_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 22),
    _NpgSessionConfigTn3270eServer_Type()
)
npgSessionConfigTn3270eServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionConfigTn3270eServer.setStatus("mandatory")
_NpgSessionConfigPort_Type = Integer32
_NpgSessionConfigPort_Object = MibTableColumn
npgSessionConfigPort = _NpgSessionConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 23),
    _NpgSessionConfigPort_Type()
)
npgSessionConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionConfigPort.setStatus("mandatory")
_NpgSessionConfigPrinterName_Type = DisplayString
_NpgSessionConfigPrinterName_Object = MibTableColumn
npgSessionConfigPrinterName = _NpgSessionConfigPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 3, 1, 24),
    _NpgSessionConfigPrinterName_Type()
)
npgSessionConfigPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgSessionConfigPrinterName.setStatus("mandatory")
_NpgDestinationTable_Object = MibTable
npgDestinationTable = _NpgDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    npgDestinationTable.setStatus("mandatory")
_NpgDestinationEntry_Object = MibTableRow
npgDestinationEntry = _NpgDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1)
)
npgDestinationEntry.setIndexNames(
    (0, "APERTUS-NPG-MIB", "npgDestinationName"),
)
if mibBuilder.loadTexts:
    npgDestinationEntry.setStatus("mandatory")
_NpgDestinationName_Type = DisplayString
_NpgDestinationName_Object = MibTableColumn
npgDestinationName = _NpgDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 1),
    _NpgDestinationName_Type()
)
npgDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationName.setStatus("mandatory")
_NpgDestinationTimeOfActiveReset_Type = DisplayString
_NpgDestinationTimeOfActiveReset_Object = MibTableColumn
npgDestinationTimeOfActiveReset = _NpgDestinationTimeOfActiveReset_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 2),
    _NpgDestinationTimeOfActiveReset_Type()
)
npgDestinationTimeOfActiveReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationTimeOfActiveReset.setStatus("mandatory")
_NpgDestinationActiveStatsProcessingTime_Type = Integer32
_NpgDestinationActiveStatsProcessingTime_Object = MibTableColumn
npgDestinationActiveStatsProcessingTime = _NpgDestinationActiveStatsProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 3),
    _NpgDestinationActiveStatsProcessingTime_Type()
)
npgDestinationActiveStatsProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationActiveStatsProcessingTime.setStatus("mandatory")
_NpgDestinationActiveStatsBytesPrinted_Type = Integer32
_NpgDestinationActiveStatsBytesPrinted_Object = MibTableColumn
npgDestinationActiveStatsBytesPrinted = _NpgDestinationActiveStatsBytesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 4),
    _NpgDestinationActiveStatsBytesPrinted_Type()
)
npgDestinationActiveStatsBytesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationActiveStatsBytesPrinted.setStatus("mandatory")
_NpgDestinationActiveStatsLinesPrinted_Type = Integer32
_NpgDestinationActiveStatsLinesPrinted_Object = MibTableColumn
npgDestinationActiveStatsLinesPrinted = _NpgDestinationActiveStatsLinesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 5),
    _NpgDestinationActiveStatsLinesPrinted_Type()
)
npgDestinationActiveStatsLinesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationActiveStatsLinesPrinted.setStatus("mandatory")
_NpgDestinationActiveStatsPagesPrinted_Type = Integer32
_NpgDestinationActiveStatsPagesPrinted_Object = MibTableColumn
npgDestinationActiveStatsPagesPrinted = _NpgDestinationActiveStatsPagesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 6),
    _NpgDestinationActiveStatsPagesPrinted_Type()
)
npgDestinationActiveStatsPagesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationActiveStatsPagesPrinted.setStatus("mandatory")
_NpgDestinationActiveStatsJobsPrinted_Type = Integer32
_NpgDestinationActiveStatsJobsPrinted_Object = MibTableColumn
npgDestinationActiveStatsJobsPrinted = _NpgDestinationActiveStatsJobsPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 7),
    _NpgDestinationActiveStatsJobsPrinted_Type()
)
npgDestinationActiveStatsJobsPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationActiveStatsJobsPrinted.setStatus("mandatory")
_NpgDestinationCumulativeStatsProcessingTime_Type = Integer32
_NpgDestinationCumulativeStatsProcessingTime_Object = MibTableColumn
npgDestinationCumulativeStatsProcessingTime = _NpgDestinationCumulativeStatsProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 8),
    _NpgDestinationCumulativeStatsProcessingTime_Type()
)
npgDestinationCumulativeStatsProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationCumulativeStatsProcessingTime.setStatus("mandatory")
_NpgDestinationCumulativeStatsBytesPrinted_Type = Integer32
_NpgDestinationCumulativeStatsBytesPrinted_Object = MibTableColumn
npgDestinationCumulativeStatsBytesPrinted = _NpgDestinationCumulativeStatsBytesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 9),
    _NpgDestinationCumulativeStatsBytesPrinted_Type()
)
npgDestinationCumulativeStatsBytesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationCumulativeStatsBytesPrinted.setStatus("mandatory")
_NpgDestinationCumulativeStatsLinesPrinted_Type = Integer32
_NpgDestinationCumulativeStatsLinesPrinted_Object = MibTableColumn
npgDestinationCumulativeStatsLinesPrinted = _NpgDestinationCumulativeStatsLinesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 10),
    _NpgDestinationCumulativeStatsLinesPrinted_Type()
)
npgDestinationCumulativeStatsLinesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationCumulativeStatsLinesPrinted.setStatus("mandatory")
_NpgDestinationCumulativeStatsPagesPrinted_Type = Integer32
_NpgDestinationCumulativeStatsPagesPrinted_Object = MibTableColumn
npgDestinationCumulativeStatsPagesPrinted = _NpgDestinationCumulativeStatsPagesPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 11),
    _NpgDestinationCumulativeStatsPagesPrinted_Type()
)
npgDestinationCumulativeStatsPagesPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationCumulativeStatsPagesPrinted.setStatus("mandatory")
_NpgDestinationCumulativeStatsJobsPrinted_Type = Integer32
_NpgDestinationCumulativeStatsJobsPrinted_Object = MibTableColumn
npgDestinationCumulativeStatsJobsPrinted = _NpgDestinationCumulativeStatsJobsPrinted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 12),
    _NpgDestinationCumulativeStatsJobsPrinted_Type()
)
npgDestinationCumulativeStatsJobsPrinted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationCumulativeStatsJobsPrinted.setStatus("mandatory")
_NpgDestinationConfigType_Type = DisplayString
_NpgDestinationConfigType_Object = MibTableColumn
npgDestinationConfigType = _NpgDestinationConfigType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 13),
    _NpgDestinationConfigType_Type()
)
npgDestinationConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationConfigType.setStatus("mandatory")
_NpgDestinationConfigProfileName_Type = DisplayString
_NpgDestinationConfigProfileName_Object = MibTableColumn
npgDestinationConfigProfileName = _NpgDestinationConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 5, 1, 4, 1, 14),
    _NpgDestinationConfigProfileName_Type()
)
npgDestinationConfigProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npgDestinationConfigProfileName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-NPG-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "npg": npg,
       "npgMib": npgMib,
       "npgMibVersionNumber": npgMibVersionNumber,
       "npgVersionNumber": npgVersionNumber,
       "npgSessionTable": npgSessionTable,
       "npgSessionEntry": npgSessionEntry,
       "npgSessionName": npgSessionName,
       "npgSessionCorrectState": npgSessionCorrectState,
       "npgSessionCurrentState": npgSessionCurrentState,
       "npgSessionWhenLastUp": npgSessionWhenLastUp,
       "npgSessionWhenLastDown": npgSessionWhenLastDown,
       "npgSessionLastErrorCode": npgSessionLastErrorCode,
       "npgSessionLastErrorMessage": npgSessionLastErrorMessage,
       "npgSessionTimeOfNextRetry": npgSessionTimeOfNextRetry,
       "npgSessionCurrentRetryValue": npgSessionCurrentRetryValue,
       "npgSessionRetryCount": npgSessionRetryCount,
       "npgSessionTimeOfActiveReset": npgSessionTimeOfActiveReset,
       "npgSessionActiveStatsProcessingTime": npgSessionActiveStatsProcessingTime,
       "npgSessionActiveStatsBytesPrinted": npgSessionActiveStatsBytesPrinted,
       "npgSessionActiveStatsLinesPrinted": npgSessionActiveStatsLinesPrinted,
       "npgSessionActiveStatsPagesPrinted": npgSessionActiveStatsPagesPrinted,
       "npgSessionActiveStatsJobsPrinted": npgSessionActiveStatsJobsPrinted,
       "npgSessionCumulativeStatsProcessingTime": npgSessionCumulativeStatsProcessingTime,
       "npgSessionCumulativeStatsBytesPrinted": npgSessionCumulativeStatsBytesPrinted,
       "npgSessionCumulativeStatsLinesPrinted": npgSessionCumulativeStatsLinesPrinted,
       "npgSessionCumulativeStatsPagesPrinted": npgSessionCumulativeStatsPagesPrinted,
       "npgSessionCumulativeStatsJobsPrinted": npgSessionCumulativeStatsJobsPrinted,
       "npgSessionConfigTn3270eServer": npgSessionConfigTn3270eServer,
       "npgSessionConfigPort": npgSessionConfigPort,
       "npgSessionConfigPrinterName": npgSessionConfigPrinterName,
       "npgDestinationTable": npgDestinationTable,
       "npgDestinationEntry": npgDestinationEntry,
       "npgDestinationName": npgDestinationName,
       "npgDestinationTimeOfActiveReset": npgDestinationTimeOfActiveReset,
       "npgDestinationActiveStatsProcessingTime": npgDestinationActiveStatsProcessingTime,
       "npgDestinationActiveStatsBytesPrinted": npgDestinationActiveStatsBytesPrinted,
       "npgDestinationActiveStatsLinesPrinted": npgDestinationActiveStatsLinesPrinted,
       "npgDestinationActiveStatsPagesPrinted": npgDestinationActiveStatsPagesPrinted,
       "npgDestinationActiveStatsJobsPrinted": npgDestinationActiveStatsJobsPrinted,
       "npgDestinationCumulativeStatsProcessingTime": npgDestinationCumulativeStatsProcessingTime,
       "npgDestinationCumulativeStatsBytesPrinted": npgDestinationCumulativeStatsBytesPrinted,
       "npgDestinationCumulativeStatsLinesPrinted": npgDestinationCumulativeStatsLinesPrinted,
       "npgDestinationCumulativeStatsPagesPrinted": npgDestinationCumulativeStatsPagesPrinted,
       "npgDestinationCumulativeStatsJobsPrinted": npgDestinationCumulativeStatsJobsPrinted,
       "npgDestinationConfigType": npgDestinationConfigType,
       "npgDestinationConfigProfileName": npgDestinationConfigProfileName}
)
