# SNMP MIB module (Nortel-Magellan-Passport-AtmUniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmUniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:23 2024
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

(atmIf,
 atmIfIndex,
 atmIfVpt,
 atmIfVptIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-AtmCoreMIB",
    "atmIf",
    "atmIfIndex",
    "atmIfVpt",
    "atmIfVptIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 Hex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "Hex",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmIfUni_ObjectIdentity = ObjectIdentity
atmIfUni = _AtmIfUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6)
)
_AtmIfUniRowStatusTable_Object = MibTable
atmIfUniRowStatusTable = _AtmIfUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1)
)
if mibBuilder.loadTexts:
    atmIfUniRowStatusTable.setStatus("mandatory")
_AtmIfUniRowStatusEntry_Object = MibTableRow
atmIfUniRowStatusEntry = _AtmIfUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1, 1)
)
atmIfUniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniRowStatusEntry.setStatus("mandatory")
_AtmIfUniRowStatus_Type = RowStatus
_AtmIfUniRowStatus_Object = MibTableColumn
atmIfUniRowStatus = _AtmIfUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1, 1, 1),
    _AtmIfUniRowStatus_Type()
)
atmIfUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniRowStatus.setStatus("mandatory")
_AtmIfUniComponentName_Type = DisplayString
_AtmIfUniComponentName_Object = MibTableColumn
atmIfUniComponentName = _AtmIfUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1, 1, 2),
    _AtmIfUniComponentName_Type()
)
atmIfUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniComponentName.setStatus("mandatory")
_AtmIfUniStorageType_Type = StorageType
_AtmIfUniStorageType_Object = MibTableColumn
atmIfUniStorageType = _AtmIfUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1, 1, 4),
    _AtmIfUniStorageType_Type()
)
atmIfUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniStorageType.setStatus("mandatory")
_AtmIfUniIndex_Type = NonReplicated
_AtmIfUniIndex_Object = MibTableColumn
atmIfUniIndex = _AtmIfUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 1, 1, 10),
    _AtmIfUniIndex_Type()
)
atmIfUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniIndex.setStatus("mandatory")
_AtmIfUniIlmi_ObjectIdentity = ObjectIdentity
atmIfUniIlmi = _AtmIfUniIlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2)
)
_AtmIfUniIlmiRowStatusTable_Object = MibTable
atmIfUniIlmiRowStatusTable = _AtmIfUniIlmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiRowStatusTable.setStatus("mandatory")
_AtmIfUniIlmiRowStatusEntry_Object = MibTableRow
atmIfUniIlmiRowStatusEntry = _AtmIfUniIlmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1, 1)
)
atmIfUniIlmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiRowStatusEntry.setStatus("mandatory")
_AtmIfUniIlmiRowStatus_Type = RowStatus
_AtmIfUniIlmiRowStatus_Object = MibTableColumn
atmIfUniIlmiRowStatus = _AtmIfUniIlmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1, 1, 1),
    _AtmIfUniIlmiRowStatus_Type()
)
atmIfUniIlmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiRowStatus.setStatus("mandatory")
_AtmIfUniIlmiComponentName_Type = DisplayString
_AtmIfUniIlmiComponentName_Object = MibTableColumn
atmIfUniIlmiComponentName = _AtmIfUniIlmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1, 1, 2),
    _AtmIfUniIlmiComponentName_Type()
)
atmIfUniIlmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiComponentName.setStatus("mandatory")
_AtmIfUniIlmiStorageType_Type = StorageType
_AtmIfUniIlmiStorageType_Object = MibTableColumn
atmIfUniIlmiStorageType = _AtmIfUniIlmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1, 1, 4),
    _AtmIfUniIlmiStorageType_Type()
)
atmIfUniIlmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiStorageType.setStatus("mandatory")
_AtmIfUniIlmiIndex_Type = NonReplicated
_AtmIfUniIlmiIndex_Object = MibTableColumn
atmIfUniIlmiIndex = _AtmIfUniIlmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 1, 1, 10),
    _AtmIfUniIlmiIndex_Type()
)
atmIfUniIlmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniIlmiIndex.setStatus("mandatory")
_AtmIfUniIlmiStateTable_Object = MibTable
atmIfUniIlmiStateTable = _AtmIfUniIlmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiStateTable.setStatus("mandatory")
_AtmIfUniIlmiStateEntry_Object = MibTableRow
atmIfUniIlmiStateEntry = _AtmIfUniIlmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 10, 1)
)
atmIfUniIlmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiStateEntry.setStatus("mandatory")


class _AtmIfUniIlmiAdminState_Type(Integer32):
    """Custom type atmIfUniIlmiAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_AtmIfUniIlmiAdminState_Type.__name__ = "Integer32"
_AtmIfUniIlmiAdminState_Object = MibTableColumn
atmIfUniIlmiAdminState = _AtmIfUniIlmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 10, 1, 1),
    _AtmIfUniIlmiAdminState_Type()
)
atmIfUniIlmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiAdminState.setStatus("mandatory")


class _AtmIfUniIlmiOperationalState_Type(Integer32):
    """Custom type atmIfUniIlmiOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfUniIlmiOperationalState_Type.__name__ = "Integer32"
_AtmIfUniIlmiOperationalState_Object = MibTableColumn
atmIfUniIlmiOperationalState = _AtmIfUniIlmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 10, 1, 2),
    _AtmIfUniIlmiOperationalState_Type()
)
atmIfUniIlmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiOperationalState.setStatus("mandatory")


class _AtmIfUniIlmiUsageState_Type(Integer32):
    """Custom type atmIfUniIlmiUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_AtmIfUniIlmiUsageState_Type.__name__ = "Integer32"
_AtmIfUniIlmiUsageState_Object = MibTableColumn
atmIfUniIlmiUsageState = _AtmIfUniIlmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 10, 1, 3),
    _AtmIfUniIlmiUsageState_Type()
)
atmIfUniIlmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiUsageState.setStatus("mandatory")
_AtmIfUniIlmiProvTable_Object = MibTable
atmIfUniIlmiProvTable = _AtmIfUniIlmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 11)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiProvTable.setStatus("mandatory")
_AtmIfUniIlmiProvEntry_Object = MibTableRow
atmIfUniIlmiProvEntry = _AtmIfUniIlmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 11, 1)
)
atmIfUniIlmiProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiProvEntry.setStatus("mandatory")


class _AtmIfUniIlmiVci_Type(Unsigned32):
    """Custom type atmIfUniIlmiVci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfUniIlmiVci_Type.__name__ = "Unsigned32"
_AtmIfUniIlmiVci_Object = MibTableColumn
atmIfUniIlmiVci = _AtmIfUniIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 11, 1, 1),
    _AtmIfUniIlmiVci_Type()
)
atmIfUniIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniIlmiVci.setStatus("mandatory")


class _AtmIfUniIlmiOperatingMode_Type(Integer32):
    """Custom type atmIfUniIlmiOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addressRegDisabled", 1),
          ("addressRegEnabled", 0),
          ("ilmiDisabled", 2))
    )


_AtmIfUniIlmiOperatingMode_Type.__name__ = "Integer32"
_AtmIfUniIlmiOperatingMode_Object = MibTableColumn
atmIfUniIlmiOperatingMode = _AtmIfUniIlmiOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 11, 1, 2),
    _AtmIfUniIlmiOperatingMode_Type()
)
atmIfUniIlmiOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniIlmiOperatingMode.setStatus("mandatory")
_AtmIfUniIlmiStatsTable_Object = MibTable
atmIfUniIlmiStatsTable = _AtmIfUniIlmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 12)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiStatsTable.setStatus("mandatory")
_AtmIfUniIlmiStatsEntry_Object = MibTableRow
atmIfUniIlmiStatsEntry = _AtmIfUniIlmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 12, 1)
)
atmIfUniIlmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiStatsEntry.setStatus("mandatory")
_AtmIfUniIlmiTxPdus_Type = Counter32
_AtmIfUniIlmiTxPdus_Object = MibTableColumn
atmIfUniIlmiTxPdus = _AtmIfUniIlmiTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 12, 1, 1),
    _AtmIfUniIlmiTxPdus_Type()
)
atmIfUniIlmiTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiTxPdus.setStatus("mandatory")
_AtmIfUniIlmiRxPdus_Type = Counter32
_AtmIfUniIlmiRxPdus_Object = MibTableColumn
atmIfUniIlmiRxPdus = _AtmIfUniIlmiRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 12, 1, 2),
    _AtmIfUniIlmiRxPdus_Type()
)
atmIfUniIlmiRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiRxPdus.setStatus("mandatory")
_AtmIfUniIlmiRxBadPdusDiscarded_Type = Counter32
_AtmIfUniIlmiRxBadPdusDiscarded_Object = MibTableColumn
atmIfUniIlmiRxBadPdusDiscarded = _AtmIfUniIlmiRxBadPdusDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 12, 1, 3),
    _AtmIfUniIlmiRxBadPdusDiscarded_Type()
)
atmIfUniIlmiRxBadPdusDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiRxBadPdusDiscarded.setStatus("mandatory")
_AtmIfUniIlmiPrefixToRegisterTable_Object = MibTable
atmIfUniIlmiPrefixToRegisterTable = _AtmIfUniIlmiPrefixToRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 287)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiPrefixToRegisterTable.setStatus("mandatory")
_AtmIfUniIlmiPrefixToRegisterEntry_Object = MibTableRow
atmIfUniIlmiPrefixToRegisterEntry = _AtmIfUniIlmiPrefixToRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 287, 1)
)
atmIfUniIlmiPrefixToRegisterEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiPrefixToRegisterValue"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiPrefixToRegisterEntry.setStatus("mandatory")


class _AtmIfUniIlmiPrefixToRegisterValue_Type(AsciiString):
    """Custom type atmIfUniIlmiPrefixToRegisterValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_AtmIfUniIlmiPrefixToRegisterValue_Type.__name__ = "AsciiString"
_AtmIfUniIlmiPrefixToRegisterValue_Object = MibTableColumn
atmIfUniIlmiPrefixToRegisterValue = _AtmIfUniIlmiPrefixToRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 287, 1, 1),
    _AtmIfUniIlmiPrefixToRegisterValue_Type()
)
atmIfUniIlmiPrefixToRegisterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniIlmiPrefixToRegisterValue.setStatus("mandatory")
_AtmIfUniIlmiPrefixToRegisterRowStatus_Type = RowStatus
_AtmIfUniIlmiPrefixToRegisterRowStatus_Object = MibTableColumn
atmIfUniIlmiPrefixToRegisterRowStatus = _AtmIfUniIlmiPrefixToRegisterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 287, 1, 2),
    _AtmIfUniIlmiPrefixToRegisterRowStatus_Type()
)
atmIfUniIlmiPrefixToRegisterRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiPrefixToRegisterRowStatus.setStatus("mandatory")
_AtmIfUniIlmiEsiToRegisterTable_Object = MibTable
atmIfUniIlmiEsiToRegisterTable = _AtmIfUniIlmiEsiToRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 288)
)
if mibBuilder.loadTexts:
    atmIfUniIlmiEsiToRegisterTable.setStatus("mandatory")
_AtmIfUniIlmiEsiToRegisterEntry_Object = MibTableRow
atmIfUniIlmiEsiToRegisterEntry = _AtmIfUniIlmiEsiToRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 288, 1)
)
atmIfUniIlmiEsiToRegisterEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIlmiEsiToRegisterValue"),
)
if mibBuilder.loadTexts:
    atmIfUniIlmiEsiToRegisterEntry.setStatus("mandatory")


