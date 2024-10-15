# SNMP MIB module (Nortel-Magellan-Passport-HdlcTransparentMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-HdlcTransparentMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:54 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
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

_Htds_ObjectIdentity = ObjectIdentity
htds = _Htds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82)
)
_HtdsRowStatusTable_Object = MibTable
htdsRowStatusTable = _HtdsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1)
)
if mibBuilder.loadTexts:
    htdsRowStatusTable.setStatus("mandatory")
_HtdsRowStatusEntry_Object = MibTableRow
htdsRowStatusEntry = _HtdsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1, 1)
)
htdsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
)
if mibBuilder.loadTexts:
    htdsRowStatusEntry.setStatus("mandatory")
_HtdsRowStatus_Type = RowStatus
_HtdsRowStatus_Object = MibTableColumn
htdsRowStatus = _HtdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1, 1, 1),
    _HtdsRowStatus_Type()
)
htdsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsRowStatus.setStatus("mandatory")
_HtdsComponentName_Type = DisplayString
_HtdsComponentName_Object = MibTableColumn
htdsComponentName = _HtdsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1, 1, 2),
    _HtdsComponentName_Type()
)
htdsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsComponentName.setStatus("mandatory")
_HtdsStorageType_Type = StorageType
_HtdsStorageType_Object = MibTableColumn
htdsStorageType = _HtdsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1, 1, 4),
    _HtdsStorageType_Type()
)
htdsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsStorageType.setStatus("mandatory")


class _HtdsIndex_Type(Integer32):
    """Custom type htdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HtdsIndex_Type.__name__ = "Integer32"
_HtdsIndex_Object = MibTableColumn
htdsIndex = _HtdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 1, 1, 10),
    _HtdsIndex_Type()
)
htdsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    htdsIndex.setStatus("mandatory")
_HtdsFramer_ObjectIdentity = ObjectIdentity
htdsFramer = _HtdsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2)
)
_HtdsFramerRowStatusTable_Object = MibTable
htdsFramerRowStatusTable = _HtdsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1)
)
if mibBuilder.loadTexts:
    htdsFramerRowStatusTable.setStatus("mandatory")
_HtdsFramerRowStatusEntry_Object = MibTableRow
htdsFramerRowStatusEntry = _HtdsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1, 1)
)
htdsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerRowStatusEntry.setStatus("mandatory")
_HtdsFramerRowStatus_Type = RowStatus
_HtdsFramerRowStatus_Object = MibTableColumn
htdsFramerRowStatus = _HtdsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1, 1, 1),
    _HtdsFramerRowStatus_Type()
)
htdsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerRowStatus.setStatus("mandatory")
_HtdsFramerComponentName_Type = DisplayString
_HtdsFramerComponentName_Object = MibTableColumn
htdsFramerComponentName = _HtdsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1, 1, 2),
    _HtdsFramerComponentName_Type()
)
htdsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerComponentName.setStatus("mandatory")
_HtdsFramerStorageType_Type = StorageType
_HtdsFramerStorageType_Object = MibTableColumn
htdsFramerStorageType = _HtdsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1, 1, 4),
    _HtdsFramerStorageType_Type()
)
htdsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerStorageType.setStatus("mandatory")
_HtdsFramerIndex_Type = NonReplicated
_HtdsFramerIndex_Object = MibTableColumn
htdsFramerIndex = _HtdsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 1, 1, 10),
    _HtdsFramerIndex_Type()
)
htdsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    htdsFramerIndex.setStatus("mandatory")
_HtdsFramerProvTable_Object = MibTable
htdsFramerProvTable = _HtdsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 10)
)
if mibBuilder.loadTexts:
    htdsFramerProvTable.setStatus("mandatory")
_HtdsFramerProvEntry_Object = MibTableRow
htdsFramerProvEntry = _HtdsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 10, 1)
)
htdsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerProvEntry.setStatus("mandatory")
_HtdsFramerInterfaceName_Type = Link
_HtdsFramerInterfaceName_Object = MibTableColumn
htdsFramerInterfaceName = _HtdsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 10, 1, 1),
    _HtdsFramerInterfaceName_Type()
)
htdsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerInterfaceName.setStatus("mandatory")
_HtdsFramerLinkTable_Object = MibTable
htdsFramerLinkTable = _HtdsFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11)
)
if mibBuilder.loadTexts:
    htdsFramerLinkTable.setStatus("mandatory")
_HtdsFramerLinkEntry_Object = MibTableRow
htdsFramerLinkEntry = _HtdsFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1)
)
htdsFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerLinkEntry.setStatus("mandatory")


class _HtdsFramerDataInversion_Type(Integer32):
    """Custom type htdsFramerDataInversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 16))
    )


_HtdsFramerDataInversion_Type.__name__ = "Integer32"
_HtdsFramerDataInversion_Object = MibTableColumn
htdsFramerDataInversion = _HtdsFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1, 2),
    _HtdsFramerDataInversion_Type()
)
htdsFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerDataInversion.setStatus("mandatory")


class _HtdsFramerNonOctetData_Type(Integer32):
    """Custom type htdsFramerNonOctetData based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HtdsFramerNonOctetData_Type.__name__ = "Integer32"
_HtdsFramerNonOctetData_Object = MibTableColumn
htdsFramerNonOctetData = _HtdsFramerNonOctetData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1, 3),
    _HtdsFramerNonOctetData_Type()
)
htdsFramerNonOctetData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerNonOctetData.setStatus("mandatory")


class _HtdsFramerFrameCrcType_Type(Integer32):
    """Custom type htdsFramerFrameCrcType based on Integer32"""
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
        *(("crc16", 0),
          ("crc32", 1),
          ("noCrc", 2))
    )


_HtdsFramerFrameCrcType_Type.__name__ = "Integer32"
_HtdsFramerFrameCrcType_Object = MibTableColumn
htdsFramerFrameCrcType = _HtdsFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1, 4),
    _HtdsFramerFrameCrcType_Type()
)
htdsFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerFrameCrcType.setStatus("mandatory")


class _HtdsFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type htdsFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HtdsFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_HtdsFramerFlagsBetweenFrames_Object = MibTableColumn
htdsFramerFlagsBetweenFrames = _HtdsFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1, 5),
    _HtdsFramerFlagsBetweenFrames_Type()
)
htdsFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerFlagsBetweenFrames.setStatus("mandatory")


class _HtdsFramerLineSignalTransport_Type(Integer32):
    """Custom type htdsFramerLineSignalTransport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HtdsFramerLineSignalTransport_Type.__name__ = "Integer32"
_HtdsFramerLineSignalTransport_Object = MibTableColumn
htdsFramerLineSignalTransport = _HtdsFramerLineSignalTransport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 11, 1, 8),
    _HtdsFramerLineSignalTransport_Type()
)
htdsFramerLineSignalTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsFramerLineSignalTransport.setStatus("mandatory")
_HtdsFramerStateTable_Object = MibTable
htdsFramerStateTable = _HtdsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 12)
)
if mibBuilder.loadTexts:
    htdsFramerStateTable.setStatus("mandatory")
