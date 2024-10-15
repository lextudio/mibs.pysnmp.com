# SNMP MIB module (Nortel-Magellan-Passport-UnackTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-UnackTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:30 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(trk,
 trkIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TrunksMIB",
    "trk",
    "trkIndex")

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

_TrkUnAcked_ObjectIdentity = ObjectIdentity
trkUnAcked = _TrkUnAcked_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2)
)
_TrkUnAckedRowStatusTable_Object = MibTable
trkUnAckedRowStatusTable = _TrkUnAckedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1)
)
if mibBuilder.loadTexts:
    trkUnAckedRowStatusTable.setStatus("mandatory")
_TrkUnAckedRowStatusEntry_Object = MibTableRow
trkUnAckedRowStatusEntry = _TrkUnAckedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1, 1)
)
trkUnAckedRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedRowStatusEntry.setStatus("mandatory")
_TrkUnAckedRowStatus_Type = RowStatus
_TrkUnAckedRowStatus_Object = MibTableColumn
trkUnAckedRowStatus = _TrkUnAckedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1, 1, 1),
    _TrkUnAckedRowStatus_Type()
)
trkUnAckedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedRowStatus.setStatus("mandatory")
_TrkUnAckedComponentName_Type = DisplayString
_TrkUnAckedComponentName_Object = MibTableColumn
trkUnAckedComponentName = _TrkUnAckedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1, 1, 2),
    _TrkUnAckedComponentName_Type()
)
trkUnAckedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedComponentName.setStatus("mandatory")
_TrkUnAckedStorageType_Type = StorageType
_TrkUnAckedStorageType_Object = MibTableColumn
trkUnAckedStorageType = _TrkUnAckedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1, 1, 4),
    _TrkUnAckedStorageType_Type()
)
trkUnAckedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedStorageType.setStatus("mandatory")
_TrkUnAckedIndex_Type = NonReplicated
_TrkUnAckedIndex_Object = MibTableColumn
trkUnAckedIndex = _TrkUnAckedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 1, 1, 10),
    _TrkUnAckedIndex_Type()
)
trkUnAckedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkUnAckedIndex.setStatus("mandatory")
_TrkUnAckedFramer_ObjectIdentity = ObjectIdentity
trkUnAckedFramer = _TrkUnAckedFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2)
)
_TrkUnAckedFramerRowStatusTable_Object = MibTable
trkUnAckedFramerRowStatusTable = _TrkUnAckedFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerRowStatusTable.setStatus("mandatory")
_TrkUnAckedFramerRowStatusEntry_Object = MibTableRow
trkUnAckedFramerRowStatusEntry = _TrkUnAckedFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1, 1)
)
trkUnAckedFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerRowStatusEntry.setStatus("mandatory")
_TrkUnAckedFramerRowStatus_Type = RowStatus
_TrkUnAckedFramerRowStatus_Object = MibTableColumn
trkUnAckedFramerRowStatus = _TrkUnAckedFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1, 1, 1),
    _TrkUnAckedFramerRowStatus_Type()
)
trkUnAckedFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerRowStatus.setStatus("mandatory")
_TrkUnAckedFramerComponentName_Type = DisplayString
_TrkUnAckedFramerComponentName_Object = MibTableColumn
trkUnAckedFramerComponentName = _TrkUnAckedFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1, 1, 2),
    _TrkUnAckedFramerComponentName_Type()
)
trkUnAckedFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerComponentName.setStatus("mandatory")
_TrkUnAckedFramerStorageType_Type = StorageType
_TrkUnAckedFramerStorageType_Object = MibTableColumn
trkUnAckedFramerStorageType = _TrkUnAckedFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1, 1, 4),
    _TrkUnAckedFramerStorageType_Type()
)
trkUnAckedFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerStorageType.setStatus("mandatory")
_TrkUnAckedFramerIndex_Type = NonReplicated
_TrkUnAckedFramerIndex_Object = MibTableColumn
trkUnAckedFramerIndex = _TrkUnAckedFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 1, 1, 10),
    _TrkUnAckedFramerIndex_Type()
)
trkUnAckedFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trkUnAckedFramerIndex.setStatus("mandatory")
_TrkUnAckedFramerProvTable_Object = MibTable
trkUnAckedFramerProvTable = _TrkUnAckedFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 10)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerProvTable.setStatus("mandatory")
_TrkUnAckedFramerProvEntry_Object = MibTableRow
trkUnAckedFramerProvEntry = _TrkUnAckedFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 10, 1)
)
trkUnAckedFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerProvEntry.setStatus("mandatory")
_TrkUnAckedFramerInterfaceName_Type = Link
_TrkUnAckedFramerInterfaceName_Object = MibTableColumn
trkUnAckedFramerInterfaceName = _TrkUnAckedFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 10, 1, 1),
    _TrkUnAckedFramerInterfaceName_Type()
)
trkUnAckedFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerInterfaceName.setStatus("mandatory")
_TrkUnAckedFramerLinkTable_Object = MibTable
trkUnAckedFramerLinkTable = _TrkUnAckedFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerLinkTable.setStatus("mandatory")
_TrkUnAckedFramerLinkEntry_Object = MibTableRow
trkUnAckedFramerLinkEntry = _TrkUnAckedFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11, 1)
)
trkUnAckedFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerLinkEntry.setStatus("mandatory")


