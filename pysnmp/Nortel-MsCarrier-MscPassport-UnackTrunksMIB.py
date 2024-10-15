# SNMP MIB module (Nortel-MsCarrier-MscPassport-UnackTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-UnackTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:11 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
    "NonReplicated",
    "PassportCounter64")

(mscTrk,
 mscTrkIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TrunksMIB",
    "mscTrk",
    "mscTrkIndex")

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

_MscTrkUnAcked_ObjectIdentity = ObjectIdentity
mscTrkUnAcked = _MscTrkUnAcked_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2)
)
_MscTrkUnAckedRowStatusTable_Object = MibTable
mscTrkUnAckedRowStatusTable = _MscTrkUnAckedRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedRowStatusTable.setStatus("mandatory")
_MscTrkUnAckedRowStatusEntry_Object = MibTableRow
mscTrkUnAckedRowStatusEntry = _MscTrkUnAckedRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1, 1)
)
mscTrkUnAckedRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedRowStatusEntry.setStatus("mandatory")
_MscTrkUnAckedRowStatus_Type = RowStatus
_MscTrkUnAckedRowStatus_Object = MibTableColumn
mscTrkUnAckedRowStatus = _MscTrkUnAckedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1, 1, 1),
    _MscTrkUnAckedRowStatus_Type()
)
mscTrkUnAckedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedRowStatus.setStatus("mandatory")
_MscTrkUnAckedComponentName_Type = DisplayString
_MscTrkUnAckedComponentName_Object = MibTableColumn
mscTrkUnAckedComponentName = _MscTrkUnAckedComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1, 1, 2),
    _MscTrkUnAckedComponentName_Type()
)
mscTrkUnAckedComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedComponentName.setStatus("mandatory")
_MscTrkUnAckedStorageType_Type = StorageType
_MscTrkUnAckedStorageType_Object = MibTableColumn
mscTrkUnAckedStorageType = _MscTrkUnAckedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1, 1, 4),
    _MscTrkUnAckedStorageType_Type()
)
mscTrkUnAckedStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedStorageType.setStatus("mandatory")
_MscTrkUnAckedIndex_Type = NonReplicated
_MscTrkUnAckedIndex_Object = MibTableColumn
mscTrkUnAckedIndex = _MscTrkUnAckedIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 1, 1, 10),
    _MscTrkUnAckedIndex_Type()
)
mscTrkUnAckedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkUnAckedIndex.setStatus("mandatory")
_MscTrkUnAckedFramer_ObjectIdentity = ObjectIdentity
mscTrkUnAckedFramer = _MscTrkUnAckedFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2)
)
_MscTrkUnAckedFramerRowStatusTable_Object = MibTable
mscTrkUnAckedFramerRowStatusTable = _MscTrkUnAckedFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerRowStatusTable.setStatus("mandatory")
_MscTrkUnAckedFramerRowStatusEntry_Object = MibTableRow
mscTrkUnAckedFramerRowStatusEntry = _MscTrkUnAckedFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1, 1)
)
mscTrkUnAckedFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerRowStatusEntry.setStatus("mandatory")
_MscTrkUnAckedFramerRowStatus_Type = RowStatus
_MscTrkUnAckedFramerRowStatus_Object = MibTableColumn
mscTrkUnAckedFramerRowStatus = _MscTrkUnAckedFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1, 1, 1),
    _MscTrkUnAckedFramerRowStatus_Type()
)
mscTrkUnAckedFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerRowStatus.setStatus("mandatory")
_MscTrkUnAckedFramerComponentName_Type = DisplayString
_MscTrkUnAckedFramerComponentName_Object = MibTableColumn
mscTrkUnAckedFramerComponentName = _MscTrkUnAckedFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1, 1, 2),
    _MscTrkUnAckedFramerComponentName_Type()
)
mscTrkUnAckedFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerComponentName.setStatus("mandatory")
_MscTrkUnAckedFramerStorageType_Type = StorageType
_MscTrkUnAckedFramerStorageType_Object = MibTableColumn
mscTrkUnAckedFramerStorageType = _MscTrkUnAckedFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1, 1, 4),
    _MscTrkUnAckedFramerStorageType_Type()
)
mscTrkUnAckedFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerStorageType.setStatus("mandatory")
_MscTrkUnAckedFramerIndex_Type = NonReplicated
_MscTrkUnAckedFramerIndex_Object = MibTableColumn
mscTrkUnAckedFramerIndex = _MscTrkUnAckedFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 1, 1, 10),
    _MscTrkUnAckedFramerIndex_Type()
)
mscTrkUnAckedFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerIndex.setStatus("mandatory")
_MscTrkUnAckedFramerProvTable_Object = MibTable
mscTrkUnAckedFramerProvTable = _MscTrkUnAckedFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerProvTable.setStatus("mandatory")
_MscTrkUnAckedFramerProvEntry_Object = MibTableRow
mscTrkUnAckedFramerProvEntry = _MscTrkUnAckedFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 10, 1)
)
mscTrkUnAckedFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerProvEntry.setStatus("mandatory")
_MscTrkUnAckedFramerInterfaceName_Type = Link
_MscTrkUnAckedFramerInterfaceName_Object = MibTableColumn
mscTrkUnAckedFramerInterfaceName = _MscTrkUnAckedFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 10, 1, 1),
    _MscTrkUnAckedFramerInterfaceName_Type()
)
mscTrkUnAckedFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerInterfaceName.setStatus("mandatory")
_MscTrkUnAckedFramerLinkTable_Object = MibTable
mscTrkUnAckedFramerLinkTable = _MscTrkUnAckedFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerLinkTable.setStatus("mandatory")
_MscTrkUnAckedFramerLinkEntry_Object = MibTableRow
mscTrkUnAckedFramerLinkEntry = _MscTrkUnAckedFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11, 1)
)
mscTrkUnAckedFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerLinkEntry.setStatus("mandatory")