class _AtmIfUniIlmiEsiToRegisterValue_Type(AsciiString):
    """Custom type atmIfUniIlmiEsiToRegisterValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_AtmIfUniIlmiEsiToRegisterValue_Type.__name__ = "AsciiString"
_AtmIfUniIlmiEsiToRegisterValue_Object = MibTableColumn
atmIfUniIlmiEsiToRegisterValue = _AtmIfUniIlmiEsiToRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 288, 1, 1),
    _AtmIfUniIlmiEsiToRegisterValue_Type()
)
atmIfUniIlmiEsiToRegisterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniIlmiEsiToRegisterValue.setStatus("mandatory")
_AtmIfUniIlmiEsiToRegisterRowStatus_Type = RowStatus
_AtmIfUniIlmiEsiToRegisterRowStatus_Object = MibTableColumn
atmIfUniIlmiEsiToRegisterRowStatus = _AtmIfUniIlmiEsiToRegisterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 2, 288, 1, 2),
    _AtmIfUniIlmiEsiToRegisterRowStatus_Type()
)
atmIfUniIlmiEsiToRegisterRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmIfUniIlmiEsiToRegisterRowStatus.setStatus("mandatory")
_AtmIfUniSig_ObjectIdentity = ObjectIdentity
atmIfUniSig = _AtmIfUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3)
)
_AtmIfUniSigRowStatusTable_Object = MibTable
atmIfUniSigRowStatusTable = _AtmIfUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfUniSigRowStatusTable.setStatus("mandatory")
_AtmIfUniSigRowStatusEntry_Object = MibTableRow
atmIfUniSigRowStatusEntry = _AtmIfUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1, 1)
)
atmIfUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigRowStatusEntry.setStatus("mandatory")
_AtmIfUniSigRowStatus_Type = RowStatus
_AtmIfUniSigRowStatus_Object = MibTableColumn
atmIfUniSigRowStatus = _AtmIfUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1, 1, 1),
    _AtmIfUniSigRowStatus_Type()
)
atmIfUniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigRowStatus.setStatus("mandatory")
_AtmIfUniSigComponentName_Type = DisplayString
_AtmIfUniSigComponentName_Object = MibTableColumn
atmIfUniSigComponentName = _AtmIfUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1, 1, 2),
    _AtmIfUniSigComponentName_Type()
)
atmIfUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigComponentName.setStatus("mandatory")
_AtmIfUniSigStorageType_Type = StorageType
_AtmIfUniSigStorageType_Object = MibTableColumn
atmIfUniSigStorageType = _AtmIfUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1, 1, 4),
    _AtmIfUniSigStorageType_Type()
)
atmIfUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigStorageType.setStatus("mandatory")
_AtmIfUniSigIndex_Type = NonReplicated
_AtmIfUniSigIndex_Object = MibTableColumn
atmIfUniSigIndex = _AtmIfUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 1, 1, 10),
    _AtmIfUniSigIndex_Type()
)
atmIfUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniSigIndex.setStatus("mandatory")
_AtmIfUniSigVcd_ObjectIdentity = ObjectIdentity
atmIfUniSigVcd = _AtmIfUniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2)
)
_AtmIfUniSigVcdRowStatusTable_Object = MibTable
atmIfUniSigVcdRowStatusTable = _AtmIfUniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfUniSigVcdRowStatusEntry_Object = MibTableRow
atmIfUniSigVcdRowStatusEntry = _AtmIfUniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1, 1)
)
atmIfUniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfUniSigVcdRowStatus_Type = RowStatus
_AtmIfUniSigVcdRowStatus_Object = MibTableColumn
atmIfUniSigVcdRowStatus = _AtmIfUniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1, 1, 1),
    _AtmIfUniSigVcdRowStatus_Type()
)
atmIfUniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdRowStatus.setStatus("mandatory")
_AtmIfUniSigVcdComponentName_Type = DisplayString
_AtmIfUniSigVcdComponentName_Object = MibTableColumn
atmIfUniSigVcdComponentName = _AtmIfUniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1, 1, 2),
    _AtmIfUniSigVcdComponentName_Type()
)
atmIfUniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigVcdComponentName.setStatus("mandatory")
_AtmIfUniSigVcdStorageType_Type = StorageType
_AtmIfUniSigVcdStorageType_Object = MibTableColumn
atmIfUniSigVcdStorageType = _AtmIfUniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1, 1, 4),
    _AtmIfUniSigVcdStorageType_Type()
)
atmIfUniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigVcdStorageType.setStatus("mandatory")
_AtmIfUniSigVcdIndex_Type = NonReplicated
_AtmIfUniSigVcdIndex_Object = MibTableColumn
atmIfUniSigVcdIndex = _AtmIfUniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 1, 1, 10),
    _AtmIfUniSigVcdIndex_Type()
)
atmIfUniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniSigVcdIndex.setStatus("mandatory")
_AtmIfUniSigVcdProvTable_Object = MibTable
atmIfUniSigVcdProvTable = _AtmIfUniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdProvTable.setStatus("mandatory")
_AtmIfUniSigVcdProvEntry_Object = MibTableRow
atmIfUniSigVcdProvEntry = _AtmIfUniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1)
)
atmIfUniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdProvEntry.setStatus("mandatory")


class _AtmIfUniSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfUniSigVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_AtmIfUniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfUniSigVcdTrafficDescType_Object = MibTableColumn
atmIfUniSigVcdTrafficDescType = _AtmIfUniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 1),
    _AtmIfUniSigVcdTrafficDescType_Type()
)
atmIfUniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfUniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfUniSigVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_AtmIfUniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfUniSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfUniSigVcdAtmServiceCategory = _AtmIfUniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 3),
    _AtmIfUniSigVcdAtmServiceCategory_Type()
)
atmIfUniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfUniSigVcdQosClass_Type(Integer32):
    """Custom type atmIfUniSigVcdQosClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4))
    )


_AtmIfUniSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfUniSigVcdQosClass_Object = MibTableColumn
atmIfUniSigVcdQosClass = _AtmIfUniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 21),
    _AtmIfUniSigVcdQosClass_Type()
)
atmIfUniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdQosClass.setStatus("mandatory")


class _AtmIfUniSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfUniSigVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_AtmIfUniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfUniSigVcdTrafficShaping_Object = MibTableColumn
atmIfUniSigVcdTrafficShaping = _AtmIfUniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 50),
    _AtmIfUniSigVcdTrafficShaping_Type()
)
atmIfUniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfUniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfUniSigVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_AtmIfUniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfUniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfUniSigVcdUnshapedTransmitQueueing = _AtmIfUniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 60),
    _AtmIfUniSigVcdUnshapedTransmitQueueing_Type()
)
atmIfUniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfUniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfUniSigVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_AtmIfUniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfUniSigVcdUsageParameterControl_Object = MibTableColumn
atmIfUniSigVcdUsageParameterControl = _AtmIfUniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 10, 1, 70),
    _AtmIfUniSigVcdUsageParameterControl_Type()
)
atmIfUniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfUniSigVcdTdpTable_Object = MibTable
atmIfUniSigVcdTdpTable = _AtmIfUniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdTdpTable.setStatus("mandatory")
_AtmIfUniSigVcdTdpEntry_Object = MibTableRow
atmIfUniSigVcdTdpEntry = _AtmIfUniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 387, 1)
)
atmIfUniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfUniSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfUniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfUniSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfUniSigVcdTdpIndex_Object = MibTableColumn
atmIfUniSigVcdTdpIndex = _AtmIfUniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 387, 1, 1),
    _AtmIfUniSigVcdTdpIndex_Type()
)
atmIfUniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfUniSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfUniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfUniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfUniSigVcdTdpValue_Object = MibTableColumn
atmIfUniSigVcdTdpValue = _AtmIfUniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 2, 387, 1, 2),
    _AtmIfUniSigVcdTdpValue_Type()
)
atmIfUniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVcdTdpValue.setStatus("mandatory")
_AtmIfUniSigProvTable_Object = MibTable
atmIfUniSigProvTable = _AtmIfUniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfUniSigProvTable.setStatus("mandatory")
_AtmIfUniSigProvEntry_Object = MibTableRow
atmIfUniSigProvEntry = _AtmIfUniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 10, 1)
)
atmIfUniSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigProvEntry.setStatus("mandatory")


class _AtmIfUniSigVci_Type(Unsigned32):
    """Custom type atmIfUniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfUniSigVci_Type.__name__ = "Unsigned32"
_AtmIfUniSigVci_Object = MibTableColumn
atmIfUniSigVci = _AtmIfUniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 10, 1, 1),
    _AtmIfUniSigVci_Type()
)
atmIfUniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigVci.setStatus("mandatory")


class _AtmIfUniSigAddressConversion_Type(Integer32):
    """Custom type atmIfUniSigAddressConversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nativeE164", 1),
          ("none", 0),
          ("nsap", 2))
    )


_AtmIfUniSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfUniSigAddressConversion_Object = MibTableColumn
atmIfUniSigAddressConversion = _AtmIfUniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 10, 1, 2),
    _AtmIfUniSigAddressConversion_Type()
)
atmIfUniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSigAddressConversion.setStatus("mandatory")
_AtmIfUniSigStateTable_Object = MibTable
atmIfUniSigStateTable = _AtmIfUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 11)
)
if mibBuilder.loadTexts:
    atmIfUniSigStateTable.setStatus("mandatory")
_AtmIfUniSigStateEntry_Object = MibTableRow
atmIfUniSigStateEntry = _AtmIfUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 11, 1)
)
atmIfUniSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigStateEntry.setStatus("mandatory")


class _AtmIfUniSigAdminState_Type(Integer32):
    """Custom type atmIfUniSigAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_AtmIfUniSigAdminState_Type.__name__ = "Integer32"
_AtmIfUniSigAdminState_Object = MibTableColumn
atmIfUniSigAdminState = _AtmIfUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 11, 1, 1),
    _AtmIfUniSigAdminState_Type()
)
atmIfUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigAdminState.setStatus("mandatory")


class _AtmIfUniSigOperationalState_Type(Integer32):
    """Custom type atmIfUniSigOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfUniSigOperationalState_Type.__name__ = "Integer32"
_AtmIfUniSigOperationalState_Object = MibTableColumn
atmIfUniSigOperationalState = _AtmIfUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 11, 1, 2),
    _AtmIfUniSigOperationalState_Type()
)
atmIfUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigOperationalState.setStatus("mandatory")


class _AtmIfUniSigUsageState_Type(Integer32):
    """Custom type atmIfUniSigUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_AtmIfUniSigUsageState_Type.__name__ = "Integer32"
_AtmIfUniSigUsageState_Object = MibTableColumn
atmIfUniSigUsageState = _AtmIfUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 11, 1, 3),
    _AtmIfUniSigUsageState_Type()
)
atmIfUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigUsageState.setStatus("mandatory")
_AtmIfUniSigOperTable_Object = MibTable
atmIfUniSigOperTable = _AtmIfUniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12)
)
if mibBuilder.loadTexts:
    atmIfUniSigOperTable.setStatus("mandatory")
_AtmIfUniSigOperEntry_Object = MibTableRow
atmIfUniSigOperEntry = _AtmIfUniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12, 1)
)
atmIfUniSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigOperEntry.setStatus("mandatory")


class _AtmIfUniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfUniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfUniSigLastTxCauseCode_Object = MibTableColumn
atmIfUniSigLastTxCauseCode = _AtmIfUniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12, 1, 1),
    _AtmIfUniSigLastTxCauseCode_Type()
)
atmIfUniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfUniSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfUniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfUniSigLastTxDiagCode_Object = MibTableColumn
atmIfUniSigLastTxDiagCode = _AtmIfUniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12, 1, 2),
    _AtmIfUniSigLastTxDiagCode_Type()
)
atmIfUniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfUniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfUniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfUniSigLastRxCauseCode_Object = MibTableColumn
atmIfUniSigLastRxCauseCode = _AtmIfUniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12, 1, 3),
    _AtmIfUniSigLastRxCauseCode_Type()
)
atmIfUniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfUniSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfUniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfUniSigLastRxDiagCode_Object = MibTableColumn
atmIfUniSigLastRxDiagCode = _AtmIfUniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 12, 1, 4),
    _AtmIfUniSigLastRxDiagCode_Type()
)
atmIfUniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigLastRxDiagCode.setStatus("mandatory")
_AtmIfUniSigStatsTable_Object = MibTable
atmIfUniSigStatsTable = _AtmIfUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13)
)
if mibBuilder.loadTexts:
    atmIfUniSigStatsTable.setStatus("mandatory")
_AtmIfUniSigStatsEntry_Object = MibTableRow
atmIfUniSigStatsEntry = _AtmIfUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1)
)
atmIfUniSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniSigStatsEntry.setStatus("mandatory")
_AtmIfUniSigCurrentConnections_Type = Counter32
_AtmIfUniSigCurrentConnections_Object = MibTableColumn
atmIfUniSigCurrentConnections = _AtmIfUniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 1),
    _AtmIfUniSigCurrentConnections_Type()
)
atmIfUniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigCurrentConnections.setStatus("obsolete")


class _AtmIfUniSigPeakConnections_Type(Gauge32):
    """Custom type atmIfUniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfUniSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfUniSigPeakConnections_Object = MibTableColumn