_HtdsFramerStateEntry_Object = MibTableRow
htdsFramerStateEntry = _HtdsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 12, 1)
)
htdsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerStateEntry.setStatus("mandatory")


class _HtdsFramerAdminState_Type(Integer32):
    """Custom type htdsFramerAdminState based on Integer32"""
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


_HtdsFramerAdminState_Type.__name__ = "Integer32"
_HtdsFramerAdminState_Object = MibTableColumn
htdsFramerAdminState = _HtdsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 12, 1, 1),
    _HtdsFramerAdminState_Type()
)
htdsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerAdminState.setStatus("mandatory")


class _HtdsFramerOperationalState_Type(Integer32):
    """Custom type htdsFramerOperationalState based on Integer32"""
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


_HtdsFramerOperationalState_Type.__name__ = "Integer32"
_HtdsFramerOperationalState_Object = MibTableColumn
htdsFramerOperationalState = _HtdsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 12, 1, 2),
    _HtdsFramerOperationalState_Type()
)
htdsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerOperationalState.setStatus("mandatory")


class _HtdsFramerUsageState_Type(Integer32):
    """Custom type htdsFramerUsageState based on Integer32"""
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


_HtdsFramerUsageState_Type.__name__ = "Integer32"
_HtdsFramerUsageState_Object = MibTableColumn
htdsFramerUsageState = _HtdsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 12, 1, 3),
    _HtdsFramerUsageState_Type()
)
htdsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerUsageState.setStatus("mandatory")
_HtdsFramerStatsTable_Object = MibTable
htdsFramerStatsTable = _HtdsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13)
)
if mibBuilder.loadTexts:
    htdsFramerStatsTable.setStatus("mandatory")
_HtdsFramerStatsEntry_Object = MibTableRow
htdsFramerStatsEntry = _HtdsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1)
)
htdsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerStatsEntry.setStatus("mandatory")
_HtdsFramerFrmToIf_Type = Counter32
_HtdsFramerFrmToIf_Object = MibTableColumn
htdsFramerFrmToIf = _HtdsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 1),
    _HtdsFramerFrmToIf_Type()
)
htdsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerFrmToIf.setStatus("mandatory")
_HtdsFramerFrmFromIf_Type = Counter32
_HtdsFramerFrmFromIf_Object = MibTableColumn
htdsFramerFrmFromIf = _HtdsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 2),
    _HtdsFramerFrmFromIf_Type()
)
htdsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerFrmFromIf.setStatus("mandatory")
_HtdsFramerOctetFromIf_Type = Counter32
_HtdsFramerOctetFromIf_Object = MibTableColumn
htdsFramerOctetFromIf = _HtdsFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 3),
    _HtdsFramerOctetFromIf_Type()
)
htdsFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerOctetFromIf.setStatus("mandatory")
_HtdsFramerAborts_Type = Counter32
_HtdsFramerAborts_Object = MibTableColumn
htdsFramerAborts = _HtdsFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 4),
    _HtdsFramerAborts_Type()
)
htdsFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerAborts.setStatus("mandatory")
_HtdsFramerCrcErrors_Type = Counter32
_HtdsFramerCrcErrors_Object = MibTableColumn
htdsFramerCrcErrors = _HtdsFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 5),
    _HtdsFramerCrcErrors_Type()
)
htdsFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerCrcErrors.setStatus("mandatory")
_HtdsFramerLrcErrors_Type = Counter32
_HtdsFramerLrcErrors_Object = MibTableColumn
htdsFramerLrcErrors = _HtdsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 6),
    _HtdsFramerLrcErrors_Type()
)
htdsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerLrcErrors.setStatus("mandatory")
_HtdsFramerNonOctetErrors_Type = Counter32
_HtdsFramerNonOctetErrors_Object = MibTableColumn
htdsFramerNonOctetErrors = _HtdsFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 7),
    _HtdsFramerNonOctetErrors_Type()
)
htdsFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerNonOctetErrors.setStatus("mandatory")
_HtdsFramerOverruns_Type = Counter32
_HtdsFramerOverruns_Object = MibTableColumn
htdsFramerOverruns = _HtdsFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 8),
    _HtdsFramerOverruns_Type()
)
htdsFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerOverruns.setStatus("mandatory")
_HtdsFramerUnderruns_Type = Counter32
_HtdsFramerUnderruns_Object = MibTableColumn
htdsFramerUnderruns = _HtdsFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 9),
    _HtdsFramerUnderruns_Type()
)
htdsFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerUnderruns.setStatus("mandatory")
_HtdsFramerLargeFrmErrors_Type = Counter32
_HtdsFramerLargeFrmErrors_Object = MibTableColumn
htdsFramerLargeFrmErrors = _HtdsFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 13, 1, 10),
    _HtdsFramerLargeFrmErrors_Type()
)
htdsFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerLargeFrmErrors.setStatus("mandatory")
_HtdsFramerUtilTable_Object = MibTable
htdsFramerUtilTable = _HtdsFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 14)
)
if mibBuilder.loadTexts:
    htdsFramerUtilTable.setStatus("mandatory")
_HtdsFramerUtilEntry_Object = MibTableRow
htdsFramerUtilEntry = _HtdsFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 14, 1)
)
htdsFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsFramerIndex"),
)
if mibBuilder.loadTexts:
    htdsFramerUtilEntry.setStatus("mandatory")


class _HtdsFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type htdsFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HtdsFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_HtdsFramerNormPrioLinkUtilToIf_Object = MibTableColumn
htdsFramerNormPrioLinkUtilToIf = _HtdsFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 14, 1, 1),
    _HtdsFramerNormPrioLinkUtilToIf_Type()
)
htdsFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _HtdsFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type htdsFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HtdsFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_HtdsFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
htdsFramerNormPrioLinkUtilFromIf = _HtdsFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 2, 14, 1, 3),
    _HtdsFramerNormPrioLinkUtilFromIf_Type()
)
htdsFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_HtdsPlc_ObjectIdentity = ObjectIdentity
htdsPlc = _HtdsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3)
)
_HtdsPlcRowStatusTable_Object = MibTable
htdsPlcRowStatusTable = _HtdsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1)
)
if mibBuilder.loadTexts:
    htdsPlcRowStatusTable.setStatus("mandatory")
_HtdsPlcRowStatusEntry_Object = MibTableRow
htdsPlcRowStatusEntry = _HtdsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1, 1)
)
htdsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsPlcIndex"),
)
if mibBuilder.loadTexts:
    htdsPlcRowStatusEntry.setStatus("mandatory")