class _TrkUnAckedFramerFramingType_Type(Integer32):
    """Custom type trkUnAckedFramerFramingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 0),
          ("interrupting", 1))
    )


_TrkUnAckedFramerFramingType_Type.__name__ = "Integer32"
_TrkUnAckedFramerFramingType_Object = MibTableColumn
trkUnAckedFramerFramingType = _TrkUnAckedFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11, 1, 1),
    _TrkUnAckedFramerFramingType_Type()
)
trkUnAckedFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerFramingType.setStatus("mandatory")


class _TrkUnAckedFramerDataInversion_Type(Integer32):
    """Custom type trkUnAckedFramerDataInversion based on Integer32"""
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


_TrkUnAckedFramerDataInversion_Type.__name__ = "Integer32"
_TrkUnAckedFramerDataInversion_Object = MibTableColumn
trkUnAckedFramerDataInversion = _TrkUnAckedFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11, 1, 2),
    _TrkUnAckedFramerDataInversion_Type()
)
trkUnAckedFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerDataInversion.setStatus("mandatory")


class _TrkUnAckedFramerFrameCrcType_Type(Integer32):
    """Custom type trkUnAckedFramerFrameCrcType based on Integer32"""
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


_TrkUnAckedFramerFrameCrcType_Type.__name__ = "Integer32"
_TrkUnAckedFramerFrameCrcType_Object = MibTableColumn
trkUnAckedFramerFrameCrcType = _TrkUnAckedFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11, 1, 3),
    _TrkUnAckedFramerFrameCrcType_Type()
)
trkUnAckedFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerFrameCrcType.setStatus("mandatory")


class _TrkUnAckedFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type trkUnAckedFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TrkUnAckedFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_TrkUnAckedFramerFlagsBetweenFrames_Object = MibTableColumn
trkUnAckedFramerFlagsBetweenFrames = _TrkUnAckedFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 11, 1, 4),
    _TrkUnAckedFramerFlagsBetweenFrames_Type()
)
trkUnAckedFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerFlagsBetweenFrames.setStatus("mandatory")
_TrkUnAckedFramerStateTable_Object = MibTable
trkUnAckedFramerStateTable = _TrkUnAckedFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 12)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerStateTable.setStatus("mandatory")
_TrkUnAckedFramerStateEntry_Object = MibTableRow
trkUnAckedFramerStateEntry = _TrkUnAckedFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 12, 1)
)
trkUnAckedFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerStateEntry.setStatus("mandatory")


class _TrkUnAckedFramerAdminState_Type(Integer32):
    """Custom type trkUnAckedFramerAdminState based on Integer32"""
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


_TrkUnAckedFramerAdminState_Type.__name__ = "Integer32"
_TrkUnAckedFramerAdminState_Object = MibTableColumn
trkUnAckedFramerAdminState = _TrkUnAckedFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 12, 1, 1),
    _TrkUnAckedFramerAdminState_Type()
)
trkUnAckedFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerAdminState.setStatus("mandatory")


class _TrkUnAckedFramerOperationalState_Type(Integer32):
    """Custom type trkUnAckedFramerOperationalState based on Integer32"""
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


_TrkUnAckedFramerOperationalState_Type.__name__ = "Integer32"
_TrkUnAckedFramerOperationalState_Object = MibTableColumn
trkUnAckedFramerOperationalState = _TrkUnAckedFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 12, 1, 2),
    _TrkUnAckedFramerOperationalState_Type()
)
trkUnAckedFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerOperationalState.setStatus("mandatory")


class _TrkUnAckedFramerUsageState_Type(Integer32):
    """Custom type trkUnAckedFramerUsageState based on Integer32"""
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


_TrkUnAckedFramerUsageState_Type.__name__ = "Integer32"
_TrkUnAckedFramerUsageState_Object = MibTableColumn
trkUnAckedFramerUsageState = _TrkUnAckedFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 12, 1, 3),
    _TrkUnAckedFramerUsageState_Type()
)
trkUnAckedFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerUsageState.setStatus("mandatory")
_TrkUnAckedFramerStatsTable_Object = MibTable
trkUnAckedFramerStatsTable = _TrkUnAckedFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerStatsTable.setStatus("mandatory")
_TrkUnAckedFramerStatsEntry_Object = MibTableRow
trkUnAckedFramerStatsEntry = _TrkUnAckedFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1)
)
trkUnAckedFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerStatsEntry.setStatus("mandatory")
_TrkUnAckedFramerFrmFromIf_Type = Counter32
_TrkUnAckedFramerFrmFromIf_Object = MibTableColumn
trkUnAckedFramerFrmFromIf = _TrkUnAckedFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 2),
    _TrkUnAckedFramerFrmFromIf_Type()
)
trkUnAckedFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerFrmFromIf.setStatus("mandatory")
_TrkUnAckedFramerOctetFromIf_Type = Counter32
_TrkUnAckedFramerOctetFromIf_Object = MibTableColumn
trkUnAckedFramerOctetFromIf = _TrkUnAckedFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 3),
    _TrkUnAckedFramerOctetFromIf_Type()
)
trkUnAckedFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerOctetFromIf.setStatus("mandatory")
_TrkUnAckedFramerAborts_Type = Counter32
_TrkUnAckedFramerAborts_Object = MibTableColumn
trkUnAckedFramerAborts = _TrkUnAckedFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 4),
    _TrkUnAckedFramerAborts_Type()
)
trkUnAckedFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerAborts.setStatus("mandatory")
_TrkUnAckedFramerCrcErrors_Type = Counter32
_TrkUnAckedFramerCrcErrors_Object = MibTableColumn
trkUnAckedFramerCrcErrors = _TrkUnAckedFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 5),
    _TrkUnAckedFramerCrcErrors_Type()
)
trkUnAckedFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerCrcErrors.setStatus("mandatory")
_TrkUnAckedFramerLrcErrors_Type = Counter32
_TrkUnAckedFramerLrcErrors_Object = MibTableColumn
trkUnAckedFramerLrcErrors = _TrkUnAckedFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 6),
    _TrkUnAckedFramerLrcErrors_Type()
)
trkUnAckedFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerLrcErrors.setStatus("mandatory")
_TrkUnAckedFramerNonOctetErrors_Type = Counter32
_TrkUnAckedFramerNonOctetErrors_Object = MibTableColumn
trkUnAckedFramerNonOctetErrors = _TrkUnAckedFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 7),
    _TrkUnAckedFramerNonOctetErrors_Type()
)
trkUnAckedFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerNonOctetErrors.setStatus("mandatory")
_TrkUnAckedFramerOverruns_Type = Counter32
_TrkUnAckedFramerOverruns_Object = MibTableColumn
trkUnAckedFramerOverruns = _TrkUnAckedFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 8),
    _TrkUnAckedFramerOverruns_Type()
)
trkUnAckedFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerOverruns.setStatus("mandatory")
_TrkUnAckedFramerUnderruns_Type = Counter32
_TrkUnAckedFramerUnderruns_Object = MibTableColumn
trkUnAckedFramerUnderruns = _TrkUnAckedFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 9),
    _TrkUnAckedFramerUnderruns_Type()
)
trkUnAckedFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerUnderruns.setStatus("mandatory")
_TrkUnAckedFramerLargeFrmErrors_Type = Counter32
_TrkUnAckedFramerLargeFrmErrors_Object = MibTableColumn
trkUnAckedFramerLargeFrmErrors = _TrkUnAckedFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 10),
    _TrkUnAckedFramerLargeFrmErrors_Type()
)
trkUnAckedFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerLargeFrmErrors.setStatus("mandatory")
_TrkUnAckedFramerFrmModeErrors_Type = Counter32
_TrkUnAckedFramerFrmModeErrors_Object = MibTableColumn
trkUnAckedFramerFrmModeErrors = _TrkUnAckedFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 11),
    _TrkUnAckedFramerFrmModeErrors_Type()
)
trkUnAckedFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerFrmModeErrors.setStatus("mandatory")
_TrkUnAckedFramerOutOfSequenceFrm_Type = Counter32
_TrkUnAckedFramerOutOfSequenceFrm_Object = MibTableColumn
trkUnAckedFramerOutOfSequenceFrm = _TrkUnAckedFramerOutOfSequenceFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 12),
    _TrkUnAckedFramerOutOfSequenceFrm_Type()
)
trkUnAckedFramerOutOfSequenceFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerOutOfSequenceFrm.setStatus("mandatory")
_TrkUnAckedFramerRepeatedFrm_Type = Counter32
_TrkUnAckedFramerRepeatedFrm_Object = MibTableColumn
trkUnAckedFramerRepeatedFrm = _TrkUnAckedFramerRepeatedFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 13, 1, 13),
    _TrkUnAckedFramerRepeatedFrm_Type()
)
trkUnAckedFramerRepeatedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerRepeatedFrm.setStatus("mandatory")
_TrkUnAckedFramerUtilTable_Object = MibTable
trkUnAckedFramerUtilTable = _TrkUnAckedFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerUtilTable.setStatus("mandatory")
_TrkUnAckedFramerUtilEntry_Object = MibTableRow
trkUnAckedFramerUtilEntry = _TrkUnAckedFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14, 1)
)
trkUnAckedFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerUtilEntry.setStatus("mandatory")


class _TrkUnAckedFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type trkUnAckedFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_TrkUnAckedFramerNormPrioLinkUtilToIf_Object = MibTableColumn
trkUnAckedFramerNormPrioLinkUtilToIf = _TrkUnAckedFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14, 1, 1),
    _TrkUnAckedFramerNormPrioLinkUtilToIf_Type()
)
trkUnAckedFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _TrkUnAckedFramerHighPrioLinkUtilToIf_Type(Gauge32):
    """Custom type trkUnAckedFramerHighPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerHighPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_TrkUnAckedFramerHighPrioLinkUtilToIf_Object = MibTableColumn