atmIfUniSigPeakConnections = _AtmIfUniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 2),
    _AtmIfUniSigPeakConnections_Type()
)
atmIfUniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigPeakConnections.setStatus("mandatory")
_AtmIfUniSigSuccessfulConnections_Type = Counter32
_AtmIfUniSigSuccessfulConnections_Object = MibTableColumn
atmIfUniSigSuccessfulConnections = _AtmIfUniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 3),
    _AtmIfUniSigSuccessfulConnections_Type()
)
atmIfUniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigSuccessfulConnections.setStatus("mandatory")
_AtmIfUniSigFailedConnections_Type = Counter32
_AtmIfUniSigFailedConnections_Object = MibTableColumn
atmIfUniSigFailedConnections = _AtmIfUniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 4),
    _AtmIfUniSigFailedConnections_Type()
)
atmIfUniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigFailedConnections.setStatus("mandatory")
_AtmIfUniSigTxPdus_Type = Counter32
_AtmIfUniSigTxPdus_Object = MibTableColumn
atmIfUniSigTxPdus = _AtmIfUniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 5),
    _AtmIfUniSigTxPdus_Type()
)
atmIfUniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigTxPdus.setStatus("mandatory")
_AtmIfUniSigRxPdus_Type = Counter32
_AtmIfUniSigRxPdus_Object = MibTableColumn
atmIfUniSigRxPdus = _AtmIfUniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 6),
    _AtmIfUniSigRxPdus_Type()
)
atmIfUniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigRxPdus.setStatus("mandatory")


class _AtmIfUniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfUniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfUniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfUniSigCurrentPmpConnections_Object = MibTableColumn
atmIfUniSigCurrentPmpConnections = _AtmIfUniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 7),
    _AtmIfUniSigCurrentPmpConnections_Type()
)
atmIfUniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfUniSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfUniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfUniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfUniSigPeakPmpConnections_Object = MibTableColumn
atmIfUniSigPeakPmpConnections = _AtmIfUniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 8),
    _AtmIfUniSigPeakPmpConnections_Type()
)
atmIfUniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigPeakPmpConnections.setStatus("mandatory")
_AtmIfUniSigSuccessfulPmpConnections_Type = Counter32
_AtmIfUniSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfUniSigSuccessfulPmpConnections = _AtmIfUniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 9),
    _AtmIfUniSigSuccessfulPmpConnections_Type()
)
atmIfUniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfUniSigFailedPmpConnections_Type = Counter32
_AtmIfUniSigFailedPmpConnections_Object = MibTableColumn
atmIfUniSigFailedPmpConnections = _AtmIfUniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 10),
    _AtmIfUniSigFailedPmpConnections_Type()
)
atmIfUniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfUniSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfUniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfUniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfUniSigNewCurrentConnections_Object = MibTableColumn
atmIfUniSigNewCurrentConnections = _AtmIfUniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 3, 13, 1, 11),
    _AtmIfUniSigNewCurrentConnections_Type()
)
atmIfUniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniSigNewCurrentConnections.setStatus("mandatory")
_AtmIfUniAddr_ObjectIdentity = ObjectIdentity
atmIfUniAddr = _AtmIfUniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4)
)
_AtmIfUniAddrRowStatusTable_Object = MibTable
atmIfUniAddrRowStatusTable = _AtmIfUniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfUniAddrRowStatusTable.setStatus("mandatory")
_AtmIfUniAddrRowStatusEntry_Object = MibTableRow
atmIfUniAddrRowStatusEntry = _AtmIfUniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1)
)
atmIfUniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAddrRowStatusEntry.setStatus("mandatory")
_AtmIfUniAddrRowStatus_Type = RowStatus
_AtmIfUniAddrRowStatus_Object = MibTableColumn
atmIfUniAddrRowStatus = _AtmIfUniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1, 1),
    _AtmIfUniAddrRowStatus_Type()
)
atmIfUniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAddrRowStatus.setStatus("mandatory")
_AtmIfUniAddrComponentName_Type = DisplayString
_AtmIfUniAddrComponentName_Object = MibTableColumn
atmIfUniAddrComponentName = _AtmIfUniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1, 2),
    _AtmIfUniAddrComponentName_Type()
)
atmIfUniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrComponentName.setStatus("mandatory")
_AtmIfUniAddrStorageType_Type = StorageType
_AtmIfUniAddrStorageType_Object = MibTableColumn
atmIfUniAddrStorageType = _AtmIfUniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1, 4),
    _AtmIfUniAddrStorageType_Type()
)
atmIfUniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrStorageType.setStatus("mandatory")


class _AtmIfUniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfUniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfUniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfUniAddrAddressIndex_Object = MibTableColumn
atmIfUniAddrAddressIndex = _AtmIfUniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1, 10),
    _AtmIfUniAddrAddressIndex_Type()
)
atmIfUniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniAddrAddressIndex.setStatus("mandatory")


class _AtmIfUniAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfUniAddrAddressTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("default", 3),
          ("primary", 0),
          ("registered", 2))
    )


_AtmIfUniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfUniAddrAddressTypeIndex_Object = MibTableColumn
atmIfUniAddrAddressTypeIndex = _AtmIfUniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 1, 1, 11),
    _AtmIfUniAddrAddressTypeIndex_Type()
)
atmIfUniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfUniAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfUniAddrTermSP = _AtmIfUniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2)
)
_AtmIfUniAddrTermSPRowStatusTable_Object = MibTable
atmIfUniAddrTermSPRowStatusTable = _AtmIfUniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfUniAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfUniAddrTermSPRowStatusEntry = _AtmIfUniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1, 1)
)
atmIfUniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfUniAddrTermSPRowStatus_Type = RowStatus
_AtmIfUniAddrTermSPRowStatus_Object = MibTableColumn
atmIfUniAddrTermSPRowStatus = _AtmIfUniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1, 1, 1),
    _AtmIfUniAddrTermSPRowStatus_Type()
)
atmIfUniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfUniAddrTermSPComponentName_Type = DisplayString
_AtmIfUniAddrTermSPComponentName_Object = MibTableColumn
atmIfUniAddrTermSPComponentName = _AtmIfUniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1, 1, 2),
    _AtmIfUniAddrTermSPComponentName_Type()
)
atmIfUniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPComponentName.setStatus("mandatory")
_AtmIfUniAddrTermSPStorageType_Type = StorageType
_AtmIfUniAddrTermSPStorageType_Object = MibTableColumn
atmIfUniAddrTermSPStorageType = _AtmIfUniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1, 1, 4),
    _AtmIfUniAddrTermSPStorageType_Type()
)
atmIfUniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPStorageType.setStatus("mandatory")
_AtmIfUniAddrTermSPIndex_Type = NonReplicated
_AtmIfUniAddrTermSPIndex_Object = MibTableColumn
atmIfUniAddrTermSPIndex = _AtmIfUniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 2, 1, 1, 10),
    _AtmIfUniAddrTermSPIndex_Type()
)
atmIfUniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniAddrTermSPIndex.setStatus("mandatory")
_AtmIfUniAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfUniAddrPnniInfo = _AtmIfUniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3)
)
_AtmIfUniAddrPnniInfoRowStatusTable_Object = MibTable
atmIfUniAddrPnniInfoRowStatusTable = _AtmIfUniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfUniAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfUniAddrPnniInfoRowStatusEntry = _AtmIfUniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1, 1)
)
atmIfUniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfUniAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfUniAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfUniAddrPnniInfoRowStatus = _AtmIfUniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1, 1, 1),
    _AtmIfUniAddrPnniInfoRowStatus_Type()
)
atmIfUniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfUniAddrPnniInfoComponentName_Type = DisplayString
_AtmIfUniAddrPnniInfoComponentName_Object = MibTableColumn
atmIfUniAddrPnniInfoComponentName = _AtmIfUniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1, 1, 2),
    _AtmIfUniAddrPnniInfoComponentName_Type()
)
atmIfUniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfUniAddrPnniInfoStorageType_Type = StorageType
_AtmIfUniAddrPnniInfoStorageType_Object = MibTableColumn
atmIfUniAddrPnniInfoStorageType = _AtmIfUniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1, 1, 4),
    _AtmIfUniAddrPnniInfoStorageType_Type()
)
atmIfUniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfUniAddrPnniInfoIndex_Type = NonReplicated
_AtmIfUniAddrPnniInfoIndex_Object = MibTableColumn
atmIfUniAddrPnniInfoIndex = _AtmIfUniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 1, 1, 10),
    _AtmIfUniAddrPnniInfoIndex_Type()
)
atmIfUniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfUniAddrPnniInfoProvTable_Object = MibTable
atmIfUniAddrPnniInfoProvTable = _AtmIfUniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfUniAddrPnniInfoProvEntry_Object = MibTableRow
atmIfUniAddrPnniInfoProvEntry = _AtmIfUniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 10, 1)
)
atmIfUniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfUniAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfUniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfUniAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfUniAddrPnniInfoScope_Object = MibTableColumn
atmIfUniAddrPnniInfoScope = _AtmIfUniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 10, 1, 1),
    _AtmIfUniAddrPnniInfoScope_Type()
)
atmIfUniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfUniAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfUniAddrPnniInfoReachability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_AtmIfUniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfUniAddrPnniInfoReachability_Object = MibTableColumn
atmIfUniAddrPnniInfoReachability = _AtmIfUniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 3, 10, 1, 2),
    _AtmIfUniAddrPnniInfoReachability_Type()
)
atmIfUniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfUniAddrOperTable_Object = MibTable
atmIfUniAddrOperTable = _AtmIfUniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 10)
)
if mibBuilder.loadTexts:
    atmIfUniAddrOperTable.setStatus("mandatory")
_AtmIfUniAddrOperEntry_Object = MibTableRow
atmIfUniAddrOperEntry = _AtmIfUniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 10, 1)
)
atmIfUniAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAddrOperEntry.setStatus("mandatory")


class _AtmIfUniAddrScope_Type(Integer32):
    """Custom type atmIfUniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfUniAddrScope_Type.__name__ = "Integer32"
_AtmIfUniAddrScope_Object = MibTableColumn
atmIfUniAddrScope = _AtmIfUniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 10, 1, 1),
    _AtmIfUniAddrScope_Type()
)
atmIfUniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrScope.setStatus("mandatory")


class _AtmIfUniAddrReachability_Type(Integer32):
    """Custom type atmIfUniAddrReachability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_AtmIfUniAddrReachability_Type.__name__ = "Integer32"
_AtmIfUniAddrReachability_Object = MibTableColumn
atmIfUniAddrReachability = _AtmIfUniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 4, 10, 1, 2),
    _AtmIfUniAddrReachability_Type()
)
atmIfUniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniAddrReachability.setStatus("mandatory")
_AtmIfUniProvTable_Object = MibTable
atmIfUniProvTable = _AtmIfUniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10)
)
if mibBuilder.loadTexts:
    atmIfUniProvTable.setStatus("mandatory")
_AtmIfUniProvEntry_Object = MibTableRow
atmIfUniProvEntry = _AtmIfUniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1)
)
atmIfUniProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniProvEntry.setStatus("mandatory")


class _AtmIfUniVersion_Type(Integer32):
    """Custom type atmIfUniVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("atmForum30", 0),
          ("atmForum31", 1))
    )


_AtmIfUniVersion_Type.__name__ = "Integer32"
_AtmIfUniVersion_Object = MibTableColumn
atmIfUniVersion = _AtmIfUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1, 1),
    _AtmIfUniVersion_Type()
)
atmIfUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniVersion.setStatus("mandatory")


class _AtmIfUniSide_Type(Integer32):
    """Custom type atmIfUniSide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network", 0),
          ("user", 1))
    )


_AtmIfUniSide_Type.__name__ = "Integer32"
_AtmIfUniSide_Object = MibTableColumn
atmIfUniSide = _AtmIfUniSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1, 2),
    _AtmIfUniSide_Type()
)
atmIfUniSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSide.setStatus("mandatory")


class _AtmIfUniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfUniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfUniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfUniSoftPvcRetryPeriod_Object = MibTableColumn
atmIfUniSoftPvcRetryPeriod = _AtmIfUniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1, 3),
    _AtmIfUniSoftPvcRetryPeriod_Type()
)
atmIfUniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfUniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfUniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfUniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfUniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfUniSoftPvpAndPvcRetryPeriod = _AtmIfUniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1, 4),
    _AtmIfUniSoftPvpAndPvcRetryPeriod_Type()
)
atmIfUniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfUniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfUniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfUniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfUniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfUniSoftPvpAndPvcHoldOffTime = _AtmIfUniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 10, 1, 5),
    _AtmIfUniSoftPvpAndPvcHoldOffTime_Type()
)
atmIfUniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfUniOperTable_Object = MibTable
atmIfUniOperTable = _AtmIfUniOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 11)
)
if mibBuilder.loadTexts:
    atmIfUniOperTable.setStatus("mandatory")