_HtdsPlcRowStatus_Type = RowStatus
_HtdsPlcRowStatus_Object = MibTableColumn
htdsPlcRowStatus = _HtdsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1, 1, 1),
    _HtdsPlcRowStatus_Type()
)
htdsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsPlcRowStatus.setStatus("mandatory")
_HtdsPlcComponentName_Type = DisplayString
_HtdsPlcComponentName_Object = MibTableColumn
htdsPlcComponentName = _HtdsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1, 1, 2),
    _HtdsPlcComponentName_Type()
)
htdsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsPlcComponentName.setStatus("mandatory")
_HtdsPlcStorageType_Type = StorageType
_HtdsPlcStorageType_Object = MibTableColumn
htdsPlcStorageType = _HtdsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1, 1, 4),
    _HtdsPlcStorageType_Type()
)
htdsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsPlcStorageType.setStatus("mandatory")
_HtdsPlcIndex_Type = NonReplicated
_HtdsPlcIndex_Object = MibTableColumn
htdsPlcIndex = _HtdsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 1, 1, 10),
    _HtdsPlcIndex_Type()
)
htdsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    htdsPlcIndex.setStatus("mandatory")
_HtdsPlcProvTable_Object = MibTable
htdsPlcProvTable = _HtdsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10)
)
if mibBuilder.loadTexts:
    htdsPlcProvTable.setStatus("mandatory")
_HtdsPlcProvEntry_Object = MibTableRow
htdsPlcProvEntry = _HtdsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1)
)
htdsPlcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsPlcIndex"),
)
if mibBuilder.loadTexts:
    htdsPlcProvEntry.setStatus("mandatory")


class _HtdsPlcRemoteName_Type(AsciiString):
    """Custom type htdsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HtdsPlcRemoteName_Type.__name__ = "AsciiString"
_HtdsPlcRemoteName_Object = MibTableColumn
htdsPlcRemoteName = _HtdsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 2),
    _HtdsPlcRemoteName_Type()
)
htdsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRemoteName.setStatus("mandatory")


class _HtdsPlcSetupPriority_Type(Unsigned32):
    """Custom type htdsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HtdsPlcSetupPriority_Type.__name__ = "Unsigned32"
_HtdsPlcSetupPriority_Object = MibTableColumn
htdsPlcSetupPriority = _HtdsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 3),
    _HtdsPlcSetupPriority_Type()
)
htdsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcSetupPriority.setStatus("mandatory")


class _HtdsPlcHoldingPriority_Type(Unsigned32):
    """Custom type htdsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HtdsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_HtdsPlcHoldingPriority_Object = MibTableColumn
htdsPlcHoldingPriority = _HtdsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 4),
    _HtdsPlcHoldingPriority_Type()
)
htdsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcHoldingPriority.setStatus("mandatory")


class _HtdsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type htdsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HtdsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_HtdsPlcRequiredTxBandwidth_Object = MibTableColumn
htdsPlcRequiredTxBandwidth = _HtdsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 5),
    _HtdsPlcRequiredTxBandwidth_Type()
)
htdsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRequiredTxBandwidth.setStatus("mandatory")


class _HtdsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type htdsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HtdsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_HtdsPlcRequiredRxBandwidth_Object = MibTableColumn
htdsPlcRequiredRxBandwidth = _HtdsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 6),
    _HtdsPlcRequiredRxBandwidth_Type()
)
htdsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRequiredRxBandwidth.setStatus("mandatory")


class _HtdsPlcRequiredTrafficType_Type(Integer32):
    """Custom type htdsPlcRequiredTrafficType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_HtdsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_HtdsPlcRequiredTrafficType_Object = MibTableColumn
htdsPlcRequiredTrafficType = _HtdsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 7),
    _HtdsPlcRequiredTrafficType_Type()
)
htdsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRequiredTrafficType.setStatus("mandatory")


class _HtdsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type htdsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HtdsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_HtdsPlcPermittedTrunkTypes_Object = MibTableColumn
htdsPlcPermittedTrunkTypes = _HtdsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 8),
    _HtdsPlcPermittedTrunkTypes_Type()
)
htdsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcPermittedTrunkTypes.setStatus("mandatory")


class _HtdsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type htdsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HtdsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_HtdsPlcRequiredSecurity_Object = MibTableColumn
htdsPlcRequiredSecurity = _HtdsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 9),
    _HtdsPlcRequiredSecurity_Type()
)
htdsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRequiredSecurity.setStatus("mandatory")


class _HtdsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type htdsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HtdsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_HtdsPlcRequiredCustomerParm_Object = MibTableColumn
htdsPlcRequiredCustomerParm = _HtdsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 10),
    _HtdsPlcRequiredCustomerParm_Type()
)
htdsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcRequiredCustomerParm.setStatus("mandatory")


class _HtdsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type htdsPlcPathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_HtdsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_HtdsPlcPathAttributeToMinimize_Object = MibTableColumn
htdsPlcPathAttributeToMinimize = _HtdsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 11),
    _HtdsPlcPathAttributeToMinimize_Type()
)
htdsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcPathAttributeToMinimize.setStatus("mandatory")


class _HtdsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type htdsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HtdsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_HtdsPlcMaximumAcceptableCost_Object = MibTableColumn
htdsPlcMaximumAcceptableCost = _HtdsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 12),
    _HtdsPlcMaximumAcceptableCost_Type()
)
htdsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcMaximumAcceptableCost.setStatus("mandatory")


class _HtdsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type htdsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_HtdsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_HtdsPlcMaximumAcceptableDelay_Object = MibTableColumn
htdsPlcMaximumAcceptableDelay = _HtdsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 13),
    _HtdsPlcMaximumAcceptableDelay_Type()
)
htdsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _HtdsPlcEmissionPriority_Type(Unsigned32):
    """Custom type htdsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HtdsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_HtdsPlcEmissionPriority_Object = MibTableColumn
htdsPlcEmissionPriority = _HtdsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 14),
    _HtdsPlcEmissionPriority_Type()
)
htdsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcEmissionPriority.setStatus("mandatory")


class _HtdsPlcDiscardPriority_Type(Unsigned32):
    """Custom type htdsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HtdsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_HtdsPlcDiscardPriority_Object = MibTableColumn
htdsPlcDiscardPriority = _HtdsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 15),
    _HtdsPlcDiscardPriority_Type()
)
htdsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcDiscardPriority.setStatus("mandatory")


class _HtdsPlcPathType_Type(Integer32):
    """Custom type htdsPlcPathType based on Integer32"""
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
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_HtdsPlcPathType_Type.__name__ = "Integer32"
_HtdsPlcPathType_Object = MibTableColumn
htdsPlcPathType = _HtdsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 16),
    _HtdsPlcPathType_Type()
)
htdsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcPathType.setStatus("mandatory")


class _HtdsPlcPathFailureAction_Type(Integer32):
    """Custom type htdsPlcPathFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_HtdsPlcPathFailureAction_Type.__name__ = "Integer32"
_HtdsPlcPathFailureAction_Object = MibTableColumn
htdsPlcPathFailureAction = _HtdsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 17),
    _HtdsPlcPathFailureAction_Type()
)
htdsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcPathFailureAction.setStatus("mandatory")


class _HtdsPlcBumpPreference_Type(Integer32):
    """Custom type htdsPlcBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_HtdsPlcBumpPreference_Type.__name__ = "Integer32"