trkUnAckedFramerHighPrioLinkUtilToIf = _TrkUnAckedFramerHighPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14, 1, 2),
    _TrkUnAckedFramerHighPrioLinkUtilToIf_Type()
)
trkUnAckedFramerHighPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerHighPrioLinkUtilToIf.setStatus("mandatory")


class _TrkUnAckedFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type trkUnAckedFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_TrkUnAckedFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
trkUnAckedFramerNormPrioLinkUtilFromIf = _TrkUnAckedFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14, 1, 3),
    _TrkUnAckedFramerNormPrioLinkUtilFromIf_Type()
)
trkUnAckedFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerNormPrioLinkUtilFromIf.setStatus("mandatory")


class _TrkUnAckedFramerHighPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type trkUnAckedFramerHighPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerHighPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_TrkUnAckedFramerHighPrioLinkUtilFromIf_Object = MibTableColumn
trkUnAckedFramerHighPrioLinkUtilFromIf = _TrkUnAckedFramerHighPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 14, 1, 4),
    _TrkUnAckedFramerHighPrioLinkUtilFromIf_Type()
)
trkUnAckedFramerHighPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedFramerHighPrioLinkUtilFromIf.setStatus("mandatory")
_TrkUnAckedFramerUtilThresholdTable_Object = MibTable
trkUnAckedFramerUtilThresholdTable = _TrkUnAckedFramerUtilThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15)
)
if mibBuilder.loadTexts:
    trkUnAckedFramerUtilThresholdTable.setStatus("mandatory")
