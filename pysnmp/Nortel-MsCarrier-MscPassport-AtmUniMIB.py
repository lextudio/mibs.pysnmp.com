# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmUniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmUniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:51 2024
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

(mscAtmIf,
 mscAtmIfIndex,
 mscAtmIfVpt,
 mscAtmIfVptIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmCoreMIB",
    "mscAtmIf",
    "mscAtmIfIndex",
    "mscAtmIfVpt",
    "mscAtmIfVptIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "Hex",
    "HexString",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscAtmIfUni_ObjectIdentity = ObjectIdentity
mscAtmIfUni = _MscAtmIfUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6)
)
_MscAtmIfUniRowStatusTable_Object = MibTable
mscAtmIfUniRowStatusTable = _MscAtmIfUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniRowStatusTable.setStatus("mandatory")
_MscAtmIfUniRowStatusEntry_Object = MibTableRow
mscAtmIfUniRowStatusEntry = _MscAtmIfUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1, 1)
)
mscAtmIfUniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniRowStatus_Type = RowStatus
_MscAtmIfUniRowStatus_Object = MibTableColumn
mscAtmIfUniRowStatus = _MscAtmIfUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1, 1, 1),
    _MscAtmIfUniRowStatus_Type()
)
mscAtmIfUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniRowStatus.setStatus("mandatory")
_MscAtmIfUniComponentName_Type = DisplayString
_MscAtmIfUniComponentName_Object = MibTableColumn
mscAtmIfUniComponentName = _MscAtmIfUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1, 1, 2),
    _MscAtmIfUniComponentName_Type()
)
mscAtmIfUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniComponentName.setStatus("mandatory")
_MscAtmIfUniStorageType_Type = StorageType
_MscAtmIfUniStorageType_Object = MibTableColumn
mscAtmIfUniStorageType = _MscAtmIfUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1, 1, 4),
    _MscAtmIfUniStorageType_Type()
)
mscAtmIfUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniStorageType.setStatus("mandatory")
_MscAtmIfUniIndex_Type = NonReplicated
_MscAtmIfUniIndex_Object = MibTableColumn
mscAtmIfUniIndex = _MscAtmIfUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 1, 1, 10),
    _MscAtmIfUniIndex_Type()
)
mscAtmIfUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniIndex.setStatus("mandatory")
_MscAtmIfUniIlmi_ObjectIdentity = ObjectIdentity
mscAtmIfUniIlmi = _MscAtmIfUniIlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2)
)
_MscAtmIfUniIlmiRowStatusTable_Object = MibTable
mscAtmIfUniIlmiRowStatusTable = _MscAtmIfUniIlmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiRowStatusTable.setStatus("mandatory")
_MscAtmIfUniIlmiRowStatusEntry_Object = MibTableRow
mscAtmIfUniIlmiRowStatusEntry = _MscAtmIfUniIlmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1, 1)
)
mscAtmIfUniIlmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniIlmiRowStatus_Type = RowStatus
_MscAtmIfUniIlmiRowStatus_Object = MibTableColumn
mscAtmIfUniIlmiRowStatus = _MscAtmIfUniIlmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1, 1, 1),
    _MscAtmIfUniIlmiRowStatus_Type()
)
mscAtmIfUniIlmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiRowStatus.setStatus("mandatory")
_MscAtmIfUniIlmiComponentName_Type = DisplayString
_MscAtmIfUniIlmiComponentName_Object = MibTableColumn
mscAtmIfUniIlmiComponentName = _MscAtmIfUniIlmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1, 1, 2),
    _MscAtmIfUniIlmiComponentName_Type()
)
mscAtmIfUniIlmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiComponentName.setStatus("mandatory")
_MscAtmIfUniIlmiStorageType_Type = StorageType
_MscAtmIfUniIlmiStorageType_Object = MibTableColumn
mscAtmIfUniIlmiStorageType = _MscAtmIfUniIlmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1, 1, 4),
    _MscAtmIfUniIlmiStorageType_Type()
)
mscAtmIfUniIlmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiStorageType.setStatus("mandatory")
_MscAtmIfUniIlmiIndex_Type = NonReplicated
_MscAtmIfUniIlmiIndex_Object = MibTableColumn
mscAtmIfUniIlmiIndex = _MscAtmIfUniIlmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 1, 1, 10),
    _MscAtmIfUniIlmiIndex_Type()
)
mscAtmIfUniIlmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiIndex.setStatus("mandatory")
_MscAtmIfUniIlmiStateTable_Object = MibTable
mscAtmIfUniIlmiStateTable = _MscAtmIfUniIlmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiStateTable.setStatus("mandatory")
_MscAtmIfUniIlmiStateEntry_Object = MibTableRow
mscAtmIfUniIlmiStateEntry = _MscAtmIfUniIlmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 10, 1)
)
mscAtmIfUniIlmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiStateEntry.setStatus("mandatory")


class _MscAtmIfUniIlmiAdminState_Type(Integer32):
    """Custom type mscAtmIfUniIlmiAdminState based on Integer32"""
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


_MscAtmIfUniIlmiAdminState_Type.__name__ = "Integer32"
_MscAtmIfUniIlmiAdminState_Object = MibTableColumn
mscAtmIfUniIlmiAdminState = _MscAtmIfUniIlmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 10, 1, 1),
    _MscAtmIfUniIlmiAdminState_Type()
)
mscAtmIfUniIlmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiAdminState.setStatus("mandatory")


class _MscAtmIfUniIlmiOperationalState_Type(Integer32):
    """Custom type mscAtmIfUniIlmiOperationalState based on Integer32"""
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


_MscAtmIfUniIlmiOperationalState_Type.__name__ = "Integer32"
_MscAtmIfUniIlmiOperationalState_Object = MibTableColumn
mscAtmIfUniIlmiOperationalState = _MscAtmIfUniIlmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 10, 1, 2),
    _MscAtmIfUniIlmiOperationalState_Type()
)
mscAtmIfUniIlmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiOperationalState.setStatus("mandatory")


class _MscAtmIfUniIlmiUsageState_Type(Integer32):
    """Custom type mscAtmIfUniIlmiUsageState based on Integer32"""
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


_MscAtmIfUniIlmiUsageState_Type.__name__ = "Integer32"
_MscAtmIfUniIlmiUsageState_Object = MibTableColumn
mscAtmIfUniIlmiUsageState = _MscAtmIfUniIlmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 10, 1, 3),
    _MscAtmIfUniIlmiUsageState_Type()
)
mscAtmIfUniIlmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiUsageState.setStatus("mandatory")
_MscAtmIfUniIlmiProvTable_Object = MibTable
mscAtmIfUniIlmiProvTable = _MscAtmIfUniIlmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiProvTable.setStatus("mandatory")
_MscAtmIfUniIlmiProvEntry_Object = MibTableRow
mscAtmIfUniIlmiProvEntry = _MscAtmIfUniIlmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 11, 1)
)
mscAtmIfUniIlmiProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiProvEntry.setStatus("mandatory")


class _MscAtmIfUniIlmiVci_Type(Unsigned32):
    """Custom type mscAtmIfUniIlmiVci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfUniIlmiVci_Type.__name__ = "Unsigned32"
_MscAtmIfUniIlmiVci_Object = MibTableColumn
mscAtmIfUniIlmiVci = _MscAtmIfUniIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 11, 1, 1),
    _MscAtmIfUniIlmiVci_Type()
)
mscAtmIfUniIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiVci.setStatus("mandatory")


class _MscAtmIfUniIlmiOperatingMode_Type(Integer32):
    """Custom type mscAtmIfUniIlmiOperatingMode based on Integer32"""
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


_MscAtmIfUniIlmiOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfUniIlmiOperatingMode_Object = MibTableColumn
mscAtmIfUniIlmiOperatingMode = _MscAtmIfUniIlmiOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 11, 1, 2),
    _MscAtmIfUniIlmiOperatingMode_Type()
)
mscAtmIfUniIlmiOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiOperatingMode.setStatus("mandatory")
_MscAtmIfUniIlmiStatsTable_Object = MibTable
mscAtmIfUniIlmiStatsTable = _MscAtmIfUniIlmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiStatsTable.setStatus("mandatory")
_MscAtmIfUniIlmiStatsEntry_Object = MibTableRow
mscAtmIfUniIlmiStatsEntry = _MscAtmIfUniIlmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 12, 1)
)
mscAtmIfUniIlmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiStatsEntry.setStatus("mandatory")
_MscAtmIfUniIlmiTxPdus_Type = Counter32
_MscAtmIfUniIlmiTxPdus_Object = MibTableColumn
mscAtmIfUniIlmiTxPdus = _MscAtmIfUniIlmiTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 12, 1, 1),
    _MscAtmIfUniIlmiTxPdus_Type()
)
mscAtmIfUniIlmiTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiTxPdus.setStatus("mandatory")
_MscAtmIfUniIlmiRxPdus_Type = Counter32
_MscAtmIfUniIlmiRxPdus_Object = MibTableColumn
mscAtmIfUniIlmiRxPdus = _MscAtmIfUniIlmiRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 12, 1, 2),
    _MscAtmIfUniIlmiRxPdus_Type()
)
mscAtmIfUniIlmiRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiRxPdus.setStatus("mandatory")
_MscAtmIfUniIlmiRxBadPdusDiscarded_Type = Counter32
_MscAtmIfUniIlmiRxBadPdusDiscarded_Object = MibTableColumn
mscAtmIfUniIlmiRxBadPdusDiscarded = _MscAtmIfUniIlmiRxBadPdusDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 12, 1, 3),
    _MscAtmIfUniIlmiRxBadPdusDiscarded_Type()
)
mscAtmIfUniIlmiRxBadPdusDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiRxBadPdusDiscarded.setStatus("mandatory")
_MscAtmIfUniIlmiPrefixToRegisterTable_Object = MibTable
mscAtmIfUniIlmiPrefixToRegisterTable = _MscAtmIfUniIlmiPrefixToRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 287)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiPrefixToRegisterTable.setStatus("mandatory")
_MscAtmIfUniIlmiPrefixToRegisterEntry_Object = MibTableRow
mscAtmIfUniIlmiPrefixToRegisterEntry = _MscAtmIfUniIlmiPrefixToRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 287, 1)
)
mscAtmIfUniIlmiPrefixToRegisterEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiPrefixToRegisterValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiPrefixToRegisterEntry.setStatus("mandatory")


class _MscAtmIfUniIlmiPrefixToRegisterValue_Type(AsciiString):
    """Custom type mscAtmIfUniIlmiPrefixToRegisterValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_MscAtmIfUniIlmiPrefixToRegisterValue_Type.__name__ = "AsciiString"
_MscAtmIfUniIlmiPrefixToRegisterValue_Object = MibTableColumn
mscAtmIfUniIlmiPrefixToRegisterValue = _MscAtmIfUniIlmiPrefixToRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 287, 1, 1),
    _MscAtmIfUniIlmiPrefixToRegisterValue_Type()
)
mscAtmIfUniIlmiPrefixToRegisterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiPrefixToRegisterValue.setStatus("mandatory")
_MscAtmIfUniIlmiPrefixToRegisterRowStatus_Type = RowStatus
_MscAtmIfUniIlmiPrefixToRegisterRowStatus_Object = MibTableColumn
mscAtmIfUniIlmiPrefixToRegisterRowStatus = _MscAtmIfUniIlmiPrefixToRegisterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 287, 1, 2),
    _MscAtmIfUniIlmiPrefixToRegisterRowStatus_Type()
)
mscAtmIfUniIlmiPrefixToRegisterRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiPrefixToRegisterRowStatus.setStatus("mandatory")
_MscAtmIfUniIlmiEsiToRegisterTable_Object = MibTable
mscAtmIfUniIlmiEsiToRegisterTable = _MscAtmIfUniIlmiEsiToRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 288)
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiEsiToRegisterTable.setStatus("mandatory")
_MscAtmIfUniIlmiEsiToRegisterEntry_Object = MibTableRow
mscAtmIfUniIlmiEsiToRegisterEntry = _MscAtmIfUniIlmiEsiToRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 288, 1)
)
mscAtmIfUniIlmiEsiToRegisterEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIlmiEsiToRegisterValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiEsiToRegisterEntry.setStatus("mandatory")


class _MscAtmIfUniIlmiEsiToRegisterValue_Type(AsciiString):
    """Custom type mscAtmIfUniIlmiEsiToRegisterValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_MscAtmIfUniIlmiEsiToRegisterValue_Type.__name__ = "AsciiString"
_MscAtmIfUniIlmiEsiToRegisterValue_Object = MibTableColumn
mscAtmIfUniIlmiEsiToRegisterValue = _MscAtmIfUniIlmiEsiToRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 288, 1, 1),
    _MscAtmIfUniIlmiEsiToRegisterValue_Type()
)
mscAtmIfUniIlmiEsiToRegisterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiEsiToRegisterValue.setStatus("mandatory")
_MscAtmIfUniIlmiEsiToRegisterRowStatus_Type = RowStatus
_MscAtmIfUniIlmiEsiToRegisterRowStatus_Object = MibTableColumn
mscAtmIfUniIlmiEsiToRegisterRowStatus = _MscAtmIfUniIlmiEsiToRegisterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 2, 288, 1, 2),
    _MscAtmIfUniIlmiEsiToRegisterRowStatus_Type()
)
mscAtmIfUniIlmiEsiToRegisterRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAtmIfUniIlmiEsiToRegisterRowStatus.setStatus("mandatory")
_MscAtmIfUniSig_ObjectIdentity = ObjectIdentity
mscAtmIfUniSig = _MscAtmIfUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3)
)
_MscAtmIfUniSigRowStatusTable_Object = MibTable
mscAtmIfUniSigRowStatusTable = _MscAtmIfUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigRowStatusTable.setStatus("mandatory")
_MscAtmIfUniSigRowStatusEntry_Object = MibTableRow
mscAtmIfUniSigRowStatusEntry = _MscAtmIfUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1, 1)
)
mscAtmIfUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniSigRowStatus_Type = RowStatus
_MscAtmIfUniSigRowStatus_Object = MibTableColumn
mscAtmIfUniSigRowStatus = _MscAtmIfUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1, 1, 1),
    _MscAtmIfUniSigRowStatus_Type()
)
mscAtmIfUniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigRowStatus.setStatus("mandatory")
_MscAtmIfUniSigComponentName_Type = DisplayString
_MscAtmIfUniSigComponentName_Object = MibTableColumn
mscAtmIfUniSigComponentName = _MscAtmIfUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1, 1, 2),
    _MscAtmIfUniSigComponentName_Type()
)
mscAtmIfUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigComponentName.setStatus("mandatory")
_MscAtmIfUniSigStorageType_Type = StorageType
_MscAtmIfUniSigStorageType_Object = MibTableColumn
mscAtmIfUniSigStorageType = _MscAtmIfUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1, 1, 4),
    _MscAtmIfUniSigStorageType_Type()
)
mscAtmIfUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigStorageType.setStatus("mandatory")
_MscAtmIfUniSigIndex_Type = NonReplicated
_MscAtmIfUniSigIndex_Object = MibTableColumn
mscAtmIfUniSigIndex = _MscAtmIfUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 1, 1, 10),
    _MscAtmIfUniSigIndex_Type()
)
mscAtmIfUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniSigIndex.setStatus("mandatory")
_MscAtmIfUniSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfUniSigVcd = _MscAtmIfUniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2)
)
_MscAtmIfUniSigVcdRowStatusTable_Object = MibTable
mscAtmIfUniSigVcdRowStatusTable = _MscAtmIfUniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfUniSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfUniSigVcdRowStatusEntry = _MscAtmIfUniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1, 1)
)
mscAtmIfUniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniSigVcdRowStatus_Type = RowStatus
_MscAtmIfUniSigVcdRowStatus_Object = MibTableColumn
mscAtmIfUniSigVcdRowStatus = _MscAtmIfUniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1, 1, 1),
    _MscAtmIfUniSigVcdRowStatus_Type()
)
mscAtmIfUniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfUniSigVcdComponentName_Type = DisplayString
_MscAtmIfUniSigVcdComponentName_Object = MibTableColumn
mscAtmIfUniSigVcdComponentName = _MscAtmIfUniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1, 1, 2),
    _MscAtmIfUniSigVcdComponentName_Type()
)
mscAtmIfUniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdComponentName.setStatus("mandatory")
_MscAtmIfUniSigVcdStorageType_Type = StorageType
_MscAtmIfUniSigVcdStorageType_Object = MibTableColumn
mscAtmIfUniSigVcdStorageType = _MscAtmIfUniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1, 1, 4),
    _MscAtmIfUniSigVcdStorageType_Type()
)
mscAtmIfUniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdStorageType.setStatus("mandatory")
_MscAtmIfUniSigVcdIndex_Type = NonReplicated
_MscAtmIfUniSigVcdIndex_Object = MibTableColumn
mscAtmIfUniSigVcdIndex = _MscAtmIfUniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 1, 1, 10),
    _MscAtmIfUniSigVcdIndex_Type()
)
mscAtmIfUniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdIndex.setStatus("mandatory")
_MscAtmIfUniSigVcdProvTable_Object = MibTable
mscAtmIfUniSigVcdProvTable = _MscAtmIfUniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdProvTable.setStatus("mandatory")
_MscAtmIfUniSigVcdProvEntry_Object = MibTableRow
mscAtmIfUniSigVcdProvEntry = _MscAtmIfUniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1)
)
mscAtmIfUniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfUniSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdTrafficDescType based on Integer32"""
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


_MscAtmIfUniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfUniSigVcdTrafficDescType = _MscAtmIfUniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 1),
    _MscAtmIfUniSigVcdTrafficDescType_Type()
)
mscAtmIfUniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfUniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdAtmServiceCategory based on Integer32"""
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


_MscAtmIfUniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfUniSigVcdAtmServiceCategory = _MscAtmIfUniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 3),
    _MscAtmIfUniSigVcdAtmServiceCategory_Type()
)
mscAtmIfUniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfUniSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfUniSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfUniSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfUniSigVcdWeight_Object = MibTableColumn
mscAtmIfUniSigVcdWeight = _MscAtmIfUniSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 4),
    _MscAtmIfUniSigVcdWeight_Type()
)
mscAtmIfUniSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdWeight.setStatus("mandatory")


class _MscAtmIfUniSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdQosClass based on Integer32"""
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


_MscAtmIfUniSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdQosClass_Object = MibTableColumn
mscAtmIfUniSigVcdQosClass = _MscAtmIfUniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 21),
    _MscAtmIfUniSigVcdQosClass_Type()
)
mscAtmIfUniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfUniSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdTrafficShaping based on Integer32"""
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


_MscAtmIfUniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfUniSigVcdTrafficShaping = _MscAtmIfUniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 50),
    _MscAtmIfUniSigVcdTrafficShaping_Type()
)
mscAtmIfUniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfUniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_MscAtmIfUniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfUniSigVcdUnshapedTransmitQueueing = _MscAtmIfUniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 60),
    _MscAtmIfUniSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfUniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfUniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdUsageParameterControl based on Integer32"""
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


_MscAtmIfUniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfUniSigVcdUsageParameterControl = _MscAtmIfUniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 10, 1, 70),
    _MscAtmIfUniSigVcdUsageParameterControl_Type()
)
mscAtmIfUniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfUniSigVcdTdpTable_Object = MibTable
mscAtmIfUniSigVcdTdpTable = _MscAtmIfUniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfUniSigVcdTdpEntry_Object = MibTableRow
mscAtmIfUniSigVcdTdpEntry = _MscAtmIfUniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 387, 1)
)
mscAtmIfUniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfUniSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfUniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfUniSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfUniSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfUniSigVcdTdpIndex = _MscAtmIfUniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 387, 1, 1),
    _MscAtmIfUniSigVcdTdpIndex_Type()
)
mscAtmIfUniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfUniSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfUniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfUniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfUniSigVcdTdpValue_Object = MibTableColumn
mscAtmIfUniSigVcdTdpValue = _MscAtmIfUniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 2, 387, 1, 2),
    _MscAtmIfUniSigVcdTdpValue_Type()
)
mscAtmIfUniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfUniSigProvTable_Object = MibTable
mscAtmIfUniSigProvTable = _MscAtmIfUniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigProvTable.setStatus("mandatory")
_MscAtmIfUniSigProvEntry_Object = MibTableRow
mscAtmIfUniSigProvEntry = _MscAtmIfUniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 10, 1)
)
mscAtmIfUniSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigProvEntry.setStatus("mandatory")


class _MscAtmIfUniSigVci_Type(Unsigned32):
    """Custom type mscAtmIfUniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfUniSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfUniSigVci_Object = MibTableColumn
mscAtmIfUniSigVci = _MscAtmIfUniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 10, 1, 1),
    _MscAtmIfUniSigVci_Type()
)
mscAtmIfUniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigVci.setStatus("mandatory")


class _MscAtmIfUniSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfUniSigAddressConversion based on Integer32"""
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


_MscAtmIfUniSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfUniSigAddressConversion_Object = MibTableColumn
mscAtmIfUniSigAddressConversion = _MscAtmIfUniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 10, 1, 2),
    _MscAtmIfUniSigAddressConversion_Type()
)
mscAtmIfUniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigAddressConversion.setStatus("mandatory")


class _MscAtmIfUniSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfUniSigOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("provisionedOnly", 1))
    )


_MscAtmIfUniSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfUniSigOperatingMode_Object = MibTableColumn
mscAtmIfUniSigOperatingMode = _MscAtmIfUniSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 10, 1, 3),
    _MscAtmIfUniSigOperatingMode_Type()
)
mscAtmIfUniSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSigOperatingMode.setStatus("mandatory")
_MscAtmIfUniSigStateTable_Object = MibTable
mscAtmIfUniSigStateTable = _MscAtmIfUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigStateTable.setStatus("mandatory")
_MscAtmIfUniSigStateEntry_Object = MibTableRow
mscAtmIfUniSigStateEntry = _MscAtmIfUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 11, 1)
)
mscAtmIfUniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigStateEntry.setStatus("mandatory")


class _MscAtmIfUniSigAdminState_Type(Integer32):
    """Custom type mscAtmIfUniSigAdminState based on Integer32"""
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


_MscAtmIfUniSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfUniSigAdminState_Object = MibTableColumn
mscAtmIfUniSigAdminState = _MscAtmIfUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 11, 1, 1),
    _MscAtmIfUniSigAdminState_Type()
)
mscAtmIfUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigAdminState.setStatus("mandatory")


class _MscAtmIfUniSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfUniSigOperationalState based on Integer32"""
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


_MscAtmIfUniSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfUniSigOperationalState_Object = MibTableColumn
mscAtmIfUniSigOperationalState = _MscAtmIfUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 11, 1, 2),
    _MscAtmIfUniSigOperationalState_Type()
)
mscAtmIfUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigOperationalState.setStatus("mandatory")


class _MscAtmIfUniSigUsageState_Type(Integer32):
    """Custom type mscAtmIfUniSigUsageState based on Integer32"""
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


_MscAtmIfUniSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfUniSigUsageState_Object = MibTableColumn
mscAtmIfUniSigUsageState = _MscAtmIfUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 11, 1, 3),
    _MscAtmIfUniSigUsageState_Type()
)
mscAtmIfUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigUsageState.setStatus("mandatory")
_MscAtmIfUniSigOperTable_Object = MibTable
mscAtmIfUniSigOperTable = _MscAtmIfUniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigOperTable.setStatus("mandatory")
_MscAtmIfUniSigOperEntry_Object = MibTableRow
mscAtmIfUniSigOperEntry = _MscAtmIfUniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12, 1)
)
mscAtmIfUniSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigOperEntry.setStatus("mandatory")


class _MscAtmIfUniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfUniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfUniSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfUniSigLastTxCauseCode = _MscAtmIfUniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12, 1, 1),
    _MscAtmIfUniSigLastTxCauseCode_Type()
)
mscAtmIfUniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfUniSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfUniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfUniSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfUniSigLastTxDiagCode = _MscAtmIfUniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12, 1, 2),
    _MscAtmIfUniSigLastTxDiagCode_Type()
)
mscAtmIfUniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfUniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfUniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfUniSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfUniSigLastRxCauseCode = _MscAtmIfUniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12, 1, 3),
    _MscAtmIfUniSigLastRxCauseCode_Type()
)
mscAtmIfUniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfUniSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfUniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfUniSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfUniSigLastRxDiagCode = _MscAtmIfUniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 12, 1, 4),
    _MscAtmIfUniSigLastRxDiagCode_Type()
)
mscAtmIfUniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfUniSigStatsTable_Object = MibTable
mscAtmIfUniSigStatsTable = _MscAtmIfUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigStatsTable.setStatus("mandatory")
_MscAtmIfUniSigStatsEntry_Object = MibTableRow
mscAtmIfUniSigStatsEntry = _MscAtmIfUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1)
)
mscAtmIfUniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniSigStatsEntry.setStatus("mandatory")
_MscAtmIfUniSigCurrentConnections_Type = Counter32
_MscAtmIfUniSigCurrentConnections_Object = MibTableColumn
mscAtmIfUniSigCurrentConnections = _MscAtmIfUniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 1),
    _MscAtmIfUniSigCurrentConnections_Type()
)
mscAtmIfUniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfUniSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfUniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniSigPeakConnections_Object = MibTableColumn
mscAtmIfUniSigPeakConnections = _MscAtmIfUniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 2),
    _MscAtmIfUniSigPeakConnections_Type()
)
mscAtmIfUniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigPeakConnections.setStatus("mandatory")
_MscAtmIfUniSigSuccessfulConnections_Type = Counter32
_MscAtmIfUniSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfUniSigSuccessfulConnections = _MscAtmIfUniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 3),
    _MscAtmIfUniSigSuccessfulConnections_Type()
)
mscAtmIfUniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfUniSigFailedConnections_Type = Counter32
_MscAtmIfUniSigFailedConnections_Object = MibTableColumn
mscAtmIfUniSigFailedConnections = _MscAtmIfUniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 4),
    _MscAtmIfUniSigFailedConnections_Type()
)
mscAtmIfUniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigFailedConnections.setStatus("mandatory")
_MscAtmIfUniSigTxPdus_Type = Counter32
_MscAtmIfUniSigTxPdus_Object = MibTableColumn
mscAtmIfUniSigTxPdus = _MscAtmIfUniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 5),
    _MscAtmIfUniSigTxPdus_Type()
)
mscAtmIfUniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigTxPdus.setStatus("mandatory")
_MscAtmIfUniSigRxPdus_Type = Counter32
_MscAtmIfUniSigRxPdus_Object = MibTableColumn
mscAtmIfUniSigRxPdus = _MscAtmIfUniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 6),
    _MscAtmIfUniSigRxPdus_Type()
)
mscAtmIfUniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigRxPdus.setStatus("mandatory")


class _MscAtmIfUniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfUniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfUniSigCurrentPmpConnections = _MscAtmIfUniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 7),
    _MscAtmIfUniSigCurrentPmpConnections_Type()
)
mscAtmIfUniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfUniSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfUniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfUniSigPeakPmpConnections = _MscAtmIfUniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 8),
    _MscAtmIfUniSigPeakPmpConnections_Type()
)
mscAtmIfUniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfUniSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfUniSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfUniSigSuccessfulPmpConnections = _MscAtmIfUniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 9),
    _MscAtmIfUniSigSuccessfulPmpConnections_Type()
)
mscAtmIfUniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfUniSigFailedPmpConnections_Type = Counter32
_MscAtmIfUniSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfUniSigFailedPmpConnections = _MscAtmIfUniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 10),
    _MscAtmIfUniSigFailedPmpConnections_Type()
)
mscAtmIfUniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfUniSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfUniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfUniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfUniSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfUniSigNewCurrentConnections = _MscAtmIfUniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 3, 13, 1, 11),
    _MscAtmIfUniSigNewCurrentConnections_Type()
)
mscAtmIfUniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfUniAddr_ObjectIdentity = ObjectIdentity
mscAtmIfUniAddr = _MscAtmIfUniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4)
)
_MscAtmIfUniAddrRowStatusTable_Object = MibTable
mscAtmIfUniAddrRowStatusTable = _MscAtmIfUniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniAddrRowStatusEntry_Object = MibTableRow
mscAtmIfUniAddrRowStatusEntry = _MscAtmIfUniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1)
)
mscAtmIfUniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniAddrRowStatus_Type = RowStatus
_MscAtmIfUniAddrRowStatus_Object = MibTableColumn
mscAtmIfUniAddrRowStatus = _MscAtmIfUniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1, 1),
    _MscAtmIfUniAddrRowStatus_Type()
)
mscAtmIfUniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrRowStatus.setStatus("mandatory")
_MscAtmIfUniAddrComponentName_Type = DisplayString
_MscAtmIfUniAddrComponentName_Object = MibTableColumn
mscAtmIfUniAddrComponentName = _MscAtmIfUniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1, 2),
    _MscAtmIfUniAddrComponentName_Type()
)
mscAtmIfUniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrComponentName.setStatus("mandatory")
_MscAtmIfUniAddrStorageType_Type = StorageType
_MscAtmIfUniAddrStorageType_Object = MibTableColumn
mscAtmIfUniAddrStorageType = _MscAtmIfUniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1, 4),
    _MscAtmIfUniAddrStorageType_Type()
)
mscAtmIfUniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrStorageType.setStatus("mandatory")


class _MscAtmIfUniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfUniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfUniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfUniAddrAddressIndex_Object = MibTableColumn
mscAtmIfUniAddrAddressIndex = _MscAtmIfUniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1, 10),
    _MscAtmIfUniAddrAddressIndex_Type()
)
mscAtmIfUniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfUniAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfUniAddrAddressTypeIndex based on Integer32"""
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


_MscAtmIfUniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfUniAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfUniAddrAddressTypeIndex = _MscAtmIfUniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 1, 1, 11),
    _MscAtmIfUniAddrAddressTypeIndex_Type()
)
mscAtmIfUniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfUniAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfUniAddrTermSP = _MscAtmIfUniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2)
)
_MscAtmIfUniAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfUniAddrTermSPRowStatusTable = _MscAtmIfUniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfUniAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfUniAddrTermSPRowStatusEntry = _MscAtmIfUniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1, 1)
)
mscAtmIfUniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfUniAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfUniAddrTermSPRowStatus = _MscAtmIfUniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1, 1, 1),
    _MscAtmIfUniAddrTermSPRowStatus_Type()
)
mscAtmIfUniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfUniAddrTermSPComponentName_Type = DisplayString
_MscAtmIfUniAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfUniAddrTermSPComponentName = _MscAtmIfUniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1, 1, 2),
    _MscAtmIfUniAddrTermSPComponentName_Type()
)
mscAtmIfUniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfUniAddrTermSPStorageType_Type = StorageType
_MscAtmIfUniAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfUniAddrTermSPStorageType = _MscAtmIfUniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1, 1, 4),
    _MscAtmIfUniAddrTermSPStorageType_Type()
)
mscAtmIfUniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfUniAddrTermSPIndex_Type = NonReplicated
_MscAtmIfUniAddrTermSPIndex_Object = MibTableColumn
mscAtmIfUniAddrTermSPIndex = _MscAtmIfUniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 2, 1, 1, 10),
    _MscAtmIfUniAddrTermSPIndex_Type()
)
mscAtmIfUniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfUniAddrPnniInfo = _MscAtmIfUniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3)
)
_MscAtmIfUniAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfUniAddrPnniInfoRowStatusTable = _MscAtmIfUniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfUniAddrPnniInfoRowStatusEntry = _MscAtmIfUniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1, 1)
)
mscAtmIfUniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfUniAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoRowStatus = _MscAtmIfUniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1, 1, 1),
    _MscAtmIfUniAddrPnniInfoRowStatus_Type()
)
mscAtmIfUniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfUniAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoComponentName = _MscAtmIfUniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1, 1, 2),
    _MscAtmIfUniAddrPnniInfoComponentName_Type()
)
mscAtmIfUniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfUniAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoStorageType = _MscAtmIfUniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1, 1, 4),
    _MscAtmIfUniAddrPnniInfoStorageType_Type()
)
mscAtmIfUniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfUniAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoIndex = _MscAtmIfUniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 1, 1, 10),
    _MscAtmIfUniAddrPnniInfoIndex_Type()
)
mscAtmIfUniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoProvTable_Object = MibTable
mscAtmIfUniAddrPnniInfoProvTable = _MscAtmIfUniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfUniAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfUniAddrPnniInfoProvEntry = _MscAtmIfUniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 10, 1)
)
mscAtmIfUniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfUniAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfUniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfUniAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfUniAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoScope = _MscAtmIfUniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 10, 1, 1),
    _MscAtmIfUniAddrPnniInfoScope_Type()
)
mscAtmIfUniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfUniAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfUniAddrPnniInfoReachability based on Integer32"""
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


_MscAtmIfUniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfUniAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfUniAddrPnniInfoReachability = _MscAtmIfUniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 3, 10, 1, 2),
    _MscAtmIfUniAddrPnniInfoReachability_Type()
)
mscAtmIfUniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfUniAddrOperTable_Object = MibTable
mscAtmIfUniAddrOperTable = _MscAtmIfUniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrOperTable.setStatus("mandatory")
_MscAtmIfUniAddrOperEntry_Object = MibTableRow
mscAtmIfUniAddrOperEntry = _MscAtmIfUniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 10, 1)
)
mscAtmIfUniAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAddrOperEntry.setStatus("mandatory")


class _MscAtmIfUniAddrScope_Type(Integer32):
    """Custom type mscAtmIfUniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfUniAddrScope_Type.__name__ = "Integer32"
_MscAtmIfUniAddrScope_Object = MibTableColumn
mscAtmIfUniAddrScope = _MscAtmIfUniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 10, 1, 1),
    _MscAtmIfUniAddrScope_Type()
)
mscAtmIfUniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrScope.setStatus("mandatory")


class _MscAtmIfUniAddrReachability_Type(Integer32):
    """Custom type mscAtmIfUniAddrReachability based on Integer32"""
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


_MscAtmIfUniAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfUniAddrReachability_Object = MibTableColumn
mscAtmIfUniAddrReachability = _MscAtmIfUniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 4, 10, 1, 2),
    _MscAtmIfUniAddrReachability_Type()
)
mscAtmIfUniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniAddrReachability.setStatus("mandatory")
_MscAtmIfUniCallingAScr_ObjectIdentity = ObjectIdentity
mscAtmIfUniCallingAScr = _MscAtmIfUniCallingAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5)
)
_MscAtmIfUniCallingAScrRowStatusTable_Object = MibTable
mscAtmIfUniCallingAScrRowStatusTable = _MscAtmIfUniCallingAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniCallingAScrRowStatusEntry_Object = MibTableRow
mscAtmIfUniCallingAScrRowStatusEntry = _MscAtmIfUniCallingAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1, 1)
)
mscAtmIfUniCallingAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniCallingAScrRowStatus_Type = RowStatus
_MscAtmIfUniCallingAScrRowStatus_Object = MibTableColumn
mscAtmIfUniCallingAScrRowStatus = _MscAtmIfUniCallingAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1, 1, 1),
    _MscAtmIfUniCallingAScrRowStatus_Type()
)
mscAtmIfUniCallingAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrRowStatus.setStatus("mandatory")
_MscAtmIfUniCallingAScrComponentName_Type = DisplayString
_MscAtmIfUniCallingAScrComponentName_Object = MibTableColumn
mscAtmIfUniCallingAScrComponentName = _MscAtmIfUniCallingAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1, 1, 2),
    _MscAtmIfUniCallingAScrComponentName_Type()
)
mscAtmIfUniCallingAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrComponentName.setStatus("mandatory")
_MscAtmIfUniCallingAScrStorageType_Type = StorageType
_MscAtmIfUniCallingAScrStorageType_Object = MibTableColumn
mscAtmIfUniCallingAScrStorageType = _MscAtmIfUniCallingAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1, 1, 4),
    _MscAtmIfUniCallingAScrStorageType_Type()
)
mscAtmIfUniCallingAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrStorageType.setStatus("mandatory")
_MscAtmIfUniCallingAScrIndex_Type = NonReplicated
_MscAtmIfUniCallingAScrIndex_Object = MibTableColumn
mscAtmIfUniCallingAScrIndex = _MscAtmIfUniCallingAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 1, 1, 10),
    _MscAtmIfUniCallingAScrIndex_Type()
)
mscAtmIfUniCallingAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrIndex.setStatus("mandatory")
_MscAtmIfUniCallingAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfUniCallingAScrAddr = _MscAtmIfUniCallingAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2)
)
_MscAtmIfUniCallingAScrAddrRowStatusTable_Object = MibTable
mscAtmIfUniCallingAScrAddrRowStatusTable = _MscAtmIfUniCallingAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniCallingAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfUniCallingAScrAddrRowStatusEntry = _MscAtmIfUniCallingAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1)
)
mscAtmIfUniCallingAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniCallingAScrAddrRowStatus_Type = RowStatus
_MscAtmIfUniCallingAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfUniCallingAScrAddrRowStatus = _MscAtmIfUniCallingAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1, 1),
    _MscAtmIfUniCallingAScrAddrRowStatus_Type()
)
mscAtmIfUniCallingAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfUniCallingAScrAddrComponentName_Type = DisplayString
_MscAtmIfUniCallingAScrAddrComponentName_Object = MibTableColumn
mscAtmIfUniCallingAScrAddrComponentName = _MscAtmIfUniCallingAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1, 2),
    _MscAtmIfUniCallingAScrAddrComponentName_Type()
)
mscAtmIfUniCallingAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfUniCallingAScrAddrStorageType_Type = StorageType
_MscAtmIfUniCallingAScrAddrStorageType_Object = MibTableColumn
mscAtmIfUniCallingAScrAddrStorageType = _MscAtmIfUniCallingAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1, 4),
    _MscAtmIfUniCallingAScrAddrStorageType_Type()
)
mscAtmIfUniCallingAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfUniCallingAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfUniCallingAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfUniCallingAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfUniCallingAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfUniCallingAScrAddrAddressIndex = _MscAtmIfUniCallingAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1, 10),
    _MscAtmIfUniCallingAScrAddrAddressIndex_Type()
)
mscAtmIfUniCallingAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfUniCallingAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfUniCallingAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfUniCallingAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfUniCallingAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfUniCallingAScrAddrAddressActionIndex = _MscAtmIfUniCallingAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 2, 1, 1, 11),
    _MscAtmIfUniCallingAScrAddrAddressActionIndex_Type()
)
mscAtmIfUniCallingAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfUniCallingAScrProvTable_Object = MibTable
mscAtmIfUniCallingAScrProvTable = _MscAtmIfUniCallingAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrProvTable.setStatus("mandatory")
_MscAtmIfUniCallingAScrProvEntry_Object = MibTableRow
mscAtmIfUniCallingAScrProvEntry = _MscAtmIfUniCallingAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 10, 1)
)
mscAtmIfUniCallingAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrProvEntry.setStatus("mandatory")


class _MscAtmIfUniCallingAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfUniCallingAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfUniCallingAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfUniCallingAScrAdminStatus_Object = MibTableColumn
mscAtmIfUniCallingAScrAdminStatus = _MscAtmIfUniCallingAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 10, 1, 1),
    _MscAtmIfUniCallingAScrAdminStatus_Type()
)
mscAtmIfUniCallingAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAdminStatus.setStatus("mandatory")


class _MscAtmIfUniCallingAScrDefaultInsertionAddress_Type(HexString):
    """Custom type mscAtmIfUniCallingAScrDefaultInsertionAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfUniCallingAScrDefaultInsertionAddress_Type.__name__ = "HexString"
_MscAtmIfUniCallingAScrDefaultInsertionAddress_Object = MibTableColumn
mscAtmIfUniCallingAScrDefaultInsertionAddress = _MscAtmIfUniCallingAScrDefaultInsertionAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 10, 1, 2),
    _MscAtmIfUniCallingAScrDefaultInsertionAddress_Type()
)
mscAtmIfUniCallingAScrDefaultInsertionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrDefaultInsertionAddress.setStatus("mandatory")
_MscAtmIfUniCallingAScrStatTable_Object = MibTable
mscAtmIfUniCallingAScrStatTable = _MscAtmIfUniCallingAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrStatTable.setStatus("mandatory")
_MscAtmIfUniCallingAScrStatEntry_Object = MibTableRow
mscAtmIfUniCallingAScrStatEntry = _MscAtmIfUniCallingAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 11, 1)
)
mscAtmIfUniCallingAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrStatEntry.setStatus("mandatory")
_MscAtmIfUniCallingAScrAcceptedCalls_Type = Counter32
_MscAtmIfUniCallingAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfUniCallingAScrAcceptedCalls = _MscAtmIfUniCallingAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 11, 1, 1),
    _MscAtmIfUniCallingAScrAcceptedCalls_Type()
)
mscAtmIfUniCallingAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfUniCallingAScrRejectedCalls_Type = Counter32
_MscAtmIfUniCallingAScrRejectedCalls_Object = MibTableColumn
mscAtmIfUniCallingAScrRejectedCalls = _MscAtmIfUniCallingAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 11, 1, 2),
    _MscAtmIfUniCallingAScrRejectedCalls_Type()
)
mscAtmIfUniCallingAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfUniCallingAScrUnmatchedCalls_Type = Counter32
_MscAtmIfUniCallingAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfUniCallingAScrUnmatchedCalls = _MscAtmIfUniCallingAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 5, 11, 1, 3),
    _MscAtmIfUniCallingAScrUnmatchedCalls_Type()
)
mscAtmIfUniCallingAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCallingAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfUniCalledAScr_ObjectIdentity = ObjectIdentity
mscAtmIfUniCalledAScr = _MscAtmIfUniCalledAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6)
)
_MscAtmIfUniCalledAScrRowStatusTable_Object = MibTable
mscAtmIfUniCalledAScrRowStatusTable = _MscAtmIfUniCalledAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniCalledAScrRowStatusEntry_Object = MibTableRow
mscAtmIfUniCalledAScrRowStatusEntry = _MscAtmIfUniCalledAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1, 1)
)
mscAtmIfUniCalledAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniCalledAScrRowStatus_Type = RowStatus
_MscAtmIfUniCalledAScrRowStatus_Object = MibTableColumn
mscAtmIfUniCalledAScrRowStatus = _MscAtmIfUniCalledAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1, 1, 1),
    _MscAtmIfUniCalledAScrRowStatus_Type()
)
mscAtmIfUniCalledAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrRowStatus.setStatus("mandatory")
_MscAtmIfUniCalledAScrComponentName_Type = DisplayString
_MscAtmIfUniCalledAScrComponentName_Object = MibTableColumn
mscAtmIfUniCalledAScrComponentName = _MscAtmIfUniCalledAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1, 1, 2),
    _MscAtmIfUniCalledAScrComponentName_Type()
)
mscAtmIfUniCalledAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrComponentName.setStatus("mandatory")
_MscAtmIfUniCalledAScrStorageType_Type = StorageType
_MscAtmIfUniCalledAScrStorageType_Object = MibTableColumn
mscAtmIfUniCalledAScrStorageType = _MscAtmIfUniCalledAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1, 1, 4),
    _MscAtmIfUniCalledAScrStorageType_Type()
)
mscAtmIfUniCalledAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrStorageType.setStatus("mandatory")
_MscAtmIfUniCalledAScrIndex_Type = NonReplicated
_MscAtmIfUniCalledAScrIndex_Object = MibTableColumn
mscAtmIfUniCalledAScrIndex = _MscAtmIfUniCalledAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 1, 1, 10),
    _MscAtmIfUniCalledAScrIndex_Type()
)
mscAtmIfUniCalledAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrIndex.setStatus("mandatory")
_MscAtmIfUniCalledAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfUniCalledAScrAddr = _MscAtmIfUniCalledAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2)
)
_MscAtmIfUniCalledAScrAddrRowStatusTable_Object = MibTable
mscAtmIfUniCalledAScrAddrRowStatusTable = _MscAtmIfUniCalledAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfUniCalledAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfUniCalledAScrAddrRowStatusEntry = _MscAtmIfUniCalledAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1)
)
mscAtmIfUniCalledAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfUniCalledAScrAddrRowStatus_Type = RowStatus
_MscAtmIfUniCalledAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfUniCalledAScrAddrRowStatus = _MscAtmIfUniCalledAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1, 1),
    _MscAtmIfUniCalledAScrAddrRowStatus_Type()
)
mscAtmIfUniCalledAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfUniCalledAScrAddrComponentName_Type = DisplayString
_MscAtmIfUniCalledAScrAddrComponentName_Object = MibTableColumn
mscAtmIfUniCalledAScrAddrComponentName = _MscAtmIfUniCalledAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1, 2),
    _MscAtmIfUniCalledAScrAddrComponentName_Type()
)
mscAtmIfUniCalledAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfUniCalledAScrAddrStorageType_Type = StorageType
_MscAtmIfUniCalledAScrAddrStorageType_Object = MibTableColumn
mscAtmIfUniCalledAScrAddrStorageType = _MscAtmIfUniCalledAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1, 4),
    _MscAtmIfUniCalledAScrAddrStorageType_Type()
)
mscAtmIfUniCalledAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfUniCalledAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfUniCalledAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfUniCalledAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfUniCalledAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfUniCalledAScrAddrAddressIndex = _MscAtmIfUniCalledAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1, 10),
    _MscAtmIfUniCalledAScrAddrAddressIndex_Type()
)
mscAtmIfUniCalledAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfUniCalledAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfUniCalledAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfUniCalledAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfUniCalledAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfUniCalledAScrAddrAddressActionIndex = _MscAtmIfUniCalledAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 2, 1, 1, 11),
    _MscAtmIfUniCalledAScrAddrAddressActionIndex_Type()
)
mscAtmIfUniCalledAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfUniCalledAScrProvTable_Object = MibTable
mscAtmIfUniCalledAScrProvTable = _MscAtmIfUniCalledAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrProvTable.setStatus("mandatory")
_MscAtmIfUniCalledAScrProvEntry_Object = MibTableRow
mscAtmIfUniCalledAScrProvEntry = _MscAtmIfUniCalledAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 10, 1)
)
mscAtmIfUniCalledAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrProvEntry.setStatus("mandatory")


class _MscAtmIfUniCalledAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfUniCalledAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfUniCalledAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfUniCalledAScrAdminStatus_Object = MibTableColumn
mscAtmIfUniCalledAScrAdminStatus = _MscAtmIfUniCalledAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 10, 1, 1),
    _MscAtmIfUniCalledAScrAdminStatus_Type()
)
mscAtmIfUniCalledAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAdminStatus.setStatus("mandatory")
_MscAtmIfUniCalledAScrStatTable_Object = MibTable
mscAtmIfUniCalledAScrStatTable = _MscAtmIfUniCalledAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrStatTable.setStatus("mandatory")
_MscAtmIfUniCalledAScrStatEntry_Object = MibTableRow
mscAtmIfUniCalledAScrStatEntry = _MscAtmIfUniCalledAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 11, 1)
)
mscAtmIfUniCalledAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrStatEntry.setStatus("mandatory")
_MscAtmIfUniCalledAScrAcceptedCalls_Type = Counter32
_MscAtmIfUniCalledAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfUniCalledAScrAcceptedCalls = _MscAtmIfUniCalledAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 11, 1, 1),
    _MscAtmIfUniCalledAScrAcceptedCalls_Type()
)
mscAtmIfUniCalledAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfUniCalledAScrRejectedCalls_Type = Counter32
_MscAtmIfUniCalledAScrRejectedCalls_Object = MibTableColumn
mscAtmIfUniCalledAScrRejectedCalls = _MscAtmIfUniCalledAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 11, 1, 2),
    _MscAtmIfUniCalledAScrRejectedCalls_Type()
)
mscAtmIfUniCalledAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfUniCalledAScrUnmatchedCalls_Type = Counter32
_MscAtmIfUniCalledAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfUniCalledAScrUnmatchedCalls = _MscAtmIfUniCalledAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 6, 11, 1, 3),
    _MscAtmIfUniCalledAScrUnmatchedCalls_Type()
)
mscAtmIfUniCalledAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniCalledAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfUniProvTable_Object = MibTable
mscAtmIfUniProvTable = _MscAtmIfUniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfUniProvTable.setStatus("mandatory")
_MscAtmIfUniProvEntry_Object = MibTableRow
mscAtmIfUniProvEntry = _MscAtmIfUniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1)
)
mscAtmIfUniProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniProvEntry.setStatus("mandatory")


class _MscAtmIfUniVersion_Type(Integer32):
    """Custom type mscAtmIfUniVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atmForum30", 0),
          ("atmForum31", 1),
          ("atmForum40", 5))
    )


_MscAtmIfUniVersion_Type.__name__ = "Integer32"
_MscAtmIfUniVersion_Object = MibTableColumn
mscAtmIfUniVersion = _MscAtmIfUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 1),
    _MscAtmIfUniVersion_Type()
)
mscAtmIfUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniVersion.setStatus("mandatory")


class _MscAtmIfUniSide_Type(Integer32):
    """Custom type mscAtmIfUniSide based on Integer32"""
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


_MscAtmIfUniSide_Type.__name__ = "Integer32"
_MscAtmIfUniSide_Object = MibTableColumn
mscAtmIfUniSide = _MscAtmIfUniSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 2),
    _MscAtmIfUniSide_Type()
)
mscAtmIfUniSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSide.setStatus("mandatory")


class _MscAtmIfUniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfUniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfUniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfUniSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfUniSoftPvcRetryPeriod = _MscAtmIfUniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 3),
    _MscAtmIfUniSoftPvcRetryPeriod_Type()
)
mscAtmIfUniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfUniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfUniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfUniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfUniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfUniSoftPvpAndPvcRetryPeriod = _MscAtmIfUniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 4),
    _MscAtmIfUniSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfUniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfUniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfUniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfUniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfUniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfUniSoftPvpAndPvcHoldOffTime = _MscAtmIfUniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 5),
    _MscAtmIfUniSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfUniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")


class _MscAtmIfUniLoopPrevention_Type(Integer32):
    """Custom type mscAtmIfUniLoopPrevention based on Integer32"""
    defaultValue = 1

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


_MscAtmIfUniLoopPrevention_Type.__name__ = "Integer32"
_MscAtmIfUniLoopPrevention_Object = MibTableColumn
mscAtmIfUniLoopPrevention = _MscAtmIfUniLoopPrevention_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 10, 1, 6),
    _MscAtmIfUniLoopPrevention_Type()
)
mscAtmIfUniLoopPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniLoopPrevention.setStatus("mandatory")
_MscAtmIfUniOperTable_Object = MibTable
mscAtmIfUniOperTable = _MscAtmIfUniOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfUniOperTable.setStatus("mandatory")
_MscAtmIfUniOperEntry_Object = MibTableRow
mscAtmIfUniOperEntry = _MscAtmIfUniOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 11, 1)
)
mscAtmIfUniOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniOperEntry.setStatus("mandatory")


class _MscAtmIfUniMacAddress_Type(AsciiString):
    """Custom type mscAtmIfUniMacAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_MscAtmIfUniMacAddress_Type.__name__ = "AsciiString"
_MscAtmIfUniMacAddress_Object = MibTableColumn
mscAtmIfUniMacAddress = _MscAtmIfUniMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 11, 1, 1),
    _MscAtmIfUniMacAddress_Type()
)
mscAtmIfUniMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfUniMacAddress.setStatus("mandatory")
_MscAtmIfUniAcctOptTable_Object = MibTable
mscAtmIfUniAcctOptTable = _MscAtmIfUniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfUniAcctOptTable.setStatus("mandatory")
_MscAtmIfUniAcctOptEntry_Object = MibTableRow
mscAtmIfUniAcctOptEntry = _MscAtmIfUniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12, 1)
)
mscAtmIfUniAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfUniAcctOptEntry.setStatus("mandatory")


class _MscAtmIfUniAccountCollection_Type(OctetString):
    """Custom type mscAtmIfUniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfUniAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfUniAccountCollection_Object = MibTableColumn
mscAtmIfUniAccountCollection = _MscAtmIfUniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12, 1, 1),
    _MscAtmIfUniAccountCollection_Type()
)
mscAtmIfUniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAccountCollection.setStatus("mandatory")