_AtmIfUniOperEntry_Object = MibTableRow
atmIfUniOperEntry = _AtmIfUniOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 11, 1)
)
atmIfUniOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniOperEntry.setStatus("mandatory")


class _AtmIfUniMacAddress_Type(AsciiString):
    """Custom type atmIfUniMacAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_AtmIfUniMacAddress_Type.__name__ = "AsciiString"
_AtmIfUniMacAddress_Object = MibTableColumn
atmIfUniMacAddress = _AtmIfUniMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 11, 1, 1),
    _AtmIfUniMacAddress_Type()
)
atmIfUniMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfUniMacAddress.setStatus("mandatory")
_AtmIfUniAcctOptTable_Object = MibTable
atmIfUniAcctOptTable = _AtmIfUniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12)
)
if mibBuilder.loadTexts:
    atmIfUniAcctOptTable.setStatus("mandatory")
_AtmIfUniAcctOptEntry_Object = MibTableRow
atmIfUniAcctOptEntry = _AtmIfUniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12, 1)
)
atmIfUniAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfUniAcctOptEntry.setStatus("mandatory")


class _AtmIfUniAccountCollection_Type(OctetString):
    """Custom type atmIfUniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfUniAccountCollection_Type.__name__ = "OctetString"
_AtmIfUniAccountCollection_Object = MibTableColumn
atmIfUniAccountCollection = _AtmIfUniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12, 1, 1),
    _AtmIfUniAccountCollection_Type()
)
atmIfUniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAccountCollection.setStatus("mandatory")


class _AtmIfUniAccountConnectionType_Type(Integer32):
    """Custom type atmIfUniAccountConnectionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("origTerm", 0))
    )


_AtmIfUniAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfUniAccountConnectionType_Object = MibTableColumn
atmIfUniAccountConnectionType = _AtmIfUniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12, 1, 2),
    _AtmIfUniAccountConnectionType_Type()
)
atmIfUniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAccountConnectionType.setStatus("mandatory")


class _AtmIfUniAccountClass_Type(Unsigned32):
    """Custom type atmIfUniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniAccountClass_Type.__name__ = "Unsigned32"
_AtmIfUniAccountClass_Object = MibTableColumn
atmIfUniAccountClass = _AtmIfUniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12, 1, 3),
    _AtmIfUniAccountClass_Type()
)
atmIfUniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniAccountClass.setStatus("mandatory")


class _AtmIfUniServiceExchange_Type(Unsigned32):
    """Custom type atmIfUniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfUniServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfUniServiceExchange_Object = MibTableColumn
atmIfUniServiceExchange = _AtmIfUniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 6, 12, 1, 4),
    _AtmIfUniServiceExchange_Type()
)
atmIfUniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfUniServiceExchange.setStatus("mandatory")
_AtmIfVptUni_ObjectIdentity = ObjectIdentity
atmIfVptUni = _AtmIfVptUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8)
)
_AtmIfVptUniRowStatusTable_Object = MibTable
atmIfVptUniRowStatusTable = _AtmIfVptUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniRowStatusTable.setStatus("mandatory")
_AtmIfVptUniRowStatusEntry_Object = MibTableRow
atmIfVptUniRowStatusEntry = _AtmIfVptUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1, 1)
)
atmIfVptUniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniRowStatus_Type = RowStatus
_AtmIfVptUniRowStatus_Object = MibTableColumn
atmIfVptUniRowStatus = _AtmIfVptUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1, 1, 1),
    _AtmIfVptUniRowStatus_Type()
)
atmIfVptUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniRowStatus.setStatus("mandatory")
_AtmIfVptUniComponentName_Type = DisplayString
_AtmIfVptUniComponentName_Object = MibTableColumn
atmIfVptUniComponentName = _AtmIfVptUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1, 1, 2),
    _AtmIfVptUniComponentName_Type()
)
atmIfVptUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniComponentName.setStatus("mandatory")
_AtmIfVptUniStorageType_Type = StorageType
_AtmIfVptUniStorageType_Object = MibTableColumn
atmIfVptUniStorageType = _AtmIfVptUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1, 1, 4),
    _AtmIfVptUniStorageType_Type()
)
atmIfVptUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniStorageType.setStatus("mandatory")
_AtmIfVptUniIndex_Type = NonReplicated
_AtmIfVptUniIndex_Object = MibTableColumn
atmIfVptUniIndex = _AtmIfVptUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 1, 1, 10),
    _AtmIfVptUniIndex_Type()
)
atmIfVptUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniIndex.setStatus("mandatory")
_AtmIfVptUniSig_ObjectIdentity = ObjectIdentity
atmIfVptUniSig = _AtmIfVptUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2)
)
_AtmIfVptUniSigRowStatusTable_Object = MibTable
atmIfVptUniSigRowStatusTable = _AtmIfVptUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigRowStatusTable.setStatus("mandatory")
_AtmIfVptUniSigRowStatusEntry_Object = MibTableRow
atmIfVptUniSigRowStatusEntry = _AtmIfVptUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1, 1)
)
atmIfVptUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniSigRowStatus_Type = RowStatus
_AtmIfVptUniSigRowStatus_Object = MibTableColumn
atmIfVptUniSigRowStatus = _AtmIfVptUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1, 1, 1),
    _AtmIfVptUniSigRowStatus_Type()
)
atmIfVptUniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigRowStatus.setStatus("mandatory")
_AtmIfVptUniSigComponentName_Type = DisplayString
_AtmIfVptUniSigComponentName_Object = MibTableColumn
atmIfVptUniSigComponentName = _AtmIfVptUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1, 1, 2),
    _AtmIfVptUniSigComponentName_Type()
)
atmIfVptUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigComponentName.setStatus("mandatory")
_AtmIfVptUniSigStorageType_Type = StorageType
_AtmIfVptUniSigStorageType_Object = MibTableColumn
atmIfVptUniSigStorageType = _AtmIfVptUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1, 1, 4),
    _AtmIfVptUniSigStorageType_Type()
)
atmIfVptUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigStorageType.setStatus("mandatory")
_AtmIfVptUniSigIndex_Type = NonReplicated
_AtmIfVptUniSigIndex_Object = MibTableColumn
atmIfVptUniSigIndex = _AtmIfVptUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 1, 1, 10),
    _AtmIfVptUniSigIndex_Type()
)
atmIfVptUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniSigIndex.setStatus("mandatory")
_AtmIfVptUniSigVcd_ObjectIdentity = ObjectIdentity
atmIfVptUniSigVcd = _AtmIfVptUniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2)
)
_AtmIfVptUniSigVcdRowStatusTable_Object = MibTable
atmIfVptUniSigVcdRowStatusTable = _AtmIfVptUniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdRowStatusTable.setStatus("mandatory")
_AtmIfVptUniSigVcdRowStatusEntry_Object = MibTableRow
atmIfVptUniSigVcdRowStatusEntry = _AtmIfVptUniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1, 1)
)
atmIfVptUniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniSigVcdRowStatus_Type = RowStatus
_AtmIfVptUniSigVcdRowStatus_Object = MibTableColumn
atmIfVptUniSigVcdRowStatus = _AtmIfVptUniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1, 1, 1),
    _AtmIfVptUniSigVcdRowStatus_Type()
)
atmIfVptUniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdRowStatus.setStatus("mandatory")
_AtmIfVptUniSigVcdComponentName_Type = DisplayString
_AtmIfVptUniSigVcdComponentName_Object = MibTableColumn
atmIfVptUniSigVcdComponentName = _AtmIfVptUniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1, 1, 2),
    _AtmIfVptUniSigVcdComponentName_Type()
)
atmIfVptUniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdComponentName.setStatus("mandatory")
_AtmIfVptUniSigVcdStorageType_Type = StorageType
_AtmIfVptUniSigVcdStorageType_Object = MibTableColumn
atmIfVptUniSigVcdStorageType = _AtmIfVptUniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1, 1, 4),
    _AtmIfVptUniSigVcdStorageType_Type()
)
atmIfVptUniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdStorageType.setStatus("mandatory")
_AtmIfVptUniSigVcdIndex_Type = NonReplicated
_AtmIfVptUniSigVcdIndex_Object = MibTableColumn
atmIfVptUniSigVcdIndex = _AtmIfVptUniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 1, 1, 10),
    _AtmIfVptUniSigVcdIndex_Type()
)
atmIfVptUniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdIndex.setStatus("mandatory")
_AtmIfVptUniSigVcdProvTable_Object = MibTable
atmIfVptUniSigVcdProvTable = _AtmIfVptUniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdProvTable.setStatus("mandatory")
_AtmIfVptUniSigVcdProvEntry_Object = MibTableRow
atmIfVptUniSigVcdProvEntry = _AtmIfVptUniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1)
)
atmIfVptUniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdProvEntry.setStatus("mandatory")


class _AtmIfVptUniSigVcdTrafficDescType_Type(Integer32):
    """Custom type atmIfVptUniSigVcdTrafficDescType based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8))
    )


_AtmIfVptUniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdTrafficDescType_Object = MibTableColumn
atmIfVptUniSigVcdTrafficDescType = _AtmIfVptUniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 1),
    _AtmIfVptUniSigVcdTrafficDescType_Type()
)
atmIfVptUniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTrafficDescType.setStatus("mandatory")


class _AtmIfVptUniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type atmIfVptUniSigVcdAtmServiceCategory based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("constantBitRate", 1),
          ("nrtVariableBitRate", 3),
          ("rtVariableBitRate", 2),
          ("unspecifiedBitRate", 0))
    )


_AtmIfVptUniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdAtmServiceCategory_Object = MibTableColumn
atmIfVptUniSigVcdAtmServiceCategory = _AtmIfVptUniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 3),
    _AtmIfVptUniSigVcdAtmServiceCategory_Type()
)
atmIfVptUniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdAtmServiceCategory.setStatus("mandatory")


class _AtmIfVptUniSigVcdQosClass_Type(Integer32):
    """Custom type atmIfVptUniSigVcdQosClass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4))
    )


_AtmIfVptUniSigVcdQosClass_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdQosClass_Object = MibTableColumn
atmIfVptUniSigVcdQosClass = _AtmIfVptUniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 21),
    _AtmIfVptUniSigVcdQosClass_Type()
)
atmIfVptUniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdQosClass.setStatus("mandatory")


class _AtmIfVptUniSigVcdTrafficShaping_Type(Integer32):
    """Custom type atmIfVptUniSigVcdTrafficShaping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_AtmIfVptUniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdTrafficShaping_Object = MibTableColumn
atmIfVptUniSigVcdTrafficShaping = _AtmIfVptUniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 50),
    _AtmIfVptUniSigVcdTrafficShaping_Type()
)
atmIfVptUniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTrafficShaping.setStatus("mandatory")


class _AtmIfVptUniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type atmIfVptUniSigVcdUnshapedTransmitQueueing based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("sameAsCa", 3))
    )


_AtmIfVptUniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
atmIfVptUniSigVcdUnshapedTransmitQueueing = _AtmIfVptUniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 60),
    _AtmIfVptUniSigVcdUnshapedTransmitQueueing_Type()
)
atmIfVptUniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _AtmIfVptUniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type atmIfVptUniSigVcdUsageParameterControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sameAsCa", 2))
    )


_AtmIfVptUniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdUsageParameterControl_Object = MibTableColumn
atmIfVptUniSigVcdUsageParameterControl = _AtmIfVptUniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 10, 1, 70),
    _AtmIfVptUniSigVcdUsageParameterControl_Type()
)
atmIfVptUniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdUsageParameterControl.setStatus("mandatory")
_AtmIfVptUniSigVcdTdpTable_Object = MibTable
atmIfVptUniSigVcdTdpTable = _AtmIfVptUniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 387)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTdpTable.setStatus("mandatory")
_AtmIfVptUniSigVcdTdpEntry_Object = MibTableRow
atmIfVptUniSigVcdTdpEntry = _AtmIfVptUniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 387, 1)
)
atmIfVptUniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigVcdIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTdpEntry.setStatus("mandatory")