_TrkUnAckedFramerUtilThresholdEntry_Object = MibTableRow
trkUnAckedFramerUtilThresholdEntry = _TrkUnAckedFramerUtilThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15, 1)
)
trkUnAckedFramerUtilThresholdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedFramerUtilThresholdEntry.setStatus("mandatory")


class _TrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkUnAckedFramerMinorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkUnAckedFramerMinorLinkUtilAlarmThreshold_Object = MibTableColumn
trkUnAckedFramerMinorLinkUtilAlarmThreshold = _TrkUnAckedFramerMinorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15, 1, 1),
    _TrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type()
)
trkUnAckedFramerMinorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerMinorLinkUtilAlarmThreshold.setStatus("mandatory")


class _TrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkUnAckedFramerMajorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkUnAckedFramerMajorLinkUtilAlarmThreshold_Object = MibTableColumn
trkUnAckedFramerMajorLinkUtilAlarmThreshold = _TrkUnAckedFramerMajorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15, 1, 2),
    _TrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type()
)
trkUnAckedFramerMajorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerMajorLinkUtilAlarmThreshold.setStatus("mandatory")


class _TrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type trkUnAckedFramerCriticalLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_TrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Object = MibTableColumn
trkUnAckedFramerCriticalLinkUtilAlarmThreshold = _TrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15, 1, 3),
    _TrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type()
)
trkUnAckedFramerCriticalLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerCriticalLinkUtilAlarmThreshold.setStatus("mandatory")