class _MscTrkUnAckedFramerFramingType_Type(Integer32):
    """Custom type mscTrkUnAckedFramerFramingType based on Integer32"""
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


_MscTrkUnAckedFramerFramingType_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerFramingType_Object = MibTableColumn
mscTrkUnAckedFramerFramingType = _MscTrkUnAckedFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11, 1, 1),
    _MscTrkUnAckedFramerFramingType_Type()
)
mscTrkUnAckedFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFramingType.setStatus("mandatory")


class _MscTrkUnAckedFramerDataInversion_Type(Integer32):
    """Custom type mscTrkUnAckedFramerDataInversion based on Integer32"""
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


_MscTrkUnAckedFramerDataInversion_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerDataInversion_Object = MibTableColumn
mscTrkUnAckedFramerDataInversion = _MscTrkUnAckedFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11, 1, 2),
    _MscTrkUnAckedFramerDataInversion_Type()
)
mscTrkUnAckedFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerDataInversion.setStatus("mandatory")


class _MscTrkUnAckedFramerFrameCrcType_Type(Integer32):
    """Custom type mscTrkUnAckedFramerFrameCrcType based on Integer32"""
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


_MscTrkUnAckedFramerFrameCrcType_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerFrameCrcType_Object = MibTableColumn
mscTrkUnAckedFramerFrameCrcType = _MscTrkUnAckedFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11, 1, 3),
    _MscTrkUnAckedFramerFrameCrcType_Type()
)
mscTrkUnAckedFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFrameCrcType.setStatus("mandatory")


class _MscTrkUnAckedFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscTrkUnAckedFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscTrkUnAckedFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscTrkUnAckedFramerFlagsBetweenFrames_Object = MibTableColumn
mscTrkUnAckedFramerFlagsBetweenFrames = _MscTrkUnAckedFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 11, 1, 4),
    _MscTrkUnAckedFramerFlagsBetweenFrames_Type()
)
mscTrkUnAckedFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFlagsBetweenFrames.setStatus("mandatory")
_MscTrkUnAckedFramerStateTable_Object = MibTable
mscTrkUnAckedFramerStateTable = _MscTrkUnAckedFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerStateTable.setStatus("mandatory")
_MscTrkUnAckedFramerStateEntry_Object = MibTableRow
mscTrkUnAckedFramerStateEntry = _MscTrkUnAckedFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 12, 1)
)
mscTrkUnAckedFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerStateEntry.setStatus("mandatory")


class _MscTrkUnAckedFramerAdminState_Type(Integer32):
    """Custom type mscTrkUnAckedFramerAdminState based on Integer32"""
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


_MscTrkUnAckedFramerAdminState_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerAdminState_Object = MibTableColumn
mscTrkUnAckedFramerAdminState = _MscTrkUnAckedFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 12, 1, 1),
    _MscTrkUnAckedFramerAdminState_Type()
)
mscTrkUnAckedFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerAdminState.setStatus("mandatory")


class _MscTrkUnAckedFramerOperationalState_Type(Integer32):
    """Custom type mscTrkUnAckedFramerOperationalState based on Integer32"""
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


_MscTrkUnAckedFramerOperationalState_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerOperationalState_Object = MibTableColumn
mscTrkUnAckedFramerOperationalState = _MscTrkUnAckedFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 12, 1, 2),
    _MscTrkUnAckedFramerOperationalState_Type()
)
mscTrkUnAckedFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerOperationalState.setStatus("mandatory")