class _MscAtmIfUniAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfUniAccountConnectionType based on Integer32"""
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


_MscAtmIfUniAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfUniAccountConnectionType_Object = MibTableColumn
mscAtmIfUniAccountConnectionType = _MscAtmIfUniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12, 1, 2),
    _MscAtmIfUniAccountConnectionType_Type()
)
mscAtmIfUniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAccountConnectionType.setStatus("mandatory")


class _MscAtmIfUniAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfUniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfUniAccountClass_Object = MibTableColumn
mscAtmIfUniAccountClass = _MscAtmIfUniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12, 1, 3),
    _MscAtmIfUniAccountClass_Type()
)
mscAtmIfUniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniAccountClass.setStatus("mandatory")


class _MscAtmIfUniServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfUniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfUniServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfUniServiceExchange_Object = MibTableColumn
mscAtmIfUniServiceExchange = _MscAtmIfUniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 6, 12, 1, 4),
    _MscAtmIfUniServiceExchange_Type()
)
mscAtmIfUniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfUniServiceExchange.setStatus("mandatory")
_MscAtmIfVptUni_ObjectIdentity = ObjectIdentity
mscAtmIfVptUni = _MscAtmIfVptUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8)
)
_MscAtmIfVptUniRowStatusTable_Object = MibTable
mscAtmIfVptUniRowStatusTable = _MscAtmIfVptUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniRowStatusEntry = _MscAtmIfVptUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1, 1)
)
mscAtmIfVptUniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniRowStatus_Type = RowStatus
_MscAtmIfVptUniRowStatus_Object = MibTableColumn
mscAtmIfVptUniRowStatus = _MscAtmIfVptUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1, 1, 1),
    _MscAtmIfVptUniRowStatus_Type()
)
mscAtmIfVptUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniRowStatus.setStatus("mandatory")
_MscAtmIfVptUniComponentName_Type = DisplayString
_MscAtmIfVptUniComponentName_Object = MibTableColumn
mscAtmIfVptUniComponentName = _MscAtmIfVptUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1, 1, 2),
    _MscAtmIfVptUniComponentName_Type()
)
mscAtmIfVptUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniComponentName.setStatus("mandatory")
_MscAtmIfVptUniStorageType_Type = StorageType
_MscAtmIfVptUniStorageType_Object = MibTableColumn
mscAtmIfVptUniStorageType = _MscAtmIfVptUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1, 1, 4),
    _MscAtmIfVptUniStorageType_Type()
)
mscAtmIfVptUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniStorageType.setStatus("mandatory")
_MscAtmIfVptUniIndex_Type = NonReplicated
_MscAtmIfVptUniIndex_Object = MibTableColumn
mscAtmIfVptUniIndex = _MscAtmIfVptUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 1, 1, 10),
    _MscAtmIfVptUniIndex_Type()
)
mscAtmIfVptUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniIndex.setStatus("mandatory")
_MscAtmIfVptUniSig_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniSig = _MscAtmIfVptUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2)
)
_MscAtmIfVptUniSigRowStatusTable_Object = MibTable
mscAtmIfVptUniSigRowStatusTable = _MscAtmIfVptUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniSigRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniSigRowStatusEntry = _MscAtmIfVptUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1, 1)
)
mscAtmIfVptUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniSigRowStatus_Type = RowStatus
_MscAtmIfVptUniSigRowStatus_Object = MibTableColumn
mscAtmIfVptUniSigRowStatus = _MscAtmIfVptUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1, 1, 1),
    _MscAtmIfVptUniSigRowStatus_Type()
)
mscAtmIfVptUniSigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigRowStatus.setStatus("mandatory")
_MscAtmIfVptUniSigComponentName_Type = DisplayString
_MscAtmIfVptUniSigComponentName_Object = MibTableColumn
mscAtmIfVptUniSigComponentName = _MscAtmIfVptUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1, 1, 2),
    _MscAtmIfVptUniSigComponentName_Type()
)
mscAtmIfVptUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigComponentName.setStatus("mandatory")
_MscAtmIfVptUniSigStorageType_Type = StorageType
_MscAtmIfVptUniSigStorageType_Object = MibTableColumn
mscAtmIfVptUniSigStorageType = _MscAtmIfVptUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1, 1, 4),
    _MscAtmIfVptUniSigStorageType_Type()
)
mscAtmIfVptUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigStorageType.setStatus("mandatory")
_MscAtmIfVptUniSigIndex_Type = NonReplicated
_MscAtmIfVptUniSigIndex_Object = MibTableColumn
mscAtmIfVptUniSigIndex = _MscAtmIfVptUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 1, 1, 10),
    _MscAtmIfVptUniSigIndex_Type()
)
mscAtmIfVptUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigIndex.setStatus("mandatory")
_MscAtmIfVptUniSigVcd_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniSigVcd = _MscAtmIfVptUniSigVcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2)
)
_MscAtmIfVptUniSigVcdRowStatusTable_Object = MibTable
mscAtmIfVptUniSigVcdRowStatusTable = _MscAtmIfVptUniSigVcdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniSigVcdRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniSigVcdRowStatusEntry = _MscAtmIfVptUniSigVcdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1, 1)
)
mscAtmIfVptUniSigVcdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniSigVcdRowStatus_Type = RowStatus
_MscAtmIfVptUniSigVcdRowStatus_Object = MibTableColumn
mscAtmIfVptUniSigVcdRowStatus = _MscAtmIfVptUniSigVcdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1, 1, 1),
    _MscAtmIfVptUniSigVcdRowStatus_Type()
)
mscAtmIfVptUniSigVcdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdRowStatus.setStatus("mandatory")
_MscAtmIfVptUniSigVcdComponentName_Type = DisplayString
_MscAtmIfVptUniSigVcdComponentName_Object = MibTableColumn
mscAtmIfVptUniSigVcdComponentName = _MscAtmIfVptUniSigVcdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1, 1, 2),
    _MscAtmIfVptUniSigVcdComponentName_Type()
)
mscAtmIfVptUniSigVcdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdComponentName.setStatus("mandatory")
_MscAtmIfVptUniSigVcdStorageType_Type = StorageType
_MscAtmIfVptUniSigVcdStorageType_Object = MibTableColumn
mscAtmIfVptUniSigVcdStorageType = _MscAtmIfVptUniSigVcdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1, 1, 4),
    _MscAtmIfVptUniSigVcdStorageType_Type()
)
mscAtmIfVptUniSigVcdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdStorageType.setStatus("mandatory")
_MscAtmIfVptUniSigVcdIndex_Type = NonReplicated
_MscAtmIfVptUniSigVcdIndex_Object = MibTableColumn
mscAtmIfVptUniSigVcdIndex = _MscAtmIfVptUniSigVcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 1, 1, 10),
    _MscAtmIfVptUniSigVcdIndex_Type()
)
mscAtmIfVptUniSigVcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdIndex.setStatus("mandatory")
_MscAtmIfVptUniSigVcdProvTable_Object = MibTable
mscAtmIfVptUniSigVcdProvTable = _MscAtmIfVptUniSigVcdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdProvTable.setStatus("mandatory")
_MscAtmIfVptUniSigVcdProvEntry_Object = MibTableRow
mscAtmIfVptUniSigVcdProvEntry = _MscAtmIfVptUniSigVcdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1)
)
mscAtmIfVptUniSigVcdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigVcdIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdTrafficDescType_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdTrafficDescType based on Integer32"""
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


_MscAtmIfVptUniSigVcdTrafficDescType_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdTrafficDescType_Object = MibTableColumn
mscAtmIfVptUniSigVcdTrafficDescType = _MscAtmIfVptUniSigVcdTrafficDescType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 1),
    _MscAtmIfVptUniSigVcdTrafficDescType_Type()
)
mscAtmIfVptUniSigVcdTrafficDescType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTrafficDescType.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdAtmServiceCategory_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdAtmServiceCategory based on Integer32"""
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


_MscAtmIfVptUniSigVcdAtmServiceCategory_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdAtmServiceCategory_Object = MibTableColumn
mscAtmIfVptUniSigVcdAtmServiceCategory = _MscAtmIfVptUniSigVcdAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 3),
    _MscAtmIfVptUniSigVcdAtmServiceCategory_Type()
)
mscAtmIfVptUniSigVcdAtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdAtmServiceCategory.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdWeight_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSigVcdWeight based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_MscAtmIfVptUniSigVcdWeight_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSigVcdWeight_Object = MibTableColumn
mscAtmIfVptUniSigVcdWeight = _MscAtmIfVptUniSigVcdWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 4),
    _MscAtmIfVptUniSigVcdWeight_Type()
)
mscAtmIfVptUniSigVcdWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdWeight.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdQosClass_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdQosClass based on Integer32"""
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


_MscAtmIfVptUniSigVcdQosClass_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdQosClass_Object = MibTableColumn
mscAtmIfVptUniSigVcdQosClass = _MscAtmIfVptUniSigVcdQosClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 21),
    _MscAtmIfVptUniSigVcdQosClass_Type()
)
mscAtmIfVptUniSigVcdQosClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdQosClass.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdTrafficShaping_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdTrafficShaping based on Integer32"""
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


_MscAtmIfVptUniSigVcdTrafficShaping_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdTrafficShaping_Object = MibTableColumn
mscAtmIfVptUniSigVcdTrafficShaping = _MscAtmIfVptUniSigVcdTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 50),
    _MscAtmIfVptUniSigVcdTrafficShaping_Type()
)
mscAtmIfVptUniSigVcdTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTrafficShaping.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdUnshapedTransmitQueueing_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdUnshapedTransmitQueueing based on Integer32"""
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


_MscAtmIfVptUniSigVcdUnshapedTransmitQueueing_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdUnshapedTransmitQueueing_Object = MibTableColumn
mscAtmIfVptUniSigVcdUnshapedTransmitQueueing = _MscAtmIfVptUniSigVcdUnshapedTransmitQueueing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 60),
    _MscAtmIfVptUniSigVcdUnshapedTransmitQueueing_Type()
)
mscAtmIfVptUniSigVcdUnshapedTransmitQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdUnshapedTransmitQueueing.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdUsageParameterControl_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdUsageParameterControl based on Integer32"""
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


_MscAtmIfVptUniSigVcdUsageParameterControl_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdUsageParameterControl_Object = MibTableColumn
mscAtmIfVptUniSigVcdUsageParameterControl = _MscAtmIfVptUniSigVcdUsageParameterControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 10, 1, 70),
    _MscAtmIfVptUniSigVcdUsageParameterControl_Type()
)
mscAtmIfVptUniSigVcdUsageParameterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdUsageParameterControl.setStatus("mandatory")
_MscAtmIfVptUniSigVcdTdpTable_Object = MibTable
mscAtmIfVptUniSigVcdTdpTable = _MscAtmIfVptUniSigVcdTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 387)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTdpTable.setStatus("mandatory")
_MscAtmIfVptUniSigVcdTdpEntry_Object = MibTableRow
mscAtmIfVptUniSigVcdTdpEntry = _MscAtmIfVptUniSigVcdTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 387, 1)
)
mscAtmIfVptUniSigVcdTdpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigVcdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigVcdTdpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTdpEntry.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdTdpIndex_Type(Integer32):
    """Custom type mscAtmIfVptUniSigVcdTdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MscAtmIfVptUniSigVcdTdpIndex_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigVcdTdpIndex_Object = MibTableColumn
mscAtmIfVptUniSigVcdTdpIndex = _MscAtmIfVptUniSigVcdTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 387, 1, 1),
    _MscAtmIfVptUniSigVcdTdpIndex_Type()
)
mscAtmIfVptUniSigVcdTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTdpIndex.setStatus("mandatory")


class _MscAtmIfVptUniSigVcdTdpValue_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSigVcdTdpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscAtmIfVptUniSigVcdTdpValue_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSigVcdTdpValue_Object = MibTableColumn
mscAtmIfVptUniSigVcdTdpValue = _MscAtmIfVptUniSigVcdTdpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 2, 387, 1, 2),
    _MscAtmIfVptUniSigVcdTdpValue_Type()
)
mscAtmIfVptUniSigVcdTdpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVcdTdpValue.setStatus("mandatory")
_MscAtmIfVptUniSigProvTable_Object = MibTable
mscAtmIfVptUniSigProvTable = _MscAtmIfVptUniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigProvTable.setStatus("mandatory")
_MscAtmIfVptUniSigProvEntry_Object = MibTableRow
mscAtmIfVptUniSigProvEntry = _MscAtmIfVptUniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 10, 1)
)
mscAtmIfVptUniSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniSigVci_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSigVci based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscAtmIfVptUniSigVci_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSigVci_Object = MibTableColumn
mscAtmIfVptUniSigVci = _MscAtmIfVptUniSigVci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 10, 1, 1),
    _MscAtmIfVptUniSigVci_Type()
)
mscAtmIfVptUniSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigVci.setStatus("mandatory")


class _MscAtmIfVptUniSigAddressConversion_Type(Integer32):
    """Custom type mscAtmIfVptUniSigAddressConversion based on Integer32"""
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


_MscAtmIfVptUniSigAddressConversion_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigAddressConversion_Object = MibTableColumn
mscAtmIfVptUniSigAddressConversion = _MscAtmIfVptUniSigAddressConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 10, 1, 2),
    _MscAtmIfVptUniSigAddressConversion_Type()
)
mscAtmIfVptUniSigAddressConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigAddressConversion.setStatus("mandatory")


class _MscAtmIfVptUniSigOperatingMode_Type(Integer32):
    """Custom type mscAtmIfVptUniSigOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("provisionedOnly", 1))
    )


_MscAtmIfVptUniSigOperatingMode_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigOperatingMode_Object = MibTableColumn
mscAtmIfVptUniSigOperatingMode = _MscAtmIfVptUniSigOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 10, 1, 3),
    _MscAtmIfVptUniSigOperatingMode_Type()
)
mscAtmIfVptUniSigOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigOperatingMode.setStatus("mandatory")
_MscAtmIfVptUniSigStateTable_Object = MibTable
mscAtmIfVptUniSigStateTable = _MscAtmIfVptUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigStateTable.setStatus("mandatory")
_MscAtmIfVptUniSigStateEntry_Object = MibTableRow
mscAtmIfVptUniSigStateEntry = _MscAtmIfVptUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 11, 1)
)
mscAtmIfVptUniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigStateEntry.setStatus("mandatory")


class _MscAtmIfVptUniSigAdminState_Type(Integer32):
    """Custom type mscAtmIfVptUniSigAdminState based on Integer32"""
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


_MscAtmIfVptUniSigAdminState_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigAdminState_Object = MibTableColumn
mscAtmIfVptUniSigAdminState = _MscAtmIfVptUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 11, 1, 1),
    _MscAtmIfVptUniSigAdminState_Type()
)
mscAtmIfVptUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigAdminState.setStatus("mandatory")


class _MscAtmIfVptUniSigOperationalState_Type(Integer32):
    """Custom type mscAtmIfVptUniSigOperationalState based on Integer32"""
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


_MscAtmIfVptUniSigOperationalState_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigOperationalState_Object = MibTableColumn
mscAtmIfVptUniSigOperationalState = _MscAtmIfVptUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 11, 1, 2),
    _MscAtmIfVptUniSigOperationalState_Type()
)
mscAtmIfVptUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigOperationalState.setStatus("mandatory")


class _MscAtmIfVptUniSigUsageState_Type(Integer32):
    """Custom type mscAtmIfVptUniSigUsageState based on Integer32"""
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


_MscAtmIfVptUniSigUsageState_Type.__name__ = "Integer32"
_MscAtmIfVptUniSigUsageState_Object = MibTableColumn
mscAtmIfVptUniSigUsageState = _MscAtmIfVptUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 11, 1, 3),
    _MscAtmIfVptUniSigUsageState_Type()
)
mscAtmIfVptUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigUsageState.setStatus("mandatory")
_MscAtmIfVptUniSigOperTable_Object = MibTable
mscAtmIfVptUniSigOperTable = _MscAtmIfVptUniSigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigOperTable.setStatus("mandatory")
_MscAtmIfVptUniSigOperEntry_Object = MibTableRow
mscAtmIfVptUniSigOperEntry = _MscAtmIfVptUniSigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12, 1)
)
mscAtmIfVptUniSigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigOperEntry.setStatus("mandatory")


class _MscAtmIfVptUniSigLastTxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSigLastTxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniSigLastTxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSigLastTxCauseCode_Object = MibTableColumn
mscAtmIfVptUniSigLastTxCauseCode = _MscAtmIfVptUniSigLastTxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12, 1, 1),
    _MscAtmIfVptUniSigLastTxCauseCode_Type()
)
mscAtmIfVptUniSigLastTxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigLastTxCauseCode.setStatus("mandatory")


class _MscAtmIfVptUniSigLastTxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptUniSigLastTxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniSigLastTxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptUniSigLastTxDiagCode_Object = MibTableColumn
mscAtmIfVptUniSigLastTxDiagCode = _MscAtmIfVptUniSigLastTxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12, 1, 2),
    _MscAtmIfVptUniSigLastTxDiagCode_Type()
)
mscAtmIfVptUniSigLastTxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigLastTxDiagCode.setStatus("mandatory")


class _MscAtmIfVptUniSigLastRxCauseCode_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSigLastRxCauseCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniSigLastRxCauseCode_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSigLastRxCauseCode_Object = MibTableColumn
mscAtmIfVptUniSigLastRxCauseCode = _MscAtmIfVptUniSigLastRxCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12, 1, 3),
    _MscAtmIfVptUniSigLastRxCauseCode_Type()
)
mscAtmIfVptUniSigLastRxCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigLastRxCauseCode.setStatus("mandatory")


class _MscAtmIfVptUniSigLastRxDiagCode_Type(Hex):
    """Custom type mscAtmIfVptUniSigLastRxDiagCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniSigLastRxDiagCode_Type.__name__ = "Hex"
_MscAtmIfVptUniSigLastRxDiagCode_Object = MibTableColumn
mscAtmIfVptUniSigLastRxDiagCode = _MscAtmIfVptUniSigLastRxDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 12, 1, 4),
    _MscAtmIfVptUniSigLastRxDiagCode_Type()
)
mscAtmIfVptUniSigLastRxDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigLastRxDiagCode.setStatus("mandatory")
_MscAtmIfVptUniSigStatsTable_Object = MibTable
mscAtmIfVptUniSigStatsTable = _MscAtmIfVptUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigStatsTable.setStatus("mandatory")
_MscAtmIfVptUniSigStatsEntry_Object = MibTableRow
mscAtmIfVptUniSigStatsEntry = _MscAtmIfVptUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1)
)
mscAtmIfVptUniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigStatsEntry.setStatus("mandatory")
_MscAtmIfVptUniSigCurrentConnections_Type = Counter32
_MscAtmIfVptUniSigCurrentConnections_Object = MibTableColumn
mscAtmIfVptUniSigCurrentConnections = _MscAtmIfVptUniSigCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 1),
    _MscAtmIfVptUniSigCurrentConnections_Type()
)
mscAtmIfVptUniSigCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigCurrentConnections.setStatus("obsolete")


class _MscAtmIfVptUniSigPeakConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniSigPeakConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniSigPeakConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniSigPeakConnections_Object = MibTableColumn
mscAtmIfVptUniSigPeakConnections = _MscAtmIfVptUniSigPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 2),
    _MscAtmIfVptUniSigPeakConnections_Type()
)
mscAtmIfVptUniSigPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigPeakConnections.setStatus("mandatory")
_MscAtmIfVptUniSigSuccessfulConnections_Type = Counter32
_MscAtmIfVptUniSigSuccessfulConnections_Object = MibTableColumn
mscAtmIfVptUniSigSuccessfulConnections = _MscAtmIfVptUniSigSuccessfulConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 3),
    _MscAtmIfVptUniSigSuccessfulConnections_Type()
)
mscAtmIfVptUniSigSuccessfulConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigSuccessfulConnections.setStatus("mandatory")
_MscAtmIfVptUniSigFailedConnections_Type = Counter32
_MscAtmIfVptUniSigFailedConnections_Object = MibTableColumn
mscAtmIfVptUniSigFailedConnections = _MscAtmIfVptUniSigFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 4),
    _MscAtmIfVptUniSigFailedConnections_Type()
)
mscAtmIfVptUniSigFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigFailedConnections.setStatus("mandatory")
_MscAtmIfVptUniSigTxPdus_Type = Counter32
_MscAtmIfVptUniSigTxPdus_Object = MibTableColumn
mscAtmIfVptUniSigTxPdus = _MscAtmIfVptUniSigTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 5),
    _MscAtmIfVptUniSigTxPdus_Type()
)
mscAtmIfVptUniSigTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigTxPdus.setStatus("mandatory")
_MscAtmIfVptUniSigRxPdus_Type = Counter32
_MscAtmIfVptUniSigRxPdus_Object = MibTableColumn
mscAtmIfVptUniSigRxPdus = _MscAtmIfVptUniSigRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 6),
    _MscAtmIfVptUniSigRxPdus_Type()
)
mscAtmIfVptUniSigRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigRxPdus.setStatus("mandatory")


class _MscAtmIfVptUniSigCurrentPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniSigCurrentPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniSigCurrentPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniSigCurrentPmpConnections_Object = MibTableColumn
mscAtmIfVptUniSigCurrentPmpConnections = _MscAtmIfVptUniSigCurrentPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 7),
    _MscAtmIfVptUniSigCurrentPmpConnections_Type()
)
mscAtmIfVptUniSigCurrentPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigCurrentPmpConnections.setStatus("mandatory")


class _MscAtmIfVptUniSigPeakPmpConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniSigPeakPmpConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniSigPeakPmpConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniSigPeakPmpConnections_Object = MibTableColumn
mscAtmIfVptUniSigPeakPmpConnections = _MscAtmIfVptUniSigPeakPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 8),
    _MscAtmIfVptUniSigPeakPmpConnections_Type()
)
mscAtmIfVptUniSigPeakPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigPeakPmpConnections.setStatus("mandatory")
_MscAtmIfVptUniSigSuccessfulPmpConnections_Type = Counter32
_MscAtmIfVptUniSigSuccessfulPmpConnections_Object = MibTableColumn
mscAtmIfVptUniSigSuccessfulPmpConnections = _MscAtmIfVptUniSigSuccessfulPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 9),
    _MscAtmIfVptUniSigSuccessfulPmpConnections_Type()
)
mscAtmIfVptUniSigSuccessfulPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigSuccessfulPmpConnections.setStatus("mandatory")
_MscAtmIfVptUniSigFailedPmpConnections_Type = Counter32
_MscAtmIfVptUniSigFailedPmpConnections_Object = MibTableColumn
mscAtmIfVptUniSigFailedPmpConnections = _MscAtmIfVptUniSigFailedPmpConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 10),
    _MscAtmIfVptUniSigFailedPmpConnections_Type()
)
mscAtmIfVptUniSigFailedPmpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigFailedPmpConnections.setStatus("mandatory")


class _MscAtmIfVptUniSigNewCurrentConnections_Type(Gauge32):
    """Custom type mscAtmIfVptUniSigNewCurrentConnections based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscAtmIfVptUniSigNewCurrentConnections_Type.__name__ = "Gauge32"
_MscAtmIfVptUniSigNewCurrentConnections_Object = MibTableColumn
mscAtmIfVptUniSigNewCurrentConnections = _MscAtmIfVptUniSigNewCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 2, 13, 1, 11),
    _MscAtmIfVptUniSigNewCurrentConnections_Type()
)
mscAtmIfVptUniSigNewCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSigNewCurrentConnections.setStatus("mandatory")
_MscAtmIfVptUniAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniAddr = _MscAtmIfVptUniAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3)
)
_MscAtmIfVptUniAddrRowStatusTable_Object = MibTable
mscAtmIfVptUniAddrRowStatusTable = _MscAtmIfVptUniAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniAddrRowStatusEntry = _MscAtmIfVptUniAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1)
)
mscAtmIfVptUniAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniAddrRowStatus_Type = RowStatus
_MscAtmIfVptUniAddrRowStatus_Object = MibTableColumn
mscAtmIfVptUniAddrRowStatus = _MscAtmIfVptUniAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1, 1),
    _MscAtmIfVptUniAddrRowStatus_Type()
)
mscAtmIfVptUniAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniAddrComponentName_Type = DisplayString
_MscAtmIfVptUniAddrComponentName_Object = MibTableColumn
mscAtmIfVptUniAddrComponentName = _MscAtmIfVptUniAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1, 2),
    _MscAtmIfVptUniAddrComponentName_Type()
)
mscAtmIfVptUniAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrComponentName.setStatus("mandatory")
_MscAtmIfVptUniAddrStorageType_Type = StorageType
_MscAtmIfVptUniAddrStorageType_Object = MibTableColumn
mscAtmIfVptUniAddrStorageType = _MscAtmIfVptUniAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1, 4),
    _MscAtmIfVptUniAddrStorageType_Type()
)
mscAtmIfVptUniAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptUniAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptUniAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptUniAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptUniAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptUniAddrAddressIndex = _MscAtmIfVptUniAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1, 10),
    _MscAtmIfVptUniAddrAddressIndex_Type()
)
mscAtmIfVptUniAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptUniAddrAddressTypeIndex_Type(Integer32):
    """Custom type mscAtmIfVptUniAddrAddressTypeIndex based on Integer32"""
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


_MscAtmIfVptUniAddrAddressTypeIndex_Type.__name__ = "Integer32"
_MscAtmIfVptUniAddrAddressTypeIndex_Object = MibTableColumn
mscAtmIfVptUniAddrAddressTypeIndex = _MscAtmIfVptUniAddrAddressTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 1, 1, 11),
    _MscAtmIfVptUniAddrAddressTypeIndex_Type()
)
mscAtmIfVptUniAddrAddressTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrAddressTypeIndex.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSP_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniAddrTermSP = _MscAtmIfVptUniAddrTermSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2)
)
_MscAtmIfVptUniAddrTermSPRowStatusTable_Object = MibTable
mscAtmIfVptUniAddrTermSPRowStatusTable = _MscAtmIfVptUniAddrTermSPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSPRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniAddrTermSPRowStatusEntry = _MscAtmIfVptUniAddrTermSPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1, 1)
)
mscAtmIfVptUniAddrTermSPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrTermSPIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSPRowStatus_Type = RowStatus
_MscAtmIfVptUniAddrTermSPRowStatus_Object = MibTableColumn
mscAtmIfVptUniAddrTermSPRowStatus = _MscAtmIfVptUniAddrTermSPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1, 1, 1),
    _MscAtmIfVptUniAddrTermSPRowStatus_Type()
)
mscAtmIfVptUniAddrTermSPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPRowStatus.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSPComponentName_Type = DisplayString
_MscAtmIfVptUniAddrTermSPComponentName_Object = MibTableColumn
mscAtmIfVptUniAddrTermSPComponentName = _MscAtmIfVptUniAddrTermSPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1, 1, 2),
    _MscAtmIfVptUniAddrTermSPComponentName_Type()
)
mscAtmIfVptUniAddrTermSPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPComponentName.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSPStorageType_Type = StorageType
_MscAtmIfVptUniAddrTermSPStorageType_Object = MibTableColumn
mscAtmIfVptUniAddrTermSPStorageType = _MscAtmIfVptUniAddrTermSPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1, 1, 4),
    _MscAtmIfVptUniAddrTermSPStorageType_Type()
)
mscAtmIfVptUniAddrTermSPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPStorageType.setStatus("mandatory")
_MscAtmIfVptUniAddrTermSPIndex_Type = NonReplicated
_MscAtmIfVptUniAddrTermSPIndex_Object = MibTableColumn
mscAtmIfVptUniAddrTermSPIndex = _MscAtmIfVptUniAddrTermSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 2, 1, 1, 10),
    _MscAtmIfVptUniAddrTermSPIndex_Type()
)
mscAtmIfVptUniAddrTermSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrTermSPIndex.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfo_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniAddrPnniInfo = _MscAtmIfVptUniAddrPnniInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3)
)
_MscAtmIfVptUniAddrPnniInfoRowStatusTable_Object = MibTable
mscAtmIfVptUniAddrPnniInfoRowStatusTable = _MscAtmIfVptUniAddrPnniInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniAddrPnniInfoRowStatusEntry = _MscAtmIfVptUniAddrPnniInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1, 1)
)
mscAtmIfVptUniAddrPnniInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoRowStatus_Type = RowStatus
_MscAtmIfVptUniAddrPnniInfoRowStatus_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoRowStatus = _MscAtmIfVptUniAddrPnniInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1, 1, 1),
    _MscAtmIfVptUniAddrPnniInfoRowStatus_Type()
)
mscAtmIfVptUniAddrPnniInfoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoRowStatus.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoComponentName_Type = DisplayString
_MscAtmIfVptUniAddrPnniInfoComponentName_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoComponentName = _MscAtmIfVptUniAddrPnniInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1, 1, 2),
    _MscAtmIfVptUniAddrPnniInfoComponentName_Type()
)
mscAtmIfVptUniAddrPnniInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoComponentName.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoStorageType_Type = StorageType
_MscAtmIfVptUniAddrPnniInfoStorageType_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoStorageType = _MscAtmIfVptUniAddrPnniInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1, 1, 4),
    _MscAtmIfVptUniAddrPnniInfoStorageType_Type()
)
mscAtmIfVptUniAddrPnniInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoStorageType.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoIndex_Type = NonReplicated
_MscAtmIfVptUniAddrPnniInfoIndex_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoIndex = _MscAtmIfVptUniAddrPnniInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 1, 1, 10),
    _MscAtmIfVptUniAddrPnniInfoIndex_Type()
)
mscAtmIfVptUniAddrPnniInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoIndex.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoProvTable_Object = MibTable
mscAtmIfVptUniAddrPnniInfoProvTable = _MscAtmIfVptUniAddrPnniInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoProvTable.setStatus("mandatory")
_MscAtmIfVptUniAddrPnniInfoProvEntry_Object = MibTableRow
mscAtmIfVptUniAddrPnniInfoProvEntry = _MscAtmIfVptUniAddrPnniInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 10, 1)
)
mscAtmIfVptUniAddrPnniInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrPnniInfoIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniAddrPnniInfoScope_Type(Integer32):
    """Custom type mscAtmIfVptUniAddrPnniInfoScope based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptUniAddrPnniInfoScope_Type.__name__ = "Integer32"
_MscAtmIfVptUniAddrPnniInfoScope_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoScope = _MscAtmIfVptUniAddrPnniInfoScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 10, 1, 1),
    _MscAtmIfVptUniAddrPnniInfoScope_Type()
)
mscAtmIfVptUniAddrPnniInfoScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoScope.setStatus("mandatory")


class _MscAtmIfVptUniAddrPnniInfoReachability_Type(Integer32):
    """Custom type mscAtmIfVptUniAddrPnniInfoReachability based on Integer32"""
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


_MscAtmIfVptUniAddrPnniInfoReachability_Type.__name__ = "Integer32"
_MscAtmIfVptUniAddrPnniInfoReachability_Object = MibTableColumn
mscAtmIfVptUniAddrPnniInfoReachability = _MscAtmIfVptUniAddrPnniInfoReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 3, 10, 1, 2),
    _MscAtmIfVptUniAddrPnniInfoReachability_Type()
)
mscAtmIfVptUniAddrPnniInfoReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrPnniInfoReachability.setStatus("mandatory")
_MscAtmIfVptUniAddrOperTable_Object = MibTable
mscAtmIfVptUniAddrOperTable = _MscAtmIfVptUniAddrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrOperTable.setStatus("mandatory")
_MscAtmIfVptUniAddrOperEntry_Object = MibTableRow
mscAtmIfVptUniAddrOperEntry = _MscAtmIfVptUniAddrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 10, 1)
)
mscAtmIfVptUniAddrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniAddrAddressTypeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrOperEntry.setStatus("mandatory")


class _MscAtmIfVptUniAddrScope_Type(Integer32):
    """Custom type mscAtmIfVptUniAddrScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 104),
    )


_MscAtmIfVptUniAddrScope_Type.__name__ = "Integer32"
_MscAtmIfVptUniAddrScope_Object = MibTableColumn
mscAtmIfVptUniAddrScope = _MscAtmIfVptUniAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 10, 1, 1),
    _MscAtmIfVptUniAddrScope_Type()
)
mscAtmIfVptUniAddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrScope.setStatus("mandatory")


class _MscAtmIfVptUniAddrReachability_Type(Integer32):
    """Custom type mscAtmIfVptUniAddrReachability based on Integer32"""
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


_MscAtmIfVptUniAddrReachability_Type.__name__ = "Integer32"
_MscAtmIfVptUniAddrReachability_Object = MibTableColumn
mscAtmIfVptUniAddrReachability = _MscAtmIfVptUniAddrReachability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 3, 10, 1, 2),
    _MscAtmIfVptUniAddrReachability_Type()
)
mscAtmIfVptUniAddrReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAddrReachability.setStatus("mandatory")
_MscAtmIfVptUniCallingAScr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniCallingAScr = _MscAtmIfVptUniCallingAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4)
)
_MscAtmIfVptUniCallingAScrRowStatusTable_Object = MibTable
mscAtmIfVptUniCallingAScrRowStatusTable = _MscAtmIfVptUniCallingAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniCallingAScrRowStatusEntry = _MscAtmIfVptUniCallingAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1, 1)
)
mscAtmIfVptUniCallingAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrRowStatus_Type = RowStatus
_MscAtmIfVptUniCallingAScrRowStatus_Object = MibTableColumn
mscAtmIfVptUniCallingAScrRowStatus = _MscAtmIfVptUniCallingAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1, 1, 1),
    _MscAtmIfVptUniCallingAScrRowStatus_Type()
)
mscAtmIfVptUniCallingAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrComponentName_Type = DisplayString
_MscAtmIfVptUniCallingAScrComponentName_Object = MibTableColumn
mscAtmIfVptUniCallingAScrComponentName = _MscAtmIfVptUniCallingAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1, 1, 2),
    _MscAtmIfVptUniCallingAScrComponentName_Type()
)
mscAtmIfVptUniCallingAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrComponentName.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrStorageType_Type = StorageType
_MscAtmIfVptUniCallingAScrStorageType_Object = MibTableColumn
mscAtmIfVptUniCallingAScrStorageType = _MscAtmIfVptUniCallingAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1, 1, 4),
    _MscAtmIfVptUniCallingAScrStorageType_Type()
)
mscAtmIfVptUniCallingAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrStorageType.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrIndex_Type = NonReplicated
_MscAtmIfVptUniCallingAScrIndex_Object = MibTableColumn
mscAtmIfVptUniCallingAScrIndex = _MscAtmIfVptUniCallingAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 1, 1, 10),
    _MscAtmIfVptUniCallingAScrIndex_Type()
)
mscAtmIfVptUniCallingAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrIndex.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniCallingAScrAddr = _MscAtmIfVptUniCallingAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2)
)
_MscAtmIfVptUniCallingAScrAddrRowStatusTable_Object = MibTable
mscAtmIfVptUniCallingAScrAddrRowStatusTable = _MscAtmIfVptUniCallingAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniCallingAScrAddrRowStatusEntry = _MscAtmIfVptUniCallingAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1)
)
mscAtmIfVptUniCallingAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAddrRowStatus_Type = RowStatus
_MscAtmIfVptUniCallingAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAddrRowStatus = _MscAtmIfVptUniCallingAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1, 1),
    _MscAtmIfVptUniCallingAScrAddrRowStatus_Type()
)
mscAtmIfVptUniCallingAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAddrComponentName_Type = DisplayString
_MscAtmIfVptUniCallingAScrAddrComponentName_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAddrComponentName = _MscAtmIfVptUniCallingAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1, 2),
    _MscAtmIfVptUniCallingAScrAddrComponentName_Type()
)
mscAtmIfVptUniCallingAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAddrStorageType_Type = StorageType
_MscAtmIfVptUniCallingAScrAddrStorageType_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAddrStorageType = _MscAtmIfVptUniCallingAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1, 4),
    _MscAtmIfVptUniCallingAScrAddrStorageType_Type()
)
mscAtmIfVptUniCallingAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptUniCallingAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptUniCallingAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptUniCallingAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptUniCallingAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAddrAddressIndex = _MscAtmIfVptUniCallingAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1, 10),
    _MscAtmIfVptUniCallingAScrAddrAddressIndex_Type()
)
mscAtmIfVptUniCallingAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptUniCallingAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfVptUniCallingAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfVptUniCallingAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfVptUniCallingAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAddrAddressActionIndex = _MscAtmIfVptUniCallingAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 2, 1, 1, 11),
    _MscAtmIfVptUniCallingAScrAddrAddressActionIndex_Type()
)
mscAtmIfVptUniCallingAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrProvTable_Object = MibTable
mscAtmIfVptUniCallingAScrProvTable = _MscAtmIfVptUniCallingAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrProvTable.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrProvEntry_Object = MibTableRow
mscAtmIfVptUniCallingAScrProvEntry = _MscAtmIfVptUniCallingAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 10, 1)
)
mscAtmIfVptUniCallingAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniCallingAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfVptUniCallingAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfVptUniCallingAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfVptUniCallingAScrAdminStatus_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAdminStatus = _MscAtmIfVptUniCallingAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 10, 1, 1),
    _MscAtmIfVptUniCallingAScrAdminStatus_Type()
)
mscAtmIfVptUniCallingAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAdminStatus.setStatus("mandatory")


class _MscAtmIfVptUniCallingAScrDefaultInsertionAddress_Type(HexString):
    """Custom type mscAtmIfVptUniCallingAScrDefaultInsertionAddress based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscAtmIfVptUniCallingAScrDefaultInsertionAddress_Type.__name__ = "HexString"