_HtdsPlcBumpPreference_Object = MibTableColumn
htdsPlcBumpPreference = _HtdsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 18),
    _HtdsPlcBumpPreference_Type()
)
htdsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcBumpPreference.setStatus("mandatory")


class _HtdsPlcOptimization_Type(Integer32):
    """Custom type htdsPlcOptimization based on Integer32"""
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


_HtdsPlcOptimization_Type.__name__ = "Integer32"
_HtdsPlcOptimization_Object = MibTableColumn
htdsPlcOptimization = _HtdsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 10, 1, 19),
    _HtdsPlcOptimization_Type()
)
htdsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcOptimization.setStatus("mandatory")
_HtdsPlcMpathTable_Object = MibTable
htdsPlcMpathTable = _HtdsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 265)
)
if mibBuilder.loadTexts:
    htdsPlcMpathTable.setStatus("mandatory")
_HtdsPlcMpathEntry_Object = MibTableRow
htdsPlcMpathEntry = _HtdsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 265, 1)
)
htdsPlcMpathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsPlcIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    htdsPlcMpathEntry.setStatus("mandatory")


class _HtdsPlcMpathIndex_Type(Integer32):
    """Custom type htdsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HtdsPlcMpathIndex_Type.__name__ = "Integer32"
_HtdsPlcMpathIndex_Object = MibTableColumn
htdsPlcMpathIndex = _HtdsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 265, 1, 1),
    _HtdsPlcMpathIndex_Type()
)
htdsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    htdsPlcMpathIndex.setStatus("mandatory")


class _HtdsPlcMpathValue_Type(AsciiString):
    """Custom type htdsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HtdsPlcMpathValue_Type.__name__ = "AsciiString"
_HtdsPlcMpathValue_Object = MibTableColumn
htdsPlcMpathValue = _HtdsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 3, 265, 1, 2),
    _HtdsPlcMpathValue_Type()
)
htdsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsPlcMpathValue.setStatus("mandatory")
_HtdsLCo_ObjectIdentity = ObjectIdentity
htdsLCo = _HtdsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4)
)
_HtdsLCoRowStatusTable_Object = MibTable
htdsLCoRowStatusTable = _HtdsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1)
)
if mibBuilder.loadTexts:
    htdsLCoRowStatusTable.setStatus("mandatory")
_HtdsLCoRowStatusEntry_Object = MibTableRow
htdsLCoRowStatusEntry = _HtdsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1, 1)
)
htdsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsLCoIndex"),
)
if mibBuilder.loadTexts:
    htdsLCoRowStatusEntry.setStatus("mandatory")
_HtdsLCoRowStatus_Type = RowStatus
_HtdsLCoRowStatus_Object = MibTableColumn
htdsLCoRowStatus = _HtdsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1, 1, 1),
    _HtdsLCoRowStatus_Type()
)
htdsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRowStatus.setStatus("mandatory")
_HtdsLCoComponentName_Type = DisplayString
_HtdsLCoComponentName_Object = MibTableColumn
htdsLCoComponentName = _HtdsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1, 1, 2),
    _HtdsLCoComponentName_Type()
)
htdsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoComponentName.setStatus("mandatory")
_HtdsLCoStorageType_Type = StorageType
_HtdsLCoStorageType_Object = MibTableColumn
htdsLCoStorageType = _HtdsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1, 1, 4),
    _HtdsLCoStorageType_Type()
)
htdsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoStorageType.setStatus("mandatory")
_HtdsLCoIndex_Type = NonReplicated
_HtdsLCoIndex_Object = MibTableColumn
htdsLCoIndex = _HtdsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 1, 1, 10),
    _HtdsLCoIndex_Type()
)
htdsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    htdsLCoIndex.setStatus("mandatory")
_HtdsLCoPathDataTable_Object = MibTable
htdsLCoPathDataTable = _HtdsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10)
)
if mibBuilder.loadTexts:
    htdsLCoPathDataTable.setStatus("mandatory")
_HtdsLCoPathDataEntry_Object = MibTableRow
htdsLCoPathDataEntry = _HtdsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1)
)
htdsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsLCoIndex"),
)
if mibBuilder.loadTexts:
    htdsLCoPathDataEntry.setStatus("mandatory")


class _HtdsLCoState_Type(Integer32):
    """Custom type htdsLCoState based on Integer32"""
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
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_HtdsLCoState_Type.__name__ = "Integer32"
_HtdsLCoState_Object = MibTableColumn
htdsLCoState = _HtdsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 1),
    _HtdsLCoState_Type()
)
htdsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoState.setStatus("mandatory")


class _HtdsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type htdsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HtdsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_HtdsLCoOverrideRemoteName_Object = MibTableColumn
htdsLCoOverrideRemoteName = _HtdsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 2),
    _HtdsLCoOverrideRemoteName_Type()
)
htdsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsLCoOverrideRemoteName.setStatus("mandatory")


class _HtdsLCoEnd_Type(Integer32):
    """Custom type htdsLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_HtdsLCoEnd_Type.__name__ = "Integer32"
_HtdsLCoEnd_Object = MibTableColumn
htdsLCoEnd = _HtdsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 3),
    _HtdsLCoEnd_Type()
)
htdsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoEnd.setStatus("mandatory")


class _HtdsLCoCostMetric_Type(Unsigned32):
    """Custom type htdsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HtdsLCoCostMetric_Type.__name__ = "Unsigned32"
_HtdsLCoCostMetric_Object = MibTableColumn
htdsLCoCostMetric = _HtdsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 4),
    _HtdsLCoCostMetric_Type()
)
htdsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoCostMetric.setStatus("mandatory")


class _HtdsLCoDelayMetric_Type(Unsigned32):
    """Custom type htdsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_HtdsLCoDelayMetric_Type.__name__ = "Unsigned32"
_HtdsLCoDelayMetric_Object = MibTableColumn
htdsLCoDelayMetric = _HtdsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 5),
    _HtdsLCoDelayMetric_Type()
)
htdsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoDelayMetric.setStatus("mandatory")


class _HtdsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type htdsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_HtdsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_HtdsLCoRoundTripDelay_Object = MibTableColumn
htdsLCoRoundTripDelay = _HtdsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 6),
    _HtdsLCoRoundTripDelay_Type()
)
htdsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRoundTripDelay.setStatus("mandatory")


class _HtdsLCoSetupPriority_Type(Unsigned32):
    """Custom type htdsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HtdsLCoSetupPriority_Type.__name__ = "Unsigned32"
_HtdsLCoSetupPriority_Object = MibTableColumn
htdsLCoSetupPriority = _HtdsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 7),
    _HtdsLCoSetupPriority_Type()
)
htdsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoSetupPriority.setStatus("mandatory")