class _MscTrkUnAckedFramerUsageState_Type(Integer32):
    """Custom type mscTrkUnAckedFramerUsageState based on Integer32"""
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


_MscTrkUnAckedFramerUsageState_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerUsageState_Object = MibTableColumn
mscTrkUnAckedFramerUsageState = _MscTrkUnAckedFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 12, 1, 3),
    _MscTrkUnAckedFramerUsageState_Type()
)
mscTrkUnAckedFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUsageState.setStatus("mandatory")
_MscTrkUnAckedFramerStatsTable_Object = MibTable
mscTrkUnAckedFramerStatsTable = _MscTrkUnAckedFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerStatsTable.setStatus("mandatory")
_MscTrkUnAckedFramerStatsEntry_Object = MibTableRow
mscTrkUnAckedFramerStatsEntry = _MscTrkUnAckedFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1)
)
mscTrkUnAckedFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerStatsEntry.setStatus("mandatory")
_MscTrkUnAckedFramerFrmToIf_Type = Counter32
_MscTrkUnAckedFramerFrmToIf_Object = MibTableColumn
mscTrkUnAckedFramerFrmToIf = _MscTrkUnAckedFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 1),
    _MscTrkUnAckedFramerFrmToIf_Type()
)
mscTrkUnAckedFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFrmToIf.setStatus("obsolete")
_MscTrkUnAckedFramerFrmFromIf_Type = Counter32
_MscTrkUnAckedFramerFrmFromIf_Object = MibTableColumn
mscTrkUnAckedFramerFrmFromIf = _MscTrkUnAckedFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 2),
    _MscTrkUnAckedFramerFrmFromIf_Type()
)
mscTrkUnAckedFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFrmFromIf.setStatus("obsolete")
_MscTrkUnAckedFramerOctetFromIf_Type = Counter32
_MscTrkUnAckedFramerOctetFromIf_Object = MibTableColumn
mscTrkUnAckedFramerOctetFromIf = _MscTrkUnAckedFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 3),
    _MscTrkUnAckedFramerOctetFromIf_Type()
)
mscTrkUnAckedFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerOctetFromIf.setStatus("obsolete")
_MscTrkUnAckedFramerAborts_Type = Counter32
_MscTrkUnAckedFramerAborts_Object = MibTableColumn
mscTrkUnAckedFramerAborts = _MscTrkUnAckedFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 4),
    _MscTrkUnAckedFramerAborts_Type()
)
mscTrkUnAckedFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerAborts.setStatus("mandatory")
_MscTrkUnAckedFramerCrcErrors_Type = Counter32
_MscTrkUnAckedFramerCrcErrors_Object = MibTableColumn
mscTrkUnAckedFramerCrcErrors = _MscTrkUnAckedFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 5),
    _MscTrkUnAckedFramerCrcErrors_Type()
)
mscTrkUnAckedFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerCrcErrors.setStatus("mandatory")
_MscTrkUnAckedFramerLrcErrors_Type = Counter32
_MscTrkUnAckedFramerLrcErrors_Object = MibTableColumn
mscTrkUnAckedFramerLrcErrors = _MscTrkUnAckedFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 6),
    _MscTrkUnAckedFramerLrcErrors_Type()
)
mscTrkUnAckedFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerLrcErrors.setStatus("mandatory")
_MscTrkUnAckedFramerNonOctetErrors_Type = Counter32
_MscTrkUnAckedFramerNonOctetErrors_Object = MibTableColumn
mscTrkUnAckedFramerNonOctetErrors = _MscTrkUnAckedFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 7),
    _MscTrkUnAckedFramerNonOctetErrors_Type()
)
mscTrkUnAckedFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerNonOctetErrors.setStatus("mandatory")
_MscTrkUnAckedFramerOverruns_Type = Counter32
_MscTrkUnAckedFramerOverruns_Object = MibTableColumn
mscTrkUnAckedFramerOverruns = _MscTrkUnAckedFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 8),
    _MscTrkUnAckedFramerOverruns_Type()
)
mscTrkUnAckedFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerOverruns.setStatus("mandatory")
_MscTrkUnAckedFramerUnderruns_Type = Counter32
_MscTrkUnAckedFramerUnderruns_Object = MibTableColumn
mscTrkUnAckedFramerUnderruns = _MscTrkUnAckedFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 9),
    _MscTrkUnAckedFramerUnderruns_Type()
)
mscTrkUnAckedFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUnderruns.setStatus("mandatory")
_MscTrkUnAckedFramerLargeFrmErrors_Type = Counter32
_MscTrkUnAckedFramerLargeFrmErrors_Object = MibTableColumn
mscTrkUnAckedFramerLargeFrmErrors = _MscTrkUnAckedFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 10),
    _MscTrkUnAckedFramerLargeFrmErrors_Type()
)
mscTrkUnAckedFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerLargeFrmErrors.setStatus("mandatory")
_MscTrkUnAckedFramerFrmModeErrors_Type = Counter32
_MscTrkUnAckedFramerFrmModeErrors_Object = MibTableColumn
mscTrkUnAckedFramerFrmModeErrors = _MscTrkUnAckedFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 11),
    _MscTrkUnAckedFramerFrmModeErrors_Type()
)
mscTrkUnAckedFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFrmModeErrors.setStatus("mandatory")
_MscTrkUnAckedFramerOutOfSequenceFrm_Type = Counter32
_MscTrkUnAckedFramerOutOfSequenceFrm_Object = MibTableColumn
mscTrkUnAckedFramerOutOfSequenceFrm = _MscTrkUnAckedFramerOutOfSequenceFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 12),
    _MscTrkUnAckedFramerOutOfSequenceFrm_Type()
)
mscTrkUnAckedFramerOutOfSequenceFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerOutOfSequenceFrm.setStatus("mandatory")
_MscTrkUnAckedFramerRepeatedFrm_Type = Counter32
_MscTrkUnAckedFramerRepeatedFrm_Object = MibTableColumn
mscTrkUnAckedFramerRepeatedFrm = _MscTrkUnAckedFramerRepeatedFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 13),
    _MscTrkUnAckedFramerRepeatedFrm_Type()
)
mscTrkUnAckedFramerRepeatedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerRepeatedFrm.setStatus("mandatory")
_MscTrkUnAckedFramerFrmFromIf64_Type = PassportCounter64
_MscTrkUnAckedFramerFrmFromIf64_Object = MibTableColumn
mscTrkUnAckedFramerFrmFromIf64 = _MscTrkUnAckedFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 15),
    _MscTrkUnAckedFramerFrmFromIf64_Type()
)
mscTrkUnAckedFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerFrmFromIf64.setStatus("mandatory")
_MscTrkUnAckedFramerOctetFromIf64_Type = PassportCounter64
_MscTrkUnAckedFramerOctetFromIf64_Object = MibTableColumn
mscTrkUnAckedFramerOctetFromIf64 = _MscTrkUnAckedFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 13, 1, 16),
    _MscTrkUnAckedFramerOctetFromIf64_Type()
)
mscTrkUnAckedFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerOctetFromIf64.setStatus("mandatory")
_MscTrkUnAckedFramerUtilTable_Object = MibTable
mscTrkUnAckedFramerUtilTable = _MscTrkUnAckedFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUtilTable.setStatus("mandatory")
_MscTrkUnAckedFramerUtilEntry_Object = MibTableRow
mscTrkUnAckedFramerUtilEntry = _MscTrkUnAckedFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14, 1)
)
mscTrkUnAckedFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUtilEntry.setStatus("mandatory")