class _AtmIfVptUniSigVcdTdpIndex_Type(Integer32):
    """Custom type atmIfVptUniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AtmIfVptUniSigVcdTdpIndex_Type.__name__ = "Integer32"
_AtmIfVptUniSigVcdTdpIndex_Object = MibTableColumn
atmIfVptUniSigVcdTdpIndex = _AtmIfVptUniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 387, 1, 1),
    _AtmIfVptUniSigVcdTdpIndex_Type()
)
atmIfVptUniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTdpIndex.setStatus("mandatory")


class _AtmIfVptUniSigVcdTdpValue_Type(Unsigned32):
    """Custom type atmIfVptUniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmIfVptUniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_AtmIfVptUniSigVcdTdpValue_Object = MibTableColumn
atmIfVptUniSigVcdTdpValue = _AtmIfVptUniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 2, 387, 1, 2),
    _AtmIfVptUniSigVcdTdpValue_Type()
)
atmIfVptUniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVcdTdpValue.setStatus("mandatory")
_AtmIfVptUniSigProvTable_Object = MibTable
atmIfVptUniSigProvTable = _AtmIfVptUniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 10)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigProvTable.setStatus("mandatory")
_AtmIfVptUniSigProvEntry_Object = MibTableRow
atmIfVptUniSigProvEntry = _AtmIfVptUniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 10, 1)
)
atmIfVptUniSigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigProvEntry.setStatus("mandatory")


class _AtmIfVptUniSigVci_Type(Unsigned32):
    """Custom type atmIfVptUniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIfVptUniSigVci_Type.__name__ = "Unsigned32"
_AtmIfVptUniSigVci_Object = MibTableColumn
atmIfVptUniSigVci = _AtmIfVptUniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 10, 1, 1),
    _AtmIfVptUniSigVci_Type()
)
atmIfVptUniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigVci.setStatus("mandatory")


class _AtmIfVptUniSigAddressConversion_Type(Integer32):
    """Custom type atmIfVptUniSigAddressConversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nativeE164", 1),
          ("none", 0),
          ("nsap", 2))
    )


_AtmIfVptUniSigAddressConversion_Type.__name__ = "Integer32"
_AtmIfVptUniSigAddressConversion_Object = MibTableColumn
atmIfVptUniSigAddressConversion = _AtmIfVptUniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 10, 1, 2),
    _AtmIfVptUniSigAddressConversion_Type()
)
atmIfVptUniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSigAddressConversion.setStatus("mandatory")
_AtmIfVptUniSigStateTable_Object = MibTable
atmIfVptUniSigStateTable = _AtmIfVptUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 11)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigStateTable.setStatus("mandatory")
_AtmIfVptUniSigStateEntry_Object = MibTableRow
atmIfVptUniSigStateEntry = _AtmIfVptUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 11, 1)
)
atmIfVptUniSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigStateEntry.setStatus("mandatory")


class _AtmIfVptUniSigAdminState_Type(Integer32):
    """Custom type atmIfVptUniSigAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_AtmIfVptUniSigAdminState_Type.__name__ = "Integer32"
_AtmIfVptUniSigAdminState_Object = MibTableColumn
atmIfVptUniSigAdminState = _AtmIfVptUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 11, 1, 1),
    _AtmIfVptUniSigAdminState_Type()
)
atmIfVptUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigAdminState.setStatus("mandatory")


class _AtmIfVptUniSigOperationalState_Type(Integer32):
    """Custom type atmIfVptUniSigOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfVptUniSigOperationalState_Type.__name__ = "Integer32"
_AtmIfVptUniSigOperationalState_Object = MibTableColumn
atmIfVptUniSigOperationalState = _AtmIfVptUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 11, 1, 2),
    _AtmIfVptUniSigOperationalState_Type()
)
atmIfVptUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigOperationalState.setStatus("mandatory")


class _AtmIfVptUniSigUsageState_Type(Integer32):
    """Custom type atmIfVptUniSigUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_AtmIfVptUniSigUsageState_Type.__name__ = "Integer32"
_AtmIfVptUniSigUsageState_Object = MibTableColumn
atmIfVptUniSigUsageState = _AtmIfVptUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 11, 1, 3),
    _AtmIfVptUniSigUsageState_Type()
)
atmIfVptUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigUsageState.setStatus("mandatory")
_AtmIfVptUniSigOperTable_Object = MibTable
atmIfVptUniSigOperTable = _AtmIfVptUniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigOperTable.setStatus("mandatory")
_AtmIfVptUniSigOperEntry_Object = MibTableRow
atmIfVptUniSigOperEntry = _AtmIfVptUniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12, 1)
)
atmIfVptUniSigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigOperEntry.setStatus("mandatory")


class _AtmIfVptUniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptUniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptUniSigLastTxCauseCode_Object = MibTableColumn
atmIfVptUniSigLastTxCauseCode = _AtmIfVptUniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12, 1, 1),
    _AtmIfVptUniSigLastTxCauseCode_Type()
)
atmIfVptUniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigLastTxCauseCode.setStatus("mandatory")


class _AtmIfVptUniSigLastTxDiagCode_Type(Hex):
    """Custom type atmIfVptUniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniSigLastTxDiagCode_Type.__name__ = "Hex"
_AtmIfVptUniSigLastTxDiagCode_Object = MibTableColumn
atmIfVptUniSigLastTxDiagCode = _AtmIfVptUniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12, 1, 2),
    _AtmIfVptUniSigLastTxDiagCode_Type()
)
atmIfVptUniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigLastTxDiagCode.setStatus("mandatory")


class _AtmIfVptUniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type atmIfVptUniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_AtmIfVptUniSigLastRxCauseCode_Object = MibTableColumn
atmIfVptUniSigLastRxCauseCode = _AtmIfVptUniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12, 1, 3),
    _AtmIfVptUniSigLastRxCauseCode_Type()
)
atmIfVptUniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigLastRxCauseCode.setStatus("mandatory")


class _AtmIfVptUniSigLastRxDiagCode_Type(Hex):
    """Custom type atmIfVptUniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniSigLastRxDiagCode_Type.__name__ = "Hex"
_AtmIfVptUniSigLastRxDiagCode_Object = MibTableColumn
atmIfVptUniSigLastRxDiagCode = _AtmIfVptUniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 12, 1, 4),
    _AtmIfVptUniSigLastRxDiagCode_Type()
)
atmIfVptUniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigLastRxDiagCode.setStatus("mandatory")
_AtmIfVptUniSigStatsTable_Object = MibTable
atmIfVptUniSigStatsTable = _AtmIfVptUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13)
)
if mibBuilder.loadTexts:
    atmIfVptUniSigStatsTable.setStatus("mandatory")
_AtmIfVptUniSigStatsEntry_Object = MibTableRow
atmIfVptUniSigStatsEntry = _AtmIfVptUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1)
)
atmIfVptUniSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniSigStatsEntry.setStatus("mandatory")
_AtmIfVptUniSigCurrentConnections_Type = Counter32
_AtmIfVptUniSigCurrentConnections_Object = MibTableColumn
atmIfVptUniSigCurrentConnections = _AtmIfVptUniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 1),
    _AtmIfVptUniSigCurrentConnections_Type()
)
atmIfVptUniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigCurrentConnections.setStatus("obsolete")


class _AtmIfVptUniSigPeakConnections_Type(Gauge32):
    """Custom type atmIfVptUniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptUniSigPeakConnections_Type.__name__ = "Gauge32"
_AtmIfVptUniSigPeakConnections_Object = MibTableColumn
atmIfVptUniSigPeakConnections = _AtmIfVptUniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 2),
    _AtmIfVptUniSigPeakConnections_Type()
)
atmIfVptUniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigPeakConnections.setStatus("mandatory")
_AtmIfVptUniSigSuccessfulConnections_Type = Counter32
_AtmIfVptUniSigSuccessfulConnections_Object = MibTableColumn
atmIfVptUniSigSuccessfulConnections = _AtmIfVptUniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 3),
    _AtmIfVptUniSigSuccessfulConnections_Type()
)
atmIfVptUniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigSuccessfulConnections.setStatus("mandatory")
_AtmIfVptUniSigFailedConnections_Type = Counter32
_AtmIfVptUniSigFailedConnections_Object = MibTableColumn
atmIfVptUniSigFailedConnections = _AtmIfVptUniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 4),
    _AtmIfVptUniSigFailedConnections_Type()
)
atmIfVptUniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigFailedConnections.setStatus("mandatory")
_AtmIfVptUniSigTxPdus_Type = Counter32
_AtmIfVptUniSigTxPdus_Object = MibTableColumn
atmIfVptUniSigTxPdus = _AtmIfVptUniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 5),
    _AtmIfVptUniSigTxPdus_Type()
)
atmIfVptUniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigTxPdus.setStatus("mandatory")
_AtmIfVptUniSigRxPdus_Type = Counter32
_AtmIfVptUniSigRxPdus_Object = MibTableColumn
atmIfVptUniSigRxPdus = _AtmIfVptUniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 6),
    _AtmIfVptUniSigRxPdus_Type()
)
atmIfVptUniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigRxPdus.setStatus("mandatory")


class _AtmIfVptUniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type atmIfVptUniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptUniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptUniSigCurrentPmpConnections_Object = MibTableColumn
atmIfVptUniSigCurrentPmpConnections = _AtmIfVptUniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 7),
    _AtmIfVptUniSigCurrentPmpConnections_Type()
)
atmIfVptUniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigCurrentPmpConnections.setStatus("mandatory")


class _AtmIfVptUniSigPeakPmpConnections_Type(Gauge32):
    """Custom type atmIfVptUniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptUniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_AtmIfVptUniSigPeakPmpConnections_Object = MibTableColumn
atmIfVptUniSigPeakPmpConnections = _AtmIfVptUniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 8),
    _AtmIfVptUniSigPeakPmpConnections_Type()
)
atmIfVptUniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigPeakPmpConnections.setStatus("mandatory")
_AtmIfVptUniSigSuccessfulPmpConnections_Type = Counter32
_AtmIfVptUniSigSuccessfulPmpConnections_Object = MibTableColumn
atmIfVptUniSigSuccessfulPmpConnections = _AtmIfVptUniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 9),
    _AtmIfVptUniSigSuccessfulPmpConnections_Type()
)
atmIfVptUniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigSuccessfulPmpConnections.setStatus("mandatory")
_AtmIfVptUniSigFailedPmpConnections_Type = Counter32
_AtmIfVptUniSigFailedPmpConnections_Object = MibTableColumn
atmIfVptUniSigFailedPmpConnections = _AtmIfVptUniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 10),
    _AtmIfVptUniSigFailedPmpConnections_Type()
)
atmIfVptUniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigFailedPmpConnections.setStatus("mandatory")


class _AtmIfVptUniSigNewCurrentConnections_Type(Gauge32):
    """Custom type atmIfVptUniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AtmIfVptUniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_AtmIfVptUniSigNewCurrentConnections_Object = MibTableColumn
atmIfVptUniSigNewCurrentConnections = _AtmIfVptUniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 2, 13, 1, 11),
    _AtmIfVptUniSigNewCurrentConnections_Type()
)
atmIfVptUniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniSigNewCurrentConnections.setStatus("mandatory")
_AtmIfVptUniAddr_ObjectIdentity = ObjectIdentity
atmIfVptUniAddr = _AtmIfVptUniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3)
)
_AtmIfVptUniAddrRowStatusTable_Object = MibTable
atmIfVptUniAddrRowStatusTable = _AtmIfVptUniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrRowStatusTable.setStatus("mandatory")
_AtmIfVptUniAddrRowStatusEntry_Object = MibTableRow
atmIfVptUniAddrRowStatusEntry = _AtmIfVptUniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1)
)
atmIfVptUniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniAddrRowStatus_Type = RowStatus
_AtmIfVptUniAddrRowStatus_Object = MibTableColumn
atmIfVptUniAddrRowStatus = _AtmIfVptUniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1, 1),
    _AtmIfVptUniAddrRowStatus_Type()
)
atmIfVptUniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAddrRowStatus.setStatus("mandatory")
_AtmIfVptUniAddrComponentName_Type = DisplayString
_AtmIfVptUniAddrComponentName_Object = MibTableColumn
atmIfVptUniAddrComponentName = _AtmIfVptUniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1, 2),
    _AtmIfVptUniAddrComponentName_Type()
)
atmIfVptUniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrComponentName.setStatus("mandatory")
_AtmIfVptUniAddrStorageType_Type = StorageType
_AtmIfVptUniAddrStorageType_Object = MibTableColumn
atmIfVptUniAddrStorageType = _AtmIfVptUniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1, 4),
    _AtmIfVptUniAddrStorageType_Type()
)
atmIfVptUniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrStorageType.setStatus("mandatory")