class _HtdsLCoHoldingPriority_Type(Unsigned32):
    """Custom type htdsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HtdsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_HtdsLCoHoldingPriority_Object = MibTableColumn
htdsLCoHoldingPriority = _HtdsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 8),
    _HtdsLCoHoldingPriority_Type()
)
htdsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoHoldingPriority.setStatus("mandatory")


class _HtdsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type htdsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HtdsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_HtdsLCoRequiredTxBandwidth_Object = MibTableColumn
htdsLCoRequiredTxBandwidth = _HtdsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 9),
    _HtdsLCoRequiredTxBandwidth_Type()
)
htdsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRequiredTxBandwidth.setStatus("mandatory")


class _HtdsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type htdsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HtdsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_HtdsLCoRequiredRxBandwidth_Object = MibTableColumn
htdsLCoRequiredRxBandwidth = _HtdsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 10),
    _HtdsLCoRequiredRxBandwidth_Type()
)
htdsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRequiredRxBandwidth.setStatus("mandatory")


class _HtdsLCoRequiredTrafficType_Type(Integer32):
    """Custom type htdsLCoRequiredTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_HtdsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_HtdsLCoRequiredTrafficType_Object = MibTableColumn
htdsLCoRequiredTrafficType = _HtdsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 11),
    _HtdsLCoRequiredTrafficType_Type()
)
htdsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRequiredTrafficType.setStatus("mandatory")


class _HtdsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type htdsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HtdsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_HtdsLCoPermittedTrunkTypes_Object = MibTableColumn
htdsLCoPermittedTrunkTypes = _HtdsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 12),
    _HtdsLCoPermittedTrunkTypes_Type()
)
htdsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPermittedTrunkTypes.setStatus("mandatory")


class _HtdsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type htdsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HtdsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_HtdsLCoRequiredSecurity_Object = MibTableColumn
htdsLCoRequiredSecurity = _HtdsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 13),
    _HtdsLCoRequiredSecurity_Type()
)
htdsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRequiredSecurity.setStatus("mandatory")


class _HtdsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type htdsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HtdsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_HtdsLCoRequiredCustomerParameter_Object = MibTableColumn
htdsLCoRequiredCustomerParameter = _HtdsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 14),
    _HtdsLCoRequiredCustomerParameter_Type()
)
htdsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRequiredCustomerParameter.setStatus("mandatory")


class _HtdsLCoEmissionPriority_Type(Unsigned32):
    """Custom type htdsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HtdsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_HtdsLCoEmissionPriority_Object = MibTableColumn
htdsLCoEmissionPriority = _HtdsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 15),
    _HtdsLCoEmissionPriority_Type()
)
htdsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoEmissionPriority.setStatus("mandatory")


class _HtdsLCoDiscardPriority_Type(Unsigned32):
    """Custom type htdsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HtdsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_HtdsLCoDiscardPriority_Object = MibTableColumn
htdsLCoDiscardPriority = _HtdsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 16),
    _HtdsLCoDiscardPriority_Type()
)
htdsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoDiscardPriority.setStatus("mandatory")


class _HtdsLCoPathType_Type(Integer32):
    """Custom type htdsLCoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_HtdsLCoPathType_Type.__name__ = "Integer32"
_HtdsLCoPathType_Object = MibTableColumn
htdsLCoPathType = _HtdsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 17),
    _HtdsLCoPathType_Type()
)
htdsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPathType.setStatus("mandatory")


class _HtdsLCoRetryCount_Type(Unsigned32):
    """Custom type htdsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HtdsLCoRetryCount_Type.__name__ = "Unsigned32"
_HtdsLCoRetryCount_Object = MibTableColumn
htdsLCoRetryCount = _HtdsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 18),
    _HtdsLCoRetryCount_Type()
)
htdsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoRetryCount.setStatus("mandatory")


class _HtdsLCoPathFailureCount_Type(Unsigned32):
    """Custom type htdsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HtdsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_HtdsLCoPathFailureCount_Object = MibTableColumn
htdsLCoPathFailureCount = _HtdsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 19),
    _HtdsLCoPathFailureCount_Type()
)
htdsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPathFailureCount.setStatus("mandatory")


class _HtdsLCoReasonForNoRoute_Type(Integer32):
    """Custom type htdsLCoReasonForNoRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_HtdsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_HtdsLCoReasonForNoRoute_Object = MibTableColumn
htdsLCoReasonForNoRoute = _HtdsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 20),
    _HtdsLCoReasonForNoRoute_Type()
)
htdsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoReasonForNoRoute.setStatus("mandatory")


class _HtdsLCoLastTearDownReason_Type(Integer32):
    """Custom type htdsLCoLastTearDownReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_HtdsLCoLastTearDownReason_Type.__name__ = "Integer32"
_HtdsLCoLastTearDownReason_Object = MibTableColumn
htdsLCoLastTearDownReason = _HtdsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 21),
    _HtdsLCoLastTearDownReason_Type()
)
htdsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoLastTearDownReason.setStatus("mandatory")


class _HtdsLCoPathFailureAction_Type(Integer32):
    """Custom type htdsLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_HtdsLCoPathFailureAction_Type.__name__ = "Integer32"
_HtdsLCoPathFailureAction_Object = MibTableColumn
htdsLCoPathFailureAction = _HtdsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 22),
    _HtdsLCoPathFailureAction_Type()
)
htdsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPathFailureAction.setStatus("mandatory")