class _MscTrkUnAckedFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscTrkUnAckedFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscTrkUnAckedFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscTrkUnAckedFramerNormPrioLinkUtilToIf = _MscTrkUnAckedFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14, 1, 1),
    _MscTrkUnAckedFramerNormPrioLinkUtilToIf_Type()
)
mscTrkUnAckedFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscTrkUnAckedFramerHighPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscTrkUnAckedFramerHighPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerHighPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscTrkUnAckedFramerHighPrioLinkUtilToIf_Object = MibTableColumn
mscTrkUnAckedFramerHighPrioLinkUtilToIf = _MscTrkUnAckedFramerHighPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14, 1, 2),
    _MscTrkUnAckedFramerHighPrioLinkUtilToIf_Type()
)
mscTrkUnAckedFramerHighPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerHighPrioLinkUtilToIf.setStatus("mandatory")


class _MscTrkUnAckedFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscTrkUnAckedFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscTrkUnAckedFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscTrkUnAckedFramerNormPrioLinkUtilFromIf = _MscTrkUnAckedFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14, 1, 3),
    _MscTrkUnAckedFramerNormPrioLinkUtilFromIf_Type()
)
mscTrkUnAckedFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerNormPrioLinkUtilFromIf.setStatus("mandatory")


class _MscTrkUnAckedFramerHighPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscTrkUnAckedFramerHighPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerHighPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscTrkUnAckedFramerHighPrioLinkUtilFromIf_Object = MibTableColumn
mscTrkUnAckedFramerHighPrioLinkUtilFromIf = _MscTrkUnAckedFramerHighPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 14, 1, 4),
    _MscTrkUnAckedFramerHighPrioLinkUtilFromIf_Type()
)
mscTrkUnAckedFramerHighPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerHighPrioLinkUtilFromIf.setStatus("mandatory")
_MscTrkUnAckedFramerUtilThresholdTable_Object = MibTable
mscTrkUnAckedFramerUtilThresholdTable = _MscTrkUnAckedFramerUtilThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUtilThresholdTable.setStatus("mandatory")
_MscTrkUnAckedFramerUtilThresholdEntry_Object = MibTableRow
mscTrkUnAckedFramerUtilThresholdEntry = _MscTrkUnAckedFramerUtilThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15, 1)
)
mscTrkUnAckedFramerUtilThresholdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedFramerIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerUtilThresholdEntry.setStatus("mandatory")