class _TrkUnAckedFramerLinkUtilAlarmStatus_Type(Integer32):
    """Custom type trkUnAckedFramerLinkUtilAlarmStatus based on Integer32"""
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


_TrkUnAckedFramerLinkUtilAlarmStatus_Type.__name__ = "Integer32"
_TrkUnAckedFramerLinkUtilAlarmStatus_Object = MibTableColumn
trkUnAckedFramerLinkUtilAlarmStatus = _TrkUnAckedFramerLinkUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 2, 15, 1, 4),
    _TrkUnAckedFramerLinkUtilAlarmStatus_Type()
)
trkUnAckedFramerLinkUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedFramerLinkUtilAlarmStatus.setStatus("mandatory")
_TrkUnAckedProvTable_Object = MibTable
trkUnAckedProvTable = _TrkUnAckedProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 10)
)
if mibBuilder.loadTexts:
    trkUnAckedProvTable.setStatus("mandatory")
_TrkUnAckedProvEntry_Object = MibTableRow
trkUnAckedProvEntry = _TrkUnAckedProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 10, 1)
)
trkUnAckedProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedProvEntry.setStatus("mandatory")


class _TrkUnAckedMaximumErroredInterval_Type(Unsigned32):
    """Custom type trkUnAckedMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_TrkUnAckedMaximumErroredInterval_Type.__name__ = "Unsigned32"
_TrkUnAckedMaximumErroredInterval_Object = MibTableColumn
trkUnAckedMaximumErroredInterval = _TrkUnAckedMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 10, 1, 1),
    _TrkUnAckedMaximumErroredInterval_Type()
)
trkUnAckedMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedMaximumErroredInterval.setStatus("mandatory")


class _TrkUnAckedReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type trkUnAckedReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_TrkUnAckedReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_TrkUnAckedReceiveErrorSensitivity_Object = MibTableColumn
trkUnAckedReceiveErrorSensitivity = _TrkUnAckedReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 10, 1, 2),
    _TrkUnAckedReceiveErrorSensitivity_Type()
)
trkUnAckedReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trkUnAckedReceiveErrorSensitivity.setStatus("mandatory")
_TrkUnAckedStateTable_Object = MibTable
trkUnAckedStateTable = _TrkUnAckedStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11)
)
if mibBuilder.loadTexts:
    trkUnAckedStateTable.setStatus("mandatory")
_TrkUnAckedStateEntry_Object = MibTableRow
trkUnAckedStateEntry = _TrkUnAckedStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1)
)
trkUnAckedStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"),
    (0, "Nortel-Magellan-Passport-UnackTrunksMIB", "trkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    trkUnAckedStateEntry.setStatus("mandatory")


class _TrkUnAckedAdminState_Type(Integer32):
    """Custom type trkUnAckedAdminState based on Integer32"""
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


_TrkUnAckedAdminState_Type.__name__ = "Integer32"
_TrkUnAckedAdminState_Object = MibTableColumn
trkUnAckedAdminState = _TrkUnAckedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 1),
    _TrkUnAckedAdminState_Type()
)
trkUnAckedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedAdminState.setStatus("mandatory")


class _TrkUnAckedOperationalState_Type(Integer32):
    """Custom type trkUnAckedOperationalState based on Integer32"""
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


_TrkUnAckedOperationalState_Type.__name__ = "Integer32"
_TrkUnAckedOperationalState_Object = MibTableColumn
trkUnAckedOperationalState = _TrkUnAckedOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 2),
    _TrkUnAckedOperationalState_Type()
)
trkUnAckedOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedOperationalState.setStatus("mandatory")


class _TrkUnAckedUsageState_Type(Integer32):
    """Custom type trkUnAckedUsageState based on Integer32"""
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


_TrkUnAckedUsageState_Type.__name__ = "Integer32"
_TrkUnAckedUsageState_Object = MibTableColumn
trkUnAckedUsageState = _TrkUnAckedUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 3),
    _TrkUnAckedUsageState_Type()
)
trkUnAckedUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedUsageState.setStatus("mandatory")


class _TrkUnAckedAvailabilityStatus_Type(OctetString):
    """Custom type trkUnAckedAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TrkUnAckedAvailabilityStatus_Type.__name__ = "OctetString"