class _AtmIfVptUniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type atmIfVptUniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AtmIfVptUniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_AtmIfVptUniAddrAddressIndex_Object = MibTableColumn
atmIfVptUniAddrAddressIndex = _AtmIfVptUniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1, 10),
    _AtmIfVptUniAddrAddressIndex_Type()
)
atmIfVptUniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniAddrAddressIndex.setStatus("mandatory")


class _AtmIfVptUniAddrAddressTypeIndex_Type(Integer32):
    """Custom type atmIfVptUniAddrAddressTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("default", 3),
          ("primary", 0),
          ("registered", 2))
    )


_AtmIfVptUniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_AtmIfVptUniAddrAddressTypeIndex_Object = MibTableColumn
atmIfVptUniAddrAddressTypeIndex = _AtmIfVptUniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 1, 1, 11),
    _AtmIfVptUniAddrAddressTypeIndex_Type()
)
atmIfVptUniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniAddrAddressTypeIndex.setStatus("mandatory")
_AtmIfVptUniAddrTermSP_ObjectIdentity = ObjectIdentity
atmIfVptUniAddrTermSP = _AtmIfVptUniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2)
)
_AtmIfVptUniAddrTermSPRowStatusTable_Object = MibTable
atmIfVptUniAddrTermSPRowStatusTable = _AtmIfVptUniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPRowStatusTable.setStatus("mandatory")
_AtmIfVptUniAddrTermSPRowStatusEntry_Object = MibTableRow
atmIfVptUniAddrTermSPRowStatusEntry = _AtmIfVptUniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1, 1)
)
atmIfVptUniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniAddrTermSPRowStatus_Type = RowStatus
_AtmIfVptUniAddrTermSPRowStatus_Object = MibTableColumn
atmIfVptUniAddrTermSPRowStatus = _AtmIfVptUniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1, 1, 1),
    _AtmIfVptUniAddrTermSPRowStatus_Type()
)
atmIfVptUniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPRowStatus.setStatus("mandatory")
_AtmIfVptUniAddrTermSPComponentName_Type = DisplayString
_AtmIfVptUniAddrTermSPComponentName_Object = MibTableColumn
atmIfVptUniAddrTermSPComponentName = _AtmIfVptUniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1, 1, 2),
    _AtmIfVptUniAddrTermSPComponentName_Type()
)
atmIfVptUniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPComponentName.setStatus("mandatory")
_AtmIfVptUniAddrTermSPStorageType_Type = StorageType
_AtmIfVptUniAddrTermSPStorageType_Object = MibTableColumn
atmIfVptUniAddrTermSPStorageType = _AtmIfVptUniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1, 1, 4),
    _AtmIfVptUniAddrTermSPStorageType_Type()
)
atmIfVptUniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPStorageType.setStatus("mandatory")
_AtmIfVptUniAddrTermSPIndex_Type = NonReplicated
_AtmIfVptUniAddrTermSPIndex_Object = MibTableColumn
atmIfVptUniAddrTermSPIndex = _AtmIfVptUniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 2, 1, 1, 10),
    _AtmIfVptUniAddrTermSPIndex_Type()
)
atmIfVptUniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniAddrTermSPIndex.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfo_ObjectIdentity = ObjectIdentity
atmIfVptUniAddrPnniInfo = _AtmIfVptUniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3)
)
_AtmIfVptUniAddrPnniInfoRowStatusTable_Object = MibTable
atmIfVptUniAddrPnniInfoRowStatusTable = _AtmIfVptUniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1)
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoRowStatusEntry_Object = MibTableRow
atmIfVptUniAddrPnniInfoRowStatusEntry = _AtmIfVptUniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1, 1)
)
atmIfVptUniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoRowStatus_Type = RowStatus
_AtmIfVptUniAddrPnniInfoRowStatus_Object = MibTableColumn
atmIfVptUniAddrPnniInfoRowStatus = _AtmIfVptUniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1, 1, 1),
    _AtmIfVptUniAddrPnniInfoRowStatus_Type()
)
atmIfVptUniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoRowStatus.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoComponentName_Type = DisplayString
_AtmIfVptUniAddrPnniInfoComponentName_Object = MibTableColumn
atmIfVptUniAddrPnniInfoComponentName = _AtmIfVptUniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1, 1, 2),
    _AtmIfVptUniAddrPnniInfoComponentName_Type()
)
atmIfVptUniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoComponentName.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoStorageType_Type = StorageType
_AtmIfVptUniAddrPnniInfoStorageType_Object = MibTableColumn
atmIfVptUniAddrPnniInfoStorageType = _AtmIfVptUniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1, 1, 4),
    _AtmIfVptUniAddrPnniInfoStorageType_Type()
)
atmIfVptUniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoStorageType.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoIndex_Type = NonReplicated
_AtmIfVptUniAddrPnniInfoIndex_Object = MibTableColumn
atmIfVptUniAddrPnniInfoIndex = _AtmIfVptUniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 1, 1, 10),
    _AtmIfVptUniAddrPnniInfoIndex_Type()
)
atmIfVptUniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoIndex.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoProvTable_Object = MibTable
atmIfVptUniAddrPnniInfoProvTable = _AtmIfVptUniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoProvTable.setStatus("mandatory")
_AtmIfVptUniAddrPnniInfoProvEntry_Object = MibTableRow
atmIfVptUniAddrPnniInfoProvEntry = _AtmIfVptUniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 10, 1)
)
atmIfVptUniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoProvEntry.setStatus("mandatory")


class _AtmIfVptUniAddrPnniInfoScope_Type(Integer32):
    """Custom type atmIfVptUniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptUniAddrPnniInfoScope_Type.__name__ = "Integer32"
_AtmIfVptUniAddrPnniInfoScope_Object = MibTableColumn
atmIfVptUniAddrPnniInfoScope = _AtmIfVptUniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 10, 1, 1),
    _AtmIfVptUniAddrPnniInfoScope_Type()
)
atmIfVptUniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoScope.setStatus("mandatory")


class _AtmIfVptUniAddrPnniInfoReachability_Type(Integer32):
    """Custom type atmIfVptUniAddrPnniInfoReachability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_AtmIfVptUniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_AtmIfVptUniAddrPnniInfoReachability_Object = MibTableColumn
atmIfVptUniAddrPnniInfoReachability = _AtmIfVptUniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 3, 10, 1, 2),
    _AtmIfVptUniAddrPnniInfoReachability_Type()
)
atmIfVptUniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAddrPnniInfoReachability.setStatus("mandatory")
_AtmIfVptUniAddrOperTable_Object = MibTable
atmIfVptUniAddrOperTable = _AtmIfVptUniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 10)
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrOperTable.setStatus("mandatory")
_AtmIfVptUniAddrOperEntry_Object = MibTableRow
atmIfVptUniAddrOperEntry = _AtmIfVptUniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 10, 1)
)
atmIfVptUniAddrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAddrOperEntry.setStatus("mandatory")


class _AtmIfVptUniAddrScope_Type(Integer32):
    """Custom type atmIfVptUniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_AtmIfVptUniAddrScope_Type.__name__ = "Integer32"
_AtmIfVptUniAddrScope_Object = MibTableColumn
atmIfVptUniAddrScope = _AtmIfVptUniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 10, 1, 1),
    _AtmIfVptUniAddrScope_Type()
)
atmIfVptUniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrScope.setStatus("mandatory")


class _AtmIfVptUniAddrReachability_Type(Integer32):
    """Custom type atmIfVptUniAddrReachability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 1),
          ("internal", 0))
    )


_AtmIfVptUniAddrReachability_Type.__name__ = "Integer32"
_AtmIfVptUniAddrReachability_Object = MibTableColumn
atmIfVptUniAddrReachability = _AtmIfVptUniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 3, 10, 1, 2),
    _AtmIfVptUniAddrReachability_Type()
)
atmIfVptUniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptUniAddrReachability.setStatus("mandatory")
_AtmIfVptUniProvTable_Object = MibTable
atmIfVptUniProvTable = _AtmIfVptUniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10)
)
if mibBuilder.loadTexts:
    atmIfVptUniProvTable.setStatus("mandatory")
_AtmIfVptUniProvEntry_Object = MibTableRow
atmIfVptUniProvEntry = _AtmIfVptUniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1)
)
atmIfVptUniProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniProvEntry.setStatus("mandatory")


class _AtmIfVptUniVersion_Type(Integer32):
    """Custom type atmIfVptUniVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("atmForum30", 0),
          ("atmForum31", 1))
    )


_AtmIfVptUniVersion_Type.__name__ = "Integer32"
_AtmIfVptUniVersion_Object = MibTableColumn
atmIfVptUniVersion = _AtmIfVptUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1, 1),
    _AtmIfVptUniVersion_Type()
)
atmIfVptUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniVersion.setStatus("mandatory")


class _AtmIfVptUniSide_Type(Integer32):
    """Custom type atmIfVptUniSide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network", 0),
          ("user", 1))
    )


_AtmIfVptUniSide_Type.__name__ = "Integer32"
_AtmIfVptUniSide_Object = MibTableColumn
atmIfVptUniSide = _AtmIfVptUniSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1, 2),
    _AtmIfVptUniSide_Type()
)
atmIfVptUniSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSide.setStatus("mandatory")


class _AtmIfVptUniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptUniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptUniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptUniSoftPvcRetryPeriod_Object = MibTableColumn
atmIfVptUniSoftPvcRetryPeriod = _AtmIfVptUniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1, 3),
    _AtmIfVptUniSoftPvcRetryPeriod_Type()
)
atmIfVptUniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSoftPvcRetryPeriod.setStatus("obsolete")


class _AtmIfVptUniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type atmIfVptUniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_AtmIfVptUniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_AtmIfVptUniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
atmIfVptUniSoftPvpAndPvcRetryPeriod = _AtmIfVptUniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1, 4),
    _AtmIfVptUniSoftPvpAndPvcRetryPeriod_Type()
)
atmIfVptUniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _AtmIfVptUniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type atmIfVptUniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_AtmIfVptUniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_AtmIfVptUniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
atmIfVptUniSoftPvpAndPvcHoldOffTime = _AtmIfVptUniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 10, 1, 5),
    _AtmIfVptUniSoftPvpAndPvcHoldOffTime_Type()
)
atmIfVptUniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")
_AtmIfVptUniAcctOptTable_Object = MibTable
atmIfVptUniAcctOptTable = _AtmIfVptUniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11)
)
if mibBuilder.loadTexts:
    atmIfVptUniAcctOptTable.setStatus("mandatory")
_AtmIfVptUniAcctOptEntry_Object = MibTableRow
atmIfVptUniAcctOptEntry = _AtmIfVptUniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11, 1)
)
atmIfVptUniAcctOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniAcctOptEntry.setStatus("mandatory")


class _AtmIfVptUniAccountCollection_Type(OctetString):
    """Custom type atmIfVptUniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmIfVptUniAccountCollection_Type.__name__ = "OctetString"
_AtmIfVptUniAccountCollection_Object = MibTableColumn
atmIfVptUniAccountCollection = _AtmIfVptUniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11, 1, 1),
    _AtmIfVptUniAccountCollection_Type()
)
atmIfVptUniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAccountCollection.setStatus("mandatory")


class _AtmIfVptUniAccountConnectionType_Type(Integer32):
    """Custom type atmIfVptUniAccountConnectionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intermediate", 1),
          ("origTerm", 0))
    )


_AtmIfVptUniAccountConnectionType_Type.__name__ = "Integer32"
_AtmIfVptUniAccountConnectionType_Object = MibTableColumn
atmIfVptUniAccountConnectionType = _AtmIfVptUniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11, 1, 2),
    _AtmIfVptUniAccountConnectionType_Type()
)
atmIfVptUniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAccountConnectionType.setStatus("mandatory")


class _AtmIfVptUniAccountClass_Type(Unsigned32):
    """Custom type atmIfVptUniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniAccountClass_Type.__name__ = "Unsigned32"
_AtmIfVptUniAccountClass_Object = MibTableColumn
atmIfVptUniAccountClass = _AtmIfVptUniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11, 1, 3),
    _AtmIfVptUniAccountClass_Type()
)
atmIfVptUniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniAccountClass.setStatus("mandatory")