class _MscTrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkUnAckedFramerMinorLinkUtilAlarmThreshold_Object = MibTableColumn
mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold = _MscTrkUnAckedFramerMinorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15, 1, 1),
    _MscTrkUnAckedFramerMinorLinkUtilAlarmThreshold_Type()
)
mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkUnAckedFramerMajorLinkUtilAlarmThreshold_Object = MibTableColumn
mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold = _MscTrkUnAckedFramerMajorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15, 1, 2),
    _MscTrkUnAckedFramerMajorLinkUtilAlarmThreshold_Type()
)
mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Object = MibTableColumn
mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold = _MscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15, 1, 3),
    _MscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold_Type()
)
mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscTrkUnAckedFramerLinkUtilAlarmStatus_Type(Integer32):
    """Custom type mscTrkUnAckedFramerLinkUtilAlarmStatus based on Integer32"""
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


_MscTrkUnAckedFramerLinkUtilAlarmStatus_Type.__name__ = "Integer32"
_MscTrkUnAckedFramerLinkUtilAlarmStatus_Object = MibTableColumn
mscTrkUnAckedFramerLinkUtilAlarmStatus = _MscTrkUnAckedFramerLinkUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 2, 15, 1, 4),
    _MscTrkUnAckedFramerLinkUtilAlarmStatus_Type()
)
mscTrkUnAckedFramerLinkUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedFramerLinkUtilAlarmStatus.setStatus("mandatory")
_MscTrkUnAckedProvTable_Object = MibTable
mscTrkUnAckedProvTable = _MscTrkUnAckedProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 10)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedProvTable.setStatus("mandatory")
_MscTrkUnAckedProvEntry_Object = MibTableRow
mscTrkUnAckedProvEntry = _MscTrkUnAckedProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 10, 1)
)
mscTrkUnAckedProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedProvEntry.setStatus("mandatory")


class _MscTrkUnAckedMaximumErroredInterval_Type(Unsigned32):
    """Custom type mscTrkUnAckedMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_MscTrkUnAckedMaximumErroredInterval_Type.__name__ = "Unsigned32"
_MscTrkUnAckedMaximumErroredInterval_Object = MibTableColumn
mscTrkUnAckedMaximumErroredInterval = _MscTrkUnAckedMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 10, 1, 1),
    _MscTrkUnAckedMaximumErroredInterval_Type()
)
mscTrkUnAckedMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedMaximumErroredInterval.setStatus("mandatory")


class _MscTrkUnAckedReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type mscTrkUnAckedReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_MscTrkUnAckedReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_MscTrkUnAckedReceiveErrorSensitivity_Object = MibTableColumn
mscTrkUnAckedReceiveErrorSensitivity = _MscTrkUnAckedReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 10, 1, 2),
    _MscTrkUnAckedReceiveErrorSensitivity_Type()
)
mscTrkUnAckedReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscTrkUnAckedReceiveErrorSensitivity.setStatus("mandatory")
_MscTrkUnAckedStateTable_Object = MibTable
mscTrkUnAckedStateTable = _MscTrkUnAckedStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11)
)
if mibBuilder.loadTexts:
    mscTrkUnAckedStateTable.setStatus("mandatory")
_MscTrkUnAckedStateEntry_Object = MibTableRow
mscTrkUnAckedStateEntry = _MscTrkUnAckedStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1)
)
mscTrkUnAckedStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-TrunksMIB", "mscTrkIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UnackTrunksMIB", "mscTrkUnAckedIndex"),
)
if mibBuilder.loadTexts:
    mscTrkUnAckedStateEntry.setStatus("mandatory")


class _MscTrkUnAckedAdminState_Type(Integer32):
    """Custom type mscTrkUnAckedAdminState based on Integer32"""
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


_MscTrkUnAckedAdminState_Type.__name__ = "Integer32"
_MscTrkUnAckedAdminState_Object = MibTableColumn
mscTrkUnAckedAdminState = _MscTrkUnAckedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 1),
    _MscTrkUnAckedAdminState_Type()
)
mscTrkUnAckedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedAdminState.setStatus("mandatory")


class _MscTrkUnAckedOperationalState_Type(Integer32):
    """Custom type mscTrkUnAckedOperationalState based on Integer32"""
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


_MscTrkUnAckedOperationalState_Type.__name__ = "Integer32"
_MscTrkUnAckedOperationalState_Object = MibTableColumn
mscTrkUnAckedOperationalState = _MscTrkUnAckedOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 2),
    _MscTrkUnAckedOperationalState_Type()
)
mscTrkUnAckedOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedOperationalState.setStatus("mandatory")


class _MscTrkUnAckedUsageState_Type(Integer32):
    """Custom type mscTrkUnAckedUsageState based on Integer32"""
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


_MscTrkUnAckedUsageState_Type.__name__ = "Integer32"
_MscTrkUnAckedUsageState_Object = MibTableColumn
mscTrkUnAckedUsageState = _MscTrkUnAckedUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 3),
    _MscTrkUnAckedUsageState_Type()
)
mscTrkUnAckedUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedUsageState.setStatus("mandatory")


class _MscTrkUnAckedAvailabilityStatus_Type(OctetString):
    """Custom type mscTrkUnAckedAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscTrkUnAckedAvailabilityStatus_Type.__name__ = "OctetString"