_MscAtmIfVptUniCallingAScrDefaultInsertionAddress_Object = MibTableColumn
mscAtmIfVptUniCallingAScrDefaultInsertionAddress = _MscAtmIfVptUniCallingAScrDefaultInsertionAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 10, 1, 2),
    _MscAtmIfVptUniCallingAScrDefaultInsertionAddress_Type()
)
mscAtmIfVptUniCallingAScrDefaultInsertionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrDefaultInsertionAddress.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrStatTable_Object = MibTable
mscAtmIfVptUniCallingAScrStatTable = _MscAtmIfVptUniCallingAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrStatTable.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrStatEntry_Object = MibTableRow
mscAtmIfVptUniCallingAScrStatEntry = _MscAtmIfVptUniCallingAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 11, 1)
)
mscAtmIfVptUniCallingAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCallingAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrStatEntry.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrAcceptedCalls_Type = Counter32
_MscAtmIfVptUniCallingAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfVptUniCallingAScrAcceptedCalls = _MscAtmIfVptUniCallingAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 11, 1, 1),
    _MscAtmIfVptUniCallingAScrAcceptedCalls_Type()
)
mscAtmIfVptUniCallingAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrRejectedCalls_Type = Counter32
_MscAtmIfVptUniCallingAScrRejectedCalls_Object = MibTableColumn
mscAtmIfVptUniCallingAScrRejectedCalls = _MscAtmIfVptUniCallingAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 11, 1, 2),
    _MscAtmIfVptUniCallingAScrRejectedCalls_Type()
)
mscAtmIfVptUniCallingAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfVptUniCallingAScrUnmatchedCalls_Type = Counter32
_MscAtmIfVptUniCallingAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfVptUniCallingAScrUnmatchedCalls = _MscAtmIfVptUniCallingAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 4, 11, 1, 3),
    _MscAtmIfVptUniCallingAScrUnmatchedCalls_Type()
)
mscAtmIfVptUniCallingAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCallingAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfVptUniCalledAScr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniCalledAScr = _MscAtmIfVptUniCalledAScr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5)
)
_MscAtmIfVptUniCalledAScrRowStatusTable_Object = MibTable
mscAtmIfVptUniCalledAScrRowStatusTable = _MscAtmIfVptUniCalledAScrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniCalledAScrRowStatusEntry = _MscAtmIfVptUniCalledAScrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1, 1)
)
mscAtmIfVptUniCalledAScrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrRowStatus_Type = RowStatus
_MscAtmIfVptUniCalledAScrRowStatus_Object = MibTableColumn
mscAtmIfVptUniCalledAScrRowStatus = _MscAtmIfVptUniCalledAScrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1, 1, 1),
    _MscAtmIfVptUniCalledAScrRowStatus_Type()
)
mscAtmIfVptUniCalledAScrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrComponentName_Type = DisplayString
_MscAtmIfVptUniCalledAScrComponentName_Object = MibTableColumn
mscAtmIfVptUniCalledAScrComponentName = _MscAtmIfVptUniCalledAScrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1, 1, 2),
    _MscAtmIfVptUniCalledAScrComponentName_Type()
)
mscAtmIfVptUniCalledAScrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrComponentName.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrStorageType_Type = StorageType
_MscAtmIfVptUniCalledAScrStorageType_Object = MibTableColumn
mscAtmIfVptUniCalledAScrStorageType = _MscAtmIfVptUniCalledAScrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1, 1, 4),
    _MscAtmIfVptUniCalledAScrStorageType_Type()
)
mscAtmIfVptUniCalledAScrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrStorageType.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrIndex_Type = NonReplicated
_MscAtmIfVptUniCalledAScrIndex_Object = MibTableColumn
mscAtmIfVptUniCalledAScrIndex = _MscAtmIfVptUniCalledAScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 1, 1, 10),
    _MscAtmIfVptUniCalledAScrIndex_Type()
)
mscAtmIfVptUniCalledAScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrIndex.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAddr_ObjectIdentity = ObjectIdentity
mscAtmIfVptUniCalledAScrAddr = _MscAtmIfVptUniCalledAScrAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2)
)
_MscAtmIfVptUniCalledAScrAddrRowStatusTable_Object = MibTable
mscAtmIfVptUniCalledAScrAddrRowStatusTable = _MscAtmIfVptUniCalledAScrAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrRowStatusTable.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAddrRowStatusEntry_Object = MibTableRow
mscAtmIfVptUniCalledAScrAddrRowStatusEntry = _MscAtmIfVptUniCalledAScrAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1)
)
mscAtmIfVptUniCalledAScrAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrAddrAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrAddrAddressActionIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAddrRowStatus_Type = RowStatus
_MscAtmIfVptUniCalledAScrAddrRowStatus_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAddrRowStatus = _MscAtmIfVptUniCalledAScrAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1, 1),
    _MscAtmIfVptUniCalledAScrAddrRowStatus_Type()
)
mscAtmIfVptUniCalledAScrAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrRowStatus.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAddrComponentName_Type = DisplayString
_MscAtmIfVptUniCalledAScrAddrComponentName_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAddrComponentName = _MscAtmIfVptUniCalledAScrAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1, 2),
    _MscAtmIfVptUniCalledAScrAddrComponentName_Type()
)
mscAtmIfVptUniCalledAScrAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrComponentName.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAddrStorageType_Type = StorageType
_MscAtmIfVptUniCalledAScrAddrStorageType_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAddrStorageType = _MscAtmIfVptUniCalledAScrAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1, 4),
    _MscAtmIfVptUniCalledAScrAddrStorageType_Type()
)
mscAtmIfVptUniCalledAScrAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrStorageType.setStatus("mandatory")


class _MscAtmIfVptUniCalledAScrAddrAddressIndex_Type(AsciiStringIndex):
    """Custom type mscAtmIfVptUniCalledAScrAddrAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscAtmIfVptUniCalledAScrAddrAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscAtmIfVptUniCalledAScrAddrAddressIndex_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAddrAddressIndex = _MscAtmIfVptUniCalledAScrAddrAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1, 10),
    _MscAtmIfVptUniCalledAScrAddrAddressIndex_Type()
)
mscAtmIfVptUniCalledAScrAddrAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrAddressIndex.setStatus("mandatory")


class _MscAtmIfVptUniCalledAScrAddrAddressActionIndex_Type(Integer32):
    """Custom type mscAtmIfVptUniCalledAScrAddrAddressActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )


_MscAtmIfVptUniCalledAScrAddrAddressActionIndex_Type.__name__ = "Integer32"
_MscAtmIfVptUniCalledAScrAddrAddressActionIndex_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAddrAddressActionIndex = _MscAtmIfVptUniCalledAScrAddrAddressActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 2, 1, 1, 11),
    _MscAtmIfVptUniCalledAScrAddrAddressActionIndex_Type()
)
mscAtmIfVptUniCalledAScrAddrAddressActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAddrAddressActionIndex.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrProvTable_Object = MibTable
mscAtmIfVptUniCalledAScrProvTable = _MscAtmIfVptUniCalledAScrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrProvTable.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrProvEntry_Object = MibTableRow
mscAtmIfVptUniCalledAScrProvEntry = _MscAtmIfVptUniCalledAScrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 10, 1)
)
mscAtmIfVptUniCalledAScrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniCalledAScrAdminStatus_Type(Integer32):
    """Custom type mscAtmIfVptUniCalledAScrAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscAtmIfVptUniCalledAScrAdminStatus_Type.__name__ = "Integer32"
_MscAtmIfVptUniCalledAScrAdminStatus_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAdminStatus = _MscAtmIfVptUniCalledAScrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 10, 1, 1),
    _MscAtmIfVptUniCalledAScrAdminStatus_Type()
)
mscAtmIfVptUniCalledAScrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAdminStatus.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrStatTable_Object = MibTable
mscAtmIfVptUniCalledAScrStatTable = _MscAtmIfVptUniCalledAScrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrStatTable.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrStatEntry_Object = MibTableRow
mscAtmIfVptUniCalledAScrStatEntry = _MscAtmIfVptUniCalledAScrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 11, 1)
)
mscAtmIfVptUniCalledAScrStatEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniCalledAScrIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrStatEntry.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrAcceptedCalls_Type = Counter32
_MscAtmIfVptUniCalledAScrAcceptedCalls_Object = MibTableColumn
mscAtmIfVptUniCalledAScrAcceptedCalls = _MscAtmIfVptUniCalledAScrAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 11, 1, 1),
    _MscAtmIfVptUniCalledAScrAcceptedCalls_Type()
)
mscAtmIfVptUniCalledAScrAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrAcceptedCalls.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrRejectedCalls_Type = Counter32
_MscAtmIfVptUniCalledAScrRejectedCalls_Object = MibTableColumn
mscAtmIfVptUniCalledAScrRejectedCalls = _MscAtmIfVptUniCalledAScrRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 11, 1, 2),
    _MscAtmIfVptUniCalledAScrRejectedCalls_Type()
)
mscAtmIfVptUniCalledAScrRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrRejectedCalls.setStatus("mandatory")
_MscAtmIfVptUniCalledAScrUnmatchedCalls_Type = Counter32
_MscAtmIfVptUniCalledAScrUnmatchedCalls_Object = MibTableColumn
mscAtmIfVptUniCalledAScrUnmatchedCalls = _MscAtmIfVptUniCalledAScrUnmatchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 5, 11, 1, 3),
    _MscAtmIfVptUniCalledAScrUnmatchedCalls_Type()
)
mscAtmIfVptUniCalledAScrUnmatchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptUniCalledAScrUnmatchedCalls.setStatus("mandatory")
_MscAtmIfVptUniProvTable_Object = MibTable
mscAtmIfVptUniProvTable = _MscAtmIfVptUniProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniProvTable.setStatus("mandatory")
_MscAtmIfVptUniProvEntry_Object = MibTableRow
mscAtmIfVptUniProvEntry = _MscAtmIfVptUniProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1)
)
mscAtmIfVptUniProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniVersion_Type(Integer32):
    """Custom type mscAtmIfVptUniVersion based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atmForum30", 0),
          ("atmForum31", 1),
          ("atmForum40", 5))
    )


_MscAtmIfVptUniVersion_Type.__name__ = "Integer32"
_MscAtmIfVptUniVersion_Object = MibTableColumn
mscAtmIfVptUniVersion = _MscAtmIfVptUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 1),
    _MscAtmIfVptUniVersion_Type()
)
mscAtmIfVptUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniVersion.setStatus("mandatory")


class _MscAtmIfVptUniSide_Type(Integer32):
    """Custom type mscAtmIfVptUniSide based on Integer32"""
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


_MscAtmIfVptUniSide_Type.__name__ = "Integer32"
_MscAtmIfVptUniSide_Object = MibTableColumn
mscAtmIfVptUniSide = _MscAtmIfVptUniSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 2),
    _MscAtmIfVptUniSide_Type()
)
mscAtmIfVptUniSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSide.setStatus("mandatory")


class _MscAtmIfVptUniSoftPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSoftPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptUniSoftPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSoftPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptUniSoftPvcRetryPeriod = _MscAtmIfVptUniSoftPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 3),
    _MscAtmIfVptUniSoftPvcRetryPeriod_Type()
)
mscAtmIfVptUniSoftPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSoftPvcRetryPeriod.setStatus("obsolete")


class _MscAtmIfVptUniSoftPvpAndPvcRetryPeriod_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSoftPvpAndPvcRetryPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 999999),
    )


_MscAtmIfVptUniSoftPvpAndPvcRetryPeriod_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSoftPvpAndPvcRetryPeriod_Object = MibTableColumn
mscAtmIfVptUniSoftPvpAndPvcRetryPeriod = _MscAtmIfVptUniSoftPvpAndPvcRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 4),
    _MscAtmIfVptUniSoftPvpAndPvcRetryPeriod_Type()
)
mscAtmIfVptUniSoftPvpAndPvcRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSoftPvpAndPvcRetryPeriod.setStatus("mandatory")


class _MscAtmIfVptUniSoftPvpAndPvcHoldOffTime_Type(Unsigned32):
    """Custom type mscAtmIfVptUniSoftPvpAndPvcHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 20000),
    )


_MscAtmIfVptUniSoftPvpAndPvcHoldOffTime_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniSoftPvpAndPvcHoldOffTime_Object = MibTableColumn
mscAtmIfVptUniSoftPvpAndPvcHoldOffTime = _MscAtmIfVptUniSoftPvpAndPvcHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 5),
    _MscAtmIfVptUniSoftPvpAndPvcHoldOffTime_Type()
)
mscAtmIfVptUniSoftPvpAndPvcHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniSoftPvpAndPvcHoldOffTime.setStatus("mandatory")


class _MscAtmIfVptUniLoopPrevention_Type(Integer32):
    """Custom type mscAtmIfVptUniLoopPrevention based on Integer32"""
    defaultValue = 1

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


_MscAtmIfVptUniLoopPrevention_Type.__name__ = "Integer32"
_MscAtmIfVptUniLoopPrevention_Object = MibTableColumn
mscAtmIfVptUniLoopPrevention = _MscAtmIfVptUniLoopPrevention_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 10, 1, 6),
    _MscAtmIfVptUniLoopPrevention_Type()
)
mscAtmIfVptUniLoopPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniLoopPrevention.setStatus("mandatory")
_MscAtmIfVptUniAcctOptTable_Object = MibTable
mscAtmIfVptUniAcctOptTable = _MscAtmIfVptUniAcctOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAcctOptTable.setStatus("mandatory")
_MscAtmIfVptUniAcctOptEntry_Object = MibTableRow
mscAtmIfVptUniAcctOptEntry = _MscAtmIfVptUniAcctOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11, 1)
)
mscAtmIfVptUniAcctOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniAcctOptEntry.setStatus("mandatory")


class _MscAtmIfVptUniAccountCollection_Type(OctetString):
    """Custom type mscAtmIfVptUniAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAtmIfVptUniAccountCollection_Type.__name__ = "OctetString"
_MscAtmIfVptUniAccountCollection_Object = MibTableColumn
mscAtmIfVptUniAccountCollection = _MscAtmIfVptUniAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11, 1, 1),
    _MscAtmIfVptUniAccountCollection_Type()
)
mscAtmIfVptUniAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAccountCollection.setStatus("mandatory")


class _MscAtmIfVptUniAccountConnectionType_Type(Integer32):
    """Custom type mscAtmIfVptUniAccountConnectionType based on Integer32"""
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


_MscAtmIfVptUniAccountConnectionType_Type.__name__ = "Integer32"
_MscAtmIfVptUniAccountConnectionType_Object = MibTableColumn
mscAtmIfVptUniAccountConnectionType = _MscAtmIfVptUniAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11, 1, 2),
    _MscAtmIfVptUniAccountConnectionType_Type()
)
mscAtmIfVptUniAccountConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAccountConnectionType.setStatus("mandatory")


class _MscAtmIfVptUniAccountClass_Type(Unsigned32):
    """Custom type mscAtmIfVptUniAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniAccountClass_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniAccountClass_Object = MibTableColumn
mscAtmIfVptUniAccountClass = _MscAtmIfVptUniAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11, 1, 3),
    _MscAtmIfVptUniAccountClass_Type()
)
mscAtmIfVptUniAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniAccountClass.setStatus("mandatory")


class _MscAtmIfVptUniServiceExchange_Type(Unsigned32):
    """Custom type mscAtmIfVptUniServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniServiceExchange_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniServiceExchange_Object = MibTableColumn
mscAtmIfVptUniServiceExchange = _MscAtmIfVptUniServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 11, 1, 4),
    _MscAtmIfVptUniServiceExchange_Type()
)
mscAtmIfVptUniServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniServiceExchange.setStatus("mandatory")
_MscAtmIfVptUniVProvTable_Object = MibTable
mscAtmIfVptUniVProvTable = _MscAtmIfVptUniVProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 12)
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniVProvTable.setStatus("mandatory")
_MscAtmIfVptUniVProvEntry_Object = MibTableRow
mscAtmIfVptUniVProvEntry = _MscAtmIfVptUniVProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 12, 1)
)
mscAtmIfVptUniVProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmUniMIB", "mscAtmIfVptUniIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptUniVProvEntry.setStatus("mandatory")