class _HtdsLCoBumpPreference_Type(Integer32):
    """Custom type htdsLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_HtdsLCoBumpPreference_Type.__name__ = "Integer32"
_HtdsLCoBumpPreference_Object = MibTableColumn
htdsLCoBumpPreference = _HtdsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 23),
    _HtdsLCoBumpPreference_Type()
)
htdsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoBumpPreference.setStatus("mandatory")


class _HtdsLCoOptimization_Type(Integer32):
    """Custom type htdsLCoOptimization based on Integer32"""
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


_HtdsLCoOptimization_Type.__name__ = "Integer32"
_HtdsLCoOptimization_Object = MibTableColumn
htdsLCoOptimization = _HtdsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 24),
    _HtdsLCoOptimization_Type()
)
htdsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoOptimization.setStatus("mandatory")


class _HtdsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type htdsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_HtdsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_HtdsLCoPathUpDateTime_Object = MibTableColumn
htdsLCoPathUpDateTime = _HtdsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 10, 1, 25),
    _HtdsLCoPathUpDateTime_Type()
)
htdsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPathUpDateTime.setStatus("mandatory")
_HtdsLCoStatsTable_Object = MibTable
htdsLCoStatsTable = _HtdsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11)
)
if mibBuilder.loadTexts:
    htdsLCoStatsTable.setStatus("mandatory")
_HtdsLCoStatsEntry_Object = MibTableRow
htdsLCoStatsEntry = _HtdsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11, 1)
)
htdsLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsLCoIndex"),
)
if mibBuilder.loadTexts:
    htdsLCoStatsEntry.setStatus("mandatory")
_HtdsLCoPktsToNetwork_Type = PassportCounter64
_HtdsLCoPktsToNetwork_Object = MibTableColumn
htdsLCoPktsToNetwork = _HtdsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11, 1, 1),
    _HtdsLCoPktsToNetwork_Type()
)
htdsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPktsToNetwork.setStatus("mandatory")
_HtdsLCoBytesToNetwork_Type = PassportCounter64
_HtdsLCoBytesToNetwork_Object = MibTableColumn
htdsLCoBytesToNetwork = _HtdsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11, 1, 2),
    _HtdsLCoBytesToNetwork_Type()
)
htdsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoBytesToNetwork.setStatus("mandatory")
_HtdsLCoPktsFromNetwork_Type = PassportCounter64
_HtdsLCoPktsFromNetwork_Object = MibTableColumn
htdsLCoPktsFromNetwork = _HtdsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11, 1, 3),
    _HtdsLCoPktsFromNetwork_Type()
)
htdsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPktsFromNetwork.setStatus("mandatory")
_HtdsLCoBytesFromNetwork_Type = PassportCounter64
_HtdsLCoBytesFromNetwork_Object = MibTableColumn
htdsLCoBytesFromNetwork = _HtdsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 11, 1, 4),
    _HtdsLCoBytesFromNetwork_Type()
)
htdsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoBytesFromNetwork.setStatus("mandatory")
_HtdsLCoPathTable_Object = MibTable
htdsLCoPathTable = _HtdsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 264)
)
if mibBuilder.loadTexts:
    htdsLCoPathTable.setStatus("mandatory")
_HtdsLCoPathEntry_Object = MibTableRow
htdsLCoPathEntry = _HtdsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 264, 1)
)
htdsLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsLCoIndex"),
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsLCoPathValue"),
)
if mibBuilder.loadTexts:
    htdsLCoPathEntry.setStatus("mandatory")


class _HtdsLCoPathValue_Type(AsciiString):
    """Custom type htdsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HtdsLCoPathValue_Type.__name__ = "AsciiString"
_HtdsLCoPathValue_Object = MibTableColumn
htdsLCoPathValue = _HtdsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 4, 264, 1, 1),
    _HtdsLCoPathValue_Type()
)
htdsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsLCoPathValue.setStatus("mandatory")
_HtdsCidDataTable_Object = MibTable
htdsCidDataTable = _HtdsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 10)
)
if mibBuilder.loadTexts:
    htdsCidDataTable.setStatus("mandatory")
_HtdsCidDataEntry_Object = MibTableRow
htdsCidDataEntry = _HtdsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 10, 1)
)
htdsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
)
if mibBuilder.loadTexts:
    htdsCidDataEntry.setStatus("mandatory")


class _HtdsCustomerIdentifier_Type(Unsigned32):
    """Custom type htdsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_HtdsCustomerIdentifier_Type.__name__ = "Unsigned32"
_HtdsCustomerIdentifier_Object = MibTableColumn
htdsCustomerIdentifier = _HtdsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 10, 1, 1),
    _HtdsCustomerIdentifier_Type()
)
htdsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsCustomerIdentifier.setStatus("mandatory")
_HtdsIfEntryTable_Object = MibTable
htdsIfEntryTable = _HtdsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 11)
)
if mibBuilder.loadTexts:
    htdsIfEntryTable.setStatus("mandatory")
_HtdsIfEntryEntry_Object = MibTableRow
htdsIfEntryEntry = _HtdsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 11, 1)
)
htdsIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
)
if mibBuilder.loadTexts:
    htdsIfEntryEntry.setStatus("mandatory")


class _HtdsIfAdminStatus_Type(Integer32):
    """Custom type htdsIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HtdsIfAdminStatus_Type.__name__ = "Integer32"
_HtdsIfAdminStatus_Object = MibTableColumn
htdsIfAdminStatus = _HtdsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 11, 1, 1),
    _HtdsIfAdminStatus_Type()
)
htdsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htdsIfAdminStatus.setStatus("mandatory")


class _HtdsIfIndex_Type(InterfaceIndex):
    """Custom type htdsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HtdsIfIndex_Type.__name__ = "InterfaceIndex"
_HtdsIfIndex_Object = MibTableColumn
htdsIfIndex = _HtdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 11, 1, 2),
    _HtdsIfIndex_Type()
)
htdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsIfIndex.setStatus("mandatory")
_HtdsOperStatusTable_Object = MibTable
htdsOperStatusTable = _HtdsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 12)
)
if mibBuilder.loadTexts:
    htdsOperStatusTable.setStatus("mandatory")
_HtdsOperStatusEntry_Object = MibTableRow
htdsOperStatusEntry = _HtdsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 12, 1)
)
htdsOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
)
if mibBuilder.loadTexts:
    htdsOperStatusEntry.setStatus("mandatory")


class _HtdsSnmpOperStatus_Type(Integer32):
    """Custom type htdsSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HtdsSnmpOperStatus_Type.__name__ = "Integer32"
_HtdsSnmpOperStatus_Object = MibTableColumn
htdsSnmpOperStatus = _HtdsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 12, 1, 1),
    _HtdsSnmpOperStatus_Type()
)
htdsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsSnmpOperStatus.setStatus("mandatory")
_HtdsStateTable_Object = MibTable
htdsStateTable = _HtdsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13)
)
if mibBuilder.loadTexts:
    htdsStateTable.setStatus("mandatory")
_HtdsStateEntry_Object = MibTableRow
htdsStateEntry = _HtdsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1)
)
htdsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-HdlcTransparentMIB", "htdsIndex"),
)
if mibBuilder.loadTexts:
    htdsStateEntry.setStatus("mandatory")


class _HtdsAdminState_Type(Integer32):
    """Custom type htdsAdminState based on Integer32"""
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


_HtdsAdminState_Type.__name__ = "Integer32"
_HtdsAdminState_Object = MibTableColumn
htdsAdminState = _HtdsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 1),
    _HtdsAdminState_Type()
)
htdsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsAdminState.setStatus("mandatory")


class _HtdsOperationalState_Type(Integer32):
    """Custom type htdsOperationalState based on Integer32"""
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


_HtdsOperationalState_Type.__name__ = "Integer32"
_HtdsOperationalState_Object = MibTableColumn
htdsOperationalState = _HtdsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 2),
    _HtdsOperationalState_Type()
)
htdsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsOperationalState.setStatus("mandatory")


class _HtdsUsageState_Type(Integer32):
    """Custom type htdsUsageState based on Integer32"""
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


_HtdsUsageState_Type.__name__ = "Integer32"
_HtdsUsageState_Object = MibTableColumn
htdsUsageState = _HtdsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 3),
    _HtdsUsageState_Type()
)
htdsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsUsageState.setStatus("mandatory")


class _HtdsAvailabilityStatus_Type(OctetString):
    """Custom type htdsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HtdsAvailabilityStatus_Type.__name__ = "OctetString"
_HtdsAvailabilityStatus_Object = MibTableColumn
htdsAvailabilityStatus = _HtdsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 4),
    _HtdsAvailabilityStatus_Type()
)
htdsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsAvailabilityStatus.setStatus("mandatory")


class _HtdsProceduralStatus_Type(OctetString):
    """Custom type htdsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HtdsProceduralStatus_Type.__name__ = "OctetString"