_MscTrkUnAckedAvailabilityStatus_Object = MibTableColumn
mscTrkUnAckedAvailabilityStatus = _MscTrkUnAckedAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 4),
    _MscTrkUnAckedAvailabilityStatus_Type()
)
mscTrkUnAckedAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedAvailabilityStatus.setStatus("mandatory")


class _MscTrkUnAckedProceduralStatus_Type(OctetString):
    """Custom type mscTrkUnAckedProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkUnAckedProceduralStatus_Type.__name__ = "OctetString"
_MscTrkUnAckedProceduralStatus_Object = MibTableColumn
mscTrkUnAckedProceduralStatus = _MscTrkUnAckedProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 5),
    _MscTrkUnAckedProceduralStatus_Type()
)
mscTrkUnAckedProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedProceduralStatus.setStatus("mandatory")


class _MscTrkUnAckedControlStatus_Type(OctetString):
    """Custom type mscTrkUnAckedControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkUnAckedControlStatus_Type.__name__ = "OctetString"
_MscTrkUnAckedControlStatus_Object = MibTableColumn
mscTrkUnAckedControlStatus = _MscTrkUnAckedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 6),
    _MscTrkUnAckedControlStatus_Type()
)
mscTrkUnAckedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedControlStatus.setStatus("mandatory")