_TrkUnAckedAvailabilityStatus_Object = MibTableColumn
trkUnAckedAvailabilityStatus = _TrkUnAckedAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 4),
    _TrkUnAckedAvailabilityStatus_Type()
)
trkUnAckedAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedAvailabilityStatus.setStatus("mandatory")


class _TrkUnAckedProceduralStatus_Type(OctetString):
    """Custom type trkUnAckedProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkUnAckedProceduralStatus_Type.__name__ = "OctetString"
_TrkUnAckedProceduralStatus_Object = MibTableColumn
trkUnAckedProceduralStatus = _TrkUnAckedProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 5),
    _TrkUnAckedProceduralStatus_Type()
)
trkUnAckedProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedProceduralStatus.setStatus("mandatory")


class _TrkUnAckedControlStatus_Type(OctetString):
    """Custom type trkUnAckedControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkUnAckedControlStatus_Type.__name__ = "OctetString"
_TrkUnAckedControlStatus_Object = MibTableColumn
trkUnAckedControlStatus = _TrkUnAckedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 6),
    _TrkUnAckedControlStatus_Type()
)
trkUnAckedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedControlStatus.setStatus("mandatory")


class _TrkUnAckedAlarmStatus_Type(OctetString):
    """Custom type trkUnAckedAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrkUnAckedAlarmStatus_Type.__name__ = "OctetString"
_TrkUnAckedAlarmStatus_Object = MibTableColumn
trkUnAckedAlarmStatus = _TrkUnAckedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 7),
    _TrkUnAckedAlarmStatus_Type()
)
trkUnAckedAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedAlarmStatus.setStatus("mandatory")


class _TrkUnAckedStandbyStatus_Type(Integer32):
    """Custom type trkUnAckedStandbyStatus based on Integer32"""
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


_TrkUnAckedStandbyStatus_Type.__name__ = "Integer32"
_TrkUnAckedStandbyStatus_Object = MibTableColumn
trkUnAckedStandbyStatus = _TrkUnAckedStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 8),
    _TrkUnAckedStandbyStatus_Type()
)
trkUnAckedStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedStandbyStatus.setStatus("mandatory")


class _TrkUnAckedUnknownStatus_Type(Integer32):
    """Custom type trkUnAckedUnknownStatus based on Integer32"""
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


_TrkUnAckedUnknownStatus_Type.__name__ = "Integer32"
_TrkUnAckedUnknownStatus_Object = MibTableColumn
trkUnAckedUnknownStatus = _TrkUnAckedUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 2, 11, 1, 9),
    _TrkUnAckedUnknownStatus_Type()
)
trkUnAckedUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trkUnAckedUnknownStatus.setStatus("mandatory")
_UnackTrunksMIB_ObjectIdentity = ObjectIdentity
unackTrunksMIB = _UnackTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22)
)
_UnackTrunksGroup_ObjectIdentity = ObjectIdentity
unackTrunksGroup = _UnackTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 1)
)
_UnackTrunksGroupBE_ObjectIdentity = ObjectIdentity
unackTrunksGroupBE = _UnackTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 1, 5)
)
_UnackTrunksGroupBE00_ObjectIdentity = ObjectIdentity
unackTrunksGroupBE00 = _UnackTrunksGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 1, 5, 1)
)
_UnackTrunksGroupBE00A_ObjectIdentity = ObjectIdentity
unackTrunksGroupBE00A = _UnackTrunksGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 1, 5, 1, 2)
)
_UnackTrunksCapabilities_ObjectIdentity = ObjectIdentity
unackTrunksCapabilities = _UnackTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 3)
)
_UnackTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesBE = _UnackTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 3, 5)
)
_UnackTrunksCapabilitiesBE00_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesBE00 = _UnackTrunksCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 3, 5, 1)
)
_UnackTrunksCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesBE00A = _UnackTrunksCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 22, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-UnackTrunksMIB",
    **{"trkUnAcked": trkUnAcked,
       "trkUnAckedRowStatusTable": trkUnAckedRowStatusTable,
       "trkUnAckedRowStatusEntry": trkUnAckedRowStatusEntry,
       "trkUnAckedRowStatus": trkUnAckedRowStatus,
       "trkUnAckedComponentName": trkUnAckedComponentName,
       "trkUnAckedStorageType": trkUnAckedStorageType,
       "trkUnAckedIndex": trkUnAckedIndex,
       "trkUnAckedFramer": trkUnAckedFramer,
       "trkUnAckedFramerRowStatusTable": trkUnAckedFramerRowStatusTable,
       "trkUnAckedFramerRowStatusEntry": trkUnAckedFramerRowStatusEntry,
       "trkUnAckedFramerRowStatus": trkUnAckedFramerRowStatus,
       "trkUnAckedFramerComponentName": trkUnAckedFramerComponentName,
       "trkUnAckedFramerStorageType": trkUnAckedFramerStorageType,
       "trkUnAckedFramerIndex": trkUnAckedFramerIndex,
       "trkUnAckedFramerProvTable": trkUnAckedFramerProvTable,
       "trkUnAckedFramerProvEntry": trkUnAckedFramerProvEntry,
       "trkUnAckedFramerInterfaceName": trkUnAckedFramerInterfaceName,
       "trkUnAckedFramerLinkTable": trkUnAckedFramerLinkTable,
       "trkUnAckedFramerLinkEntry": trkUnAckedFramerLinkEntry,
       "trkUnAckedFramerFramingType": trkUnAckedFramerFramingType,
       "trkUnAckedFramerDataInversion": trkUnAckedFramerDataInversion,
       "trkUnAckedFramerFrameCrcType": trkUnAckedFramerFrameCrcType,
       "trkUnAckedFramerFlagsBetweenFrames": trkUnAckedFramerFlagsBetweenFrames,
       "trkUnAckedFramerStateTable": trkUnAckedFramerStateTable,
       "trkUnAckedFramerStateEntry": trkUnAckedFramerStateEntry,
       "trkUnAckedFramerAdminState": trkUnAckedFramerAdminState,
       "trkUnAckedFramerOperationalState": trkUnAckedFramerOperationalState,
       "trkUnAckedFramerUsageState": trkUnAckedFramerUsageState,
       "trkUnAckedFramerStatsTable": trkUnAckedFramerStatsTable,
       "trkUnAckedFramerStatsEntry": trkUnAckedFramerStatsEntry,
       "trkUnAckedFramerFrmFromIf": trkUnAckedFramerFrmFromIf,
       "trkUnAckedFramerOctetFromIf": trkUnAckedFramerOctetFromIf,
       "trkUnAckedFramerAborts": trkUnAckedFramerAborts,
       "trkUnAckedFramerCrcErrors": trkUnAckedFramerCrcErrors,
       "trkUnAckedFramerLrcErrors": trkUnAckedFramerLrcErrors,
       "trkUnAckedFramerNonOctetErrors": trkUnAckedFramerNonOctetErrors,
       "trkUnAckedFramerOverruns": trkUnAckedFramerOverruns,
       "trkUnAckedFramerUnderruns": trkUnAckedFramerUnderruns,
       "trkUnAckedFramerLargeFrmErrors": trkUnAckedFramerLargeFrmErrors,
       "trkUnAckedFramerFrmModeErrors": trkUnAckedFramerFrmModeErrors,
       "trkUnAckedFramerOutOfSequenceFrm": trkUnAckedFramerOutOfSequenceFrm,
       "trkUnAckedFramerRepeatedFrm": trkUnAckedFramerRepeatedFrm,
       "trkUnAckedFramerUtilTable": trkUnAckedFramerUtilTable,
       "trkUnAckedFramerUtilEntry": trkUnAckedFramerUtilEntry,
       "trkUnAckedFramerNormPrioLinkUtilToIf": trkUnAckedFramerNormPrioLinkUtilToIf,
       "trkUnAckedFramerHighPrioLinkUtilToIf": trkUnAckedFramerHighPrioLinkUtilToIf,
       "trkUnAckedFramerNormPrioLinkUtilFromIf": trkUnAckedFramerNormPrioLinkUtilFromIf,
       "trkUnAckedFramerHighPrioLinkUtilFromIf": trkUnAckedFramerHighPrioLinkUtilFromIf,
       "trkUnAckedFramerUtilThresholdTable": trkUnAckedFramerUtilThresholdTable,
       "trkUnAckedFramerUtilThresholdEntry": trkUnAckedFramerUtilThresholdEntry,
       "trkUnAckedFramerMinorLinkUtilAlarmThreshold": trkUnAckedFramerMinorLinkUtilAlarmThreshold,
       "trkUnAckedFramerMajorLinkUtilAlarmThreshold": trkUnAckedFramerMajorLinkUtilAlarmThreshold,
       "trkUnAckedFramerCriticalLinkUtilAlarmThreshold": trkUnAckedFramerCriticalLinkUtilAlarmThreshold,
       "trkUnAckedFramerLinkUtilAlarmStatus": trkUnAckedFramerLinkUtilAlarmStatus,
       "trkUnAckedProvTable": trkUnAckedProvTable,
       "trkUnAckedProvEntry": trkUnAckedProvEntry,
       "trkUnAckedMaximumErroredInterval": trkUnAckedMaximumErroredInterval,
       "trkUnAckedReceiveErrorSensitivity": trkUnAckedReceiveErrorSensitivity,
       "trkUnAckedStateTable": trkUnAckedStateTable,
       "trkUnAckedStateEntry": trkUnAckedStateEntry,
       "trkUnAckedAdminState": trkUnAckedAdminState,
       "trkUnAckedOperationalState": trkUnAckedOperationalState,
       "trkUnAckedUsageState": trkUnAckedUsageState,
       "trkUnAckedAvailabilityStatus": trkUnAckedAvailabilityStatus,
       "trkUnAckedProceduralStatus": trkUnAckedProceduralStatus,
       "trkUnAckedControlStatus": trkUnAckedControlStatus,
       "trkUnAckedAlarmStatus": trkUnAckedAlarmStatus,
       "trkUnAckedStandbyStatus": trkUnAckedStandbyStatus,
       "trkUnAckedUnknownStatus": trkUnAckedUnknownStatus,
       "unackTrunksMIB": unackTrunksMIB,
       "unackTrunksGroup": unackTrunksGroup,
       "unackTrunksGroupBE": unackTrunksGroupBE,
       "unackTrunksGroupBE00": unackTrunksGroupBE00,
       "unackTrunksGroupBE00A": unackTrunksGroupBE00A,
       "unackTrunksCapabilities": unackTrunksCapabilities,
       "unackTrunksCapabilitiesBE": unackTrunksCapabilitiesBE,
       "unackTrunksCapabilitiesBE00": unackTrunksCapabilitiesBE00,
       "unackTrunksCapabilitiesBE00A": unackTrunksCapabilitiesBE00A}
)