class _AtmIfVptUniServiceExchange_Type(Unsigned32):
    """Custom type atmIfVptUniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniServiceExchange_Type.__name__ = "Unsigned32"
_AtmIfVptUniServiceExchange_Object = MibTableColumn
atmIfVptUniServiceExchange = _AtmIfVptUniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 11, 1, 4),
    _AtmIfVptUniServiceExchange_Type()
)
atmIfVptUniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniServiceExchange.setStatus("mandatory")
_AtmIfVptUniVProvTable_Object = MibTable
atmIfVptUniVProvTable = _AtmIfVptUniVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 12)
)
if mibBuilder.loadTexts:
    atmIfVptUniVProvTable.setStatus("mandatory")
_AtmIfVptUniVProvEntry_Object = MibTableRow
atmIfVptUniVProvEntry = _AtmIfVptUniVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 12, 1)
)
atmIfVptUniVProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmUniMIB", "atmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptUniVProvEntry.setStatus("mandatory")


class _AtmIfVptUniVpci_Type(Unsigned32):
    """Custom type atmIfVptUniVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmIfVptUniVpci_Type.__name__ = "Unsigned32"
_AtmIfVptUniVpci_Object = MibTableColumn
atmIfVptUniVpci = _AtmIfVptUniVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 8, 12, 1, 1),
    _AtmIfVptUniVpci_Type()
)
atmIfVptUniVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptUniVpci.setStatus("mandatory")
_AtmUniMIB_ObjectIdentity = ObjectIdentity
atmUniMIB = _AtmUniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69)
)
_AtmUniGroup_ObjectIdentity = ObjectIdentity
atmUniGroup = _AtmUniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 1)
)
_AtmUniGroupBE_ObjectIdentity = ObjectIdentity
atmUniGroupBE = _AtmUniGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 1, 5)
)
_AtmUniGroupBE00_ObjectIdentity = ObjectIdentity
atmUniGroupBE00 = _AtmUniGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 1, 5, 1)
)
_AtmUniGroupBE00A_ObjectIdentity = ObjectIdentity
atmUniGroupBE00A = _AtmUniGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 1, 5, 1, 2)
)
_AtmUniCapabilities_ObjectIdentity = ObjectIdentity
atmUniCapabilities = _AtmUniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 3)
)
_AtmUniCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesBE = _AtmUniCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 3, 5)
)
_AtmUniCapabilitiesBE00_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesBE00 = _AtmUniCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 3, 5, 1)
)
_AtmUniCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesBE00A = _AtmUniCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 69, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmUniMIB",
    **{"atmIfUni": atmIfUni,
       "atmIfUniRowStatusTable": atmIfUniRowStatusTable,
       "atmIfUniRowStatusEntry": atmIfUniRowStatusEntry,
       "atmIfUniRowStatus": atmIfUniRowStatus,
       "atmIfUniComponentName": atmIfUniComponentName,
       "atmIfUniStorageType": atmIfUniStorageType,
       "atmIfUniIndex": atmIfUniIndex,
       "atmIfUniIlmi": atmIfUniIlmi,
       "atmIfUniIlmiRowStatusTable": atmIfUniIlmiRowStatusTable,
       "atmIfUniIlmiRowStatusEntry": atmIfUniIlmiRowStatusEntry,
       "atmIfUniIlmiRowStatus": atmIfUniIlmiRowStatus,
       "atmIfUniIlmiComponentName": atmIfUniIlmiComponentName,
       "atmIfUniIlmiStorageType": atmIfUniIlmiStorageType,
       "atmIfUniIlmiIndex": atmIfUniIlmiIndex,
       "atmIfUniIlmiStateTable": atmIfUniIlmiStateTable,
       "atmIfUniIlmiStateEntry": atmIfUniIlmiStateEntry,
       "atmIfUniIlmiAdminState": atmIfUniIlmiAdminState,
       "atmIfUniIlmiOperationalState": atmIfUniIlmiOperationalState,
       "atmIfUniIlmiUsageState": atmIfUniIlmiUsageState,
       "atmIfUniIlmiProvTable": atmIfUniIlmiProvTable,
       "atmIfUniIlmiProvEntry": atmIfUniIlmiProvEntry,
       "atmIfUniIlmiVci": atmIfUniIlmiVci,
       "atmIfUniIlmiOperatingMode": atmIfUniIlmiOperatingMode,
       "atmIfUniIlmiStatsTable": atmIfUniIlmiStatsTable,
       "atmIfUniIlmiStatsEntry": atmIfUniIlmiStatsEntry,
       "atmIfUniIlmiTxPdus": atmIfUniIlmiTxPdus,
       "atmIfUniIlmiRxPdus": atmIfUniIlmiRxPdus,
       "atmIfUniIlmiRxBadPdusDiscarded": atmIfUniIlmiRxBadPdusDiscarded,
       "atmIfUniIlmiPrefixToRegisterTable": atmIfUniIlmiPrefixToRegisterTable,
       "atmIfUniIlmiPrefixToRegisterEntry": atmIfUniIlmiPrefixToRegisterEntry,
       "atmIfUniIlmiPrefixToRegisterValue": atmIfUniIlmiPrefixToRegisterValue,
       "atmIfUniIlmiPrefixToRegisterRowStatus": atmIfUniIlmiPrefixToRegisterRowStatus,
       "atmIfUniIlmiEsiToRegisterTable": atmIfUniIlmiEsiToRegisterTable,
       "atmIfUniIlmiEsiToRegisterEntry": atmIfUniIlmiEsiToRegisterEntry,
       "atmIfUniIlmiEsiToRegisterValue": atmIfUniIlmiEsiToRegisterValue,
       "atmIfUniIlmiEsiToRegisterRowStatus": atmIfUniIlmiEsiToRegisterRowStatus,
       "atmIfUniSig": atmIfUniSig,
       "atmIfUniSigRowStatusTable": atmIfUniSigRowStatusTable,
       "atmIfUniSigRowStatusEntry": atmIfUniSigRowStatusEntry,
       "atmIfUniSigRowStatus": atmIfUniSigRowStatus,
       "atmIfUniSigComponentName": atmIfUniSigComponentName,
       "atmIfUniSigStorageType": atmIfUniSigStorageType,
       "atmIfUniSigIndex": atmIfUniSigIndex,
       "atmIfUniSigVcd": atmIfUniSigVcd,
       "atmIfUniSigVcdRowStatusTable": atmIfUniSigVcdRowStatusTable,
       "atmIfUniSigVcdRowStatusEntry": atmIfUniSigVcdRowStatusEntry,
       "atmIfUniSigVcdRowStatus": atmIfUniSigVcdRowStatus,
       "atmIfUniSigVcdComponentName": atmIfUniSigVcdComponentName,
       "atmIfUniSigVcdStorageType": atmIfUniSigVcdStorageType,
       "atmIfUniSigVcdIndex": atmIfUniSigVcdIndex,
       "atmIfUniSigVcdProvTable": atmIfUniSigVcdProvTable,
       "atmIfUniSigVcdProvEntry": atmIfUniSigVcdProvEntry,
       "atmIfUniSigVcdTrafficDescType": atmIfUniSigVcdTrafficDescType,
       "atmIfUniSigVcdAtmServiceCategory": atmIfUniSigVcdAtmServiceCategory,
       "atmIfUniSigVcdQosClass": atmIfUniSigVcdQosClass,
       "atmIfUniSigVcdTrafficShaping": atmIfUniSigVcdTrafficShaping,
       "atmIfUniSigVcdUnshapedTransmitQueueing": atmIfUniSigVcdUnshapedTransmitQueueing,
       "atmIfUniSigVcdUsageParameterControl": atmIfUniSigVcdUsageParameterControl,
       "atmIfUniSigVcdTdpTable": atmIfUniSigVcdTdpTable,
       "atmIfUniSigVcdTdpEntry": atmIfUniSigVcdTdpEntry,
       "atmIfUniSigVcdTdpIndex": atmIfUniSigVcdTdpIndex,
       "atmIfUniSigVcdTdpValue": atmIfUniSigVcdTdpValue,
       "atmIfUniSigProvTable": atmIfUniSigProvTable,
       "atmIfUniSigProvEntry": atmIfUniSigProvEntry,
       "atmIfUniSigVci": atmIfUniSigVci,
       "atmIfUniSigAddressConversion": atmIfUniSigAddressConversion,
       "atmIfUniSigStateTable": atmIfUniSigStateTable,
       "atmIfUniSigStateEntry": atmIfUniSigStateEntry,
       "atmIfUniSigAdminState": atmIfUniSigAdminState,
       "atmIfUniSigOperationalState": atmIfUniSigOperationalState,
       "atmIfUniSigUsageState": atmIfUniSigUsageState,
       "atmIfUniSigOperTable": atmIfUniSigOperTable,
       "atmIfUniSigOperEntry": atmIfUniSigOperEntry,
       "atmIfUniSigLastTxCauseCode": atmIfUniSigLastTxCauseCode,
       "atmIfUniSigLastTxDiagCode": atmIfUniSigLastTxDiagCode,
       "atmIfUniSigLastRxCauseCode": atmIfUniSigLastRxCauseCode,
       "atmIfUniSigLastRxDiagCode": atmIfUniSigLastRxDiagCode,
       "atmIfUniSigStatsTable": atmIfUniSigStatsTable,
       "atmIfUniSigStatsEntry": atmIfUniSigStatsEntry,
       "atmIfUniSigCurrentConnections": atmIfUniSigCurrentConnections,
       "atmIfUniSigPeakConnections": atmIfUniSigPeakConnections,
       "atmIfUniSigSuccessfulConnections": atmIfUniSigSuccessfulConnections,
       "atmIfUniSigFailedConnections": atmIfUniSigFailedConnections,
       "atmIfUniSigTxPdus": atmIfUniSigTxPdus,
       "atmIfUniSigRxPdus": atmIfUniSigRxPdus,
       "atmIfUniSigCurrentPmpConnections": atmIfUniSigCurrentPmpConnections,
       "atmIfUniSigPeakPmpConnections": atmIfUniSigPeakPmpConnections,
       "atmIfUniSigSuccessfulPmpConnections": atmIfUniSigSuccessfulPmpConnections,
       "atmIfUniSigFailedPmpConnections": atmIfUniSigFailedPmpConnections,
       "atmIfUniSigNewCurrentConnections": atmIfUniSigNewCurrentConnections,
       "atmIfUniAddr": atmIfUniAddr,
       "atmIfUniAddrRowStatusTable": atmIfUniAddrRowStatusTable,
       "atmIfUniAddrRowStatusEntry": atmIfUniAddrRowStatusEntry,
       "atmIfUniAddrRowStatus": atmIfUniAddrRowStatus,
       "atmIfUniAddrComponentName": atmIfUniAddrComponentName,
       "atmIfUniAddrStorageType": atmIfUniAddrStorageType,
       "atmIfUniAddrAddressIndex": atmIfUniAddrAddressIndex,
       "atmIfUniAddrAddressTypeIndex": atmIfUniAddrAddressTypeIndex,
       "atmIfUniAddrTermSP": atmIfUniAddrTermSP,
       "atmIfUniAddrTermSPRowStatusTable": atmIfUniAddrTermSPRowStatusTable,
       "atmIfUniAddrTermSPRowStatusEntry": atmIfUniAddrTermSPRowStatusEntry,
       "atmIfUniAddrTermSPRowStatus": atmIfUniAddrTermSPRowStatus,
       "atmIfUniAddrTermSPComponentName": atmIfUniAddrTermSPComponentName,
       "atmIfUniAddrTermSPStorageType": atmIfUniAddrTermSPStorageType,
       "atmIfUniAddrTermSPIndex": atmIfUniAddrTermSPIndex,
       "atmIfUniAddrPnniInfo": atmIfUniAddrPnniInfo,
       "atmIfUniAddrPnniInfoRowStatusTable": atmIfUniAddrPnniInfoRowStatusTable,
       "atmIfUniAddrPnniInfoRowStatusEntry": atmIfUniAddrPnniInfoRowStatusEntry,
       "atmIfUniAddrPnniInfoRowStatus": atmIfUniAddrPnniInfoRowStatus,
       "atmIfUniAddrPnniInfoComponentName": atmIfUniAddrPnniInfoComponentName,
       "atmIfUniAddrPnniInfoStorageType": atmIfUniAddrPnniInfoStorageType,
       "atmIfUniAddrPnniInfoIndex": atmIfUniAddrPnniInfoIndex,
       "atmIfUniAddrPnniInfoProvTable": atmIfUniAddrPnniInfoProvTable,
       "atmIfUniAddrPnniInfoProvEntry": atmIfUniAddrPnniInfoProvEntry,
       "atmIfUniAddrPnniInfoScope": atmIfUniAddrPnniInfoScope,
       "atmIfUniAddrPnniInfoReachability": atmIfUniAddrPnniInfoReachability,
       "atmIfUniAddrOperTable": atmIfUniAddrOperTable,
       "atmIfUniAddrOperEntry": atmIfUniAddrOperEntry,
       "atmIfUniAddrScope": atmIfUniAddrScope,
       "atmIfUniAddrReachability": atmIfUniAddrReachability,
       "atmIfUniProvTable": atmIfUniProvTable,
       "atmIfUniProvEntry": atmIfUniProvEntry,
       "atmIfUniVersion": atmIfUniVersion,
       "atmIfUniSide": atmIfUniSide,
       "atmIfUniSoftPvcRetryPeriod": atmIfUniSoftPvcRetryPeriod,
       "atmIfUniSoftPvpAndPvcRetryPeriod": atmIfUniSoftPvpAndPvcRetryPeriod,
       "atmIfUniSoftPvpAndPvcHoldOffTime": atmIfUniSoftPvpAndPvcHoldOffTime,
       "atmIfUniOperTable": atmIfUniOperTable,
       "atmIfUniOperEntry": atmIfUniOperEntry,
       "atmIfUniMacAddress": atmIfUniMacAddress,
       "atmIfUniAcctOptTable": atmIfUniAcctOptTable,
       "atmIfUniAcctOptEntry": atmIfUniAcctOptEntry,
       "atmIfUniAccountCollection": atmIfUniAccountCollection,
       "atmIfUniAccountConnectionType": atmIfUniAccountConnectionType,
       "atmIfUniAccountClass": atmIfUniAccountClass,
       "atmIfUniServiceExchange": atmIfUniServiceExchange,
       "atmIfVptUni": atmIfVptUni,
       "atmIfVptUniRowStatusTable": atmIfVptUniRowStatusTable,
       "atmIfVptUniRowStatusEntry": atmIfVptUniRowStatusEntry,
       "atmIfVptUniRowStatus": atmIfVptUniRowStatus,
       "atmIfVptUniComponentName": atmIfVptUniComponentName,
       "atmIfVptUniStorageType": atmIfVptUniStorageType,
       "atmIfVptUniIndex": atmIfVptUniIndex,
       "atmIfVptUniSig": atmIfVptUniSig,
       "atmIfVptUniSigRowStatusTable": atmIfVptUniSigRowStatusTable,
       "atmIfVptUniSigRowStatusEntry": atmIfVptUniSigRowStatusEntry,
       "atmIfVptUniSigRowStatus": atmIfVptUniSigRowStatus,
       "atmIfVptUniSigComponentName": atmIfVptUniSigComponentName,
       "atmIfVptUniSigStorageType": atmIfVptUniSigStorageType,
       "atmIfVptUniSigIndex": atmIfVptUniSigIndex,
       "atmIfVptUniSigVcd": atmIfVptUniSigVcd,
       "atmIfVptUniSigVcdRowStatusTable": atmIfVptUniSigVcdRowStatusTable,
       "atmIfVptUniSigVcdRowStatusEntry": atmIfVptUniSigVcdRowStatusEntry,
       "atmIfVptUniSigVcdRowStatus": atmIfVptUniSigVcdRowStatus,
       "atmIfVptUniSigVcdComponentName": atmIfVptUniSigVcdComponentName,
       "atmIfVptUniSigVcdStorageType": atmIfVptUniSigVcdStorageType,
       "atmIfVptUniSigVcdIndex": atmIfVptUniSigVcdIndex,
       "atmIfVptUniSigVcdProvTable": atmIfVptUniSigVcdProvTable,
       "atmIfVptUniSigVcdProvEntry": atmIfVptUniSigVcdProvEntry,
       "atmIfVptUniSigVcdTrafficDescType": atmIfVptUniSigVcdTrafficDescType,
       "atmIfVptUniSigVcdAtmServiceCategory": atmIfVptUniSigVcdAtmServiceCategory,
       "atmIfVptUniSigVcdQosClass": atmIfVptUniSigVcdQosClass,
       "atmIfVptUniSigVcdTrafficShaping": atmIfVptUniSigVcdTrafficShaping,
       "atmIfVptUniSigVcdUnshapedTransmitQueueing": atmIfVptUniSigVcdUnshapedTransmitQueueing,
       "atmIfVptUniSigVcdUsageParameterControl": atmIfVptUniSigVcdUsageParameterControl,
       "atmIfVptUniSigVcdTdpTable": atmIfVptUniSigVcdTdpTable,
       "atmIfVptUniSigVcdTdpEntry": atmIfVptUniSigVcdTdpEntry,
       "atmIfVptUniSigVcdTdpIndex": atmIfVptUniSigVcdTdpIndex,
       "atmIfVptUniSigVcdTdpValue": atmIfVptUniSigVcdTdpValue,
       "atmIfVptUniSigProvTable": atmIfVptUniSigProvTable,
       "atmIfVptUniSigProvEntry": atmIfVptUniSigProvEntry,
       "atmIfVptUniSigVci": atmIfVptUniSigVci,
       "atmIfVptUniSigAddressConversion": atmIfVptUniSigAddressConversion,
       "atmIfVptUniSigStateTable": atmIfVptUniSigStateTable,
       "atmIfVptUniSigStateEntry": atmIfVptUniSigStateEntry,
       "atmIfVptUniSigAdminState": atmIfVptUniSigAdminState,
       "atmIfVptUniSigOperationalState": atmIfVptUniSigOperationalState,
       "atmIfVptUniSigUsageState": atmIfVptUniSigUsageState,
       "atmIfVptUniSigOperTable": atmIfVptUniSigOperTable,
       "atmIfVptUniSigOperEntry": atmIfVptUniSigOperEntry,
       "atmIfVptUniSigLastTxCauseCode": atmIfVptUniSigLastTxCauseCode,
       "atmIfVptUniSigLastTxDiagCode": atmIfVptUniSigLastTxDiagCode,
       "atmIfVptUniSigLastRxCauseCode": atmIfVptUniSigLastRxCauseCode,
       "atmIfVptUniSigLastRxDiagCode": atmIfVptUniSigLastRxDiagCode,
       "atmIfVptUniSigStatsTable": atmIfVptUniSigStatsTable,
       "atmIfVptUniSigStatsEntry": atmIfVptUniSigStatsEntry,
       "atmIfVptUniSigCurrentConnections": atmIfVptUniSigCurrentConnections,
       "atmIfVptUniSigPeakConnections": atmIfVptUniSigPeakConnections,
       "atmIfVptUniSigSuccessfulConnections": atmIfVptUniSigSuccessfulConnections,
       "atmIfVptUniSigFailedConnections": atmIfVptUniSigFailedConnections,
       "atmIfVptUniSigTxPdus": atmIfVptUniSigTxPdus,
       "atmIfVptUniSigRxPdus": atmIfVptUniSigRxPdus,
       "atmIfVptUniSigCurrentPmpConnections": atmIfVptUniSigCurrentPmpConnections,
       "atmIfVptUniSigPeakPmpConnections": atmIfVptUniSigPeakPmpConnections,
       "atmIfVptUniSigSuccessfulPmpConnections": atmIfVptUniSigSuccessfulPmpConnections,
       "atmIfVptUniSigFailedPmpConnections": atmIfVptUniSigFailedPmpConnections,
       "atmIfVptUniSigNewCurrentConnections": atmIfVptUniSigNewCurrentConnections,
       "atmIfVptUniAddr": atmIfVptUniAddr,
       "atmIfVptUniAddrRowStatusTable": atmIfVptUniAddrRowStatusTable,
       "atmIfVptUniAddrRowStatusEntry": atmIfVptUniAddrRowStatusEntry,
       "atmIfVptUniAddrRowStatus": atmIfVptUniAddrRowStatus,
       "atmIfVptUniAddrComponentName": atmIfVptUniAddrComponentName,
       "atmIfVptUniAddrStorageType": atmIfVptUniAddrStorageType,
       "atmIfVptUniAddrAddressIndex": atmIfVptUniAddrAddressIndex,
       "atmIfVptUniAddrAddressTypeIndex": atmIfVptUniAddrAddressTypeIndex,
       "atmIfVptUniAddrTermSP": atmIfVptUniAddrTermSP,
       "atmIfVptUniAddrTermSPRowStatusTable": atmIfVptUniAddrTermSPRowStatusTable,
       "atmIfVptUniAddrTermSPRowStatusEntry": atmIfVptUniAddrTermSPRowStatusEntry,
       "atmIfVptUniAddrTermSPRowStatus": atmIfVptUniAddrTermSPRowStatus,
       "atmIfVptUniAddrTermSPComponentName": atmIfVptUniAddrTermSPComponentName,
       "atmIfVptUniAddrTermSPStorageType": atmIfVptUniAddrTermSPStorageType,
       "atmIfVptUniAddrTermSPIndex": atmIfVptUniAddrTermSPIndex,
       "atmIfVptUniAddrPnniInfo": atmIfVptUniAddrPnniInfo,
       "atmIfVptUniAddrPnniInfoRowStatusTable": atmIfVptUniAddrPnniInfoRowStatusTable,
       "atmIfVptUniAddrPnniInfoRowStatusEntry": atmIfVptUniAddrPnniInfoRowStatusEntry,
       "atmIfVptUniAddrPnniInfoRowStatus": atmIfVptUniAddrPnniInfoRowStatus,
       "atmIfVptUniAddrPnniInfoComponentName": atmIfVptUniAddrPnniInfoComponentName,
       "atmIfVptUniAddrPnniInfoStorageType": atmIfVptUniAddrPnniInfoStorageType,
       "atmIfVptUniAddrPnniInfoIndex": atmIfVptUniAddrPnniInfoIndex,
       "atmIfVptUniAddrPnniInfoProvTable": atmIfVptUniAddrPnniInfoProvTable,
       "atmIfVptUniAddrPnniInfoProvEntry": atmIfVptUniAddrPnniInfoProvEntry,
       "atmIfVptUniAddrPnniInfoScope": atmIfVptUniAddrPnniInfoScope,
       "atmIfVptUniAddrPnniInfoReachability": atmIfVptUniAddrPnniInfoReachability,
       "atmIfVptUniAddrOperTable": atmIfVptUniAddrOperTable,
       "atmIfVptUniAddrOperEntry": atmIfVptUniAddrOperEntry,
       "atmIfVptUniAddrScope": atmIfVptUniAddrScope,
       "atmIfVptUniAddrReachability": atmIfVptUniAddrReachability,
       "atmIfVptUniProvTable": atmIfVptUniProvTable,
       "atmIfVptUniProvEntry": atmIfVptUniProvEntry,
       "atmIfVptUniVersion": atmIfVptUniVersion,
       "atmIfVptUniSide": atmIfVptUniSide,
       "atmIfVptUniSoftPvcRetryPeriod": atmIfVptUniSoftPvcRetryPeriod,
       "atmIfVptUniSoftPvpAndPvcRetryPeriod": atmIfVptUniSoftPvpAndPvcRetryPeriod,
       "atmIfVptUniSoftPvpAndPvcHoldOffTime": atmIfVptUniSoftPvpAndPvcHoldOffTime,
       "atmIfVptUniAcctOptTable": atmIfVptUniAcctOptTable,
       "atmIfVptUniAcctOptEntry": atmIfVptUniAcctOptEntry,
       "atmIfVptUniAccountCollection": atmIfVptUniAccountCollection,
       "atmIfVptUniAccountConnectionType": atmIfVptUniAccountConnectionType,
       "atmIfVptUniAccountClass": atmIfVptUniAccountClass,
       "atmIfVptUniServiceExchange": atmIfVptUniServiceExchange,
       "atmIfVptUniVProvTable": atmIfVptUniVProvTable,
       "atmIfVptUniVProvEntry": atmIfVptUniVProvEntry,
       "atmIfVptUniVpci": atmIfVptUniVpci,
       "atmUniMIB": atmUniMIB,
       "atmUniGroup": atmUniGroup,
       "atmUniGroupBE": atmUniGroupBE,
       "atmUniGroupBE00": atmUniGroupBE00,
       "atmUniGroupBE00A": atmUniGroupBE00A,
       "atmUniCapabilities": atmUniCapabilities,
       "atmUniCapabilitiesBE": atmUniCapabilitiesBE,
       "atmUniCapabilitiesBE00": atmUniCapabilitiesBE00,
       "atmUniCapabilitiesBE00A": atmUniCapabilitiesBE00A}
)