class _MscTrkUnAckedAlarmStatus_Type(OctetString):
    """Custom type mscTrkUnAckedAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscTrkUnAckedAlarmStatus_Type.__name__ = "OctetString"
_MscTrkUnAckedAlarmStatus_Object = MibTableColumn
mscTrkUnAckedAlarmStatus = _MscTrkUnAckedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 7),
    _MscTrkUnAckedAlarmStatus_Type()
)
mscTrkUnAckedAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedAlarmStatus.setStatus("mandatory")


class _MscTrkUnAckedStandbyStatus_Type(Integer32):
    """Custom type mscTrkUnAckedStandbyStatus based on Integer32"""
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


_MscTrkUnAckedStandbyStatus_Type.__name__ = "Integer32"
_MscTrkUnAckedStandbyStatus_Object = MibTableColumn
mscTrkUnAckedStandbyStatus = _MscTrkUnAckedStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 8),
    _MscTrkUnAckedStandbyStatus_Type()
)
mscTrkUnAckedStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedStandbyStatus.setStatus("mandatory")


class _MscTrkUnAckedUnknownStatus_Type(Integer32):
    """Custom type mscTrkUnAckedUnknownStatus based on Integer32"""
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


_MscTrkUnAckedUnknownStatus_Type.__name__ = "Integer32"
_MscTrkUnAckedUnknownStatus_Object = MibTableColumn
mscTrkUnAckedUnknownStatus = _MscTrkUnAckedUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 60, 2, 11, 1, 9),
    _MscTrkUnAckedUnknownStatus_Type()
)
mscTrkUnAckedUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscTrkUnAckedUnknownStatus.setStatus("mandatory")
_UnackTrunksMIB_ObjectIdentity = ObjectIdentity
unackTrunksMIB = _UnackTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22)
)
_UnackTrunksGroup_ObjectIdentity = ObjectIdentity
unackTrunksGroup = _UnackTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 1)
)
_UnackTrunksGroupCB_ObjectIdentity = ObjectIdentity
unackTrunksGroupCB = _UnackTrunksGroupCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 1, 2)
)
_UnackTrunksGroupCB01_ObjectIdentity = ObjectIdentity
unackTrunksGroupCB01 = _UnackTrunksGroupCB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 1, 2, 2)
)
_UnackTrunksGroupCB01A_ObjectIdentity = ObjectIdentity
unackTrunksGroupCB01A = _UnackTrunksGroupCB01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 1, 2, 2, 2)
)
_UnackTrunksCapabilities_ObjectIdentity = ObjectIdentity
unackTrunksCapabilities = _UnackTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 3)
)
_UnackTrunksCapabilitiesCB_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesCB = _UnackTrunksCapabilitiesCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 3, 2)
)
_UnackTrunksCapabilitiesCB01_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesCB01 = _UnackTrunksCapabilitiesCB01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 3, 2, 2)
)
_UnackTrunksCapabilitiesCB01A_ObjectIdentity = ObjectIdentity
unackTrunksCapabilitiesCB01A = _UnackTrunksCapabilitiesCB01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 22, 3, 2, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-UnackTrunksMIB",
    **{"mscTrkUnAcked": mscTrkUnAcked,
       "mscTrkUnAckedRowStatusTable": mscTrkUnAckedRowStatusTable,
       "mscTrkUnAckedRowStatusEntry": mscTrkUnAckedRowStatusEntry,
       "mscTrkUnAckedRowStatus": mscTrkUnAckedRowStatus,
       "mscTrkUnAckedComponentName": mscTrkUnAckedComponentName,
       "mscTrkUnAckedStorageType": mscTrkUnAckedStorageType,
       "mscTrkUnAckedIndex": mscTrkUnAckedIndex,
       "mscTrkUnAckedFramer": mscTrkUnAckedFramer,
       "mscTrkUnAckedFramerRowStatusTable": mscTrkUnAckedFramerRowStatusTable,
       "mscTrkUnAckedFramerRowStatusEntry": mscTrkUnAckedFramerRowStatusEntry,
       "mscTrkUnAckedFramerRowStatus": mscTrkUnAckedFramerRowStatus,
       "mscTrkUnAckedFramerComponentName": mscTrkUnAckedFramerComponentName,
       "mscTrkUnAckedFramerStorageType": mscTrkUnAckedFramerStorageType,
       "mscTrkUnAckedFramerIndex": mscTrkUnAckedFramerIndex,
       "mscTrkUnAckedFramerProvTable": mscTrkUnAckedFramerProvTable,
       "mscTrkUnAckedFramerProvEntry": mscTrkUnAckedFramerProvEntry,
       "mscTrkUnAckedFramerInterfaceName": mscTrkUnAckedFramerInterfaceName,
       "mscTrkUnAckedFramerLinkTable": mscTrkUnAckedFramerLinkTable,
       "mscTrkUnAckedFramerLinkEntry": mscTrkUnAckedFramerLinkEntry,
       "mscTrkUnAckedFramerFramingType": mscTrkUnAckedFramerFramingType,
       "mscTrkUnAckedFramerDataInversion": mscTrkUnAckedFramerDataInversion,
       "mscTrkUnAckedFramerFrameCrcType": mscTrkUnAckedFramerFrameCrcType,
       "mscTrkUnAckedFramerFlagsBetweenFrames": mscTrkUnAckedFramerFlagsBetweenFrames,
       "mscTrkUnAckedFramerStateTable": mscTrkUnAckedFramerStateTable,
       "mscTrkUnAckedFramerStateEntry": mscTrkUnAckedFramerStateEntry,
       "mscTrkUnAckedFramerAdminState": mscTrkUnAckedFramerAdminState,
       "mscTrkUnAckedFramerOperationalState": mscTrkUnAckedFramerOperationalState,
       "mscTrkUnAckedFramerUsageState": mscTrkUnAckedFramerUsageState,
       "mscTrkUnAckedFramerStatsTable": mscTrkUnAckedFramerStatsTable,
       "mscTrkUnAckedFramerStatsEntry": mscTrkUnAckedFramerStatsEntry,
       "mscTrkUnAckedFramerFrmToIf": mscTrkUnAckedFramerFrmToIf,
       "mscTrkUnAckedFramerFrmFromIf": mscTrkUnAckedFramerFrmFromIf,
       "mscTrkUnAckedFramerOctetFromIf": mscTrkUnAckedFramerOctetFromIf,
       "mscTrkUnAckedFramerAborts": mscTrkUnAckedFramerAborts,
       "mscTrkUnAckedFramerCrcErrors": mscTrkUnAckedFramerCrcErrors,
       "mscTrkUnAckedFramerLrcErrors": mscTrkUnAckedFramerLrcErrors,
       "mscTrkUnAckedFramerNonOctetErrors": mscTrkUnAckedFramerNonOctetErrors,
       "mscTrkUnAckedFramerOverruns": mscTrkUnAckedFramerOverruns,
       "mscTrkUnAckedFramerUnderruns": mscTrkUnAckedFramerUnderruns,
       "mscTrkUnAckedFramerLargeFrmErrors": mscTrkUnAckedFramerLargeFrmErrors,
       "mscTrkUnAckedFramerFrmModeErrors": mscTrkUnAckedFramerFrmModeErrors,
       "mscTrkUnAckedFramerOutOfSequenceFrm": mscTrkUnAckedFramerOutOfSequenceFrm,
       "mscTrkUnAckedFramerRepeatedFrm": mscTrkUnAckedFramerRepeatedFrm,
       "mscTrkUnAckedFramerFrmFromIf64": mscTrkUnAckedFramerFrmFromIf64,
       "mscTrkUnAckedFramerOctetFromIf64": mscTrkUnAckedFramerOctetFromIf64,
       "mscTrkUnAckedFramerUtilTable": mscTrkUnAckedFramerUtilTable,
       "mscTrkUnAckedFramerUtilEntry": mscTrkUnAckedFramerUtilEntry,
       "mscTrkUnAckedFramerNormPrioLinkUtilToIf": mscTrkUnAckedFramerNormPrioLinkUtilToIf,
       "mscTrkUnAckedFramerHighPrioLinkUtilToIf": mscTrkUnAckedFramerHighPrioLinkUtilToIf,
       "mscTrkUnAckedFramerNormPrioLinkUtilFromIf": mscTrkUnAckedFramerNormPrioLinkUtilFromIf,
       "mscTrkUnAckedFramerHighPrioLinkUtilFromIf": mscTrkUnAckedFramerHighPrioLinkUtilFromIf,
       "mscTrkUnAckedFramerUtilThresholdTable": mscTrkUnAckedFramerUtilThresholdTable,
       "mscTrkUnAckedFramerUtilThresholdEntry": mscTrkUnAckedFramerUtilThresholdEntry,
       "mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold": mscTrkUnAckedFramerMinorLinkUtilAlarmThreshold,
       "mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold": mscTrkUnAckedFramerMajorLinkUtilAlarmThreshold,
       "mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold": mscTrkUnAckedFramerCriticalLinkUtilAlarmThreshold,
       "mscTrkUnAckedFramerLinkUtilAlarmStatus": mscTrkUnAckedFramerLinkUtilAlarmStatus,
       "mscTrkUnAckedProvTable": mscTrkUnAckedProvTable,
       "mscTrkUnAckedProvEntry": mscTrkUnAckedProvEntry,
       "mscTrkUnAckedMaximumErroredInterval": mscTrkUnAckedMaximumErroredInterval,
       "mscTrkUnAckedReceiveErrorSensitivity": mscTrkUnAckedReceiveErrorSensitivity,
       "mscTrkUnAckedStateTable": mscTrkUnAckedStateTable,
       "mscTrkUnAckedStateEntry": mscTrkUnAckedStateEntry,
       "mscTrkUnAckedAdminState": mscTrkUnAckedAdminState,
       "mscTrkUnAckedOperationalState": mscTrkUnAckedOperationalState,
       "mscTrkUnAckedUsageState": mscTrkUnAckedUsageState,
       "mscTrkUnAckedAvailabilityStatus": mscTrkUnAckedAvailabilityStatus,
       "mscTrkUnAckedProceduralStatus": mscTrkUnAckedProceduralStatus,
       "mscTrkUnAckedControlStatus": mscTrkUnAckedControlStatus,
       "mscTrkUnAckedAlarmStatus": mscTrkUnAckedAlarmStatus,
       "mscTrkUnAckedStandbyStatus": mscTrkUnAckedStandbyStatus,
       "mscTrkUnAckedUnknownStatus": mscTrkUnAckedUnknownStatus,
       "unackTrunksMIB": unackTrunksMIB,
       "unackTrunksGroup": unackTrunksGroup,
       "unackTrunksGroupCB": unackTrunksGroupCB,
       "unackTrunksGroupCB01": unackTrunksGroupCB01,
       "unackTrunksGroupCB01A": unackTrunksGroupCB01A,
       "unackTrunksCapabilities": unackTrunksCapabilities,
       "unackTrunksCapabilitiesCB": unackTrunksCapabilitiesCB,
       "unackTrunksCapabilitiesCB01": unackTrunksCapabilitiesCB01,
       "unackTrunksCapabilitiesCB01A": unackTrunksCapabilitiesCB01A}
)