_HtdsProceduralStatus_Object = MibTableColumn
htdsProceduralStatus = _HtdsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 5),
    _HtdsProceduralStatus_Type()
)
htdsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsProceduralStatus.setStatus("mandatory")


class _HtdsControlStatus_Type(OctetString):
    """Custom type htdsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HtdsControlStatus_Type.__name__ = "OctetString"
_HtdsControlStatus_Object = MibTableColumn
htdsControlStatus = _HtdsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 6),
    _HtdsControlStatus_Type()
)
htdsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsControlStatus.setStatus("mandatory")


class _HtdsAlarmStatus_Type(OctetString):
    """Custom type htdsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HtdsAlarmStatus_Type.__name__ = "OctetString"
_HtdsAlarmStatus_Object = MibTableColumn
htdsAlarmStatus = _HtdsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 7),
    _HtdsAlarmStatus_Type()
)
htdsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsAlarmStatus.setStatus("mandatory")


class _HtdsStandbyStatus_Type(Integer32):
    """Custom type htdsStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_HtdsStandbyStatus_Type.__name__ = "Integer32"
_HtdsStandbyStatus_Object = MibTableColumn
htdsStandbyStatus = _HtdsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 8),
    _HtdsStandbyStatus_Type()
)
htdsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsStandbyStatus.setStatus("mandatory")


class _HtdsUnknownStatus_Type(Integer32):
    """Custom type htdsUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HtdsUnknownStatus_Type.__name__ = "Integer32"