class _MscAtmIfVptUniVpci_Type(Unsigned32):
    """Custom type mscAtmIfVptUniVpci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmIfVptUniVpci_Type.__name__ = "Unsigned32"
_MscAtmIfVptUniVpci_Object = MibTableColumn
mscAtmIfVptUniVpci = _MscAtmIfVptUniVpci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 8, 12, 1, 1),
    _MscAtmIfVptUniVpci_Type()
)
mscAtmIfVptUniVpci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptUniVpci.setStatus("mandatory")
_AtmUniMIB_ObjectIdentity = ObjectIdentity
atmUniMIB = _AtmUniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69)
)
_AtmUniGroup_ObjectIdentity = ObjectIdentity
atmUniGroup = _AtmUniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 1)
)
_AtmUniGroupCA_ObjectIdentity = ObjectIdentity
atmUniGroupCA = _AtmUniGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 1, 1)
)
_AtmUniGroupCA02_ObjectIdentity = ObjectIdentity
atmUniGroupCA02 = _AtmUniGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 1, 1, 3)
)
_AtmUniGroupCA02A_ObjectIdentity = ObjectIdentity
atmUniGroupCA02A = _AtmUniGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 1, 1, 3, 2)
)
_AtmUniCapabilities_ObjectIdentity = ObjectIdentity
atmUniCapabilities = _AtmUniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 3)
)
_AtmUniCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesCA = _AtmUniCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 3, 1)
)
_AtmUniCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesCA02 = _AtmUniCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 3, 1, 3)
)
_AtmUniCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmUniCapabilitiesCA02A = _AtmUniCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 69, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmUniMIB",
    **{"mscAtmIfUni": mscAtmIfUni,
       "mscAtmIfUniRowStatusTable": mscAtmIfUniRowStatusTable,
       "mscAtmIfUniRowStatusEntry": mscAtmIfUniRowStatusEntry,
       "mscAtmIfUniRowStatus": mscAtmIfUniRowStatus,
       "mscAtmIfUniComponentName": mscAtmIfUniComponentName,
       "mscAtmIfUniStorageType": mscAtmIfUniStorageType,
       "mscAtmIfUniIndex": mscAtmIfUniIndex,
       "mscAtmIfUniIlmi": mscAtmIfUniIlmi,
       "mscAtmIfUniIlmiRowStatusTable": mscAtmIfUniIlmiRowStatusTable,
       "mscAtmIfUniIlmiRowStatusEntry": mscAtmIfUniIlmiRowStatusEntry,
       "mscAtmIfUniIlmiRowStatus": mscAtmIfUniIlmiRowStatus,
       "mscAtmIfUniIlmiComponentName": mscAtmIfUniIlmiComponentName,
       "mscAtmIfUniIlmiStorageType": mscAtmIfUniIlmiStorageType,
       "mscAtmIfUniIlmiIndex": mscAtmIfUniIlmiIndex,
       "mscAtmIfUniIlmiStateTable": mscAtmIfUniIlmiStateTable,
       "mscAtmIfUniIlmiStateEntry": mscAtmIfUniIlmiStateEntry,
       "mscAtmIfUniIlmiAdminState": mscAtmIfUniIlmiAdminState,
       "mscAtmIfUniIlmiOperationalState": mscAtmIfUniIlmiOperationalState,
       "mscAtmIfUniIlmiUsageState": mscAtmIfUniIlmiUsageState,
       "mscAtmIfUniIlmiProvTable": mscAtmIfUniIlmiProvTable,
       "mscAtmIfUniIlmiProvEntry": mscAtmIfUniIlmiProvEntry,
       "mscAtmIfUniIlmiVci": mscAtmIfUniIlmiVci,
       "mscAtmIfUniIlmiOperatingMode": mscAtmIfUniIlmiOperatingMode,
       "mscAtmIfUniIlmiStatsTable": mscAtmIfUniIlmiStatsTable,
       "mscAtmIfUniIlmiStatsEntry": mscAtmIfUniIlmiStatsEntry,
       "mscAtmIfUniIlmiTxPdus": mscAtmIfUniIlmiTxPdus,
       "mscAtmIfUniIlmiRxPdus": mscAtmIfUniIlmiRxPdus,
       "mscAtmIfUniIlmiRxBadPdusDiscarded": mscAtmIfUniIlmiRxBadPdusDiscarded,
       "mscAtmIfUniIlmiPrefixToRegisterTable": mscAtmIfUniIlmiPrefixToRegisterTable,
       "mscAtmIfUniIlmiPrefixToRegisterEntry": mscAtmIfUniIlmiPrefixToRegisterEntry,
       "mscAtmIfUniIlmiPrefixToRegisterValue": mscAtmIfUniIlmiPrefixToRegisterValue,
       "mscAtmIfUniIlmiPrefixToRegisterRowStatus": mscAtmIfUniIlmiPrefixToRegisterRowStatus,
       "mscAtmIfUniIlmiEsiToRegisterTable": mscAtmIfUniIlmiEsiToRegisterTable,
       "mscAtmIfUniIlmiEsiToRegisterEntry": mscAtmIfUniIlmiEsiToRegisterEntry,
       "mscAtmIfUniIlmiEsiToRegisterValue": mscAtmIfUniIlmiEsiToRegisterValue,
       "mscAtmIfUniIlmiEsiToRegisterRowStatus": mscAtmIfUniIlmiEsiToRegisterRowStatus,
       "mscAtmIfUniSig": mscAtmIfUniSig,
       "mscAtmIfUniSigRowStatusTable": mscAtmIfUniSigRowStatusTable,
       "mscAtmIfUniSigRowStatusEntry": mscAtmIfUniSigRowStatusEntry,
       "mscAtmIfUniSigRowStatus": mscAtmIfUniSigRowStatus,
       "mscAtmIfUniSigComponentName": mscAtmIfUniSigComponentName,
       "mscAtmIfUniSigStorageType": mscAtmIfUniSigStorageType,
       "mscAtmIfUniSigIndex": mscAtmIfUniSigIndex,
       "mscAtmIfUniSigVcd": mscAtmIfUniSigVcd,
       "mscAtmIfUniSigVcdRowStatusTable": mscAtmIfUniSigVcdRowStatusTable,
       "mscAtmIfUniSigVcdRowStatusEntry": mscAtmIfUniSigVcdRowStatusEntry,
       "mscAtmIfUniSigVcdRowStatus": mscAtmIfUniSigVcdRowStatus,
       "mscAtmIfUniSigVcdComponentName": mscAtmIfUniSigVcdComponentName,
       "mscAtmIfUniSigVcdStorageType": mscAtmIfUniSigVcdStorageType,
       "mscAtmIfUniSigVcdIndex": mscAtmIfUniSigVcdIndex,
       "mscAtmIfUniSigVcdProvTable": mscAtmIfUniSigVcdProvTable,
       "mscAtmIfUniSigVcdProvEntry": mscAtmIfUniSigVcdProvEntry,
       "mscAtmIfUniSigVcdTrafficDescType": mscAtmIfUniSigVcdTrafficDescType,
       "mscAtmIfUniSigVcdAtmServiceCategory": mscAtmIfUniSigVcdAtmServiceCategory,
       "mscAtmIfUniSigVcdWeight": mscAtmIfUniSigVcdWeight,
       "mscAtmIfUniSigVcdQosClass": mscAtmIfUniSigVcdQosClass,
       "mscAtmIfUniSigVcdTrafficShaping": mscAtmIfUniSigVcdTrafficShaping,
       "mscAtmIfUniSigVcdUnshapedTransmitQueueing": mscAtmIfUniSigVcdUnshapedTransmitQueueing,
       "mscAtmIfUniSigVcdUsageParameterControl": mscAtmIfUniSigVcdUsageParameterControl,
       "mscAtmIfUniSigVcdTdpTable": mscAtmIfUniSigVcdTdpTable,
       "mscAtmIfUniSigVcdTdpEntry": mscAtmIfUniSigVcdTdpEntry,
       "mscAtmIfUniSigVcdTdpIndex": mscAtmIfUniSigVcdTdpIndex,
       "mscAtmIfUniSigVcdTdpValue": mscAtmIfUniSigVcdTdpValue,
       "mscAtmIfUniSigProvTable": mscAtmIfUniSigProvTable,
       "mscAtmIfUniSigProvEntry": mscAtmIfUniSigProvEntry,
       "mscAtmIfUniSigVci": mscAtmIfUniSigVci,
       "mscAtmIfUniSigAddressConversion": mscAtmIfUniSigAddressConversion,
       "mscAtmIfUniSigOperatingMode": mscAtmIfUniSigOperatingMode,
       "mscAtmIfUniSigStateTable": mscAtmIfUniSigStateTable,
       "mscAtmIfUniSigStateEntry": mscAtmIfUniSigStateEntry,
       "mscAtmIfUniSigAdminState": mscAtmIfUniSigAdminState,
       "mscAtmIfUniSigOperationalState": mscAtmIfUniSigOperationalState,
       "mscAtmIfUniSigUsageState": mscAtmIfUniSigUsageState,
       "mscAtmIfUniSigOperTable": mscAtmIfUniSigOperTable,
       "mscAtmIfUniSigOperEntry": mscAtmIfUniSigOperEntry,
       "mscAtmIfUniSigLastTxCauseCode": mscAtmIfUniSigLastTxCauseCode,
       "mscAtmIfUniSigLastTxDiagCode": mscAtmIfUniSigLastTxDiagCode,
       "mscAtmIfUniSigLastRxCauseCode": mscAtmIfUniSigLastRxCauseCode,
       "mscAtmIfUniSigLastRxDiagCode": mscAtmIfUniSigLastRxDiagCode,
       "mscAtmIfUniSigStatsTable": mscAtmIfUniSigStatsTable,
       "mscAtmIfUniSigStatsEntry": mscAtmIfUniSigStatsEntry,
       "mscAtmIfUniSigCurrentConnections": mscAtmIfUniSigCurrentConnections,
       "mscAtmIfUniSigPeakConnections": mscAtmIfUniSigPeakConnections,
       "mscAtmIfUniSigSuccessfulConnections": mscAtmIfUniSigSuccessfulConnections,
       "mscAtmIfUniSigFailedConnections": mscAtmIfUniSigFailedConnections,
       "mscAtmIfUniSigTxPdus": mscAtmIfUniSigTxPdus,
       "mscAtmIfUniSigRxPdus": mscAtmIfUniSigRxPdus,
       "mscAtmIfUniSigCurrentPmpConnections": mscAtmIfUniSigCurrentPmpConnections,
       "mscAtmIfUniSigPeakPmpConnections": mscAtmIfUniSigPeakPmpConnections,
       "mscAtmIfUniSigSuccessfulPmpConnections": mscAtmIfUniSigSuccessfulPmpConnections,
       "mscAtmIfUniSigFailedPmpConnections": mscAtmIfUniSigFailedPmpConnections,
       "mscAtmIfUniSigNewCurrentConnections": mscAtmIfUniSigNewCurrentConnections,
       "mscAtmIfUniAddr": mscAtmIfUniAddr,
       "mscAtmIfUniAddrRowStatusTable": mscAtmIfUniAddrRowStatusTable,
       "mscAtmIfUniAddrRowStatusEntry": mscAtmIfUniAddrRowStatusEntry,
       "mscAtmIfUniAddrRowStatus": mscAtmIfUniAddrRowStatus,
       "mscAtmIfUniAddrComponentName": mscAtmIfUniAddrComponentName,
       "mscAtmIfUniAddrStorageType": mscAtmIfUniAddrStorageType,
       "mscAtmIfUniAddrAddressIndex": mscAtmIfUniAddrAddressIndex,
       "mscAtmIfUniAddrAddressTypeIndex": mscAtmIfUniAddrAddressTypeIndex,
       "mscAtmIfUniAddrTermSP": mscAtmIfUniAddrTermSP,
       "mscAtmIfUniAddrTermSPRowStatusTable": mscAtmIfUniAddrTermSPRowStatusTable,
       "mscAtmIfUniAddrTermSPRowStatusEntry": mscAtmIfUniAddrTermSPRowStatusEntry,
       "mscAtmIfUniAddrTermSPRowStatus": mscAtmIfUniAddrTermSPRowStatus,
       "mscAtmIfUniAddrTermSPComponentName": mscAtmIfUniAddrTermSPComponentName,
       "mscAtmIfUniAddrTermSPStorageType": mscAtmIfUniAddrTermSPStorageType,
       "mscAtmIfUniAddrTermSPIndex": mscAtmIfUniAddrTermSPIndex,
       "mscAtmIfUniAddrPnniInfo": mscAtmIfUniAddrPnniInfo,
       "mscAtmIfUniAddrPnniInfoRowStatusTable": mscAtmIfUniAddrPnniInfoRowStatusTable,
       "mscAtmIfUniAddrPnniInfoRowStatusEntry": mscAtmIfUniAddrPnniInfoRowStatusEntry,
       "mscAtmIfUniAddrPnniInfoRowStatus": mscAtmIfUniAddrPnniInfoRowStatus,
       "mscAtmIfUniAddrPnniInfoComponentName": mscAtmIfUniAddrPnniInfoComponentName,
       "mscAtmIfUniAddrPnniInfoStorageType": mscAtmIfUniAddrPnniInfoStorageType,
       "mscAtmIfUniAddrPnniInfoIndex": mscAtmIfUniAddrPnniInfoIndex,
       "mscAtmIfUniAddrPnniInfoProvTable": mscAtmIfUniAddrPnniInfoProvTable,
       "mscAtmIfUniAddrPnniInfoProvEntry": mscAtmIfUniAddrPnniInfoProvEntry,
       "mscAtmIfUniAddrPnniInfoScope": mscAtmIfUniAddrPnniInfoScope,
       "mscAtmIfUniAddrPnniInfoReachability": mscAtmIfUniAddrPnniInfoReachability,
       "mscAtmIfUniAddrOperTable": mscAtmIfUniAddrOperTable,
       "mscAtmIfUniAddrOperEntry": mscAtmIfUniAddrOperEntry,
       "mscAtmIfUniAddrScope": mscAtmIfUniAddrScope,
       "mscAtmIfUniAddrReachability": mscAtmIfUniAddrReachability,
       "mscAtmIfUniCallingAScr": mscAtmIfUniCallingAScr,
       "mscAtmIfUniCallingAScrRowStatusTable": mscAtmIfUniCallingAScrRowStatusTable,
       "mscAtmIfUniCallingAScrRowStatusEntry": mscAtmIfUniCallingAScrRowStatusEntry,
       "mscAtmIfUniCallingAScrRowStatus": mscAtmIfUniCallingAScrRowStatus,
       "mscAtmIfUniCallingAScrComponentName": mscAtmIfUniCallingAScrComponentName,
       "mscAtmIfUniCallingAScrStorageType": mscAtmIfUniCallingAScrStorageType,
       "mscAtmIfUniCallingAScrIndex": mscAtmIfUniCallingAScrIndex,
       "mscAtmIfUniCallingAScrAddr": mscAtmIfUniCallingAScrAddr,
       "mscAtmIfUniCallingAScrAddrRowStatusTable": mscAtmIfUniCallingAScrAddrRowStatusTable,
       "mscAtmIfUniCallingAScrAddrRowStatusEntry": mscAtmIfUniCallingAScrAddrRowStatusEntry,
       "mscAtmIfUniCallingAScrAddrRowStatus": mscAtmIfUniCallingAScrAddrRowStatus,
       "mscAtmIfUniCallingAScrAddrComponentName": mscAtmIfUniCallingAScrAddrComponentName,
       "mscAtmIfUniCallingAScrAddrStorageType": mscAtmIfUniCallingAScrAddrStorageType,
       "mscAtmIfUniCallingAScrAddrAddressIndex": mscAtmIfUniCallingAScrAddrAddressIndex,
       "mscAtmIfUniCallingAScrAddrAddressActionIndex": mscAtmIfUniCallingAScrAddrAddressActionIndex,
       "mscAtmIfUniCallingAScrProvTable": mscAtmIfUniCallingAScrProvTable,
       "mscAtmIfUniCallingAScrProvEntry": mscAtmIfUniCallingAScrProvEntry,
       "mscAtmIfUniCallingAScrAdminStatus": mscAtmIfUniCallingAScrAdminStatus,
       "mscAtmIfUniCallingAScrDefaultInsertionAddress": mscAtmIfUniCallingAScrDefaultInsertionAddress,
       "mscAtmIfUniCallingAScrStatTable": mscAtmIfUniCallingAScrStatTable,
       "mscAtmIfUniCallingAScrStatEntry": mscAtmIfUniCallingAScrStatEntry,
       "mscAtmIfUniCallingAScrAcceptedCalls": mscAtmIfUniCallingAScrAcceptedCalls,
       "mscAtmIfUniCallingAScrRejectedCalls": mscAtmIfUniCallingAScrRejectedCalls,
       "mscAtmIfUniCallingAScrUnmatchedCalls": mscAtmIfUniCallingAScrUnmatchedCalls,
       "mscAtmIfUniCalledAScr": mscAtmIfUniCalledAScr,
       "mscAtmIfUniCalledAScrRowStatusTable": mscAtmIfUniCalledAScrRowStatusTable,
       "mscAtmIfUniCalledAScrRowStatusEntry": mscAtmIfUniCalledAScrRowStatusEntry,
       "mscAtmIfUniCalledAScrRowStatus": mscAtmIfUniCalledAScrRowStatus,
       "mscAtmIfUniCalledAScrComponentName": mscAtmIfUniCalledAScrComponentName,
       "mscAtmIfUniCalledAScrStorageType": mscAtmIfUniCalledAScrStorageType,
       "mscAtmIfUniCalledAScrIndex": mscAtmIfUniCalledAScrIndex,
       "mscAtmIfUniCalledAScrAddr": mscAtmIfUniCalledAScrAddr,
       "mscAtmIfUniCalledAScrAddrRowStatusTable": mscAtmIfUniCalledAScrAddrRowStatusTable,
       "mscAtmIfUniCalledAScrAddrRowStatusEntry": mscAtmIfUniCalledAScrAddrRowStatusEntry,
       "mscAtmIfUniCalledAScrAddrRowStatus": mscAtmIfUniCalledAScrAddrRowStatus,
       "mscAtmIfUniCalledAScrAddrComponentName": mscAtmIfUniCalledAScrAddrComponentName,
       "mscAtmIfUniCalledAScrAddrStorageType": mscAtmIfUniCalledAScrAddrStorageType,
       "mscAtmIfUniCalledAScrAddrAddressIndex": mscAtmIfUniCalledAScrAddrAddressIndex,
       "mscAtmIfUniCalledAScrAddrAddressActionIndex": mscAtmIfUniCalledAScrAddrAddressActionIndex,
       "mscAtmIfUniCalledAScrProvTable": mscAtmIfUniCalledAScrProvTable,
       "mscAtmIfUniCalledAScrProvEntry": mscAtmIfUniCalledAScrProvEntry,
       "mscAtmIfUniCalledAScrAdminStatus": mscAtmIfUniCalledAScrAdminStatus,
       "mscAtmIfUniCalledAScrStatTable": mscAtmIfUniCalledAScrStatTable,
       "mscAtmIfUniCalledAScrStatEntry": mscAtmIfUniCalledAScrStatEntry,
       "mscAtmIfUniCalledAScrAcceptedCalls": mscAtmIfUniCalledAScrAcceptedCalls,
       "mscAtmIfUniCalledAScrRejectedCalls": mscAtmIfUniCalledAScrRejectedCalls,
       "mscAtmIfUniCalledAScrUnmatchedCalls": mscAtmIfUniCalledAScrUnmatchedCalls,
       "mscAtmIfUniProvTable": mscAtmIfUniProvTable,
       "mscAtmIfUniProvEntry": mscAtmIfUniProvEntry,
       "mscAtmIfUniVersion": mscAtmIfUniVersion,
       "mscAtmIfUniSide": mscAtmIfUniSide,
       "mscAtmIfUniSoftPvcRetryPeriod": mscAtmIfUniSoftPvcRetryPeriod,
       "mscAtmIfUniSoftPvpAndPvcRetryPeriod": mscAtmIfUniSoftPvpAndPvcRetryPeriod,
       "mscAtmIfUniSoftPvpAndPvcHoldOffTime": mscAtmIfUniSoftPvpAndPvcHoldOffTime,
       "mscAtmIfUniLoopPrevention": mscAtmIfUniLoopPrevention,
       "mscAtmIfUniOperTable": mscAtmIfUniOperTable,
       "mscAtmIfUniOperEntry": mscAtmIfUniOperEntry,
       "mscAtmIfUniMacAddress": mscAtmIfUniMacAddress,
       "mscAtmIfUniAcctOptTable": mscAtmIfUniAcctOptTable,
       "mscAtmIfUniAcctOptEntry": mscAtmIfUniAcctOptEntry,
       "mscAtmIfUniAccountCollection": mscAtmIfUniAccountCollection,
       "mscAtmIfUniAccountConnectionType": mscAtmIfUniAccountConnectionType,
       "mscAtmIfUniAccountClass": mscAtmIfUniAccountClass,
       "mscAtmIfUniServiceExchange": mscAtmIfUniServiceExchange,
       "mscAtmIfVptUni": mscAtmIfVptUni,
       "mscAtmIfVptUniRowStatusTable": mscAtmIfVptUniRowStatusTable,
       "mscAtmIfVptUniRowStatusEntry": mscAtmIfVptUniRowStatusEntry,
       "mscAtmIfVptUniRowStatus": mscAtmIfVptUniRowStatus,
       "mscAtmIfVptUniComponentName": mscAtmIfVptUniComponentName,
       "mscAtmIfVptUniStorageType": mscAtmIfVptUniStorageType,
       "mscAtmIfVptUniIndex": mscAtmIfVptUniIndex,
       "mscAtmIfVptUniSig": mscAtmIfVptUniSig,
       "mscAtmIfVptUniSigRowStatusTable": mscAtmIfVptUniSigRowStatusTable,
       "mscAtmIfVptUniSigRowStatusEntry": mscAtmIfVptUniSigRowStatusEntry,
       "mscAtmIfVptUniSigRowStatus": mscAtmIfVptUniSigRowStatus,
       "mscAtmIfVptUniSigComponentName": mscAtmIfVptUniSigComponentName,
       "mscAtmIfVptUniSigStorageType": mscAtmIfVptUniSigStorageType,
       "mscAtmIfVptUniSigIndex": mscAtmIfVptUniSigIndex,
       "mscAtmIfVptUniSigVcd": mscAtmIfVptUniSigVcd,
       "mscAtmIfVptUniSigVcdRowStatusTable": mscAtmIfVptUniSigVcdRowStatusTable,
       "mscAtmIfVptUniSigVcdRowStatusEntry": mscAtmIfVptUniSigVcdRowStatusEntry,
       "mscAtmIfVptUniSigVcdRowStatus": mscAtmIfVptUniSigVcdRowStatus,
       "mscAtmIfVptUniSigVcdComponentName": mscAtmIfVptUniSigVcdComponentName,
       "mscAtmIfVptUniSigVcdStorageType": mscAtmIfVptUniSigVcdStorageType,
       "mscAtmIfVptUniSigVcdIndex": mscAtmIfVptUniSigVcdIndex,
       "mscAtmIfVptUniSigVcdProvTable": mscAtmIfVptUniSigVcdProvTable,
       "mscAtmIfVptUniSigVcdProvEntry": mscAtmIfVptUniSigVcdProvEntry,
       "mscAtmIfVptUniSigVcdTrafficDescType": mscAtmIfVptUniSigVcdTrafficDescType,
       "mscAtmIfVptUniSigVcdAtmServiceCategory": mscAtmIfVptUniSigVcdAtmServiceCategory,
       "mscAtmIfVptUniSigVcdWeight": mscAtmIfVptUniSigVcdWeight,
       "mscAtmIfVptUniSigVcdQosClass": mscAtmIfVptUniSigVcdQosClass,
       "mscAtmIfVptUniSigVcdTrafficShaping": mscAtmIfVptUniSigVcdTrafficShaping,
       "mscAtmIfVptUniSigVcdUnshapedTransmitQueueing": mscAtmIfVptUniSigVcdUnshapedTransmitQueueing,
       "mscAtmIfVptUniSigVcdUsageParameterControl": mscAtmIfVptUniSigVcdUsageParameterControl,
       "mscAtmIfVptUniSigVcdTdpTable": mscAtmIfVptUniSigVcdTdpTable,
       "mscAtmIfVptUniSigVcdTdpEntry": mscAtmIfVptUniSigVcdTdpEntry,
       "mscAtmIfVptUniSigVcdTdpIndex": mscAtmIfVptUniSigVcdTdpIndex,
       "mscAtmIfVptUniSigVcdTdpValue": mscAtmIfVptUniSigVcdTdpValue,
       "mscAtmIfVptUniSigProvTable": mscAtmIfVptUniSigProvTable,
       "mscAtmIfVptUniSigProvEntry": mscAtmIfVptUniSigProvEntry,
       "mscAtmIfVptUniSigVci": mscAtmIfVptUniSigVci,
       "mscAtmIfVptUniSigAddressConversion": mscAtmIfVptUniSigAddressConversion,
       "mscAtmIfVptUniSigOperatingMode": mscAtmIfVptUniSigOperatingMode,
       "mscAtmIfVptUniSigStateTable": mscAtmIfVptUniSigStateTable,
       "mscAtmIfVptUniSigStateEntry": mscAtmIfVptUniSigStateEntry,
       "mscAtmIfVptUniSigAdminState": mscAtmIfVptUniSigAdminState,
       "mscAtmIfVptUniSigOperationalState": mscAtmIfVptUniSigOperationalState,
       "mscAtmIfVptUniSigUsageState": mscAtmIfVptUniSigUsageState,
       "mscAtmIfVptUniSigOperTable": mscAtmIfVptUniSigOperTable,
       "mscAtmIfVptUniSigOperEntry": mscAtmIfVptUniSigOperEntry,
       "mscAtmIfVptUniSigLastTxCauseCode": mscAtmIfVptUniSigLastTxCauseCode,
       "mscAtmIfVptUniSigLastTxDiagCode": mscAtmIfVptUniSigLastTxDiagCode,
       "mscAtmIfVptUniSigLastRxCauseCode": mscAtmIfVptUniSigLastRxCauseCode,
       "mscAtmIfVptUniSigLastRxDiagCode": mscAtmIfVptUniSigLastRxDiagCode,
       "mscAtmIfVptUniSigStatsTable": mscAtmIfVptUniSigStatsTable,
       "mscAtmIfVptUniSigStatsEntry": mscAtmIfVptUniSigStatsEntry,
       "mscAtmIfVptUniSigCurrentConnections": mscAtmIfVptUniSigCurrentConnections,
       "mscAtmIfVptUniSigPeakConnections": mscAtmIfVptUniSigPeakConnections,
       "mscAtmIfVptUniSigSuccessfulConnections": mscAtmIfVptUniSigSuccessfulConnections,
       "mscAtmIfVptUniSigFailedConnections": mscAtmIfVptUniSigFailedConnections,
       "mscAtmIfVptUniSigTxPdus": mscAtmIfVptUniSigTxPdus,
       "mscAtmIfVptUniSigRxPdus": mscAtmIfVptUniSigRxPdus,
       "mscAtmIfVptUniSigCurrentPmpConnections": mscAtmIfVptUniSigCurrentPmpConnections,
       "mscAtmIfVptUniSigPeakPmpConnections": mscAtmIfVptUniSigPeakPmpConnections,
       "mscAtmIfVptUniSigSuccessfulPmpConnections": mscAtmIfVptUniSigSuccessfulPmpConnections,
       "mscAtmIfVptUniSigFailedPmpConnections": mscAtmIfVptUniSigFailedPmpConnections,
       "mscAtmIfVptUniSigNewCurrentConnections": mscAtmIfVptUniSigNewCurrentConnections,
       "mscAtmIfVptUniAddr": mscAtmIfVptUniAddr,
       "mscAtmIfVptUniAddrRowStatusTable": mscAtmIfVptUniAddrRowStatusTable,
       "mscAtmIfVptUniAddrRowStatusEntry": mscAtmIfVptUniAddrRowStatusEntry,
       "mscAtmIfVptUniAddrRowStatus": mscAtmIfVptUniAddrRowStatus,
       "mscAtmIfVptUniAddrComponentName": mscAtmIfVptUniAddrComponentName,
       "mscAtmIfVptUniAddrStorageType": mscAtmIfVptUniAddrStorageType,
       "mscAtmIfVptUniAddrAddressIndex": mscAtmIfVptUniAddrAddressIndex,
       "mscAtmIfVptUniAddrAddressTypeIndex": mscAtmIfVptUniAddrAddressTypeIndex,
       "mscAtmIfVptUniAddrTermSP": mscAtmIfVptUniAddrTermSP,
       "mscAtmIfVptUniAddrTermSPRowStatusTable": mscAtmIfVptUniAddrTermSPRowStatusTable,
       "mscAtmIfVptUniAddrTermSPRowStatusEntry": mscAtmIfVptUniAddrTermSPRowStatusEntry,
       "mscAtmIfVptUniAddrTermSPRowStatus": mscAtmIfVptUniAddrTermSPRowStatus,
       "mscAtmIfVptUniAddrTermSPComponentName": mscAtmIfVptUniAddrTermSPComponentName,
       "mscAtmIfVptUniAddrTermSPStorageType": mscAtmIfVptUniAddrTermSPStorageType,
       "mscAtmIfVptUniAddrTermSPIndex": mscAtmIfVptUniAddrTermSPIndex,
       "mscAtmIfVptUniAddrPnniInfo": mscAtmIfVptUniAddrPnniInfo,
       "mscAtmIfVptUniAddrPnniInfoRowStatusTable": mscAtmIfVptUniAddrPnniInfoRowStatusTable,
       "mscAtmIfVptUniAddrPnniInfoRowStatusEntry": mscAtmIfVptUniAddrPnniInfoRowStatusEntry,
       "mscAtmIfVptUniAddrPnniInfoRowStatus": mscAtmIfVptUniAddrPnniInfoRowStatus,
       "mscAtmIfVptUniAddrPnniInfoComponentName": mscAtmIfVptUniAddrPnniInfoComponentName,
       "mscAtmIfVptUniAddrPnniInfoStorageType": mscAtmIfVptUniAddrPnniInfoStorageType,
       "mscAtmIfVptUniAddrPnniInfoIndex": mscAtmIfVptUniAddrPnniInfoIndex,
       "mscAtmIfVptUniAddrPnniInfoProvTable": mscAtmIfVptUniAddrPnniInfoProvTable,
       "mscAtmIfVptUniAddrPnniInfoProvEntry": mscAtmIfVptUniAddrPnniInfoProvEntry,
       "mscAtmIfVptUniAddrPnniInfoScope": mscAtmIfVptUniAddrPnniInfoScope,
       "mscAtmIfVptUniAddrPnniInfoReachability": mscAtmIfVptUniAddrPnniInfoReachability,
       "mscAtmIfVptUniAddrOperTable": mscAtmIfVptUniAddrOperTable,
       "mscAtmIfVptUniAddrOperEntry": mscAtmIfVptUniAddrOperEntry,
       "mscAtmIfVptUniAddrScope": mscAtmIfVptUniAddrScope,
       "mscAtmIfVptUniAddrReachability": mscAtmIfVptUniAddrReachability,
       "mscAtmIfVptUniCallingAScr": mscAtmIfVptUniCallingAScr,
       "mscAtmIfVptUniCallingAScrRowStatusTable": mscAtmIfVptUniCallingAScrRowStatusTable,
       "mscAtmIfVptUniCallingAScrRowStatusEntry": mscAtmIfVptUniCallingAScrRowStatusEntry,
       "mscAtmIfVptUniCallingAScrRowStatus": mscAtmIfVptUniCallingAScrRowStatus,
       "mscAtmIfVptUniCallingAScrComponentName": mscAtmIfVptUniCallingAScrComponentName,
       "mscAtmIfVptUniCallingAScrStorageType": mscAtmIfVptUniCallingAScrStorageType,
       "mscAtmIfVptUniCallingAScrIndex": mscAtmIfVptUniCallingAScrIndex,
       "mscAtmIfVptUniCallingAScrAddr": mscAtmIfVptUniCallingAScrAddr,
       "mscAtmIfVptUniCallingAScrAddrRowStatusTable": mscAtmIfVptUniCallingAScrAddrRowStatusTable,
       "mscAtmIfVptUniCallingAScrAddrRowStatusEntry": mscAtmIfVptUniCallingAScrAddrRowStatusEntry,
       "mscAtmIfVptUniCallingAScrAddrRowStatus": mscAtmIfVptUniCallingAScrAddrRowStatus,
       "mscAtmIfVptUniCallingAScrAddrComponentName": mscAtmIfVptUniCallingAScrAddrComponentName,
       "mscAtmIfVptUniCallingAScrAddrStorageType": mscAtmIfVptUniCallingAScrAddrStorageType,
       "mscAtmIfVptUniCallingAScrAddrAddressIndex": mscAtmIfVptUniCallingAScrAddrAddressIndex,
       "mscAtmIfVptUniCallingAScrAddrAddressActionIndex": mscAtmIfVptUniCallingAScrAddrAddressActionIndex,
       "mscAtmIfVptUniCallingAScrProvTable": mscAtmIfVptUniCallingAScrProvTable,
       "mscAtmIfVptUniCallingAScrProvEntry": mscAtmIfVptUniCallingAScrProvEntry,
       "mscAtmIfVptUniCallingAScrAdminStatus": mscAtmIfVptUniCallingAScrAdminStatus,
       "mscAtmIfVptUniCallingAScrDefaultInsertionAddress": mscAtmIfVptUniCallingAScrDefaultInsertionAddress,
       "mscAtmIfVptUniCallingAScrStatTable": mscAtmIfVptUniCallingAScrStatTable,
       "mscAtmIfVptUniCallingAScrStatEntry": mscAtmIfVptUniCallingAScrStatEntry,
       "mscAtmIfVptUniCallingAScrAcceptedCalls": mscAtmIfVptUniCallingAScrAcceptedCalls,
       "mscAtmIfVptUniCallingAScrRejectedCalls": mscAtmIfVptUniCallingAScrRejectedCalls,
       "mscAtmIfVptUniCallingAScrUnmatchedCalls": mscAtmIfVptUniCallingAScrUnmatchedCalls,
       "mscAtmIfVptUniCalledAScr": mscAtmIfVptUniCalledAScr,
       "mscAtmIfVptUniCalledAScrRowStatusTable": mscAtmIfVptUniCalledAScrRowStatusTable,
       "mscAtmIfVptUniCalledAScrRowStatusEntry": mscAtmIfVptUniCalledAScrRowStatusEntry,
       "mscAtmIfVptUniCalledAScrRowStatus": mscAtmIfVptUniCalledAScrRowStatus,
       "mscAtmIfVptUniCalledAScrComponentName": mscAtmIfVptUniCalledAScrComponentName,
       "mscAtmIfVptUniCalledAScrStorageType": mscAtmIfVptUniCalledAScrStorageType,
       "mscAtmIfVptUniCalledAScrIndex": mscAtmIfVptUniCalledAScrIndex,
       "mscAtmIfVptUniCalledAScrAddr": mscAtmIfVptUniCalledAScrAddr,
       "mscAtmIfVptUniCalledAScrAddrRowStatusTable": mscAtmIfVptUniCalledAScrAddrRowStatusTable,
       "mscAtmIfVptUniCalledAScrAddrRowStatusEntry": mscAtmIfVptUniCalledAScrAddrRowStatusEntry,
       "mscAtmIfVptUniCalledAScrAddrRowStatus": mscAtmIfVptUniCalledAScrAddrRowStatus,
       "mscAtmIfVptUniCalledAScrAddrComponentName": mscAtmIfVptUniCalledAScrAddrComponentName,
       "mscAtmIfVptUniCalledAScrAddrStorageType": mscAtmIfVptUniCalledAScrAddrStorageType,
       "mscAtmIfVptUniCalledAScrAddrAddressIndex": mscAtmIfVptUniCalledAScrAddrAddressIndex,
       "mscAtmIfVptUniCalledAScrAddrAddressActionIndex": mscAtmIfVptUniCalledAScrAddrAddressActionIndex,
       "mscAtmIfVptUniCalledAScrProvTable": mscAtmIfVptUniCalledAScrProvTable,
       "mscAtmIfVptUniCalledAScrProvEntry": mscAtmIfVptUniCalledAScrProvEntry,
       "mscAtmIfVptUniCalledAScrAdminStatus": mscAtmIfVptUniCalledAScrAdminStatus,
       "mscAtmIfVptUniCalledAScrStatTable": mscAtmIfVptUniCalledAScrStatTable,
       "mscAtmIfVptUniCalledAScrStatEntry": mscAtmIfVptUniCalledAScrStatEntry,
       "mscAtmIfVptUniCalledAScrAcceptedCalls": mscAtmIfVptUniCalledAScrAcceptedCalls,
       "mscAtmIfVptUniCalledAScrRejectedCalls": mscAtmIfVptUniCalledAScrRejectedCalls,
       "mscAtmIfVptUniCalledAScrUnmatchedCalls": mscAtmIfVptUniCalledAScrUnmatchedCalls,
       "mscAtmIfVptUniProvTable": mscAtmIfVptUniProvTable,
       "mscAtmIfVptUniProvEntry": mscAtmIfVptUniProvEntry,
       "mscAtmIfVptUniVersion": mscAtmIfVptUniVersion,
       "mscAtmIfVptUniSide": mscAtmIfVptUniSide,
       "mscAtmIfVptUniSoftPvcRetryPeriod": mscAtmIfVptUniSoftPvcRetryPeriod,
       "mscAtmIfVptUniSoftPvpAndPvcRetryPeriod": mscAtmIfVptUniSoftPvpAndPvcRetryPeriod,
       "mscAtmIfVptUniSoftPvpAndPvcHoldOffTime": mscAtmIfVptUniSoftPvpAndPvcHoldOffTime,
       "mscAtmIfVptUniLoopPrevention": mscAtmIfVptUniLoopPrevention,
       "mscAtmIfVptUniAcctOptTable": mscAtmIfVptUniAcctOptTable,
       "mscAtmIfVptUniAcctOptEntry": mscAtmIfVptUniAcctOptEntry,
       "mscAtmIfVptUniAccountCollection": mscAtmIfVptUniAccountCollection,
       "mscAtmIfVptUniAccountConnectionType": mscAtmIfVptUniAccountConnectionType,
       "mscAtmIfVptUniAccountClass": mscAtmIfVptUniAccountClass,
       "mscAtmIfVptUniServiceExchange": mscAtmIfVptUniServiceExchange,
       "mscAtmIfVptUniVProvTable": mscAtmIfVptUniVProvTable,
       "mscAtmIfVptUniVProvEntry": mscAtmIfVptUniVProvEntry,
       "mscAtmIfVptUniVpci": mscAtmIfVptUniVpci,
       "atmUniMIB": atmUniMIB,
       "atmUniGroup": atmUniGroup,
       "atmUniGroupCA": atmUniGroupCA,
       "atmUniGroupCA02": atmUniGroupCA02,
       "atmUniGroupCA02A": atmUniGroupCA02A,
       "atmUniCapabilities": atmUniCapabilities,
       "atmUniCapabilitiesCA": atmUniCapabilitiesCA,
       "atmUniCapabilitiesCA02": atmUniCapabilitiesCA02,
       "atmUniCapabilitiesCA02A": atmUniCapabilitiesCA02A}
)