_HtdsUnknownStatus_Object = MibTableColumn
htdsUnknownStatus = _HtdsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 82, 13, 1, 9),
    _HtdsUnknownStatus_Type()
)
htdsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htdsUnknownStatus.setStatus("mandatory")
_HdlcTransparentMIB_ObjectIdentity = ObjectIdentity
hdlcTransparentMIB = _HdlcTransparentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47)
)
_HdlcTransparentGroup_ObjectIdentity = ObjectIdentity
hdlcTransparentGroup = _HdlcTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 1)
)
_HdlcTransparentGroupBC_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupBC = _HdlcTransparentGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 1, 3)
)
_HdlcTransparentGroupBC03_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupBC03 = _HdlcTransparentGroupBC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 1, 3, 4)
)
_HdlcTransparentGroupBC03A_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupBC03A = _HdlcTransparentGroupBC03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 1, 3, 4, 2)
)
_HdlcTransparentCapabilities_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilities = _HdlcTransparentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 3)
)
_HdlcTransparentCapabilitiesBC_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesBC = _HdlcTransparentCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 3, 3)
)
_HdlcTransparentCapabilitiesBC03_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesBC03 = _HdlcTransparentCapabilitiesBC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 3, 3, 4)
)
_HdlcTransparentCapabilitiesBC03A_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesBC03A = _HdlcTransparentCapabilitiesBC03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 47, 3, 3, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-HdlcTransparentMIB",
    **{"htds": htds,
       "htdsRowStatusTable": htdsRowStatusTable,
       "htdsRowStatusEntry": htdsRowStatusEntry,
       "htdsRowStatus": htdsRowStatus,
       "htdsComponentName": htdsComponentName,
       "htdsStorageType": htdsStorageType,
       "htdsIndex": htdsIndex,
       "htdsFramer": htdsFramer,
       "htdsFramerRowStatusTable": htdsFramerRowStatusTable,
       "htdsFramerRowStatusEntry": htdsFramerRowStatusEntry,
       "htdsFramerRowStatus": htdsFramerRowStatus,
       "htdsFramerComponentName": htdsFramerComponentName,
       "htdsFramerStorageType": htdsFramerStorageType,
       "htdsFramerIndex": htdsFramerIndex,
       "htdsFramerProvTable": htdsFramerProvTable,
       "htdsFramerProvEntry": htdsFramerProvEntry,
       "htdsFramerInterfaceName": htdsFramerInterfaceName,
       "htdsFramerLinkTable": htdsFramerLinkTable,
       "htdsFramerLinkEntry": htdsFramerLinkEntry,
       "htdsFramerDataInversion": htdsFramerDataInversion,
       "htdsFramerNonOctetData": htdsFramerNonOctetData,
       "htdsFramerFrameCrcType": htdsFramerFrameCrcType,
       "htdsFramerFlagsBetweenFrames": htdsFramerFlagsBetweenFrames,
       "htdsFramerLineSignalTransport": htdsFramerLineSignalTransport,
       "htdsFramerStateTable": htdsFramerStateTable,
       "htdsFramerStateEntry": htdsFramerStateEntry,
       "htdsFramerAdminState": htdsFramerAdminState,
       "htdsFramerOperationalState": htdsFramerOperationalState,
       "htdsFramerUsageState": htdsFramerUsageState,
       "htdsFramerStatsTable": htdsFramerStatsTable,
       "htdsFramerStatsEntry": htdsFramerStatsEntry,
       "htdsFramerFrmToIf": htdsFramerFrmToIf,
       "htdsFramerFrmFromIf": htdsFramerFrmFromIf,
       "htdsFramerOctetFromIf": htdsFramerOctetFromIf,
       "htdsFramerAborts": htdsFramerAborts,
       "htdsFramerCrcErrors": htdsFramerCrcErrors,
       "htdsFramerLrcErrors": htdsFramerLrcErrors,
       "htdsFramerNonOctetErrors": htdsFramerNonOctetErrors,
       "htdsFramerOverruns": htdsFramerOverruns,
       "htdsFramerUnderruns": htdsFramerUnderruns,
       "htdsFramerLargeFrmErrors": htdsFramerLargeFrmErrors,
       "htdsFramerUtilTable": htdsFramerUtilTable,
       "htdsFramerUtilEntry": htdsFramerUtilEntry,
       "htdsFramerNormPrioLinkUtilToIf": htdsFramerNormPrioLinkUtilToIf,
       "htdsFramerNormPrioLinkUtilFromIf": htdsFramerNormPrioLinkUtilFromIf,
       "htdsPlc": htdsPlc,
       "htdsPlcRowStatusTable": htdsPlcRowStatusTable,
       "htdsPlcRowStatusEntry": htdsPlcRowStatusEntry,
       "htdsPlcRowStatus": htdsPlcRowStatus,
       "htdsPlcComponentName": htdsPlcComponentName,
       "htdsPlcStorageType": htdsPlcStorageType,
       "htdsPlcIndex": htdsPlcIndex,
       "htdsPlcProvTable": htdsPlcProvTable,
       "htdsPlcProvEntry": htdsPlcProvEntry,
       "htdsPlcRemoteName": htdsPlcRemoteName,
       "htdsPlcSetupPriority": htdsPlcSetupPriority,
       "htdsPlcHoldingPriority": htdsPlcHoldingPriority,
       "htdsPlcRequiredTxBandwidth": htdsPlcRequiredTxBandwidth,
       "htdsPlcRequiredRxBandwidth": htdsPlcRequiredRxBandwidth,
       "htdsPlcRequiredTrafficType": htdsPlcRequiredTrafficType,
       "htdsPlcPermittedTrunkTypes": htdsPlcPermittedTrunkTypes,
       "htdsPlcRequiredSecurity": htdsPlcRequiredSecurity,
       "htdsPlcRequiredCustomerParm": htdsPlcRequiredCustomerParm,
       "htdsPlcPathAttributeToMinimize": htdsPlcPathAttributeToMinimize,
       "htdsPlcMaximumAcceptableCost": htdsPlcMaximumAcceptableCost,
       "htdsPlcMaximumAcceptableDelay": htdsPlcMaximumAcceptableDelay,
       "htdsPlcEmissionPriority": htdsPlcEmissionPriority,
       "htdsPlcDiscardPriority": htdsPlcDiscardPriority,
       "htdsPlcPathType": htdsPlcPathType,
       "htdsPlcPathFailureAction": htdsPlcPathFailureAction,
       "htdsPlcBumpPreference": htdsPlcBumpPreference,
       "htdsPlcOptimization": htdsPlcOptimization,
       "htdsPlcMpathTable": htdsPlcMpathTable,
       "htdsPlcMpathEntry": htdsPlcMpathEntry,
       "htdsPlcMpathIndex": htdsPlcMpathIndex,
       "htdsPlcMpathValue": htdsPlcMpathValue,
       "htdsLCo": htdsLCo,
       "htdsLCoRowStatusTable": htdsLCoRowStatusTable,
       "htdsLCoRowStatusEntry": htdsLCoRowStatusEntry,
       "htdsLCoRowStatus": htdsLCoRowStatus,
       "htdsLCoComponentName": htdsLCoComponentName,
       "htdsLCoStorageType": htdsLCoStorageType,
       "htdsLCoIndex": htdsLCoIndex,
       "htdsLCoPathDataTable": htdsLCoPathDataTable,
       "htdsLCoPathDataEntry": htdsLCoPathDataEntry,
       "htdsLCoState": htdsLCoState,
       "htdsLCoOverrideRemoteName": htdsLCoOverrideRemoteName,
       "htdsLCoEnd": htdsLCoEnd,
       "htdsLCoCostMetric": htdsLCoCostMetric,
       "htdsLCoDelayMetric": htdsLCoDelayMetric,
       "htdsLCoRoundTripDelay": htdsLCoRoundTripDelay,
       "htdsLCoSetupPriority": htdsLCoSetupPriority,
       "htdsLCoHoldingPriority": htdsLCoHoldingPriority,
       "htdsLCoRequiredTxBandwidth": htdsLCoRequiredTxBandwidth,
       "htdsLCoRequiredRxBandwidth": htdsLCoRequiredRxBandwidth,
       "htdsLCoRequiredTrafficType": htdsLCoRequiredTrafficType,
       "htdsLCoPermittedTrunkTypes": htdsLCoPermittedTrunkTypes,
       "htdsLCoRequiredSecurity": htdsLCoRequiredSecurity,
       "htdsLCoRequiredCustomerParameter": htdsLCoRequiredCustomerParameter,
       "htdsLCoEmissionPriority": htdsLCoEmissionPriority,
       "htdsLCoDiscardPriority": htdsLCoDiscardPriority,
       "htdsLCoPathType": htdsLCoPathType,
       "htdsLCoRetryCount": htdsLCoRetryCount,
       "htdsLCoPathFailureCount": htdsLCoPathFailureCount,
       "htdsLCoReasonForNoRoute": htdsLCoReasonForNoRoute,
       "htdsLCoLastTearDownReason": htdsLCoLastTearDownReason,
       "htdsLCoPathFailureAction": htdsLCoPathFailureAction,
       "htdsLCoBumpPreference": htdsLCoBumpPreference,
       "htdsLCoOptimization": htdsLCoOptimization,
       "htdsLCoPathUpDateTime": htdsLCoPathUpDateTime,
       "htdsLCoStatsTable": htdsLCoStatsTable,
       "htdsLCoStatsEntry": htdsLCoStatsEntry,
       "htdsLCoPktsToNetwork": htdsLCoPktsToNetwork,
       "htdsLCoBytesToNetwork": htdsLCoBytesToNetwork,
       "htdsLCoPktsFromNetwork": htdsLCoPktsFromNetwork,
       "htdsLCoBytesFromNetwork": htdsLCoBytesFromNetwork,
       "htdsLCoPathTable": htdsLCoPathTable,
       "htdsLCoPathEntry": htdsLCoPathEntry,
       "htdsLCoPathValue": htdsLCoPathValue,
       "htdsCidDataTable": htdsCidDataTable,
       "htdsCidDataEntry": htdsCidDataEntry,
       "htdsCustomerIdentifier": htdsCustomerIdentifier,
       "htdsIfEntryTable": htdsIfEntryTable,
       "htdsIfEntryEntry": htdsIfEntryEntry,
       "htdsIfAdminStatus": htdsIfAdminStatus,
       "htdsIfIndex": htdsIfIndex,
       "htdsOperStatusTable": htdsOperStatusTable,
       "htdsOperStatusEntry": htdsOperStatusEntry,
       "htdsSnmpOperStatus": htdsSnmpOperStatus,
       "htdsStateTable": htdsStateTable,
       "htdsStateEntry": htdsStateEntry,
       "htdsAdminState": htdsAdminState,
       "htdsOperationalState": htdsOperationalState,
       "htdsUsageState": htdsUsageState,
       "htdsAvailabilityStatus": htdsAvailabilityStatus,
       "htdsProceduralStatus": htdsProceduralStatus,
       "htdsControlStatus": htdsControlStatus,
       "htdsAlarmStatus": htdsAlarmStatus,
       "htdsStandbyStatus": htdsStandbyStatus,
       "htdsUnknownStatus": htdsUnknownStatus,
       "hdlcTransparentMIB": hdlcTransparentMIB,
       "hdlcTransparentGroup": hdlcTransparentGroup,
       "hdlcTransparentGroupBC": hdlcTransparentGroupBC,
       "hdlcTransparentGroupBC03": hdlcTransparentGroupBC03,
       "hdlcTransparentGroupBC03A": hdlcTransparentGroupBC03A,
       "hdlcTransparentCapabilities": hdlcTransparentCapabilities,
       "hdlcTransparentCapabilitiesBC": hdlcTransparentCapabilitiesBC,
       "hdlcTransparentCapabilitiesBC03": hdlcTransparentCapabilitiesBC03,
       "hdlcTransparentCapabilitiesBC03A": hdlcTransparentCapabilitiesBC03A}
)
