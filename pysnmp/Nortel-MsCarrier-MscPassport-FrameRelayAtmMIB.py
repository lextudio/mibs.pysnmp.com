# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:24 2024
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
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 HexString,
 IntegerSequence,
 Link,
 NonReplicated,
 PassportCounter64,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "HexString",
    "IntegerSequence",
    "Link",
    "NonReplicated",
    "PassportCounter64",
    "Unsigned64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
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

_MscFrAtm_ObjectIdentity = ObjectIdentity
mscFrAtm = _MscFrAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72)
)
_MscFrAtmRowStatusTable_Object = MibTable
mscFrAtmRowStatusTable = _MscFrAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmRowStatusTable.setStatus("mandatory")
_MscFrAtmRowStatusEntry_Object = MibTableRow
mscFrAtmRowStatusEntry = _MscFrAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1, 1)
)
mscFrAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmRowStatusEntry.setStatus("mandatory")
_MscFrAtmRowStatus_Type = RowStatus
_MscFrAtmRowStatus_Object = MibTableColumn
mscFrAtmRowStatus = _MscFrAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1, 1, 1),
    _MscFrAtmRowStatus_Type()
)
mscFrAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmRowStatus.setStatus("mandatory")
_MscFrAtmComponentName_Type = DisplayString
_MscFrAtmComponentName_Object = MibTableColumn
mscFrAtmComponentName = _MscFrAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1, 1, 2),
    _MscFrAtmComponentName_Type()
)
mscFrAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmComponentName.setStatus("mandatory")
_MscFrAtmStorageType_Type = StorageType
_MscFrAtmStorageType_Object = MibTableColumn
mscFrAtmStorageType = _MscFrAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1, 1, 4),
    _MscFrAtmStorageType_Type()
)
mscFrAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmStorageType.setStatus("mandatory")


class _MscFrAtmIndex_Type(Integer32):
    """Custom type mscFrAtmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrAtmIndex_Type.__name__ = "Integer32"
_MscFrAtmIndex_Object = MibTableColumn
mscFrAtmIndex = _MscFrAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 1, 1, 10),
    _MscFrAtmIndex_Type()
)
mscFrAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmIndex.setStatus("mandatory")
_MscFrAtmFramer_ObjectIdentity = ObjectIdentity
mscFrAtmFramer = _MscFrAtmFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2)
)
_MscFrAtmFramerRowStatusTable_Object = MibTable
mscFrAtmFramerRowStatusTable = _MscFrAtmFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerRowStatusTable.setStatus("mandatory")
_MscFrAtmFramerRowStatusEntry_Object = MibTableRow
mscFrAtmFramerRowStatusEntry = _MscFrAtmFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1, 1)
)
mscFrAtmFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerRowStatusEntry.setStatus("mandatory")
_MscFrAtmFramerRowStatus_Type = RowStatus
_MscFrAtmFramerRowStatus_Object = MibTableColumn
mscFrAtmFramerRowStatus = _MscFrAtmFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1, 1, 1),
    _MscFrAtmFramerRowStatus_Type()
)
mscFrAtmFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmFramerRowStatus.setStatus("mandatory")
_MscFrAtmFramerComponentName_Type = DisplayString
_MscFrAtmFramerComponentName_Object = MibTableColumn
mscFrAtmFramerComponentName = _MscFrAtmFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1, 1, 2),
    _MscFrAtmFramerComponentName_Type()
)
mscFrAtmFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerComponentName.setStatus("mandatory")
_MscFrAtmFramerStorageType_Type = StorageType
_MscFrAtmFramerStorageType_Object = MibTableColumn
mscFrAtmFramerStorageType = _MscFrAtmFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1, 1, 4),
    _MscFrAtmFramerStorageType_Type()
)
mscFrAtmFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerStorageType.setStatus("mandatory")
_MscFrAtmFramerIndex_Type = NonReplicated
_MscFrAtmFramerIndex_Object = MibTableColumn
mscFrAtmFramerIndex = _MscFrAtmFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 1, 1, 10),
    _MscFrAtmFramerIndex_Type()
)
mscFrAtmFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmFramerIndex.setStatus("mandatory")
_MscFrAtmFramerProvTable_Object = MibTable
mscFrAtmFramerProvTable = _MscFrAtmFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerProvTable.setStatus("mandatory")
_MscFrAtmFramerProvEntry_Object = MibTableRow
mscFrAtmFramerProvEntry = _MscFrAtmFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 10, 1)
)
mscFrAtmFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerProvEntry.setStatus("mandatory")
_MscFrAtmFramerInterfaceName_Type = Link
_MscFrAtmFramerInterfaceName_Object = MibTableColumn
mscFrAtmFramerInterfaceName = _MscFrAtmFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 10, 1, 1),
    _MscFrAtmFramerInterfaceName_Type()
)
mscFrAtmFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmFramerInterfaceName.setStatus("mandatory")
_MscFrAtmFramerLinkTable_Object = MibTable
mscFrAtmFramerLinkTable = _MscFrAtmFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerLinkTable.setStatus("mandatory")
_MscFrAtmFramerLinkEntry_Object = MibTableRow
mscFrAtmFramerLinkEntry = _MscFrAtmFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 11, 1)
)
mscFrAtmFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerLinkEntry.setStatus("mandatory")


class _MscFrAtmFramerDataInversion_Type(Integer32):
    """Custom type mscFrAtmFramerDataInversion based on Integer32"""
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


_MscFrAtmFramerDataInversion_Type.__name__ = "Integer32"
_MscFrAtmFramerDataInversion_Object = MibTableColumn
mscFrAtmFramerDataInversion = _MscFrAtmFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 11, 1, 2),
    _MscFrAtmFramerDataInversion_Type()
)
mscFrAtmFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmFramerDataInversion.setStatus("mandatory")


class _MscFrAtmFramerFrameCrcType_Type(Integer32):
    """Custom type mscFrAtmFramerFrameCrcType based on Integer32"""
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


_MscFrAtmFramerFrameCrcType_Type.__name__ = "Integer32"
_MscFrAtmFramerFrameCrcType_Object = MibTableColumn
mscFrAtmFramerFrameCrcType = _MscFrAtmFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 11, 1, 3),
    _MscFrAtmFramerFrameCrcType_Type()
)
mscFrAtmFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrameCrcType.setStatus("mandatory")


class _MscFrAtmFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscFrAtmFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscFrAtmFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscFrAtmFramerFlagsBetweenFrames_Object = MibTableColumn
mscFrAtmFramerFlagsBetweenFrames = _MscFrAtmFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 11, 1, 4),
    _MscFrAtmFramerFlagsBetweenFrames_Type()
)
mscFrAtmFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmFramerFlagsBetweenFrames.setStatus("mandatory")
_MscFrAtmFramerStateTable_Object = MibTable
mscFrAtmFramerStateTable = _MscFrAtmFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerStateTable.setStatus("mandatory")
_MscFrAtmFramerStateEntry_Object = MibTableRow
mscFrAtmFramerStateEntry = _MscFrAtmFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 12, 1)
)
mscFrAtmFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerStateEntry.setStatus("mandatory")


class _MscFrAtmFramerAdminState_Type(Integer32):
    """Custom type mscFrAtmFramerAdminState based on Integer32"""
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


_MscFrAtmFramerAdminState_Type.__name__ = "Integer32"
_MscFrAtmFramerAdminState_Object = MibTableColumn
mscFrAtmFramerAdminState = _MscFrAtmFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 12, 1, 1),
    _MscFrAtmFramerAdminState_Type()
)
mscFrAtmFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerAdminState.setStatus("mandatory")


class _MscFrAtmFramerOperationalState_Type(Integer32):
    """Custom type mscFrAtmFramerOperationalState based on Integer32"""
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


_MscFrAtmFramerOperationalState_Type.__name__ = "Integer32"
_MscFrAtmFramerOperationalState_Object = MibTableColumn
mscFrAtmFramerOperationalState = _MscFrAtmFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 12, 1, 2),
    _MscFrAtmFramerOperationalState_Type()
)
mscFrAtmFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerOperationalState.setStatus("mandatory")


class _MscFrAtmFramerUsageState_Type(Integer32):
    """Custom type mscFrAtmFramerUsageState based on Integer32"""
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


_MscFrAtmFramerUsageState_Type.__name__ = "Integer32"
_MscFrAtmFramerUsageState_Object = MibTableColumn
mscFrAtmFramerUsageState = _MscFrAtmFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 12, 1, 3),
    _MscFrAtmFramerUsageState_Type()
)
mscFrAtmFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerUsageState.setStatus("mandatory")
_MscFrAtmFramerStatsTable_Object = MibTable
mscFrAtmFramerStatsTable = _MscFrAtmFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerStatsTable.setStatus("mandatory")
_MscFrAtmFramerStatsEntry_Object = MibTableRow
mscFrAtmFramerStatsEntry = _MscFrAtmFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1)
)
mscFrAtmFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerStatsEntry.setStatus("mandatory")
_MscFrAtmFramerFrmToIf_Type = Counter32
_MscFrAtmFramerFrmToIf_Object = MibTableColumn
mscFrAtmFramerFrmToIf = _MscFrAtmFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 1),
    _MscFrAtmFramerFrmToIf_Type()
)
mscFrAtmFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrmToIf.setStatus("obsolete")
_MscFrAtmFramerFrmFromIf_Type = Counter32
_MscFrAtmFramerFrmFromIf_Object = MibTableColumn
mscFrAtmFramerFrmFromIf = _MscFrAtmFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 2),
    _MscFrAtmFramerFrmFromIf_Type()
)
mscFrAtmFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrmFromIf.setStatus("obsolete")
_MscFrAtmFramerOctetFromIf_Type = Counter32
_MscFrAtmFramerOctetFromIf_Object = MibTableColumn
mscFrAtmFramerOctetFromIf = _MscFrAtmFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 3),
    _MscFrAtmFramerOctetFromIf_Type()
)
mscFrAtmFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerOctetFromIf.setStatus("obsolete")
_MscFrAtmFramerAborts_Type = Counter32
_MscFrAtmFramerAborts_Object = MibTableColumn
mscFrAtmFramerAborts = _MscFrAtmFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 4),
    _MscFrAtmFramerAborts_Type()
)
mscFrAtmFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerAborts.setStatus("mandatory")
_MscFrAtmFramerCrcErrors_Type = Counter32
_MscFrAtmFramerCrcErrors_Object = MibTableColumn
mscFrAtmFramerCrcErrors = _MscFrAtmFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 5),
    _MscFrAtmFramerCrcErrors_Type()
)
mscFrAtmFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerCrcErrors.setStatus("mandatory")
_MscFrAtmFramerLrcErrors_Type = Counter32
_MscFrAtmFramerLrcErrors_Object = MibTableColumn
mscFrAtmFramerLrcErrors = _MscFrAtmFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 6),
    _MscFrAtmFramerLrcErrors_Type()
)
mscFrAtmFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerLrcErrors.setStatus("mandatory")
_MscFrAtmFramerNonOctetErrors_Type = Counter32
_MscFrAtmFramerNonOctetErrors_Object = MibTableColumn
mscFrAtmFramerNonOctetErrors = _MscFrAtmFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 7),
    _MscFrAtmFramerNonOctetErrors_Type()
)
mscFrAtmFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerNonOctetErrors.setStatus("mandatory")
_MscFrAtmFramerOverruns_Type = Counter32
_MscFrAtmFramerOverruns_Object = MibTableColumn
mscFrAtmFramerOverruns = _MscFrAtmFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 8),
    _MscFrAtmFramerOverruns_Type()
)
mscFrAtmFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerOverruns.setStatus("mandatory")
_MscFrAtmFramerUnderruns_Type = Counter32
_MscFrAtmFramerUnderruns_Object = MibTableColumn
mscFrAtmFramerUnderruns = _MscFrAtmFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 9),
    _MscFrAtmFramerUnderruns_Type()
)
mscFrAtmFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerUnderruns.setStatus("mandatory")
_MscFrAtmFramerLargeFrmErrors_Type = Counter32
_MscFrAtmFramerLargeFrmErrors_Object = MibTableColumn
mscFrAtmFramerLargeFrmErrors = _MscFrAtmFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 10),
    _MscFrAtmFramerLargeFrmErrors_Type()
)
mscFrAtmFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerLargeFrmErrors.setStatus("mandatory")
_MscFrAtmFramerFrmModeErrors_Type = Counter32
_MscFrAtmFramerFrmModeErrors_Object = MibTableColumn
mscFrAtmFramerFrmModeErrors = _MscFrAtmFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 11),
    _MscFrAtmFramerFrmModeErrors_Type()
)
mscFrAtmFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrmModeErrors.setStatus("mandatory")
_MscFrAtmFramerFrmToIf64_Type = PassportCounter64
_MscFrAtmFramerFrmToIf64_Object = MibTableColumn
mscFrAtmFramerFrmToIf64 = _MscFrAtmFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 14),
    _MscFrAtmFramerFrmToIf64_Type()
)
mscFrAtmFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrmToIf64.setStatus("mandatory")
_MscFrAtmFramerFrmFromIf64_Type = PassportCounter64
_MscFrAtmFramerFrmFromIf64_Object = MibTableColumn
mscFrAtmFramerFrmFromIf64 = _MscFrAtmFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 15),
    _MscFrAtmFramerFrmFromIf64_Type()
)
mscFrAtmFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerFrmFromIf64.setStatus("mandatory")
_MscFrAtmFramerOctetFromIf64_Type = PassportCounter64
_MscFrAtmFramerOctetFromIf64_Object = MibTableColumn
mscFrAtmFramerOctetFromIf64 = _MscFrAtmFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 13, 1, 16),
    _MscFrAtmFramerOctetFromIf64_Type()
)
mscFrAtmFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerOctetFromIf64.setStatus("mandatory")
_MscFrAtmFramerUtilTable_Object = MibTable
mscFrAtmFramerUtilTable = _MscFrAtmFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmFramerUtilTable.setStatus("mandatory")
_MscFrAtmFramerUtilEntry_Object = MibTableRow
mscFrAtmFramerUtilEntry = _MscFrAtmFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 14, 1)
)
mscFrAtmFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFramerUtilEntry.setStatus("mandatory")


class _MscFrAtmFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscFrAtmFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrAtmFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscFrAtmFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscFrAtmFramerNormPrioLinkUtilToIf = _MscFrAtmFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 14, 1, 1),
    _MscFrAtmFramerNormPrioLinkUtilToIf_Type()
)
mscFrAtmFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscFrAtmFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscFrAtmFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrAtmFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscFrAtmFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscFrAtmFramerNormPrioLinkUtilFromIf = _MscFrAtmFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 2, 14, 1, 3),
    _MscFrAtmFramerNormPrioLinkUtilFromIf_Type()
)
mscFrAtmFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscFrAtmLmi_ObjectIdentity = ObjectIdentity
mscFrAtmLmi = _MscFrAtmLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3)
)
_MscFrAtmLmiRowStatusTable_Object = MibTable
mscFrAtmLmiRowStatusTable = _MscFrAtmLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiRowStatusTable.setStatus("mandatory")
_MscFrAtmLmiRowStatusEntry_Object = MibTableRow
mscFrAtmLmiRowStatusEntry = _MscFrAtmLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1, 1)
)
mscFrAtmLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiRowStatusEntry.setStatus("mandatory")
_MscFrAtmLmiRowStatus_Type = RowStatus
_MscFrAtmLmiRowStatus_Object = MibTableColumn
mscFrAtmLmiRowStatus = _MscFrAtmLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1, 1, 1),
    _MscFrAtmLmiRowStatus_Type()
)
mscFrAtmLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiRowStatus.setStatus("mandatory")
_MscFrAtmLmiComponentName_Type = DisplayString
_MscFrAtmLmiComponentName_Object = MibTableColumn
mscFrAtmLmiComponentName = _MscFrAtmLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1, 1, 2),
    _MscFrAtmLmiComponentName_Type()
)
mscFrAtmLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiComponentName.setStatus("mandatory")
_MscFrAtmLmiStorageType_Type = StorageType
_MscFrAtmLmiStorageType_Object = MibTableColumn
mscFrAtmLmiStorageType = _MscFrAtmLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1, 1, 4),
    _MscFrAtmLmiStorageType_Type()
)
mscFrAtmLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiStorageType.setStatus("mandatory")
_MscFrAtmLmiIndex_Type = NonReplicated
_MscFrAtmLmiIndex_Object = MibTableColumn
mscFrAtmLmiIndex = _MscFrAtmLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 1, 1, 10),
    _MscFrAtmLmiIndex_Type()
)
mscFrAtmLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmLmiIndex.setStatus("mandatory")
_MscFrAtmLmiParmsTable_Object = MibTable
mscFrAtmLmiParmsTable = _MscFrAtmLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiParmsTable.setStatus("mandatory")
_MscFrAtmLmiParmsEntry_Object = MibTableRow
mscFrAtmLmiParmsEntry = _MscFrAtmLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1)
)
mscFrAtmLmiParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiParmsEntry.setStatus("mandatory")


class _MscFrAtmLmiProcedures_Type(Integer32):
    """Custom type mscFrAtmLmiProcedures based on Integer32"""
    defaultValue = 4

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
        *(("ansi", 2),
          ("autoConfigure", 4),
          ("itu", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_MscFrAtmLmiProcedures_Type.__name__ = "Integer32"
_MscFrAtmLmiProcedures_Object = MibTableColumn
mscFrAtmLmiProcedures = _MscFrAtmLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 1),
    _MscFrAtmLmiProcedures_Type()
)
mscFrAtmLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiProcedures.setStatus("mandatory")


class _MscFrAtmLmiAsyncStatusReport_Type(Integer32):
    """Custom type mscFrAtmLmiAsyncStatusReport based on Integer32"""
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


_MscFrAtmLmiAsyncStatusReport_Type.__name__ = "Integer32"
_MscFrAtmLmiAsyncStatusReport_Object = MibTableColumn
mscFrAtmLmiAsyncStatusReport = _MscFrAtmLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 2),
    _MscFrAtmLmiAsyncStatusReport_Type()
)
mscFrAtmLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiAsyncStatusReport.setStatus("mandatory")


class _MscFrAtmLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mscFrAtmLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrAtmLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_MscFrAtmLmiErrorEventThreshold_Object = MibTableColumn
mscFrAtmLmiErrorEventThreshold = _MscFrAtmLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 3),
    _MscFrAtmLmiErrorEventThreshold_Type()
)
mscFrAtmLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiErrorEventThreshold.setStatus("mandatory")


class _MscFrAtmLmiEventCount_Type(Unsigned32):
    """Custom type mscFrAtmLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrAtmLmiEventCount_Type.__name__ = "Unsigned32"
_MscFrAtmLmiEventCount_Object = MibTableColumn
mscFrAtmLmiEventCount = _MscFrAtmLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 4),
    _MscFrAtmLmiEventCount_Type()
)
mscFrAtmLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiEventCount.setStatus("mandatory")


class _MscFrAtmLmiCheckPointTimer_Type(Unsigned32):
    """Custom type mscFrAtmLmiCheckPointTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_MscFrAtmLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_MscFrAtmLmiCheckPointTimer_Object = MibTableColumn
mscFrAtmLmiCheckPointTimer = _MscFrAtmLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 5),
    _MscFrAtmLmiCheckPointTimer_Type()
)
mscFrAtmLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiCheckPointTimer.setStatus("mandatory")


class _MscFrAtmLmiMessageCountTimer_Type(Unsigned32):
    """Custom type mscFrAtmLmiMessageCountTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_MscFrAtmLmiMessageCountTimer_Type.__name__ = "Unsigned32"
_MscFrAtmLmiMessageCountTimer_Object = MibTableColumn
mscFrAtmLmiMessageCountTimer = _MscFrAtmLmiMessageCountTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 6),
    _MscFrAtmLmiMessageCountTimer_Type()
)
mscFrAtmLmiMessageCountTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiMessageCountTimer.setStatus("mandatory")


class _MscFrAtmLmiIgnoreActiveBit_Type(Integer32):
    """Custom type mscFrAtmLmiIgnoreActiveBit based on Integer32"""
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


_MscFrAtmLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_MscFrAtmLmiIgnoreActiveBit_Object = MibTableColumn
mscFrAtmLmiIgnoreActiveBit = _MscFrAtmLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 7),
    _MscFrAtmLmiIgnoreActiveBit_Type()
)
mscFrAtmLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiIgnoreActiveBit.setStatus("mandatory")


class _MscFrAtmLmiSide_Type(Integer32):
    """Custom type mscFrAtmLmiSide based on Integer32"""
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
        *(("both", 2),
          ("network", 0),
          ("user", 1))
    )


_MscFrAtmLmiSide_Type.__name__ = "Integer32"
_MscFrAtmLmiSide_Object = MibTableColumn
mscFrAtmLmiSide = _MscFrAtmLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 8),
    _MscFrAtmLmiSide_Type()
)
mscFrAtmLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiSide.setStatus("mandatory")


class _MscFrAtmLmiPvcConfigParmsInFsr_Type(Integer32):
    """Custom type mscFrAtmLmiPvcConfigParmsInFsr based on Integer32"""
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


_MscFrAtmLmiPvcConfigParmsInFsr_Type.__name__ = "Integer32"
_MscFrAtmLmiPvcConfigParmsInFsr_Object = MibTableColumn
mscFrAtmLmiPvcConfigParmsInFsr = _MscFrAtmLmiPvcConfigParmsInFsr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 10, 1, 9),
    _MscFrAtmLmiPvcConfigParmsInFsr_Type()
)
mscFrAtmLmiPvcConfigParmsInFsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiPvcConfigParmsInFsr.setStatus("mandatory")
_MscFrAtmLmiStateTable_Object = MibTable
mscFrAtmLmiStateTable = _MscFrAtmLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiStateTable.setStatus("mandatory")
_MscFrAtmLmiStateEntry_Object = MibTableRow
mscFrAtmLmiStateEntry = _MscFrAtmLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 11, 1)
)
mscFrAtmLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiStateEntry.setStatus("mandatory")


class _MscFrAtmLmiAdminState_Type(Integer32):
    """Custom type mscFrAtmLmiAdminState based on Integer32"""
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


_MscFrAtmLmiAdminState_Type.__name__ = "Integer32"
_MscFrAtmLmiAdminState_Object = MibTableColumn
mscFrAtmLmiAdminState = _MscFrAtmLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 11, 1, 1),
    _MscFrAtmLmiAdminState_Type()
)
mscFrAtmLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiAdminState.setStatus("mandatory")


class _MscFrAtmLmiOperationalState_Type(Integer32):
    """Custom type mscFrAtmLmiOperationalState based on Integer32"""
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


_MscFrAtmLmiOperationalState_Type.__name__ = "Integer32"
_MscFrAtmLmiOperationalState_Object = MibTableColumn
mscFrAtmLmiOperationalState = _MscFrAtmLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 11, 1, 2),
    _MscFrAtmLmiOperationalState_Type()
)
mscFrAtmLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiOperationalState.setStatus("mandatory")


class _MscFrAtmLmiUsageState_Type(Integer32):
    """Custom type mscFrAtmLmiUsageState based on Integer32"""
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


_MscFrAtmLmiUsageState_Type.__name__ = "Integer32"
_MscFrAtmLmiUsageState_Object = MibTableColumn
mscFrAtmLmiUsageState = _MscFrAtmLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 11, 1, 3),
    _MscFrAtmLmiUsageState_Type()
)
mscFrAtmLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiUsageState.setStatus("mandatory")
_MscFrAtmLmiPsiTable_Object = MibTable
mscFrAtmLmiPsiTable = _MscFrAtmLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiPsiTable.setStatus("mandatory")
_MscFrAtmLmiPsiEntry_Object = MibTableRow
mscFrAtmLmiPsiEntry = _MscFrAtmLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 12, 1)
)
mscFrAtmLmiPsiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiPsiEntry.setStatus("mandatory")


class _MscFrAtmLmiProtocolStatus_Type(Integer32):
    """Custom type mscFrAtmLmiProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 2),
          ("errorCondition", 0),
          ("normalCondition", 1))
    )


_MscFrAtmLmiProtocolStatus_Type.__name__ = "Integer32"
_MscFrAtmLmiProtocolStatus_Object = MibTableColumn
mscFrAtmLmiProtocolStatus = _MscFrAtmLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 12, 1, 1),
    _MscFrAtmLmiProtocolStatus_Type()
)
mscFrAtmLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiProtocolStatus.setStatus("mandatory")


class _MscFrAtmLmiOpProcedures_Type(Integer32):
    """Custom type mscFrAtmLmiOpProcedures based on Integer32"""
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
        *(("ansi", 2),
          ("itu", 3),
          ("none", 0),
          ("unknown", 4),
          ("vendorForum", 1))
    )


_MscFrAtmLmiOpProcedures_Type.__name__ = "Integer32"
_MscFrAtmLmiOpProcedures_Object = MibTableColumn
mscFrAtmLmiOpProcedures = _MscFrAtmLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 12, 1, 2),
    _MscFrAtmLmiOpProcedures_Type()
)
mscFrAtmLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiOpProcedures.setStatus("mandatory")
_MscFrAtmLmiStatsTable_Object = MibTable
mscFrAtmLmiStatsTable = _MscFrAtmLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiStatsTable.setStatus("mandatory")
_MscFrAtmLmiStatsEntry_Object = MibTableRow
mscFrAtmLmiStatsEntry = _MscFrAtmLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1)
)
mscFrAtmLmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiStatsEntry.setStatus("mandatory")
_MscFrAtmLmiKeepAliveStatusToIf_Type = Counter32
_MscFrAtmLmiKeepAliveStatusToIf_Object = MibTableColumn
mscFrAtmLmiKeepAliveStatusToIf = _MscFrAtmLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 1),
    _MscFrAtmLmiKeepAliveStatusToIf_Type()
)
mscFrAtmLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiKeepAliveStatusToIf.setStatus("mandatory")
_MscFrAtmLmiFullStatusToIf_Type = Counter32
_MscFrAtmLmiFullStatusToIf_Object = MibTableColumn
mscFrAtmLmiFullStatusToIf = _MscFrAtmLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 2),
    _MscFrAtmLmiFullStatusToIf_Type()
)
mscFrAtmLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiFullStatusToIf.setStatus("mandatory")
_MscFrAtmLmiKeepAliveStatusEnqFromIf_Type = Counter32
_MscFrAtmLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
mscFrAtmLmiKeepAliveStatusEnqFromIf = _MscFrAtmLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 3),
    _MscFrAtmLmiKeepAliveStatusEnqFromIf_Type()
)
mscFrAtmLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_MscFrAtmLmiFullStatusEnqFromIf_Type = Counter32
_MscFrAtmLmiFullStatusEnqFromIf_Object = MibTableColumn
mscFrAtmLmiFullStatusEnqFromIf = _MscFrAtmLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 4),
    _MscFrAtmLmiFullStatusEnqFromIf_Type()
)
mscFrAtmLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiFullStatusEnqFromIf.setStatus("mandatory")


class _MscFrAtmLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type mscFrAtmLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrAtmLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_MscFrAtmLmiNetworkSideEventHistory_Object = MibTableColumn
mscFrAtmLmiNetworkSideEventHistory = _MscFrAtmLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 5),
    _MscFrAtmLmiNetworkSideEventHistory_Type()
)
mscFrAtmLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiNetworkSideEventHistory.setStatus("mandatory")
_MscFrAtmLmiProtocolErrors_Type = Counter32
_MscFrAtmLmiProtocolErrors_Object = MibTableColumn
mscFrAtmLmiProtocolErrors = _MscFrAtmLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 6),
    _MscFrAtmLmiProtocolErrors_Type()
)
mscFrAtmLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiProtocolErrors.setStatus("mandatory")
_MscFrAtmLmiUnexpectedIes_Type = Counter32
_MscFrAtmLmiUnexpectedIes_Object = MibTableColumn
mscFrAtmLmiUnexpectedIes = _MscFrAtmLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 7),
    _MscFrAtmLmiUnexpectedIes_Type()
)
mscFrAtmLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiUnexpectedIes.setStatus("mandatory")
_MscFrAtmLmiSequenceErrors_Type = Counter32
_MscFrAtmLmiSequenceErrors_Object = MibTableColumn
mscFrAtmLmiSequenceErrors = _MscFrAtmLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 8),
    _MscFrAtmLmiSequenceErrors_Type()
)
mscFrAtmLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiSequenceErrors.setStatus("mandatory")
_MscFrAtmLmiUnexpectedReports_Type = Counter32
_MscFrAtmLmiUnexpectedReports_Object = MibTableColumn
mscFrAtmLmiUnexpectedReports = _MscFrAtmLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 9),
    _MscFrAtmLmiUnexpectedReports_Type()
)
mscFrAtmLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiUnexpectedReports.setStatus("mandatory")
_MscFrAtmLmiPollingVerifTimeouts_Type = Counter32
_MscFrAtmLmiPollingVerifTimeouts_Object = MibTableColumn
mscFrAtmLmiPollingVerifTimeouts = _MscFrAtmLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 10),
    _MscFrAtmLmiPollingVerifTimeouts_Type()
)
mscFrAtmLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiPollingVerifTimeouts.setStatus("mandatory")
_MscFrAtmLmiKeepAliveEnqToIf_Type = Counter32
_MscFrAtmLmiKeepAliveEnqToIf_Object = MibTableColumn
mscFrAtmLmiKeepAliveEnqToIf = _MscFrAtmLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 11),
    _MscFrAtmLmiKeepAliveEnqToIf_Type()
)
mscFrAtmLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiKeepAliveEnqToIf.setStatus("mandatory")
_MscFrAtmLmiFullStatusEnqToIf_Type = Counter32
_MscFrAtmLmiFullStatusEnqToIf_Object = MibTableColumn
mscFrAtmLmiFullStatusEnqToIf = _MscFrAtmLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 12),
    _MscFrAtmLmiFullStatusEnqToIf_Type()
)
mscFrAtmLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiFullStatusEnqToIf.setStatus("mandatory")


class _MscFrAtmLmiUserSideEventHistory_Type(AsciiString):
    """Custom type mscFrAtmLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrAtmLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_MscFrAtmLmiUserSideEventHistory_Object = MibTableColumn
mscFrAtmLmiUserSideEventHistory = _MscFrAtmLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 13),
    _MscFrAtmLmiUserSideEventHistory_Type()
)
mscFrAtmLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiUserSideEventHistory.setStatus("mandatory")
_MscFrAtmLmiStatusSequenceErrors_Type = Counter32
_MscFrAtmLmiStatusSequenceErrors_Object = MibTableColumn
mscFrAtmLmiStatusSequenceErrors = _MscFrAtmLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 14),
    _MscFrAtmLmiStatusSequenceErrors_Type()
)
mscFrAtmLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiStatusSequenceErrors.setStatus("mandatory")
_MscFrAtmLmiNoStatusReportCount_Type = Counter32
_MscFrAtmLmiNoStatusReportCount_Object = MibTableColumn
mscFrAtmLmiNoStatusReportCount = _MscFrAtmLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 13, 1, 15),
    _MscFrAtmLmiNoStatusReportCount_Type()
)
mscFrAtmLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLmiNoStatusReportCount.setStatus("mandatory")
_MscFrAtmLmiUspParmsTable_Object = MibTable
mscFrAtmLmiUspParmsTable = _MscFrAtmLmiUspParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmLmiUspParmsTable.setStatus("mandatory")
_MscFrAtmLmiUspParmsEntry_Object = MibTableRow
mscFrAtmLmiUspParmsEntry = _MscFrAtmLmiUspParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 14, 1)
)
mscFrAtmLmiUspParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmLmiUspParmsEntry.setStatus("mandatory")


class _MscFrAtmLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mscFrAtmLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrAtmLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_MscFrAtmLmiFullStatusPollingCycles_Object = MibTableColumn
mscFrAtmLmiFullStatusPollingCycles = _MscFrAtmLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 14, 1, 1),
    _MscFrAtmLmiFullStatusPollingCycles_Type()
)
mscFrAtmLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiFullStatusPollingCycles.setStatus("mandatory")


class _MscFrAtmLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mscFrAtmLmiLinkVerificationTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_MscFrAtmLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_MscFrAtmLmiLinkVerificationTimer_Object = MibTableColumn
mscFrAtmLmiLinkVerificationTimer = _MscFrAtmLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 3, 14, 1, 2),
    _MscFrAtmLmiLinkVerificationTimer_Type()
)
mscFrAtmLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmLmiLinkVerificationTimer.setStatus("mandatory")
_MscFrAtmDlci_ObjectIdentity = ObjectIdentity
mscFrAtmDlci = _MscFrAtmDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4)
)
_MscFrAtmDlciRowStatusTable_Object = MibTable
mscFrAtmDlciRowStatusTable = _MscFrAtmDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciRowStatusEntry_Object = MibTableRow
mscFrAtmDlciRowStatusEntry = _MscFrAtmDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1, 1)
)
mscFrAtmDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciRowStatus_Type = RowStatus
_MscFrAtmDlciRowStatus_Object = MibTableColumn
mscFrAtmDlciRowStatus = _MscFrAtmDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1, 1, 1),
    _MscFrAtmDlciRowStatus_Type()
)
mscFrAtmDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciRowStatus.setStatus("mandatory")
_MscFrAtmDlciComponentName_Type = DisplayString
_MscFrAtmDlciComponentName_Object = MibTableColumn
mscFrAtmDlciComponentName = _MscFrAtmDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1, 1, 2),
    _MscFrAtmDlciComponentName_Type()
)
mscFrAtmDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciComponentName.setStatus("mandatory")
_MscFrAtmDlciStorageType_Type = StorageType
_MscFrAtmDlciStorageType_Object = MibTableColumn
mscFrAtmDlciStorageType = _MscFrAtmDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1, 1, 4),
    _MscFrAtmDlciStorageType_Type()
)
mscFrAtmDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciStorageType.setStatus("mandatory")


class _MscFrAtmDlciIndex_Type(Integer32):
    """Custom type mscFrAtmDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrAtmDlciIndex_Type.__name__ = "Integer32"
_MscFrAtmDlciIndex_Object = MibTableColumn
mscFrAtmDlciIndex = _MscFrAtmDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 1, 1, 10),
    _MscFrAtmDlciIndex_Type()
)
mscFrAtmDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciIndex.setStatus("mandatory")
_MscFrAtmDlciSp_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSp = _MscFrAtmDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2)
)
_MscFrAtmDlciSpRowStatusTable_Object = MibTable
mscFrAtmDlciSpRowStatusTable = _MscFrAtmDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSpRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSpRowStatusEntry = _MscFrAtmDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1, 1)
)
mscFrAtmDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSpRowStatus_Type = RowStatus
_MscFrAtmDlciSpRowStatus_Object = MibTableColumn
mscFrAtmDlciSpRowStatus = _MscFrAtmDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1, 1, 1),
    _MscFrAtmDlciSpRowStatus_Type()
)
mscFrAtmDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpRowStatus.setStatus("mandatory")
_MscFrAtmDlciSpComponentName_Type = DisplayString
_MscFrAtmDlciSpComponentName_Object = MibTableColumn
mscFrAtmDlciSpComponentName = _MscFrAtmDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1, 1, 2),
    _MscFrAtmDlciSpComponentName_Type()
)
mscFrAtmDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpComponentName.setStatus("mandatory")
_MscFrAtmDlciSpStorageType_Type = StorageType
_MscFrAtmDlciSpStorageType_Object = MibTableColumn
mscFrAtmDlciSpStorageType = _MscFrAtmDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1, 1, 4),
    _MscFrAtmDlciSpStorageType_Type()
)
mscFrAtmDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpStorageType.setStatus("mandatory")
_MscFrAtmDlciSpIndex_Type = NonReplicated
_MscFrAtmDlciSpIndex_Object = MibTableColumn
mscFrAtmDlciSpIndex = _MscFrAtmDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 1, 1, 10),
    _MscFrAtmDlciSpIndex_Type()
)
mscFrAtmDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpIndex.setStatus("mandatory")
_MscFrAtmDlciSpProvTable_Object = MibTable
mscFrAtmDlciSpProvTable = _MscFrAtmDlciSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpProvTable.setStatus("mandatory")
_MscFrAtmDlciSpProvEntry_Object = MibTableRow
mscFrAtmDlciSpProvEntry = _MscFrAtmDlciSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1)
)
mscFrAtmDlciSpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpProvEntry.setStatus("mandatory")


class _MscFrAtmDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrAtmDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSpMaximumFrameSize_Object = MibTableColumn
mscFrAtmDlciSpMaximumFrameSize = _MscFrAtmDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 1),
    _MscFrAtmDlciSpMaximumFrameSize_Type()
)
mscFrAtmDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpMaximumFrameSize.setStatus("mandatory")


class _MscFrAtmDlciSpRateEnforcement_Type(Integer32):
    """Custom type mscFrAtmDlciSpRateEnforcement based on Integer32"""
    defaultValue = 1

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


_MscFrAtmDlciSpRateEnforcement_Type.__name__ = "Integer32"
_MscFrAtmDlciSpRateEnforcement_Object = MibTableColumn
mscFrAtmDlciSpRateEnforcement = _MscFrAtmDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 2),
    _MscFrAtmDlciSpRateEnforcement_Type()
)
mscFrAtmDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpRateEnforcement.setStatus("mandatory")


class _MscFrAtmDlciSpCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrAtmDlciSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSpCommittedInformationRate_Object = MibTableColumn
mscFrAtmDlciSpCommittedInformationRate = _MscFrAtmDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 3),
    _MscFrAtmDlciSpCommittedInformationRate_Type()
)
mscFrAtmDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpCommittedInformationRate.setStatus("mandatory")


class _MscFrAtmDlciSpCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSpCommittedBurstSize_Object = MibTableColumn
mscFrAtmDlciSpCommittedBurstSize = _MscFrAtmDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 4),
    _MscFrAtmDlciSpCommittedBurstSize_Type()
)
mscFrAtmDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpCommittedBurstSize.setStatus("mandatory")


class _MscFrAtmDlciSpExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciSpExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSpExcessBurstSize_Object = MibTableColumn
mscFrAtmDlciSpExcessBurstSize = _MscFrAtmDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 5),
    _MscFrAtmDlciSpExcessBurstSize_Type()
)
mscFrAtmDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpExcessBurstSize.setStatus("mandatory")


class _MscFrAtmDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrAtmDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscFrAtmDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSpMeasurementInterval_Object = MibTableColumn
mscFrAtmDlciSpMeasurementInterval = _MscFrAtmDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 6),
    _MscFrAtmDlciSpMeasurementInterval_Type()
)
mscFrAtmDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpMeasurementInterval.setStatus("mandatory")


class _MscFrAtmDlciSpEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmDlciSpEmissionPriorityToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 0))
    )


_MscFrAtmDlciSpEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciSpEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmDlciSpEmissionPriorityToIf = _MscFrAtmDlciSpEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 7),
    _MscFrAtmDlciSpEmissionPriorityToIf_Type()
)
mscFrAtmDlciSpEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpEmissionPriorityToIf.setStatus("obsolete")


class _MscFrAtmDlciSpEmissionPrioToIf_Type(Integer32):
    """Custom type mscFrAtmDlciSpEmissionPrioToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MscFrAtmDlciSpEmissionPrioToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciSpEmissionPrioToIf_Object = MibTableColumn
mscFrAtmDlciSpEmissionPrioToIf = _MscFrAtmDlciSpEmissionPrioToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 8),
    _MscFrAtmDlciSpEmissionPrioToIf_Type()
)
mscFrAtmDlciSpEmissionPrioToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpEmissionPrioToIf.setStatus("obsolete")


class _MscFrAtmDlciSpAccounting_Type(Integer32):
    """Custom type mscFrAtmDlciSpAccounting based on Integer32"""
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


_MscFrAtmDlciSpAccounting_Type.__name__ = "Integer32"
_MscFrAtmDlciSpAccounting_Object = MibTableColumn
mscFrAtmDlciSpAccounting = _MscFrAtmDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 2, 10, 1, 9),
    _MscFrAtmDlciSpAccounting_Type()
)
mscFrAtmDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSpAccounting.setStatus("mandatory")
_MscFrAtmDlciSiwf_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwf = _MscFrAtmDlciSiwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3)
)
_MscFrAtmDlciSiwfRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfRowStatusTable = _MscFrAtmDlciSiwfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfRowStatusEntry = _MscFrAtmDlciSiwfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1, 1)
)
mscFrAtmDlciSiwfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfRowStatus = _MscFrAtmDlciSiwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1, 1, 1),
    _MscFrAtmDlciSiwfRowStatus_Type()
)
mscFrAtmDlciSiwfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfComponentName_Type = DisplayString
_MscFrAtmDlciSiwfComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfComponentName = _MscFrAtmDlciSiwfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1, 1, 2),
    _MscFrAtmDlciSiwfComponentName_Type()
)
mscFrAtmDlciSiwfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfStorageType_Type = StorageType
_MscFrAtmDlciSiwfStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfStorageType = _MscFrAtmDlciSiwfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1, 1, 4),
    _MscFrAtmDlciSiwfStorageType_Type()
)
mscFrAtmDlciSiwfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfIndex_Type = NonReplicated
_MscFrAtmDlciSiwfIndex_Object = MibTableColumn
mscFrAtmDlciSiwfIndex = _MscFrAtmDlciSiwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 1, 1, 10),
    _MscFrAtmDlciSiwfIndex_Type()
)
mscFrAtmDlciSiwfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfSd_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwfSd = _MscFrAtmDlciSiwfSd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2)
)
_MscFrAtmDlciSiwfSdRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfSdRowStatusTable = _MscFrAtmDlciSiwfSdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSdRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfSdRowStatusEntry = _MscFrAtmDlciSiwfSdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1, 1)
)
mscFrAtmDlciSiwfSdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfSdIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfSdRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfSdRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfSdRowStatus = _MscFrAtmDlciSiwfSdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1, 1, 1),
    _MscFrAtmDlciSiwfSdRowStatus_Type()
)
mscFrAtmDlciSiwfSdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfSdComponentName_Type = DisplayString
_MscFrAtmDlciSiwfSdComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfSdComponentName = _MscFrAtmDlciSiwfSdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1, 1, 2),
    _MscFrAtmDlciSiwfSdComponentName_Type()
)
mscFrAtmDlciSiwfSdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfSdStorageType_Type = StorageType
_MscFrAtmDlciSiwfSdStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfSdStorageType = _MscFrAtmDlciSiwfSdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1, 1, 4),
    _MscFrAtmDlciSiwfSdStorageType_Type()
)
mscFrAtmDlciSiwfSdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfSdIndex_Type = NonReplicated
_MscFrAtmDlciSiwfSdIndex_Object = MibTableColumn
mscFrAtmDlciSiwfSdIndex = _MscFrAtmDlciSiwfSdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 1, 1, 10),
    _MscFrAtmDlciSiwfSdIndex_Type()
)
mscFrAtmDlciSiwfSdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfSdProvTable_Object = MibTable
mscFrAtmDlciSiwfSdProvTable = _MscFrAtmDlciSiwfSdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdProvTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSdProvEntry_Object = MibTableRow
mscFrAtmDlciSiwfSdProvEntry = _MscFrAtmDlciSiwfSdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1)
)
mscFrAtmDlciSiwfSdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfSdIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdProvEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfSdMode_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfSdMode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sameAsInterface", 255),
          ("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_MscFrAtmDlciSiwfSdMode_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfSdMode_Object = MibTableColumn
mscFrAtmDlciSiwfSdMode = _MscFrAtmDlciSiwfSdMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1, 1),
    _MscFrAtmDlciSiwfSdMode_Type()
)
mscFrAtmDlciSiwfSdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdMode.setStatus("mandatory")


class _MscFrAtmDlciSiwfSdDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfSdDeToClpMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfSdDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfSdDeToClpMapping_Object = MibTableColumn
mscFrAtmDlciSiwfSdDeToClpMapping = _MscFrAtmDlciSiwfSdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1, 2),
    _MscFrAtmDlciSiwfSdDeToClpMapping_Type()
)
mscFrAtmDlciSiwfSdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdDeToClpMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfSdClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfSdClpToDeMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfSdClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfSdClpToDeMapping_Object = MibTableColumn
mscFrAtmDlciSiwfSdClpToDeMapping = _MscFrAtmDlciSiwfSdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1, 3),
    _MscFrAtmDlciSiwfSdClpToDeMapping_Type()
)
mscFrAtmDlciSiwfSdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdClpToDeMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfSdFecnToEfciMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfSdFecnToEfciMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfSdFecnToEfciMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfSdFecnToEfciMapping_Object = MibTableColumn
mscFrAtmDlciSiwfSdFecnToEfciMapping = _MscFrAtmDlciSiwfSdFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1, 4),
    _MscFrAtmDlciSiwfSdFecnToEfciMapping_Type()
)
mscFrAtmDlciSiwfSdFecnToEfciMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdFecnToEfciMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfSdCrToUuMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfSdCrToUuMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfSdCrToUuMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfSdCrToUuMapping_Object = MibTableColumn
mscFrAtmDlciSiwfSdCrToUuMapping = _MscFrAtmDlciSiwfSdCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 2, 10, 1, 5),
    _MscFrAtmDlciSiwfSdCrToUuMapping_Type()
)
mscFrAtmDlciSiwfSdCrToUuMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdCrToUuMapping.setStatus("obsolete")
_MscFrAtmDlciSiwfNPvc_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwfNPvc = _MscFrAtmDlciSiwfNPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3)
)
_MscFrAtmDlciSiwfNPvcRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfNPvcRowStatusTable = _MscFrAtmDlciSiwfNPvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfNPvcRowStatusEntry = _MscFrAtmDlciSiwfNPvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1, 1)
)
mscFrAtmDlciSiwfNPvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfNPvcRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcRowStatus = _MscFrAtmDlciSiwfNPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1, 1, 1),
    _MscFrAtmDlciSiwfNPvcRowStatus_Type()
)
mscFrAtmDlciSiwfNPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcComponentName_Type = DisplayString
_MscFrAtmDlciSiwfNPvcComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcComponentName = _MscFrAtmDlciSiwfNPvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1, 1, 2),
    _MscFrAtmDlciSiwfNPvcComponentName_Type()
)
mscFrAtmDlciSiwfNPvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcStorageType_Type = StorageType
_MscFrAtmDlciSiwfNPvcStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcStorageType = _MscFrAtmDlciSiwfNPvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1, 1, 4),
    _MscFrAtmDlciSiwfNPvcStorageType_Type()
)
mscFrAtmDlciSiwfNPvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcIndex_Type = NonReplicated
_MscFrAtmDlciSiwfNPvcIndex_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcIndex = _MscFrAtmDlciSiwfNPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 1, 1, 10),
    _MscFrAtmDlciSiwfNPvcIndex_Type()
)
mscFrAtmDlciSiwfNPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcProvTable_Object = MibTable
mscFrAtmDlciSiwfNPvcProvTable = _MscFrAtmDlciSiwfNPvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcProvTable.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcProvEntry_Object = MibTableRow
mscFrAtmDlciSiwfNPvcProvEntry = _MscFrAtmDlciSiwfNPvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 10, 1)
)
mscFrAtmDlciSiwfNPvcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcProvEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcAtmConnection_Type = Link
_MscFrAtmDlciSiwfNPvcAtmConnection_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcAtmConnection = _MscFrAtmDlciSiwfNPvcAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 10, 1, 1),
    _MscFrAtmDlciSiwfNPvcAtmConnection_Type()
)
mscFrAtmDlciSiwfNPvcAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcAtmConnection.setStatus("mandatory")


class _MscFrAtmDlciSiwfNPvcCorrelationTag_Type(HexString):
    """Custom type mscFrAtmDlciSiwfNPvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_MscFrAtmDlciSiwfNPvcCorrelationTag_Type.__name__ = "HexString"
_MscFrAtmDlciSiwfNPvcCorrelationTag_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcCorrelationTag = _MscFrAtmDlciSiwfNPvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 10, 1, 3),
    _MscFrAtmDlciSiwfNPvcCorrelationTag_Type()
)
mscFrAtmDlciSiwfNPvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcCorrelationTag.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcSiwfNpvcOpTable_Object = MibTable
mscFrAtmDlciSiwfNPvcSiwfNpvcOpTable = _MscFrAtmDlciSiwfNPvcSiwfNpvcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcSiwfNpvcOpTable.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry_Object = MibTableRow
mscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry = _MscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 11, 1)
)
mscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfNPvcConnectionToAtm_Type = RowPointer
_MscFrAtmDlciSiwfNPvcConnectionToAtm_Object = MibTableColumn
mscFrAtmDlciSiwfNPvcConnectionToAtm = _MscFrAtmDlciSiwfNPvcConnectionToAtm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 3, 11, 1, 1),
    _MscFrAtmDlciSiwfNPvcConnectionToAtm_Type()
)
mscFrAtmDlciSiwfNPvcConnectionToAtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfNPvcConnectionToAtm.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvc_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwfSPvc = _MscFrAtmDlciSiwfSPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4)
)
_MscFrAtmDlciSiwfSPvcRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfSPvcRowStatusTable = _MscFrAtmDlciSiwfSPvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfSPvcRowStatusEntry = _MscFrAtmDlciSiwfSPvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1, 1)
)
mscFrAtmDlciSiwfSPvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfSPvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfSPvcRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcRowStatus = _MscFrAtmDlciSiwfSPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1, 1, 1),
    _MscFrAtmDlciSiwfSPvcRowStatus_Type()
)
mscFrAtmDlciSiwfSPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcComponentName_Type = DisplayString
_MscFrAtmDlciSiwfSPvcComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcComponentName = _MscFrAtmDlciSiwfSPvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1, 1, 2),
    _MscFrAtmDlciSiwfSPvcComponentName_Type()
)
mscFrAtmDlciSiwfSPvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcStorageType_Type = StorageType
_MscFrAtmDlciSiwfSPvcStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcStorageType = _MscFrAtmDlciSiwfSPvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1, 1, 4),
    _MscFrAtmDlciSiwfSPvcStorageType_Type()
)
mscFrAtmDlciSiwfSPvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcIndex_Type = NonReplicated
_MscFrAtmDlciSiwfSPvcIndex_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcIndex = _MscFrAtmDlciSiwfSPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 1, 1, 10),
    _MscFrAtmDlciSiwfSPvcIndex_Type()
)
mscFrAtmDlciSiwfSPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcProvTable_Object = MibTable
mscFrAtmDlciSiwfSPvcProvTable = _MscFrAtmDlciSiwfSPvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcProvTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSPvcProvEntry_Object = MibTableRow
mscFrAtmDlciSiwfSPvcProvEntry = _MscFrAtmDlciSiwfSPvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 10, 1)
)
mscFrAtmDlciSiwfSPvcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfSPvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcProvEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfSPvcRemoteAddress_Type(AsciiString):
    """Custom type mscFrAtmDlciSiwfSPvcRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscFrAtmDlciSiwfSPvcRemoteAddress_Type.__name__ = "AsciiString"
_MscFrAtmDlciSiwfSPvcRemoteAddress_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcRemoteAddress = _MscFrAtmDlciSiwfSPvcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 10, 1, 2),
    _MscFrAtmDlciSiwfSPvcRemoteAddress_Type()
)
mscFrAtmDlciSiwfSPvcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcRemoteAddress.setStatus("mandatory")


class _MscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_MscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_MscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier = _MscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 10, 1, 3),
    _MscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type()
)
mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier.setStatus("mandatory")


class _MscFrAtmDlciSiwfSPvcCorrelationTag_Type(HexString):
    """Custom type mscFrAtmDlciSiwfSPvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_MscFrAtmDlciSiwfSPvcCorrelationTag_Type.__name__ = "HexString"
_MscFrAtmDlciSiwfSPvcCorrelationTag_Object = MibTableColumn
mscFrAtmDlciSiwfSPvcCorrelationTag = _MscFrAtmDlciSiwfSPvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 4, 10, 1, 4),
    _MscFrAtmDlciSiwfSPvcCorrelationTag_Type()
)
mscFrAtmDlciSiwfSPvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSPvcCorrelationTag.setStatus("mandatory")
_MscFrAtmDlciSiwfQoS_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwfQoS = _MscFrAtmDlciSiwfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5)
)
_MscFrAtmDlciSiwfQoSRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfQoSRowStatusTable = _MscFrAtmDlciSiwfQoSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfQoSRowStatusEntry = _MscFrAtmDlciSiwfQoSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1, 1)
)
mscFrAtmDlciSiwfQoSRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfQoSRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfQoSRowStatus = _MscFrAtmDlciSiwfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1, 1, 1),
    _MscFrAtmDlciSiwfQoSRowStatus_Type()
)
mscFrAtmDlciSiwfQoSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSComponentName_Type = DisplayString
_MscFrAtmDlciSiwfQoSComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfQoSComponentName = _MscFrAtmDlciSiwfQoSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1, 1, 2),
    _MscFrAtmDlciSiwfQoSComponentName_Type()
)
mscFrAtmDlciSiwfQoSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSStorageType_Type = StorageType
_MscFrAtmDlciSiwfQoSStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfQoSStorageType = _MscFrAtmDlciSiwfQoSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1, 1, 4),
    _MscFrAtmDlciSiwfQoSStorageType_Type()
)
mscFrAtmDlciSiwfQoSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSIndex_Type = NonReplicated
_MscFrAtmDlciSiwfQoSIndex_Object = MibTableColumn
mscFrAtmDlciSiwfQoSIndex = _MscFrAtmDlciSiwfQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 1, 1, 10),
    _MscFrAtmDlciSiwfQoSIndex_Type()
)
mscFrAtmDlciSiwfQoSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSProvTable_Object = MibTable
mscFrAtmDlciSiwfQoSProvTable = _MscFrAtmDlciSiwfQoSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSProvTable.setStatus("mandatory")
_MscFrAtmDlciSiwfQoSProvEntry_Object = MibTableRow
mscFrAtmDlciSiwfQoSProvEntry = _MscFrAtmDlciSiwfQoSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 10, 1)
)
mscFrAtmDlciSiwfQoSProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSProvEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfQoSEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfQoSEmissionPriorityToIf based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfQoSEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfQoSEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmDlciSiwfQoSEmissionPriorityToIf = _MscFrAtmDlciSiwfQoSEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 10, 1, 1),
    _MscFrAtmDlciSiwfQoSEmissionPriorityToIf_Type()
)
mscFrAtmDlciSiwfQoSEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSEmissionPriorityToIf.setStatus("mandatory")


class _MscFrAtmDlciSiwfQoSTransferPriority_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfQoSTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciSiwfQoSTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfQoSTransferPriority_Object = MibTableColumn
mscFrAtmDlciSiwfQoSTransferPriority = _MscFrAtmDlciSiwfQoSTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 5, 10, 1, 2),
    _MscFrAtmDlciSiwfQoSTransferPriority_Type()
)
mscFrAtmDlciSiwfQoSTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfQoSTransferPriority.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmCon_ObjectIdentity = ObjectIdentity
mscFrAtmDlciSiwfAtmCon = _MscFrAtmDlciSiwfAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6)
)
_MscFrAtmDlciSiwfAtmConRowStatusTable_Object = MibTable
mscFrAtmDlciSiwfAtmConRowStatusTable = _MscFrAtmDlciSiwfAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConRowStatusEntry_Object = MibTableRow
mscFrAtmDlciSiwfAtmConRowStatusEntry = _MscFrAtmDlciSiwfAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1, 1)
)
mscFrAtmDlciSiwfAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConRowStatus_Type = RowStatus
_MscFrAtmDlciSiwfAtmConRowStatus_Object = MibTableColumn
mscFrAtmDlciSiwfAtmConRowStatus = _MscFrAtmDlciSiwfAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1, 1, 1),
    _MscFrAtmDlciSiwfAtmConRowStatus_Type()
)
mscFrAtmDlciSiwfAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConRowStatus.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConComponentName_Type = DisplayString
_MscFrAtmDlciSiwfAtmConComponentName_Object = MibTableColumn
mscFrAtmDlciSiwfAtmConComponentName = _MscFrAtmDlciSiwfAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1, 1, 2),
    _MscFrAtmDlciSiwfAtmConComponentName_Type()
)
mscFrAtmDlciSiwfAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConComponentName.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConStorageType_Type = StorageType
_MscFrAtmDlciSiwfAtmConStorageType_Object = MibTableColumn
mscFrAtmDlciSiwfAtmConStorageType = _MscFrAtmDlciSiwfAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1, 1, 4),
    _MscFrAtmDlciSiwfAtmConStorageType_Type()
)
mscFrAtmDlciSiwfAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConStorageType.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConIndex_Type = NonReplicated
_MscFrAtmDlciSiwfAtmConIndex_Object = MibTableColumn
mscFrAtmDlciSiwfAtmConIndex = _MscFrAtmDlciSiwfAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 1, 1, 10),
    _MscFrAtmDlciSiwfAtmConIndex_Type()
)
mscFrAtmDlciSiwfAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConIndex.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConOperTable_Object = MibTable
mscFrAtmDlciSiwfAtmConOperTable = _MscFrAtmDlciSiwfAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConOperTable.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConOperEntry_Object = MibTableRow
mscFrAtmDlciSiwfAtmConOperEntry = _MscFrAtmDlciSiwfAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 10, 1)
)
mscFrAtmDlciSiwfAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConOperEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfAtmConNextHop_Type = RowPointer
_MscFrAtmDlciSiwfAtmConNextHop_Object = MibTableColumn
mscFrAtmDlciSiwfAtmConNextHop = _MscFrAtmDlciSiwfAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 6, 10, 1, 1),
    _MscFrAtmDlciSiwfAtmConNextHop_Type()
)
mscFrAtmDlciSiwfAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmConNextHop.setStatus("mandatory")
_MscFrAtmDlciSiwfConnOpTable_Object = MibTable
mscFrAtmDlciSiwfConnOpTable = _MscFrAtmDlciSiwfConnOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfConnOpTable.setStatus("mandatory")
_MscFrAtmDlciSiwfConnOpEntry_Object = MibTableRow
mscFrAtmDlciSiwfConnOpEntry = _MscFrAtmDlciSiwfConnOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1)
)
mscFrAtmDlciSiwfConnOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfConnOpEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfDiscardPriority_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_MscFrAtmDlciSiwfDiscardPriority_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfDiscardPriority_Object = MibTableColumn
mscFrAtmDlciSiwfDiscardPriority = _MscFrAtmDlciSiwfDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 2),
    _MscFrAtmDlciSiwfDiscardPriority_Type()
)
mscFrAtmDlciSiwfDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfDiscardPriority.setStatus("mandatory")


class _MscFrAtmDlciSiwfAtmServiceCategory_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfAtmServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("notApplicable", 5),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 0))
    )


_MscFrAtmDlciSiwfAtmServiceCategory_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfAtmServiceCategory_Object = MibTableColumn
mscFrAtmDlciSiwfAtmServiceCategory = _MscFrAtmDlciSiwfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 4),
    _MscFrAtmDlciSiwfAtmServiceCategory_Type()
)
mscFrAtmDlciSiwfAtmServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAtmServiceCategory.setStatus("mandatory")


class _MscFrAtmDlciSiwfTrafficParmConvPolicy_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfTrafficParmConvPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("notApplicable", 7))
    )


_MscFrAtmDlciSiwfTrafficParmConvPolicy_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfTrafficParmConvPolicy_Object = MibTableColumn
mscFrAtmDlciSiwfTrafficParmConvPolicy = _MscFrAtmDlciSiwfTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 5),
    _MscFrAtmDlciSiwfTrafficParmConvPolicy_Type()
)
mscFrAtmDlciSiwfTrafficParmConvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfTrafficParmConvPolicy.setStatus("mandatory")


class _MscFrAtmDlciSiwfAvgFrameSize_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfAvgFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_MscFrAtmDlciSiwfAvgFrameSize_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfAvgFrameSize_Object = MibTableColumn
mscFrAtmDlciSiwfAvgFrameSize = _MscFrAtmDlciSiwfAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 6),
    _MscFrAtmDlciSiwfAvgFrameSize_Type()
)
mscFrAtmDlciSiwfAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAvgFrameSize.setStatus("mandatory")


class _MscFrAtmDlciSiwfRemoteAddress_Type(AsciiString):
    """Custom type mscFrAtmDlciSiwfRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscFrAtmDlciSiwfRemoteAddress_Type.__name__ = "AsciiString"
_MscFrAtmDlciSiwfRemoteAddress_Object = MibTableColumn
mscFrAtmDlciSiwfRemoteAddress = _MscFrAtmDlciSiwfRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 8),
    _MscFrAtmDlciSiwfRemoteAddress_Type()
)
mscFrAtmDlciSiwfRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfRemoteAddress.setStatus("mandatory")


class _MscFrAtmDlciSiwfRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type mscFrAtmDlciSiwfRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_MscFrAtmDlciSiwfRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_MscFrAtmDlciSiwfRemoteConnectionIdentifier_Object = MibTableColumn
mscFrAtmDlciSiwfRemoteConnectionIdentifier = _MscFrAtmDlciSiwfRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 11, 1, 9),
    _MscFrAtmDlciSiwfRemoteConnectionIdentifier_Type()
)
mscFrAtmDlciSiwfRemoteConnectionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfRemoteConnectionIdentifier.setStatus("mandatory")
_MscFrAtmDlciSiwfSdOpTable_Object = MibTable
mscFrAtmDlciSiwfSdOpTable = _MscFrAtmDlciSiwfSdOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdOpTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSdOpEntry_Object = MibTableRow
mscFrAtmDlciSiwfSdOpEntry = _MscFrAtmDlciSiwfSdOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1)
)
mscFrAtmDlciSiwfSdOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSdOpEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfMode_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_MscFrAtmDlciSiwfMode_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfMode_Object = MibTableColumn
mscFrAtmDlciSiwfMode = _MscFrAtmDlciSiwfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 1),
    _MscFrAtmDlciSiwfMode_Type()
)
mscFrAtmDlciSiwfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfMode.setStatus("mandatory")


class _MscFrAtmDlciSiwfDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfDeToClpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmDlciSiwfDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfDeToClpMapping_Object = MibTableColumn
mscFrAtmDlciSiwfDeToClpMapping = _MscFrAtmDlciSiwfDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 2),
    _MscFrAtmDlciSiwfDeToClpMapping_Type()
)
mscFrAtmDlciSiwfDeToClpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfDeToClpMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfClpToDeMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmDlciSiwfClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfClpToDeMapping_Object = MibTableColumn
mscFrAtmDlciSiwfClpToDeMapping = _MscFrAtmDlciSiwfClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 3),
    _MscFrAtmDlciSiwfClpToDeMapping_Type()
)
mscFrAtmDlciSiwfClpToDeMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfClpToDeMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfFecnToEfciMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfFecnToEfciMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_MscFrAtmDlciSiwfFecnToEfciMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfFecnToEfciMapping_Object = MibTableColumn
mscFrAtmDlciSiwfFecnToEfciMapping = _MscFrAtmDlciSiwfFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 4),
    _MscFrAtmDlciSiwfFecnToEfciMapping_Type()
)
mscFrAtmDlciSiwfFecnToEfciMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfFecnToEfciMapping.setStatus("mandatory")


class _MscFrAtmDlciSiwfCrToUuMapping_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfCrToUuMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_MscFrAtmDlciSiwfCrToUuMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfCrToUuMapping_Object = MibTableColumn
mscFrAtmDlciSiwfCrToUuMapping = _MscFrAtmDlciSiwfCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 5),
    _MscFrAtmDlciSiwfCrToUuMapping_Type()
)
mscFrAtmDlciSiwfCrToUuMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfCrToUuMapping.setStatus("obsolete")


class _MscFrAtmDlciSiwfTransferPriority_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfTransferPriority based on Integer32"""
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
              253)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("notApplicable", 253))
    )


_MscFrAtmDlciSiwfTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfTransferPriority_Object = MibTableColumn
mscFrAtmDlciSiwfTransferPriority = _MscFrAtmDlciSiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 6),
    _MscFrAtmDlciSiwfTransferPriority_Type()
)
mscFrAtmDlciSiwfTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfTransferPriority.setStatus("mandatory")


class _MscFrAtmDlciSiwfAssignedBandwidthPool_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfAssignedBandwidthPool based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_MscFrAtmDlciSiwfAssignedBandwidthPool_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfAssignedBandwidthPool_Object = MibTableColumn
mscFrAtmDlciSiwfAssignedBandwidthPool = _MscFrAtmDlciSiwfAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 12, 1, 7),
    _MscFrAtmDlciSiwfAssignedBandwidthPool_Type()
)
mscFrAtmDlciSiwfAssignedBandwidthPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfAssignedBandwidthPool.setStatus("mandatory")
_MscFrAtmDlciSiwfSiwfSpvcOpTable_Object = MibTable
mscFrAtmDlciSiwfSiwfSpvcOpTable = _MscFrAtmDlciSiwfSiwfSpvcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSiwfSpvcOpTable.setStatus("mandatory")
_MscFrAtmDlciSiwfSiwfSpvcOpEntry_Object = MibTableRow
mscFrAtmDlciSiwfSiwfSpvcOpEntry = _MscFrAtmDlciSiwfSiwfSpvcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1)
)
mscFrAtmDlciSiwfSiwfSpvcOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSiwfSpvcOpEntry.setStatus("mandatory")


class _MscFrAtmDlciSiwfPeakCellRate0_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfPeakCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfPeakCellRate0_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfPeakCellRate0_Object = MibTableColumn
mscFrAtmDlciSiwfPeakCellRate0 = _MscFrAtmDlciSiwfPeakCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 1),
    _MscFrAtmDlciSiwfPeakCellRate0_Type()
)
mscFrAtmDlciSiwfPeakCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfPeakCellRate0.setStatus("mandatory")


class _MscFrAtmDlciSiwfPeakCellRate01_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfPeakCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfPeakCellRate01_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfPeakCellRate01_Object = MibTableColumn
mscFrAtmDlciSiwfPeakCellRate01 = _MscFrAtmDlciSiwfPeakCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 2),
    _MscFrAtmDlciSiwfPeakCellRate01_Type()
)
mscFrAtmDlciSiwfPeakCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfPeakCellRate01.setStatus("mandatory")


class _MscFrAtmDlciSiwfSustainedCellRate0_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfSustainedCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfSustainedCellRate0_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfSustainedCellRate0_Object = MibTableColumn
mscFrAtmDlciSiwfSustainedCellRate0 = _MscFrAtmDlciSiwfSustainedCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 3),
    _MscFrAtmDlciSiwfSustainedCellRate0_Type()
)
mscFrAtmDlciSiwfSustainedCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSustainedCellRate0.setStatus("mandatory")


class _MscFrAtmDlciSiwfSustainedCellRate01_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfSustainedCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfSustainedCellRate01_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfSustainedCellRate01_Object = MibTableColumn
mscFrAtmDlciSiwfSustainedCellRate01 = _MscFrAtmDlciSiwfSustainedCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 4),
    _MscFrAtmDlciSiwfSustainedCellRate01_Type()
)
mscFrAtmDlciSiwfSustainedCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfSustainedCellRate01.setStatus("mandatory")


class _MscFrAtmDlciSiwfMaximumBurstSize0_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfMaximumBurstSize0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfMaximumBurstSize0_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfMaximumBurstSize0_Object = MibTableColumn
mscFrAtmDlciSiwfMaximumBurstSize0 = _MscFrAtmDlciSiwfMaximumBurstSize0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 5),
    _MscFrAtmDlciSiwfMaximumBurstSize0_Type()
)
mscFrAtmDlciSiwfMaximumBurstSize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfMaximumBurstSize0.setStatus("mandatory")


class _MscFrAtmDlciSiwfMaximumBurstSize01_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfMaximumBurstSize01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfMaximumBurstSize01_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfMaximumBurstSize01_Object = MibTableColumn
mscFrAtmDlciSiwfMaximumBurstSize01 = _MscFrAtmDlciSiwfMaximumBurstSize01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 6),
    _MscFrAtmDlciSiwfMaximumBurstSize01_Type()
)
mscFrAtmDlciSiwfMaximumBurstSize01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfMaximumBurstSize01.setStatus("mandatory")


class _MscFrAtmDlciSiwfEquivalentBitRate_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfEquivalentBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciSiwfEquivalentBitRate_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfEquivalentBitRate_Object = MibTableColumn
mscFrAtmDlciSiwfEquivalentBitRate = _MscFrAtmDlciSiwfEquivalentBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 7),
    _MscFrAtmDlciSiwfEquivalentBitRate_Type()
)
mscFrAtmDlciSiwfEquivalentBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfEquivalentBitRate.setStatus("mandatory")


class _MscFrAtmDlciSiwfType_Type(Integer32):
    """Custom type mscFrAtmDlciSiwfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_MscFrAtmDlciSiwfType_Type.__name__ = "Integer32"
_MscFrAtmDlciSiwfType_Object = MibTableColumn
mscFrAtmDlciSiwfType = _MscFrAtmDlciSiwfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 9),
    _MscFrAtmDlciSiwfType_Type()
)
mscFrAtmDlciSiwfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfType.setStatus("mandatory")


class _MscFrAtmDlciSiwfVccClearCause_Type(Unsigned32):
    """Custom type mscFrAtmDlciSiwfVccClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrAtmDlciSiwfVccClearCause_Type.__name__ = "Unsigned32"
_MscFrAtmDlciSiwfVccClearCause_Object = MibTableColumn
mscFrAtmDlciSiwfVccClearCause = _MscFrAtmDlciSiwfVccClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 10),
    _MscFrAtmDlciSiwfVccClearCause_Type()
)
mscFrAtmDlciSiwfVccClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfVccClearCause.setStatus("mandatory")


class _MscFrAtmDlciSiwfVccCauseDiag_Type(HexString):
    """Custom type mscFrAtmDlciSiwfVccCauseDiag based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscFrAtmDlciSiwfVccCauseDiag_Type.__name__ = "HexString"
_MscFrAtmDlciSiwfVccCauseDiag_Object = MibTableColumn
mscFrAtmDlciSiwfVccCauseDiag = _MscFrAtmDlciSiwfVccCauseDiag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 13, 1, 15),
    _MscFrAtmDlciSiwfVccCauseDiag_Type()
)
mscFrAtmDlciSiwfVccCauseDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfVccCauseDiag.setStatus("mandatory")
_MscFrAtmDlciSiwfStatsTable_Object = MibTable
mscFrAtmDlciSiwfStatsTable = _MscFrAtmDlciSiwfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfStatsTable.setStatus("mandatory")
_MscFrAtmDlciSiwfStatsEntry_Object = MibTableRow
mscFrAtmDlciSiwfStatsEntry = _MscFrAtmDlciSiwfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1)
)
mscFrAtmDlciSiwfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfStatsEntry.setStatus("mandatory")
_MscFrAtmDlciSiwfUnknown1490Frames_Type = Counter32
_MscFrAtmDlciSiwfUnknown1490Frames_Object = MibTableColumn
mscFrAtmDlciSiwfUnknown1490Frames = _MscFrAtmDlciSiwfUnknown1490Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 1),
    _MscFrAtmDlciSiwfUnknown1490Frames_Type()
)
mscFrAtmDlciSiwfUnknown1490Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfUnknown1490Frames.setStatus("mandatory")
_MscFrAtmDlciSiwfInvalid1490Frames_Type = Counter32
_MscFrAtmDlciSiwfInvalid1490Frames_Object = MibTableColumn
mscFrAtmDlciSiwfInvalid1490Frames = _MscFrAtmDlciSiwfInvalid1490Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 2),
    _MscFrAtmDlciSiwfInvalid1490Frames_Type()
)
mscFrAtmDlciSiwfInvalid1490Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfInvalid1490Frames.setStatus("mandatory")


class _MscFrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type(HexString):
    """Custom type mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscFrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type.__name__ = "HexString"
_MscFrAtmDlciSiwfLastUnknown1490ProtocolHeader_Object = MibTableColumn
mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader = _MscFrAtmDlciSiwfLastUnknown1490ProtocolHeader_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 3),
    _MscFrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type()
)
mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader.setStatus("mandatory")
_MscFrAtmDlciSiwfUnknown1483Frames_Type = Counter32
_MscFrAtmDlciSiwfUnknown1483Frames_Object = MibTableColumn
mscFrAtmDlciSiwfUnknown1483Frames = _MscFrAtmDlciSiwfUnknown1483Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 4),
    _MscFrAtmDlciSiwfUnknown1483Frames_Type()
)
mscFrAtmDlciSiwfUnknown1483Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfUnknown1483Frames.setStatus("mandatory")
_MscFrAtmDlciSiwfInvalid1483Frames_Type = Counter32
_MscFrAtmDlciSiwfInvalid1483Frames_Object = MibTableColumn
mscFrAtmDlciSiwfInvalid1483Frames = _MscFrAtmDlciSiwfInvalid1483Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 5),
    _MscFrAtmDlciSiwfInvalid1483Frames_Type()
)
mscFrAtmDlciSiwfInvalid1483Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfInvalid1483Frames.setStatus("mandatory")


class _MscFrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type(HexString):
    """Custom type mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscFrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type.__name__ = "HexString"
_MscFrAtmDlciSiwfLastUnknown1483ProtocolHeader_Object = MibTableColumn
mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader = _MscFrAtmDlciSiwfLastUnknown1483ProtocolHeader_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 3, 14, 1, 6),
    _MscFrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type()
)
mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader.setStatus("mandatory")
_MscFrAtmDlciNiwf_ObjectIdentity = ObjectIdentity
mscFrAtmDlciNiwf = _MscFrAtmDlciNiwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4)
)
_MscFrAtmDlciNiwfRowStatusTable_Object = MibTable
mscFrAtmDlciNiwfRowStatusTable = _MscFrAtmDlciNiwfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciNiwfRowStatusEntry_Object = MibTableRow
mscFrAtmDlciNiwfRowStatusEntry = _MscFrAtmDlciNiwfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1, 1)
)
mscFrAtmDlciNiwfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciNiwfRowStatus_Type = RowStatus
_MscFrAtmDlciNiwfRowStatus_Object = MibTableColumn
mscFrAtmDlciNiwfRowStatus = _MscFrAtmDlciNiwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1, 1, 1),
    _MscFrAtmDlciNiwfRowStatus_Type()
)
mscFrAtmDlciNiwfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfRowStatus.setStatus("mandatory")
_MscFrAtmDlciNiwfComponentName_Type = DisplayString
_MscFrAtmDlciNiwfComponentName_Object = MibTableColumn
mscFrAtmDlciNiwfComponentName = _MscFrAtmDlciNiwfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1, 1, 2),
    _MscFrAtmDlciNiwfComponentName_Type()
)
mscFrAtmDlciNiwfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfComponentName.setStatus("mandatory")
_MscFrAtmDlciNiwfStorageType_Type = StorageType
_MscFrAtmDlciNiwfStorageType_Object = MibTableColumn
mscFrAtmDlciNiwfStorageType = _MscFrAtmDlciNiwfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1, 1, 4),
    _MscFrAtmDlciNiwfStorageType_Type()
)
mscFrAtmDlciNiwfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfStorageType.setStatus("mandatory")
_MscFrAtmDlciNiwfIndex_Type = NonReplicated
_MscFrAtmDlciNiwfIndex_Object = MibTableColumn
mscFrAtmDlciNiwfIndex = _MscFrAtmDlciNiwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 1, 1, 10),
    _MscFrAtmDlciNiwfIndex_Type()
)
mscFrAtmDlciNiwfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfIndex.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvc_ObjectIdentity = ObjectIdentity
mscFrAtmDlciNiwfSpvc = _MscFrAtmDlciNiwfSpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2)
)
_MscFrAtmDlciNiwfSpvcRowStatusTable_Object = MibTable
mscFrAtmDlciNiwfSpvcRowStatusTable = _MscFrAtmDlciNiwfSpvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcRowStatusEntry_Object = MibTableRow
mscFrAtmDlciNiwfSpvcRowStatusEntry = _MscFrAtmDlciNiwfSpvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1, 1)
)
mscFrAtmDlciNiwfSpvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfSpvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcRowStatus_Type = RowStatus
_MscFrAtmDlciNiwfSpvcRowStatus_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcRowStatus = _MscFrAtmDlciNiwfSpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1, 1, 1),
    _MscFrAtmDlciNiwfSpvcRowStatus_Type()
)
mscFrAtmDlciNiwfSpvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcRowStatus.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcComponentName_Type = DisplayString
_MscFrAtmDlciNiwfSpvcComponentName_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcComponentName = _MscFrAtmDlciNiwfSpvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1, 1, 2),
    _MscFrAtmDlciNiwfSpvcComponentName_Type()
)
mscFrAtmDlciNiwfSpvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcComponentName.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcStorageType_Type = StorageType
_MscFrAtmDlciNiwfSpvcStorageType_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcStorageType = _MscFrAtmDlciNiwfSpvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1, 1, 4),
    _MscFrAtmDlciNiwfSpvcStorageType_Type()
)
mscFrAtmDlciNiwfSpvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcStorageType.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcIndex_Type = NonReplicated
_MscFrAtmDlciNiwfSpvcIndex_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcIndex = _MscFrAtmDlciNiwfSpvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 1, 1, 10),
    _MscFrAtmDlciNiwfSpvcIndex_Type()
)
mscFrAtmDlciNiwfSpvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcIndex.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcProvTable_Object = MibTable
mscFrAtmDlciNiwfSpvcProvTable = _MscFrAtmDlciNiwfSpvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcProvTable.setStatus("mandatory")
_MscFrAtmDlciNiwfSpvcProvEntry_Object = MibTableRow
mscFrAtmDlciNiwfSpvcProvEntry = _MscFrAtmDlciNiwfSpvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 10, 1)
)
mscFrAtmDlciNiwfSpvcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfSpvcIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcProvEntry.setStatus("mandatory")


class _MscFrAtmDlciNiwfSpvcRemoteAddress_Type(AsciiString):
    """Custom type mscFrAtmDlciNiwfSpvcRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscFrAtmDlciNiwfSpvcRemoteAddress_Type.__name__ = "AsciiString"
_MscFrAtmDlciNiwfSpvcRemoteAddress_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcRemoteAddress = _MscFrAtmDlciNiwfSpvcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 10, 1, 1),
    _MscFrAtmDlciNiwfSpvcRemoteAddress_Type()
)
mscFrAtmDlciNiwfSpvcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcRemoteAddress.setStatus("mandatory")


class _MscFrAtmDlciNiwfSpvcRemoteDlci_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfSpvcRemoteDlci based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
        ValueRangeConstraint(1022, 1022),
    )


_MscFrAtmDlciNiwfSpvcRemoteDlci_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfSpvcRemoteDlci_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcRemoteDlci = _MscFrAtmDlciNiwfSpvcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 10, 1, 2),
    _MscFrAtmDlciNiwfSpvcRemoteDlci_Type()
)
mscFrAtmDlciNiwfSpvcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcRemoteDlci.setStatus("mandatory")


class _MscFrAtmDlciNiwfSpvcCorrelationTag_Type(HexString):
    """Custom type mscFrAtmDlciNiwfSpvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_MscFrAtmDlciNiwfSpvcCorrelationTag_Type.__name__ = "HexString"
_MscFrAtmDlciNiwfSpvcCorrelationTag_Object = MibTableColumn
mscFrAtmDlciNiwfSpvcCorrelationTag = _MscFrAtmDlciNiwfSpvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 2, 10, 1, 3),
    _MscFrAtmDlciNiwfSpvcCorrelationTag_Type()
)
mscFrAtmDlciNiwfSpvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfSpvcCorrelationTag.setStatus("mandatory")
_MscFrAtmDlciNiwfNd_ObjectIdentity = ObjectIdentity
mscFrAtmDlciNiwfNd = _MscFrAtmDlciNiwfNd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3)
)
_MscFrAtmDlciNiwfNdRowStatusTable_Object = MibTable
mscFrAtmDlciNiwfNdRowStatusTable = _MscFrAtmDlciNiwfNdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciNiwfNdRowStatusEntry_Object = MibTableRow
mscFrAtmDlciNiwfNdRowStatusEntry = _MscFrAtmDlciNiwfNdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1, 1)
)
mscFrAtmDlciNiwfNdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfNdIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciNiwfNdRowStatus_Type = RowStatus
_MscFrAtmDlciNiwfNdRowStatus_Object = MibTableColumn
mscFrAtmDlciNiwfNdRowStatus = _MscFrAtmDlciNiwfNdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1, 1, 1),
    _MscFrAtmDlciNiwfNdRowStatus_Type()
)
mscFrAtmDlciNiwfNdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdRowStatus.setStatus("mandatory")
_MscFrAtmDlciNiwfNdComponentName_Type = DisplayString
_MscFrAtmDlciNiwfNdComponentName_Object = MibTableColumn
mscFrAtmDlciNiwfNdComponentName = _MscFrAtmDlciNiwfNdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1, 1, 2),
    _MscFrAtmDlciNiwfNdComponentName_Type()
)
mscFrAtmDlciNiwfNdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdComponentName.setStatus("mandatory")
_MscFrAtmDlciNiwfNdStorageType_Type = StorageType
_MscFrAtmDlciNiwfNdStorageType_Object = MibTableColumn
mscFrAtmDlciNiwfNdStorageType = _MscFrAtmDlciNiwfNdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1, 1, 4),
    _MscFrAtmDlciNiwfNdStorageType_Type()
)
mscFrAtmDlciNiwfNdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdStorageType.setStatus("mandatory")
_MscFrAtmDlciNiwfNdIndex_Type = NonReplicated
_MscFrAtmDlciNiwfNdIndex_Object = MibTableColumn
mscFrAtmDlciNiwfNdIndex = _MscFrAtmDlciNiwfNdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 1, 1, 10),
    _MscFrAtmDlciNiwfNdIndex_Type()
)
mscFrAtmDlciNiwfNdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdIndex.setStatus("mandatory")
_MscFrAtmDlciNiwfNdProvTable_Object = MibTable
mscFrAtmDlciNiwfNdProvTable = _MscFrAtmDlciNiwfNdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdProvTable.setStatus("mandatory")
_MscFrAtmDlciNiwfNdProvEntry_Object = MibTableRow
mscFrAtmDlciNiwfNdProvEntry = _MscFrAtmDlciNiwfNdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 10, 1)
)
mscFrAtmDlciNiwfNdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfNdIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdProvEntry.setStatus("mandatory")


class _MscFrAtmDlciNiwfNdDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfNdDeToClpMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciNiwfNdDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfNdDeToClpMapping_Object = MibTableColumn
mscFrAtmDlciNiwfNdDeToClpMapping = _MscFrAtmDlciNiwfNdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 10, 1, 1),
    _MscFrAtmDlciNiwfNdDeToClpMapping_Type()
)
mscFrAtmDlciNiwfNdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdDeToClpMapping.setStatus("mandatory")


class _MscFrAtmDlciNiwfNdClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfNdClpToDeMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("sameAsInterface", 255),
          ("transparent", 3))
    )


_MscFrAtmDlciNiwfNdClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfNdClpToDeMapping_Object = MibTableColumn
mscFrAtmDlciNiwfNdClpToDeMapping = _MscFrAtmDlciNiwfNdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 10, 1, 2),
    _MscFrAtmDlciNiwfNdClpToDeMapping_Type()
)
mscFrAtmDlciNiwfNdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdClpToDeMapping.setStatus("mandatory")


class _MscFrAtmDlciNiwfNdTransferPriority_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfNdTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciNiwfNdTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfNdTransferPriority_Object = MibTableColumn
mscFrAtmDlciNiwfNdTransferPriority = _MscFrAtmDlciNiwfNdTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 3, 10, 1, 3),
    _MscFrAtmDlciNiwfNdTransferPriority_Type()
)
mscFrAtmDlciNiwfNdTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfNdTransferPriority.setStatus("obsolete")
_MscFrAtmDlciNiwfQoS_ObjectIdentity = ObjectIdentity
mscFrAtmDlciNiwfQoS = _MscFrAtmDlciNiwfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4)
)
_MscFrAtmDlciNiwfQoSRowStatusTable_Object = MibTable
mscFrAtmDlciNiwfQoSRowStatusTable = _MscFrAtmDlciNiwfQoSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSRowStatusEntry_Object = MibTableRow
mscFrAtmDlciNiwfQoSRowStatusEntry = _MscFrAtmDlciNiwfQoSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1, 1)
)
mscFrAtmDlciNiwfQoSRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSRowStatus_Type = RowStatus
_MscFrAtmDlciNiwfQoSRowStatus_Object = MibTableColumn
mscFrAtmDlciNiwfQoSRowStatus = _MscFrAtmDlciNiwfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1, 1, 1),
    _MscFrAtmDlciNiwfQoSRowStatus_Type()
)
mscFrAtmDlciNiwfQoSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSRowStatus.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSComponentName_Type = DisplayString
_MscFrAtmDlciNiwfQoSComponentName_Object = MibTableColumn
mscFrAtmDlciNiwfQoSComponentName = _MscFrAtmDlciNiwfQoSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1, 1, 2),
    _MscFrAtmDlciNiwfQoSComponentName_Type()
)
mscFrAtmDlciNiwfQoSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSComponentName.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSStorageType_Type = StorageType
_MscFrAtmDlciNiwfQoSStorageType_Object = MibTableColumn
mscFrAtmDlciNiwfQoSStorageType = _MscFrAtmDlciNiwfQoSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1, 1, 4),
    _MscFrAtmDlciNiwfQoSStorageType_Type()
)
mscFrAtmDlciNiwfQoSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSStorageType.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSIndex_Type = NonReplicated
_MscFrAtmDlciNiwfQoSIndex_Object = MibTableColumn
mscFrAtmDlciNiwfQoSIndex = _MscFrAtmDlciNiwfQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 1, 1, 10),
    _MscFrAtmDlciNiwfQoSIndex_Type()
)
mscFrAtmDlciNiwfQoSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSIndex.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSProvTable_Object = MibTable
mscFrAtmDlciNiwfQoSProvTable = _MscFrAtmDlciNiwfQoSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSProvTable.setStatus("mandatory")
_MscFrAtmDlciNiwfQoSProvEntry_Object = MibTableRow
mscFrAtmDlciNiwfQoSProvEntry = _MscFrAtmDlciNiwfQoSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 10, 1)
)
mscFrAtmDlciNiwfQoSProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSProvEntry.setStatus("mandatory")


class _MscFrAtmDlciNiwfQoSEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfQoSEmissionPriorityToIf based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciNiwfQoSEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfQoSEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmDlciNiwfQoSEmissionPriorityToIf = _MscFrAtmDlciNiwfQoSEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 10, 1, 1),
    _MscFrAtmDlciNiwfQoSEmissionPriorityToIf_Type()
)
mscFrAtmDlciNiwfQoSEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSEmissionPriorityToIf.setStatus("mandatory")


class _MscFrAtmDlciNiwfQoSTransferPriority_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfQoSTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_MscFrAtmDlciNiwfQoSTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfQoSTransferPriority_Object = MibTableColumn
mscFrAtmDlciNiwfQoSTransferPriority = _MscFrAtmDlciNiwfQoSTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 4, 10, 1, 2),
    _MscFrAtmDlciNiwfQoSTransferPriority_Type()
)
mscFrAtmDlciNiwfQoSTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfQoSTransferPriority.setStatus("mandatory")
_MscFrAtmDlciNiwfOperTable_Object = MibTable
mscFrAtmDlciNiwfOperTable = _MscFrAtmDlciNiwfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfOperTable.setStatus("mandatory")
_MscFrAtmDlciNiwfOperEntry_Object = MibTableRow
mscFrAtmDlciNiwfOperEntry = _MscFrAtmDlciNiwfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1)
)
mscFrAtmDlciNiwfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciNiwfIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfOperEntry.setStatus("mandatory")


class _MscFrAtmDlciNiwfDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfDeToClpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmDlciNiwfDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfDeToClpMapping_Object = MibTableColumn
mscFrAtmDlciNiwfDeToClpMapping = _MscFrAtmDlciNiwfDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 1),
    _MscFrAtmDlciNiwfDeToClpMapping_Type()
)
mscFrAtmDlciNiwfDeToClpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfDeToClpMapping.setStatus("mandatory")


class _MscFrAtmDlciNiwfClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfClpToDeMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("transparent", 3))
    )


_MscFrAtmDlciNiwfClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfClpToDeMapping_Object = MibTableColumn
mscFrAtmDlciNiwfClpToDeMapping = _MscFrAtmDlciNiwfClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 2),
    _MscFrAtmDlciNiwfClpToDeMapping_Type()
)
mscFrAtmDlciNiwfClpToDeMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfClpToDeMapping.setStatus("mandatory")


class _MscFrAtmDlciNiwfTransferPriority_Type(Unsigned32):
    """Custom type mscFrAtmDlciNiwfTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmDlciNiwfTransferPriority_Type.__name__ = "Unsigned32"
_MscFrAtmDlciNiwfTransferPriority_Object = MibTableColumn
mscFrAtmDlciNiwfTransferPriority = _MscFrAtmDlciNiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 3),
    _MscFrAtmDlciNiwfTransferPriority_Type()
)
mscFrAtmDlciNiwfTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfTransferPriority.setStatus("mandatory")


class _MscFrAtmDlciNiwfAtmServiceCategory_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfAtmServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("scNotAvailable", 255),
          ("ubr", 0))
    )


_MscFrAtmDlciNiwfAtmServiceCategory_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfAtmServiceCategory_Object = MibTableColumn
mscFrAtmDlciNiwfAtmServiceCategory = _MscFrAtmDlciNiwfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 4),
    _MscFrAtmDlciNiwfAtmServiceCategory_Type()
)
mscFrAtmDlciNiwfAtmServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfAtmServiceCategory.setStatus("mandatory")


class _MscFrAtmDlciNiwfTrafficParmConvPolicy_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfTrafficParmConvPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("policyNotAvailable", 0))
    )


_MscFrAtmDlciNiwfTrafficParmConvPolicy_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfTrafficParmConvPolicy_Object = MibTableColumn
mscFrAtmDlciNiwfTrafficParmConvPolicy = _MscFrAtmDlciNiwfTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 5),
    _MscFrAtmDlciNiwfTrafficParmConvPolicy_Type()
)
mscFrAtmDlciNiwfTrafficParmConvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfTrafficParmConvPolicy.setStatus("mandatory")


class _MscFrAtmDlciNiwfAvgFrameSize_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfAvgFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_MscFrAtmDlciNiwfAvgFrameSize_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfAvgFrameSize_Object = MibTableColumn
mscFrAtmDlciNiwfAvgFrameSize = _MscFrAtmDlciNiwfAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 6),
    _MscFrAtmDlciNiwfAvgFrameSize_Type()
)
mscFrAtmDlciNiwfAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfAvgFrameSize.setStatus("mandatory")


class _MscFrAtmDlciNiwfEquivalentBitRate_Type(Unsigned32):
    """Custom type mscFrAtmDlciNiwfEquivalentBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciNiwfEquivalentBitRate_Type.__name__ = "Unsigned32"
_MscFrAtmDlciNiwfEquivalentBitRate_Object = MibTableColumn
mscFrAtmDlciNiwfEquivalentBitRate = _MscFrAtmDlciNiwfEquivalentBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 7),
    _MscFrAtmDlciNiwfEquivalentBitRate_Type()
)
mscFrAtmDlciNiwfEquivalentBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfEquivalentBitRate.setStatus("mandatory")


class _MscFrAtmDlciNiwfAtmDlci_Type(AsciiString):
    """Custom type mscFrAtmDlciNiwfAtmDlci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscFrAtmDlciNiwfAtmDlci_Type.__name__ = "AsciiString"
_MscFrAtmDlciNiwfAtmDlci_Object = MibTableColumn
mscFrAtmDlciNiwfAtmDlci = _MscFrAtmDlciNiwfAtmDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 8),
    _MscFrAtmDlciNiwfAtmDlci_Type()
)
mscFrAtmDlciNiwfAtmDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfAtmDlci.setStatus("mandatory")


class _MscFrAtmDlciNiwfAssignedBandwidthPool_Type(Integer32):
    """Custom type mscFrAtmDlciNiwfAssignedBandwidthPool based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_MscFrAtmDlciNiwfAssignedBandwidthPool_Type.__name__ = "Integer32"
_MscFrAtmDlciNiwfAssignedBandwidthPool_Object = MibTableColumn
mscFrAtmDlciNiwfAssignedBandwidthPool = _MscFrAtmDlciNiwfAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 4, 10, 1, 9),
    _MscFrAtmDlciNiwfAssignedBandwidthPool_Type()
)
mscFrAtmDlciNiwfAssignedBandwidthPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciNiwfAssignedBandwidthPool.setStatus("mandatory")
_MscFrAtmDlciEgSp_ObjectIdentity = ObjectIdentity
mscFrAtmDlciEgSp = _MscFrAtmDlciEgSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5)
)
_MscFrAtmDlciEgSpRowStatusTable_Object = MibTable
mscFrAtmDlciEgSpRowStatusTable = _MscFrAtmDlciEgSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpRowStatusTable.setStatus("mandatory")
_MscFrAtmDlciEgSpRowStatusEntry_Object = MibTableRow
mscFrAtmDlciEgSpRowStatusEntry = _MscFrAtmDlciEgSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1, 1)
)
mscFrAtmDlciEgSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciEgSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpRowStatusEntry.setStatus("mandatory")
_MscFrAtmDlciEgSpRowStatus_Type = RowStatus
_MscFrAtmDlciEgSpRowStatus_Object = MibTableColumn
mscFrAtmDlciEgSpRowStatus = _MscFrAtmDlciEgSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1, 1, 1),
    _MscFrAtmDlciEgSpRowStatus_Type()
)
mscFrAtmDlciEgSpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpRowStatus.setStatus("mandatory")
_MscFrAtmDlciEgSpComponentName_Type = DisplayString
_MscFrAtmDlciEgSpComponentName_Object = MibTableColumn
mscFrAtmDlciEgSpComponentName = _MscFrAtmDlciEgSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1, 1, 2),
    _MscFrAtmDlciEgSpComponentName_Type()
)
mscFrAtmDlciEgSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpComponentName.setStatus("mandatory")
_MscFrAtmDlciEgSpStorageType_Type = StorageType
_MscFrAtmDlciEgSpStorageType_Object = MibTableColumn
mscFrAtmDlciEgSpStorageType = _MscFrAtmDlciEgSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1, 1, 4),
    _MscFrAtmDlciEgSpStorageType_Type()
)
mscFrAtmDlciEgSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpStorageType.setStatus("mandatory")
_MscFrAtmDlciEgSpIndex_Type = NonReplicated
_MscFrAtmDlciEgSpIndex_Object = MibTableColumn
mscFrAtmDlciEgSpIndex = _MscFrAtmDlciEgSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 1, 1, 10),
    _MscFrAtmDlciEgSpIndex_Type()
)
mscFrAtmDlciEgSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpIndex.setStatus("mandatory")
_MscFrAtmDlciEgSpProvTable_Object = MibTable
mscFrAtmDlciEgSpProvTable = _MscFrAtmDlciEgSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpProvTable.setStatus("mandatory")
_MscFrAtmDlciEgSpProvEntry_Object = MibTableRow
mscFrAtmDlciEgSpProvEntry = _MscFrAtmDlciEgSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10, 1)
)
mscFrAtmDlciEgSpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciEgSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpProvEntry.setStatus("mandatory")


class _MscFrAtmDlciEgSpCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrAtmDlciEgSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciEgSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEgSpCommittedInformationRate_Object = MibTableColumn
mscFrAtmDlciEgSpCommittedInformationRate = _MscFrAtmDlciEgSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10, 1, 1),
    _MscFrAtmDlciEgSpCommittedInformationRate_Type()
)
mscFrAtmDlciEgSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpCommittedInformationRate.setStatus("mandatory")


class _MscFrAtmDlciEgSpCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciEgSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciEgSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEgSpCommittedBurstSize_Object = MibTableColumn
mscFrAtmDlciEgSpCommittedBurstSize = _MscFrAtmDlciEgSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10, 1, 2),
    _MscFrAtmDlciEgSpCommittedBurstSize_Type()
)
mscFrAtmDlciEgSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpCommittedBurstSize.setStatus("mandatory")


class _MscFrAtmDlciEgSpExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciEgSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciEgSpExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEgSpExcessBurstSize_Object = MibTableColumn
mscFrAtmDlciEgSpExcessBurstSize = _MscFrAtmDlciEgSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10, 1, 3),
    _MscFrAtmDlciEgSpExcessBurstSize_Type()
)
mscFrAtmDlciEgSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpExcessBurstSize.setStatus("mandatory")


class _MscFrAtmDlciEgSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrAtmDlciEgSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscFrAtmDlciEgSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEgSpMeasurementInterval_Object = MibTableColumn
mscFrAtmDlciEgSpMeasurementInterval = _MscFrAtmDlciEgSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 5, 10, 1, 4),
    _MscFrAtmDlciEgSpMeasurementInterval_Type()
)
mscFrAtmDlciEgSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmDlciEgSpMeasurementInterval.setStatus("mandatory")
_MscFrAtmDlciStateTable_Object = MibTable
mscFrAtmDlciStateTable = _MscFrAtmDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciStateTable.setStatus("mandatory")
_MscFrAtmDlciStateEntry_Object = MibTableRow
mscFrAtmDlciStateEntry = _MscFrAtmDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 10, 1)
)
mscFrAtmDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciStateEntry.setStatus("mandatory")


class _MscFrAtmDlciAdminState_Type(Integer32):
    """Custom type mscFrAtmDlciAdminState based on Integer32"""
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


_MscFrAtmDlciAdminState_Type.__name__ = "Integer32"
_MscFrAtmDlciAdminState_Object = MibTableColumn
mscFrAtmDlciAdminState = _MscFrAtmDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 10, 1, 1),
    _MscFrAtmDlciAdminState_Type()
)
mscFrAtmDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciAdminState.setStatus("mandatory")


class _MscFrAtmDlciOperationalState_Type(Integer32):
    """Custom type mscFrAtmDlciOperationalState based on Integer32"""
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


_MscFrAtmDlciOperationalState_Type.__name__ = "Integer32"
_MscFrAtmDlciOperationalState_Object = MibTableColumn
mscFrAtmDlciOperationalState = _MscFrAtmDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 10, 1, 2),
    _MscFrAtmDlciOperationalState_Type()
)
mscFrAtmDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciOperationalState.setStatus("mandatory")


class _MscFrAtmDlciUsageState_Type(Integer32):
    """Custom type mscFrAtmDlciUsageState based on Integer32"""
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


_MscFrAtmDlciUsageState_Type.__name__ = "Integer32"
_MscFrAtmDlciUsageState_Object = MibTableColumn
mscFrAtmDlciUsageState = _MscFrAtmDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 10, 1, 3),
    _MscFrAtmDlciUsageState_Type()
)
mscFrAtmDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciUsageState.setStatus("mandatory")
_MscFrAtmDlciABitTable_Object = MibTable
mscFrAtmDlciABitTable = _MscFrAtmDlciABitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciABitTable.setStatus("mandatory")
_MscFrAtmDlciABitEntry_Object = MibTableRow
mscFrAtmDlciABitEntry = _MscFrAtmDlciABitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11, 1)
)
mscFrAtmDlciABitEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciABitEntry.setStatus("mandatory")


class _MscFrAtmDlciABitStatusToIf_Type(Integer32):
    """Custom type mscFrAtmDlciABitStatusToIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_MscFrAtmDlciABitStatusToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciABitStatusToIf_Object = MibTableColumn
mscFrAtmDlciABitStatusToIf = _MscFrAtmDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11, 1, 1),
    _MscFrAtmDlciABitStatusToIf_Type()
)
mscFrAtmDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciABitStatusToIf.setStatus("mandatory")


class _MscFrAtmDlciABitReasonToIf_Type(Integer32):
    """Custom type mscFrAtmDlciABitReasonToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1))
    )


_MscFrAtmDlciABitReasonToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciABitReasonToIf_Object = MibTableColumn
mscFrAtmDlciABitReasonToIf = _MscFrAtmDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11, 1, 2),
    _MscFrAtmDlciABitReasonToIf_Type()
)
mscFrAtmDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciABitReasonToIf.setStatus("mandatory")


class _MscFrAtmDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscFrAtmDlciABitStatusFromIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_MscFrAtmDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscFrAtmDlciABitStatusFromIf_Object = MibTableColumn
mscFrAtmDlciABitStatusFromIf = _MscFrAtmDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11, 1, 3),
    _MscFrAtmDlciABitStatusFromIf_Type()
)
mscFrAtmDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciABitStatusFromIf.setStatus("mandatory")


class _MscFrAtmDlciABitReasonFromIf_Type(Integer32):
    """Custom type mscFrAtmDlciABitReasonFromIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("missingFromLmiReport", 7),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteUserSignaled", 1))
    )


_MscFrAtmDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MscFrAtmDlciABitReasonFromIf_Object = MibTableColumn
mscFrAtmDlciABitReasonFromIf = _MscFrAtmDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 11, 1, 4),
    _MscFrAtmDlciABitReasonFromIf_Type()
)
mscFrAtmDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciABitReasonFromIf.setStatus("mandatory")
_MscFrAtmDlciSpOpTable_Object = MibTable
mscFrAtmDlciSpOpTable = _MscFrAtmDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpOpTable.setStatus("mandatory")
_MscFrAtmDlciSpOpEntry_Object = MibTableRow
mscFrAtmDlciSpOpEntry = _MscFrAtmDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1)
)
mscFrAtmDlciSpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciSpOpEntry.setStatus("mandatory")


class _MscFrAtmDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrAtmDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciMaximumFrameSize_Object = MibTableColumn
mscFrAtmDlciMaximumFrameSize = _MscFrAtmDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 1),
    _MscFrAtmDlciMaximumFrameSize_Type()
)
mscFrAtmDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciMaximumFrameSize.setStatus("mandatory")


class _MscFrAtmDlciRateEnforcement_Type(Integer32):
    """Custom type mscFrAtmDlciRateEnforcement based on Integer32"""
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


_MscFrAtmDlciRateEnforcement_Type.__name__ = "Integer32"
_MscFrAtmDlciRateEnforcement_Object = MibTableColumn
mscFrAtmDlciRateEnforcement = _MscFrAtmDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 2),
    _MscFrAtmDlciRateEnforcement_Type()
)
mscFrAtmDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciRateEnforcement.setStatus("mandatory")


class _MscFrAtmDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrAtmDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrAtmDlciCommittedInformationRate_Object = MibTableColumn
mscFrAtmDlciCommittedInformationRate = _MscFrAtmDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 3),
    _MscFrAtmDlciCommittedInformationRate_Type()
)
mscFrAtmDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciCommittedInformationRate.setStatus("mandatory")


class _MscFrAtmDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciCommittedBurstSize_Object = MibTableColumn
mscFrAtmDlciCommittedBurstSize = _MscFrAtmDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 4),
    _MscFrAtmDlciCommittedBurstSize_Type()
)
mscFrAtmDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciCommittedBurstSize.setStatus("mandatory")


class _MscFrAtmDlciExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrAtmDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrAtmDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrAtmDlciExcessBurstSize_Object = MibTableColumn
mscFrAtmDlciExcessBurstSize = _MscFrAtmDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 5),
    _MscFrAtmDlciExcessBurstSize_Type()
)
mscFrAtmDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciExcessBurstSize.setStatus("mandatory")


class _MscFrAtmDlciMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrAtmDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrAtmDlciMeasurementInterval_Object = MibTableColumn
mscFrAtmDlciMeasurementInterval = _MscFrAtmDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 6),
    _MscFrAtmDlciMeasurementInterval_Type()
)
mscFrAtmDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciMeasurementInterval.setStatus("mandatory")


class _MscFrAtmDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MscFrAtmDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmDlciEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmDlciEmissionPriorityToIf = _MscFrAtmDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 7),
    _MscFrAtmDlciEmissionPriorityToIf_Type()
)
mscFrAtmDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEmissionPriorityToIf.setStatus("mandatory")


class _MscFrAtmDlciDlciType_Type(Integer32):
    """Custom type mscFrAtmDlciDlciType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkInterworking", 1),
          ("serviceInterworking", 0))
    )


_MscFrAtmDlciDlciType_Type.__name__ = "Integer32"
_MscFrAtmDlciDlciType_Object = MibTableColumn
mscFrAtmDlciDlciType = _MscFrAtmDlciDlciType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 8),
    _MscFrAtmDlciDlciType_Type()
)
mscFrAtmDlciDlciType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDlciType.setStatus("mandatory")


class _MscFrAtmDlciTroubled_Type(Integer32):
    """Custom type mscFrAtmDlciTroubled based on Integer32"""
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


_MscFrAtmDlciTroubled_Type.__name__ = "Integer32"
_MscFrAtmDlciTroubled_Object = MibTableColumn
mscFrAtmDlciTroubled = _MscFrAtmDlciTroubled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 9),
    _MscFrAtmDlciTroubled_Type()
)
mscFrAtmDlciTroubled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTroubled.setStatus("mandatory")


class _MscFrAtmDlciTroubledReason_Type(Integer32):
    """Custom type mscFrAtmDlciTroubledReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdmitted", 1),
          ("notApplicable", 0))
    )


_MscFrAtmDlciTroubledReason_Type.__name__ = "Integer32"
_MscFrAtmDlciTroubledReason_Object = MibTableColumn
mscFrAtmDlciTroubledReason = _MscFrAtmDlciTroubledReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 12, 1, 10),
    _MscFrAtmDlciTroubledReason_Type()
)
mscFrAtmDlciTroubledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTroubledReason.setStatus("mandatory")
_MscFrAtmDlciStatsTable_Object = MibTable
mscFrAtmDlciStatsTable = _MscFrAtmDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciStatsTable.setStatus("mandatory")
_MscFrAtmDlciStatsEntry_Object = MibTableRow
mscFrAtmDlciStatsEntry = _MscFrAtmDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1)
)
mscFrAtmDlciStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciStatsEntry.setStatus("mandatory")
_MscFrAtmDlciFrmToIf_Type = Counter32
_MscFrAtmDlciFrmToIf_Object = MibTableColumn
mscFrAtmDlciFrmToIf = _MscFrAtmDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 1),
    _MscFrAtmDlciFrmToIf_Type()
)
mscFrAtmDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciFrmToIf.setStatus("mandatory")
_MscFrAtmDlciFecnFrmToIf_Type = Counter32
_MscFrAtmDlciFecnFrmToIf_Object = MibTableColumn
mscFrAtmDlciFecnFrmToIf = _MscFrAtmDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 2),
    _MscFrAtmDlciFecnFrmToIf_Type()
)
mscFrAtmDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciFecnFrmToIf.setStatus("mandatory")
_MscFrAtmDlciBecnFrmToIf_Type = Counter32
_MscFrAtmDlciBecnFrmToIf_Object = MibTableColumn
mscFrAtmDlciBecnFrmToIf = _MscFrAtmDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 3),
    _MscFrAtmDlciBecnFrmToIf_Type()
)
mscFrAtmDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciBecnFrmToIf.setStatus("mandatory")
_MscFrAtmDlciDeFrmToIf_Type = Counter32
_MscFrAtmDlciDeFrmToIf_Object = MibTableColumn
mscFrAtmDlciDeFrmToIf = _MscFrAtmDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 4),
    _MscFrAtmDlciDeFrmToIf_Type()
)
mscFrAtmDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDeFrmToIf.setStatus("mandatory")
_MscFrAtmDlciDiscCongestedToIf_Type = Counter32
_MscFrAtmDlciDiscCongestedToIf_Object = MibTableColumn
mscFrAtmDlciDiscCongestedToIf = _MscFrAtmDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 5),
    _MscFrAtmDlciDiscCongestedToIf_Type()
)
mscFrAtmDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscCongestedToIf.setStatus("mandatory")
_MscFrAtmDlciDiscDeCongestedToIf_Type = Counter32
_MscFrAtmDlciDiscDeCongestedToIf_Object = MibTableColumn
mscFrAtmDlciDiscDeCongestedToIf = _MscFrAtmDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 6),
    _MscFrAtmDlciDiscDeCongestedToIf_Type()
)
mscFrAtmDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscDeCongestedToIf.setStatus("mandatory")
_MscFrAtmDlciFrmFromIf_Type = Counter32
_MscFrAtmDlciFrmFromIf_Object = MibTableColumn
mscFrAtmDlciFrmFromIf = _MscFrAtmDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 7),
    _MscFrAtmDlciFrmFromIf_Type()
)
mscFrAtmDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciFecnFrmFromIf_Type = Counter32
_MscFrAtmDlciFecnFrmFromIf_Object = MibTableColumn
mscFrAtmDlciFecnFrmFromIf = _MscFrAtmDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 8),
    _MscFrAtmDlciFecnFrmFromIf_Type()
)
mscFrAtmDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciFecnFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciBecnFrmFromIf_Type = Counter32
_MscFrAtmDlciBecnFrmFromIf_Object = MibTableColumn
mscFrAtmDlciBecnFrmFromIf = _MscFrAtmDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 9),
    _MscFrAtmDlciBecnFrmFromIf_Type()
)
mscFrAtmDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciBecnFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciEfciFrmFromNetwork_Type = Counter32
_MscFrAtmDlciEfciFrmFromNetwork_Object = MibTableColumn
mscFrAtmDlciEfciFrmFromNetwork = _MscFrAtmDlciEfciFrmFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 10),
    _MscFrAtmDlciEfciFrmFromNetwork_Type()
)
mscFrAtmDlciEfciFrmFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEfciFrmFromNetwork.setStatus("mandatory")
_MscFrAtmDlciDeFrmFromIf_Type = Counter32
_MscFrAtmDlciDeFrmFromIf_Object = MibTableColumn
mscFrAtmDlciDeFrmFromIf = _MscFrAtmDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 11),
    _MscFrAtmDlciDeFrmFromIf_Type()
)
mscFrAtmDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDeFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciExcessFrmFromIf_Type = Counter32
_MscFrAtmDlciExcessFrmFromIf_Object = MibTableColumn
mscFrAtmDlciExcessFrmFromIf = _MscFrAtmDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 12),
    _MscFrAtmDlciExcessFrmFromIf_Type()
)
mscFrAtmDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciExcessFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciDiscExcessFromIf_Type = Counter32
_MscFrAtmDlciDiscExcessFromIf_Object = MibTableColumn
mscFrAtmDlciDiscExcessFromIf = _MscFrAtmDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 13),
    _MscFrAtmDlciDiscExcessFromIf_Type()
)
mscFrAtmDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscExcessFromIf.setStatus("mandatory")
_MscFrAtmDlciDiscFrameAbit_Type = Counter32
_MscFrAtmDlciDiscFrameAbit_Object = MibTableColumn
mscFrAtmDlciDiscFrameAbit = _MscFrAtmDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 14),
    _MscFrAtmDlciDiscFrameAbit_Type()
)
mscFrAtmDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscFrameAbit.setStatus("mandatory")
_MscFrAtmDlciDiscCongestedFromIf_Type = Counter32
_MscFrAtmDlciDiscCongestedFromIf_Object = MibTableColumn
mscFrAtmDlciDiscCongestedFromIf = _MscFrAtmDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 15),
    _MscFrAtmDlciDiscCongestedFromIf_Type()
)
mscFrAtmDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscCongestedFromIf.setStatus("mandatory")
_MscFrAtmDlciDiscDeCongestedFromIf_Type = Counter32
_MscFrAtmDlciDiscDeCongestedFromIf_Object = MibTableColumn
mscFrAtmDlciDiscDeCongestedFromIf = _MscFrAtmDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 16),
    _MscFrAtmDlciDiscDeCongestedFromIf_Type()
)
mscFrAtmDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscDeCongestedFromIf.setStatus("mandatory")
_MscFrAtmDlciErrorShortFrmFromIf_Type = Counter32
_MscFrAtmDlciErrorShortFrmFromIf_Object = MibTableColumn
mscFrAtmDlciErrorShortFrmFromIf = _MscFrAtmDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 17),
    _MscFrAtmDlciErrorShortFrmFromIf_Type()
)
mscFrAtmDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciErrorShortFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciErrorLongFrmFromIf_Type = Counter32
_MscFrAtmDlciErrorLongFrmFromIf_Object = MibTableColumn
mscFrAtmDlciErrorLongFrmFromIf = _MscFrAtmDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 18),
    _MscFrAtmDlciErrorLongFrmFromIf_Type()
)
mscFrAtmDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciErrorLongFrmFromIf.setStatus("mandatory")
_MscFrAtmDlciBecnFrmSetByService_Type = Counter32
_MscFrAtmDlciBecnFrmSetByService_Object = MibTableColumn
mscFrAtmDlciBecnFrmSetByService = _MscFrAtmDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 19),
    _MscFrAtmDlciBecnFrmSetByService_Type()
)
mscFrAtmDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciBecnFrmSetByService.setStatus("mandatory")
_MscFrAtmDlciBytesToIf_Type = Counter32
_MscFrAtmDlciBytesToIf_Object = MibTableColumn
mscFrAtmDlciBytesToIf = _MscFrAtmDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 20),
    _MscFrAtmDlciBytesToIf_Type()
)
mscFrAtmDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciBytesToIf.setStatus("mandatory")
_MscFrAtmDlciDeBytesToIf_Type = Counter32
_MscFrAtmDlciDeBytesToIf_Object = MibTableColumn
mscFrAtmDlciDeBytesToIf = _MscFrAtmDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 21),
    _MscFrAtmDlciDeBytesToIf_Type()
)
mscFrAtmDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDeBytesToIf.setStatus("mandatory")
_MscFrAtmDlciDiscCongestedToIfBytes_Type = Counter32
_MscFrAtmDlciDiscCongestedToIfBytes_Object = MibTableColumn
mscFrAtmDlciDiscCongestedToIfBytes = _MscFrAtmDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 22),
    _MscFrAtmDlciDiscCongestedToIfBytes_Type()
)
mscFrAtmDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscCongestedToIfBytes.setStatus("mandatory")
_MscFrAtmDlciDiscDeCongestedToIfBytes_Type = Counter32
_MscFrAtmDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
mscFrAtmDlciDiscDeCongestedToIfBytes = _MscFrAtmDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 23),
    _MscFrAtmDlciDiscDeCongestedToIfBytes_Type()
)
mscFrAtmDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscDeCongestedToIfBytes.setStatus("mandatory")
_MscFrAtmDlciBytesFromIf_Type = Counter32
_MscFrAtmDlciBytesFromIf_Object = MibTableColumn
mscFrAtmDlciBytesFromIf = _MscFrAtmDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 24),
    _MscFrAtmDlciBytesFromIf_Type()
)
mscFrAtmDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciBytesFromIf.setStatus("mandatory")
_MscFrAtmDlciDeBytesFromIf_Type = Counter32
_MscFrAtmDlciDeBytesFromIf_Object = MibTableColumn
mscFrAtmDlciDeBytesFromIf = _MscFrAtmDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 25),
    _MscFrAtmDlciDeBytesFromIf_Type()
)
mscFrAtmDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDeBytesFromIf.setStatus("mandatory")
_MscFrAtmDlciExcessBytesFromIf_Type = Counter32
_MscFrAtmDlciExcessBytesFromIf_Object = MibTableColumn
mscFrAtmDlciExcessBytesFromIf = _MscFrAtmDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 26),
    _MscFrAtmDlciExcessBytesFromIf_Type()
)
mscFrAtmDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciExcessBytesFromIf.setStatus("mandatory")
_MscFrAtmDlciDiscExcessFromIfBytes_Type = Counter32
_MscFrAtmDlciDiscExcessFromIfBytes_Object = MibTableColumn
mscFrAtmDlciDiscExcessFromIfBytes = _MscFrAtmDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 27),
    _MscFrAtmDlciDiscExcessFromIfBytes_Type()
)
mscFrAtmDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscExcessFromIfBytes.setStatus("mandatory")
_MscFrAtmDlciDiscByteAbit_Type = Counter32
_MscFrAtmDlciDiscByteAbit_Object = MibTableColumn
mscFrAtmDlciDiscByteAbit = _MscFrAtmDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 28),
    _MscFrAtmDlciDiscByteAbit_Type()
)
mscFrAtmDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscByteAbit.setStatus("mandatory")
_MscFrAtmDlciDiscCongestedFromIfBytes_Type = Counter32
_MscFrAtmDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mscFrAtmDlciDiscCongestedFromIfBytes = _MscFrAtmDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 29),
    _MscFrAtmDlciDiscCongestedFromIfBytes_Type()
)
mscFrAtmDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscCongestedFromIfBytes.setStatus("mandatory")
_MscFrAtmDlciDiscDeCongestedFromIfBytes_Type = Counter32
_MscFrAtmDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mscFrAtmDlciDiscDeCongestedFromIfBytes = _MscFrAtmDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 30),
    _MscFrAtmDlciDiscDeCongestedFromIfBytes_Type()
)
mscFrAtmDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")
_MscFrAtmDlciErrorShortBytesFromIf_Type = Counter32
_MscFrAtmDlciErrorShortBytesFromIf_Object = MibTableColumn
mscFrAtmDlciErrorShortBytesFromIf = _MscFrAtmDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 31),
    _MscFrAtmDlciErrorShortBytesFromIf_Type()
)
mscFrAtmDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciErrorShortBytesFromIf.setStatus("mandatory")
_MscFrAtmDlciErrorLongBytesFromIf_Type = Counter32
_MscFrAtmDlciErrorLongBytesFromIf_Object = MibTableColumn
mscFrAtmDlciErrorLongBytesFromIf = _MscFrAtmDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 13, 1, 32),
    _MscFrAtmDlciErrorLongBytesFromIf_Type()
)
mscFrAtmDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciErrorLongBytesFromIf.setStatus("mandatory")
_MscFrAtmDlciCalldTable_Object = MibTable
mscFrAtmDlciCalldTable = _MscFrAtmDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciCalldTable.setStatus("mandatory")
_MscFrAtmDlciCalldEntry_Object = MibTableRow
mscFrAtmDlciCalldEntry = _MscFrAtmDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 14, 1)
)
mscFrAtmDlciCalldEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciCalldEntry.setStatus("mandatory")


class _MscFrAtmDlciAccountingEnabled_Type(Integer32):
    """Custom type mscFrAtmDlciAccountingEnabled based on Integer32"""
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


_MscFrAtmDlciAccountingEnabled_Type.__name__ = "Integer32"
_MscFrAtmDlciAccountingEnabled_Object = MibTableColumn
mscFrAtmDlciAccountingEnabled = _MscFrAtmDlciAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 14, 1, 1),
    _MscFrAtmDlciAccountingEnabled_Type()
)
mscFrAtmDlciAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciAccountingEnabled.setStatus("mandatory")


class _MscFrAtmDlciAccountingEnd_Type(Integer32):
    """Custom type mscFrAtmDlciAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_MscFrAtmDlciAccountingEnd_Type.__name__ = "Integer32"
_MscFrAtmDlciAccountingEnd_Object = MibTableColumn
mscFrAtmDlciAccountingEnd = _MscFrAtmDlciAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 14, 1, 2),
    _MscFrAtmDlciAccountingEnd_Type()
)
mscFrAtmDlciAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciAccountingEnd.setStatus("mandatory")


class _MscFrAtmDlciCorrelationTag_Type(HexString):
    """Custom type mscFrAtmDlciCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_MscFrAtmDlciCorrelationTag_Type.__name__ = "HexString"
_MscFrAtmDlciCorrelationTag_Object = MibTableColumn
mscFrAtmDlciCorrelationTag = _MscFrAtmDlciCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 14, 1, 3),
    _MscFrAtmDlciCorrelationTag_Type()
)
mscFrAtmDlciCorrelationTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciCorrelationTag.setStatus("mandatory")
_MscFrAtmDlciIntTable_Object = MibTable
mscFrAtmDlciIntTable = _MscFrAtmDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15)
)
if mibBuilder.loadTexts:
    mscFrAtmDlciIntTable.setStatus("mandatory")
_MscFrAtmDlciIntEntry_Object = MibTableRow
mscFrAtmDlciIntEntry = _MscFrAtmDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1)
)
mscFrAtmDlciIntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmDlciIntEntry.setStatus("mandatory")


class _MscFrAtmDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrAtmDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrAtmDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrAtmDlciStartTime_Object = MibTableColumn
mscFrAtmDlciStartTime = _MscFrAtmDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 1),
    _MscFrAtmDlciStartTime_Type()
)
mscFrAtmDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciStartTime.setStatus("mandatory")


class _MscFrAtmDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type mscFrAtmDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrAtmDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_MscFrAtmDlciTotalIngressBytes_Object = MibTableColumn
mscFrAtmDlciTotalIngressBytes = _MscFrAtmDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 2),
    _MscFrAtmDlciTotalIngressBytes_Type()
)
mscFrAtmDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTotalIngressBytes.setStatus("mandatory")


class _MscFrAtmDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type mscFrAtmDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrAtmDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_MscFrAtmDlciTotalEgressBytes_Object = MibTableColumn
mscFrAtmDlciTotalEgressBytes = _MscFrAtmDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 3),
    _MscFrAtmDlciTotalEgressBytes_Type()
)
mscFrAtmDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTotalEgressBytes.setStatus("mandatory")


class _MscFrAtmDlciEirIngressBytes_Type(Unsigned64):
    """Custom type mscFrAtmDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrAtmDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_MscFrAtmDlciEirIngressBytes_Object = MibTableColumn
mscFrAtmDlciEirIngressBytes = _MscFrAtmDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 4),
    _MscFrAtmDlciEirIngressBytes_Type()
)
mscFrAtmDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEirIngressBytes.setStatus("mandatory")


class _MscFrAtmDlciEirEgressBytes_Type(Unsigned64):
    """Custom type mscFrAtmDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrAtmDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_MscFrAtmDlciEirEgressBytes_Object = MibTableColumn
mscFrAtmDlciEirEgressBytes = _MscFrAtmDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 5),
    _MscFrAtmDlciEirEgressBytes_Type()
)
mscFrAtmDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEirEgressBytes.setStatus("mandatory")


class _MscFrAtmDlciDiscardedBytes_Type(Unsigned64):
    """Custom type mscFrAtmDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrAtmDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_MscFrAtmDlciDiscardedBytes_Object = MibTableColumn
mscFrAtmDlciDiscardedBytes = _MscFrAtmDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 6),
    _MscFrAtmDlciDiscardedBytes_Type()
)
mscFrAtmDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscardedBytes.setStatus("mandatory")


class _MscFrAtmDlciTotalIngressFrames_Type(Unsigned32):
    """Custom type mscFrAtmDlciTotalIngressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciTotalIngressFrames_Type.__name__ = "Unsigned32"
_MscFrAtmDlciTotalIngressFrames_Object = MibTableColumn
mscFrAtmDlciTotalIngressFrames = _MscFrAtmDlciTotalIngressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 7),
    _MscFrAtmDlciTotalIngressFrames_Type()
)
mscFrAtmDlciTotalIngressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTotalIngressFrames.setStatus("mandatory")


class _MscFrAtmDlciTotalEgressFrames_Type(Unsigned32):
    """Custom type mscFrAtmDlciTotalEgressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciTotalEgressFrames_Type.__name__ = "Unsigned32"
_MscFrAtmDlciTotalEgressFrames_Object = MibTableColumn
mscFrAtmDlciTotalEgressFrames = _MscFrAtmDlciTotalEgressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 8),
    _MscFrAtmDlciTotalEgressFrames_Type()
)
mscFrAtmDlciTotalEgressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciTotalEgressFrames.setStatus("mandatory")


class _MscFrAtmDlciEirIngressFrames_Type(Unsigned32):
    """Custom type mscFrAtmDlciEirIngressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciEirIngressFrames_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEirIngressFrames_Object = MibTableColumn
mscFrAtmDlciEirIngressFrames = _MscFrAtmDlciEirIngressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 9),
    _MscFrAtmDlciEirIngressFrames_Type()
)
mscFrAtmDlciEirIngressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEirIngressFrames.setStatus("mandatory")


class _MscFrAtmDlciEirEgressFrames_Type(Unsigned32):
    """Custom type mscFrAtmDlciEirEgressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciEirEgressFrames_Type.__name__ = "Unsigned32"
_MscFrAtmDlciEirEgressFrames_Object = MibTableColumn
mscFrAtmDlciEirEgressFrames = _MscFrAtmDlciEirEgressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 10),
    _MscFrAtmDlciEirEgressFrames_Type()
)
mscFrAtmDlciEirEgressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciEirEgressFrames.setStatus("mandatory")


class _MscFrAtmDlciDiscardedFrames_Type(Unsigned32):
    """Custom type mscFrAtmDlciDiscardedFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciDiscardedFrames_Type.__name__ = "Unsigned32"
_MscFrAtmDlciDiscardedFrames_Object = MibTableColumn
mscFrAtmDlciDiscardedFrames = _MscFrAtmDlciDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 11),
    _MscFrAtmDlciDiscardedFrames_Type()
)
mscFrAtmDlciDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciDiscardedFrames.setStatus("mandatory")


class _MscFrAtmDlciElapsedDifference_Type(Unsigned32):
    """Custom type mscFrAtmDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmDlciElapsedDifference_Type.__name__ = "Unsigned32"
_MscFrAtmDlciElapsedDifference_Object = MibTableColumn
mscFrAtmDlciElapsedDifference = _MscFrAtmDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 4, 15, 1, 12),
    _MscFrAtmDlciElapsedDifference_Type()
)
mscFrAtmDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmDlciElapsedDifference.setStatus("mandatory")
_MscFrAtmVFramer_ObjectIdentity = ObjectIdentity
mscFrAtmVFramer = _MscFrAtmVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5)
)
_MscFrAtmVFramerRowStatusTable_Object = MibTable
mscFrAtmVFramerRowStatusTable = _MscFrAtmVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerRowStatusTable.setStatus("mandatory")
_MscFrAtmVFramerRowStatusEntry_Object = MibTableRow
mscFrAtmVFramerRowStatusEntry = _MscFrAtmVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1, 1)
)
mscFrAtmVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerRowStatusEntry.setStatus("mandatory")
_MscFrAtmVFramerRowStatus_Type = RowStatus
_MscFrAtmVFramerRowStatus_Object = MibTableColumn
mscFrAtmVFramerRowStatus = _MscFrAtmVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1, 1, 1),
    _MscFrAtmVFramerRowStatus_Type()
)
mscFrAtmVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmVFramerRowStatus.setStatus("mandatory")
_MscFrAtmVFramerComponentName_Type = DisplayString
_MscFrAtmVFramerComponentName_Object = MibTableColumn
mscFrAtmVFramerComponentName = _MscFrAtmVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1, 1, 2),
    _MscFrAtmVFramerComponentName_Type()
)
mscFrAtmVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerComponentName.setStatus("mandatory")
_MscFrAtmVFramerStorageType_Type = StorageType
_MscFrAtmVFramerStorageType_Object = MibTableColumn
mscFrAtmVFramerStorageType = _MscFrAtmVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1, 1, 4),
    _MscFrAtmVFramerStorageType_Type()
)
mscFrAtmVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerStorageType.setStatus("mandatory")
_MscFrAtmVFramerIndex_Type = NonReplicated
_MscFrAtmVFramerIndex_Object = MibTableColumn
mscFrAtmVFramerIndex = _MscFrAtmVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 1, 1, 10),
    _MscFrAtmVFramerIndex_Type()
)
mscFrAtmVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmVFramerIndex.setStatus("mandatory")
_MscFrAtmVFramerProvTable_Object = MibTable
mscFrAtmVFramerProvTable = _MscFrAtmVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerProvTable.setStatus("mandatory")
_MscFrAtmVFramerProvEntry_Object = MibTableRow
mscFrAtmVFramerProvEntry = _MscFrAtmVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 10, 1)
)
mscFrAtmVFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerProvEntry.setStatus("mandatory")
_MscFrAtmVFramerOtherVirtualFramer_Type = Link
_MscFrAtmVFramerOtherVirtualFramer_Object = MibTableColumn
mscFrAtmVFramerOtherVirtualFramer = _MscFrAtmVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 10, 1, 1),
    _MscFrAtmVFramerOtherVirtualFramer_Type()
)
mscFrAtmVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmVFramerOtherVirtualFramer.setStatus("mandatory")
_MscFrAtmVFramerLogicalProcessor_Type = Link
_MscFrAtmVFramerLogicalProcessor_Object = MibTableColumn
mscFrAtmVFramerLogicalProcessor = _MscFrAtmVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 10, 1, 2),
    _MscFrAtmVFramerLogicalProcessor_Type()
)
mscFrAtmVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmVFramerLogicalProcessor.setStatus("mandatory")
_MscFrAtmVFramerStateTable_Object = MibTable
mscFrAtmVFramerStateTable = _MscFrAtmVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerStateTable.setStatus("mandatory")
_MscFrAtmVFramerStateEntry_Object = MibTableRow
mscFrAtmVFramerStateEntry = _MscFrAtmVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 11, 1)
)
mscFrAtmVFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerStateEntry.setStatus("mandatory")


class _MscFrAtmVFramerAdminState_Type(Integer32):
    """Custom type mscFrAtmVFramerAdminState based on Integer32"""
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


_MscFrAtmVFramerAdminState_Type.__name__ = "Integer32"
_MscFrAtmVFramerAdminState_Object = MibTableColumn
mscFrAtmVFramerAdminState = _MscFrAtmVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 11, 1, 1),
    _MscFrAtmVFramerAdminState_Type()
)
mscFrAtmVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerAdminState.setStatus("mandatory")


class _MscFrAtmVFramerOperationalState_Type(Integer32):
    """Custom type mscFrAtmVFramerOperationalState based on Integer32"""
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


_MscFrAtmVFramerOperationalState_Type.__name__ = "Integer32"
_MscFrAtmVFramerOperationalState_Object = MibTableColumn
mscFrAtmVFramerOperationalState = _MscFrAtmVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 11, 1, 2),
    _MscFrAtmVFramerOperationalState_Type()
)
mscFrAtmVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerOperationalState.setStatus("mandatory")


class _MscFrAtmVFramerUsageState_Type(Integer32):
    """Custom type mscFrAtmVFramerUsageState based on Integer32"""
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


_MscFrAtmVFramerUsageState_Type.__name__ = "Integer32"
_MscFrAtmVFramerUsageState_Object = MibTableColumn
mscFrAtmVFramerUsageState = _MscFrAtmVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 11, 1, 3),
    _MscFrAtmVFramerUsageState_Type()
)
mscFrAtmVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerUsageState.setStatus("mandatory")
_MscFrAtmVFramerStatsTable_Object = MibTable
mscFrAtmVFramerStatsTable = _MscFrAtmVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerStatsTable.setStatus("mandatory")
_MscFrAtmVFramerStatsEntry_Object = MibTableRow
mscFrAtmVFramerStatsEntry = _MscFrAtmVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 12, 1)
)
mscFrAtmVFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmVFramerStatsEntry.setStatus("mandatory")
_MscFrAtmVFramerFrmToOtherVFramer_Type = PassportCounter64
_MscFrAtmVFramerFrmToOtherVFramer_Object = MibTableColumn
mscFrAtmVFramerFrmToOtherVFramer = _MscFrAtmVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 12, 1, 2),
    _MscFrAtmVFramerFrmToOtherVFramer_Type()
)
mscFrAtmVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerFrmToOtherVFramer.setStatus("mandatory")
_MscFrAtmVFramerFrmFromOtherVFramer_Type = PassportCounter64
_MscFrAtmVFramerFrmFromOtherVFramer_Object = MibTableColumn
mscFrAtmVFramerFrmFromOtherVFramer = _MscFrAtmVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 12, 1, 3),
    _MscFrAtmVFramerFrmFromOtherVFramer_Type()
)
mscFrAtmVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerFrmFromOtherVFramer.setStatus("mandatory")
_MscFrAtmVFramerOctetFromOtherVFramer_Type = PassportCounter64
_MscFrAtmVFramerOctetFromOtherVFramer_Object = MibTableColumn
mscFrAtmVFramerOctetFromOtherVFramer = _MscFrAtmVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 5, 12, 1, 5),
    _MscFrAtmVFramerOctetFromOtherVFramer_Type()
)
mscFrAtmVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmVFramerOctetFromOtherVFramer.setStatus("mandatory")
_MscFrAtmAddr_ObjectIdentity = ObjectIdentity
mscFrAtmAddr = _MscFrAtmAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6)
)
_MscFrAtmAddrRowStatusTable_Object = MibTable
mscFrAtmAddrRowStatusTable = _MscFrAtmAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmAddrRowStatusTable.setStatus("mandatory")
_MscFrAtmAddrRowStatusEntry_Object = MibTableRow
mscFrAtmAddrRowStatusEntry = _MscFrAtmAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1, 1)
)
mscFrAtmAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmAddrRowStatusEntry.setStatus("mandatory")
_MscFrAtmAddrRowStatus_Type = RowStatus
_MscFrAtmAddrRowStatus_Object = MibTableColumn
mscFrAtmAddrRowStatus = _MscFrAtmAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1, 1, 1),
    _MscFrAtmAddrRowStatus_Type()
)
mscFrAtmAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmAddrRowStatus.setStatus("mandatory")
_MscFrAtmAddrComponentName_Type = DisplayString
_MscFrAtmAddrComponentName_Object = MibTableColumn
mscFrAtmAddrComponentName = _MscFrAtmAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1, 1, 2),
    _MscFrAtmAddrComponentName_Type()
)
mscFrAtmAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAddrComponentName.setStatus("mandatory")
_MscFrAtmAddrStorageType_Type = StorageType
_MscFrAtmAddrStorageType_Object = MibTableColumn
mscFrAtmAddrStorageType = _MscFrAtmAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1, 1, 4),
    _MscFrAtmAddrStorageType_Type()
)
mscFrAtmAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAddrStorageType.setStatus("mandatory")
_MscFrAtmAddrIndex_Type = NonReplicated
_MscFrAtmAddrIndex_Object = MibTableColumn
mscFrAtmAddrIndex = _MscFrAtmAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 1, 1, 10),
    _MscFrAtmAddrIndex_Type()
)
mscFrAtmAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmAddrIndex.setStatus("mandatory")
_MscFrAtmAddrProvTable_Object = MibTable
mscFrAtmAddrProvTable = _MscFrAtmAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmAddrProvTable.setStatus("mandatory")
_MscFrAtmAddrProvEntry_Object = MibTableRow
mscFrAtmAddrProvEntry = _MscFrAtmAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 10, 1)
)
mscFrAtmAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmAddrProvEntry.setStatus("mandatory")


class _MscFrAtmAddrAddress_Type(AsciiString):
    """Custom type mscFrAtmAddrAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscFrAtmAddrAddress_Type.__name__ = "AsciiString"
_MscFrAtmAddrAddress_Object = MibTableColumn
mscFrAtmAddrAddress = _MscFrAtmAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 10, 1, 2),
    _MscFrAtmAddrAddress_Type()
)
mscFrAtmAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmAddrAddress.setStatus("mandatory")
_MscFrAtmAddrAddrOpTable_Object = MibTable
mscFrAtmAddrAddrOpTable = _MscFrAtmAddrAddrOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmAddrAddrOpTable.setStatus("mandatory")
_MscFrAtmAddrAddrOpEntry_Object = MibTableRow
mscFrAtmAddrAddrOpEntry = _MscFrAtmAddrAddrOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 11, 1)
)
mscFrAtmAddrAddrOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmAddrAddrOpEntry.setStatus("mandatory")


class _MscFrAtmAddrMyAddress_Type(AsciiString):
    """Custom type mscFrAtmAddrMyAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_MscFrAtmAddrMyAddress_Type.__name__ = "AsciiString"
_MscFrAtmAddrMyAddress_Object = MibTableColumn
mscFrAtmAddrMyAddress = _MscFrAtmAddrMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 6, 11, 1, 1),
    _MscFrAtmAddrMyAddress_Type()
)
mscFrAtmAddrMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAddrMyAddress.setStatus("mandatory")
_MscFrAtmCa_ObjectIdentity = ObjectIdentity
mscFrAtmCa = _MscFrAtmCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7)
)
_MscFrAtmCaRowStatusTable_Object = MibTable
mscFrAtmCaRowStatusTable = _MscFrAtmCaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmCaRowStatusTable.setStatus("mandatory")
_MscFrAtmCaRowStatusEntry_Object = MibTableRow
mscFrAtmCaRowStatusEntry = _MscFrAtmCaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1, 1)
)
mscFrAtmCaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaRowStatusEntry.setStatus("mandatory")
_MscFrAtmCaRowStatus_Type = RowStatus
_MscFrAtmCaRowStatus_Object = MibTableColumn
mscFrAtmCaRowStatus = _MscFrAtmCaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1, 1, 1),
    _MscFrAtmCaRowStatus_Type()
)
mscFrAtmCaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaRowStatus.setStatus("mandatory")
_MscFrAtmCaComponentName_Type = DisplayString
_MscFrAtmCaComponentName_Object = MibTableColumn
mscFrAtmCaComponentName = _MscFrAtmCaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1, 1, 2),
    _MscFrAtmCaComponentName_Type()
)
mscFrAtmCaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaComponentName.setStatus("mandatory")
_MscFrAtmCaStorageType_Type = StorageType
_MscFrAtmCaStorageType_Object = MibTableColumn
mscFrAtmCaStorageType = _MscFrAtmCaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1, 1, 4),
    _MscFrAtmCaStorageType_Type()
)
mscFrAtmCaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaStorageType.setStatus("mandatory")
_MscFrAtmCaIndex_Type = NonReplicated
_MscFrAtmCaIndex_Object = MibTableColumn
mscFrAtmCaIndex = _MscFrAtmCaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 1, 1, 10),
    _MscFrAtmCaIndex_Type()
)
mscFrAtmCaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaIndex.setStatus("mandatory")
_MscFrAtmCaTpm_ObjectIdentity = ObjectIdentity
mscFrAtmCaTpm = _MscFrAtmCaTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2)
)
_MscFrAtmCaTpmRowStatusTable_Object = MibTable
mscFrAtmCaTpmRowStatusTable = _MscFrAtmCaTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrAtmCaTpmRowStatusTable.setStatus("mandatory")
_MscFrAtmCaTpmRowStatusEntry_Object = MibTableRow
mscFrAtmCaTpmRowStatusEntry = _MscFrAtmCaTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1, 1)
)
mscFrAtmCaTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaTpmRowStatusEntry.setStatus("mandatory")
_MscFrAtmCaTpmRowStatus_Type = RowStatus
_MscFrAtmCaTpmRowStatus_Object = MibTableColumn
mscFrAtmCaTpmRowStatus = _MscFrAtmCaTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1, 1, 1),
    _MscFrAtmCaTpmRowStatus_Type()
)
mscFrAtmCaTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmRowStatus.setStatus("mandatory")
_MscFrAtmCaTpmComponentName_Type = DisplayString
_MscFrAtmCaTpmComponentName_Object = MibTableColumn
mscFrAtmCaTpmComponentName = _MscFrAtmCaTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1, 1, 2),
    _MscFrAtmCaTpmComponentName_Type()
)
mscFrAtmCaTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmComponentName.setStatus("mandatory")
_MscFrAtmCaTpmStorageType_Type = StorageType
_MscFrAtmCaTpmStorageType_Object = MibTableColumn
mscFrAtmCaTpmStorageType = _MscFrAtmCaTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1, 1, 4),
    _MscFrAtmCaTpmStorageType_Type()
)
mscFrAtmCaTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmStorageType.setStatus("mandatory")


class _MscFrAtmCaTpmIndex_Type(Integer32):
    """Custom type mscFrAtmCaTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaTpmIndex_Type.__name__ = "Integer32"
_MscFrAtmCaTpmIndex_Object = MibTableColumn
mscFrAtmCaTpmIndex = _MscFrAtmCaTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 1, 1, 10),
    _MscFrAtmCaTpmIndex_Type()
)
mscFrAtmCaTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmIndex.setStatus("mandatory")
_MscFrAtmCaTpmProvTable_Object = MibTable
mscFrAtmCaTpmProvTable = _MscFrAtmCaTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmCaTpmProvTable.setStatus("mandatory")
_MscFrAtmCaTpmProvEntry_Object = MibTableRow
mscFrAtmCaTpmProvEntry = _MscFrAtmCaTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 10, 1)
)
mscFrAtmCaTpmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaTpmProvEntry.setStatus("mandatory")


class _MscFrAtmCaTpmAssignedBandwidthPool_Type(Integer32):
    """Custom type mscFrAtmCaTpmAssignedBandwidthPool based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("samePoolAsModule", 255))
    )


_MscFrAtmCaTpmAssignedBandwidthPool_Type.__name__ = "Integer32"
_MscFrAtmCaTpmAssignedBandwidthPool_Object = MibTableColumn
mscFrAtmCaTpmAssignedBandwidthPool = _MscFrAtmCaTpmAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 10, 1, 1),
    _MscFrAtmCaTpmAssignedBandwidthPool_Type()
)
mscFrAtmCaTpmAssignedBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmAssignedBandwidthPool.setStatus("mandatory")


class _MscFrAtmCaTpmTrafficParmConvPolicy_Type(Integer32):
    """Custom type mscFrAtmCaTpmTrafficParmConvPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("policy3", 3),
          ("policy4", 4),
          ("policy5", 5),
          ("policy6", 6),
          ("sameAsModule", 0))
    )


_MscFrAtmCaTpmTrafficParmConvPolicy_Type.__name__ = "Integer32"
_MscFrAtmCaTpmTrafficParmConvPolicy_Object = MibTableColumn
mscFrAtmCaTpmTrafficParmConvPolicy = _MscFrAtmCaTpmTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 10, 1, 2),
    _MscFrAtmCaTpmTrafficParmConvPolicy_Type()
)
mscFrAtmCaTpmTrafficParmConvPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmTrafficParmConvPolicy.setStatus("mandatory")


class _MscFrAtmCaTpmAverageFrameSize_Type(Integer32):
    """Custom type mscFrAtmCaTpmAverageFrameSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_MscFrAtmCaTpmAverageFrameSize_Type.__name__ = "Integer32"
_MscFrAtmCaTpmAverageFrameSize_Object = MibTableColumn
mscFrAtmCaTpmAverageFrameSize = _MscFrAtmCaTpmAverageFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 2, 10, 1, 3),
    _MscFrAtmCaTpmAverageFrameSize_Type()
)
mscFrAtmCaTpmAverageFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaTpmAverageFrameSize.setStatus("mandatory")
_MscFrAtmCaProvTable_Object = MibTable
mscFrAtmCaProvTable = _MscFrAtmCaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmCaProvTable.setStatus("mandatory")
_MscFrAtmCaProvEntry_Object = MibTableRow
mscFrAtmCaProvEntry = _MscFrAtmCaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 10, 1)
)
mscFrAtmCaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaProvEntry.setStatus("mandatory")


class _MscFrAtmCaCallAdmissionControl_Type(Integer32):
    """Custom type mscFrAtmCaCallAdmissionControl based on Integer32"""
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


_MscFrAtmCaCallAdmissionControl_Type.__name__ = "Integer32"
_MscFrAtmCaCallAdmissionControl_Object = MibTableColumn
mscFrAtmCaCallAdmissionControl = _MscFrAtmCaCallAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 10, 1, 1),
    _MscFrAtmCaCallAdmissionControl_Type()
)
mscFrAtmCaCallAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaCallAdmissionControl.setStatus("mandatory")


class _MscFrAtmCaOverrideLinkRate_Type(Unsigned32):
    """Custom type mscFrAtmCaOverrideLinkRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrAtmCaOverrideLinkRate_Type.__name__ = "Unsigned32"
_MscFrAtmCaOverrideLinkRate_Object = MibTableColumn
mscFrAtmCaOverrideLinkRate = _MscFrAtmCaOverrideLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 10, 1, 2),
    _MscFrAtmCaOverrideLinkRate_Type()
)
mscFrAtmCaOverrideLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaOverrideLinkRate.setStatus("mandatory")
_MscFrAtmCaSdTable_Object = MibTable
mscFrAtmCaSdTable = _MscFrAtmCaSdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmCaSdTable.setStatus("mandatory")
_MscFrAtmCaSdEntry_Object = MibTableRow
mscFrAtmCaSdEntry = _MscFrAtmCaSdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1)
)
mscFrAtmCaSdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaSdEntry.setStatus("mandatory")


class _MscFrAtmCaSdMode_Type(Integer32):
    """Custom type mscFrAtmCaSdMode based on Integer32"""
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
        *(("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_MscFrAtmCaSdMode_Type.__name__ = "Integer32"
_MscFrAtmCaSdMode_Object = MibTableColumn
mscFrAtmCaSdMode = _MscFrAtmCaSdMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1, 1),
    _MscFrAtmCaSdMode_Type()
)
mscFrAtmCaSdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSdMode.setStatus("mandatory")


class _MscFrAtmCaSdDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmCaSdDeToClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmCaSdDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmCaSdDeToClpMapping_Object = MibTableColumn
mscFrAtmCaSdDeToClpMapping = _MscFrAtmCaSdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1, 2),
    _MscFrAtmCaSdDeToClpMapping_Type()
)
mscFrAtmCaSdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSdDeToClpMapping.setStatus("mandatory")


class _MscFrAtmCaSdClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmCaSdClpToDeMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmCaSdClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmCaSdClpToDeMapping_Object = MibTableColumn
mscFrAtmCaSdClpToDeMapping = _MscFrAtmCaSdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1, 3),
    _MscFrAtmCaSdClpToDeMapping_Type()
)
mscFrAtmCaSdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSdClpToDeMapping.setStatus("mandatory")


class _MscFrAtmCaSdFecnToEfciMapping_Type(Integer32):
    """Custom type mscFrAtmCaSdFecnToEfciMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_MscFrAtmCaSdFecnToEfciMapping_Type.__name__ = "Integer32"
_MscFrAtmCaSdFecnToEfciMapping_Object = MibTableColumn
mscFrAtmCaSdFecnToEfciMapping = _MscFrAtmCaSdFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1, 4),
    _MscFrAtmCaSdFecnToEfciMapping_Type()
)
mscFrAtmCaSdFecnToEfciMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSdFecnToEfciMapping.setStatus("mandatory")


class _MscFrAtmCaSdCrToUuMapping_Type(Integer32):
    """Custom type mscFrAtmCaSdCrToUuMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_MscFrAtmCaSdCrToUuMapping_Type.__name__ = "Integer32"
_MscFrAtmCaSdCrToUuMapping_Object = MibTableColumn
mscFrAtmCaSdCrToUuMapping = _MscFrAtmCaSdCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 11, 1, 5),
    _MscFrAtmCaSdCrToUuMapping_Type()
)
mscFrAtmCaSdCrToUuMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSdCrToUuMapping.setStatus("obsolete")
_MscFrAtmCaNdTable_Object = MibTable
mscFrAtmCaNdTable = _MscFrAtmCaNdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmCaNdTable.setStatus("mandatory")
_MscFrAtmCaNdEntry_Object = MibTableRow
mscFrAtmCaNdEntry = _MscFrAtmCaNdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 12, 1)
)
mscFrAtmCaNdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaNdEntry.setStatus("mandatory")


class _MscFrAtmCaNdDeToClpMapping_Type(Integer32):
    """Custom type mscFrAtmCaNdDeToClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_MscFrAtmCaNdDeToClpMapping_Type.__name__ = "Integer32"
_MscFrAtmCaNdDeToClpMapping_Object = MibTableColumn
mscFrAtmCaNdDeToClpMapping = _MscFrAtmCaNdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 12, 1, 1),
    _MscFrAtmCaNdDeToClpMapping_Type()
)
mscFrAtmCaNdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaNdDeToClpMapping.setStatus("mandatory")


class _MscFrAtmCaNdClpToDeMapping_Type(Integer32):
    """Custom type mscFrAtmCaNdClpToDeMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("transparent", 3))
    )


_MscFrAtmCaNdClpToDeMapping_Type.__name__ = "Integer32"
_MscFrAtmCaNdClpToDeMapping_Object = MibTableColumn
mscFrAtmCaNdClpToDeMapping = _MscFrAtmCaNdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 12, 1, 2),
    _MscFrAtmCaNdClpToDeMapping_Type()
)
mscFrAtmCaNdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaNdClpToDeMapping.setStatus("mandatory")
_MscFrAtmCaIfQoSTable_Object = MibTable
mscFrAtmCaIfQoSTable = _MscFrAtmCaIfQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmCaIfQoSTable.setStatus("mandatory")
_MscFrAtmCaIfQoSEntry_Object = MibTableRow
mscFrAtmCaIfQoSEntry = _MscFrAtmCaIfQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13, 1)
)
mscFrAtmCaIfQoSEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaIfQoSEntry.setStatus("mandatory")


class _MscFrAtmCaSiwfEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmCaSiwfEmissionPriorityToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3))
    )


_MscFrAtmCaSiwfEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmCaSiwfEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmCaSiwfEmissionPriorityToIf = _MscFrAtmCaSiwfEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13, 1, 1),
    _MscFrAtmCaSiwfEmissionPriorityToIf_Type()
)
mscFrAtmCaSiwfEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSiwfEmissionPriorityToIf.setStatus("mandatory")


class _MscFrAtmCaSiwfTransferPriority_Type(Integer32):
    """Custom type mscFrAtmCaSiwfTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaSiwfTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmCaSiwfTransferPriority_Object = MibTableColumn
mscFrAtmCaSiwfTransferPriority = _MscFrAtmCaSiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13, 1, 2),
    _MscFrAtmCaSiwfTransferPriority_Type()
)
mscFrAtmCaSiwfTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaSiwfTransferPriority.setStatus("mandatory")


class _MscFrAtmCaNiwfEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrAtmCaNiwfEmissionPriorityToIf based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3))
    )


_MscFrAtmCaNiwfEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrAtmCaNiwfEmissionPriorityToIf_Object = MibTableColumn
mscFrAtmCaNiwfEmissionPriorityToIf = _MscFrAtmCaNiwfEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13, 1, 3),
    _MscFrAtmCaNiwfEmissionPriorityToIf_Type()
)
mscFrAtmCaNiwfEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaNiwfEmissionPriorityToIf.setStatus("mandatory")


class _MscFrAtmCaNiwfTransferPriority_Type(Integer32):
    """Custom type mscFrAtmCaNiwfTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaNiwfTransferPriority_Type.__name__ = "Integer32"
_MscFrAtmCaNiwfTransferPriority_Object = MibTableColumn
mscFrAtmCaNiwfTransferPriority = _MscFrAtmCaNiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 13, 1, 4),
    _MscFrAtmCaNiwfTransferPriority_Type()
)
mscFrAtmCaNiwfTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaNiwfTransferPriority.setStatus("mandatory")
_MscFrAtmCaOpTable_Object = MibTable
mscFrAtmCaOpTable = _MscFrAtmCaOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmCaOpTable.setStatus("mandatory")
_MscFrAtmCaOpEntry_Object = MibTableRow
mscFrAtmCaOpEntry = _MscFrAtmCaOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14, 1)
)
mscFrAtmCaOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaOpEntry.setStatus("mandatory")


class _MscFrAtmCaLinkRate_Type(Unsigned32):
    """Custom type mscFrAtmCaLinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrAtmCaLinkRate_Type.__name__ = "Unsigned32"
_MscFrAtmCaLinkRate_Object = MibTableColumn
mscFrAtmCaLinkRate = _MscFrAtmCaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14, 1, 1),
    _MscFrAtmCaLinkRate_Type()
)
mscFrAtmCaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaLinkRate.setStatus("mandatory")


class _MscFrAtmCaNailedUpPvcs_Type(Gauge32):
    """Custom type mscFrAtmCaNailedUpPvcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrAtmCaNailedUpPvcs_Type.__name__ = "Gauge32"
_MscFrAtmCaNailedUpPvcs_Object = MibTableColumn
mscFrAtmCaNailedUpPvcs = _MscFrAtmCaNailedUpPvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14, 1, 3),
    _MscFrAtmCaNailedUpPvcs_Type()
)
mscFrAtmCaNailedUpPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaNailedUpPvcs.setStatus("mandatory")


class _MscFrAtmCaTroubledDlcis_Type(Gauge32):
    """Custom type mscFrAtmCaTroubledDlcis based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrAtmCaTroubledDlcis_Type.__name__ = "Gauge32"
_MscFrAtmCaTroubledDlcis_Object = MibTableColumn
mscFrAtmCaTroubledDlcis = _MscFrAtmCaTroubledDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14, 1, 5),
    _MscFrAtmCaTroubledDlcis_Type()
)
mscFrAtmCaTroubledDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaTroubledDlcis.setStatus("mandatory")


class _MscFrAtmCaSoftPvcs_Type(Gauge32):
    """Custom type mscFrAtmCaSoftPvcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrAtmCaSoftPvcs_Type.__name__ = "Gauge32"
_MscFrAtmCaSoftPvcs_Object = MibTableColumn
mscFrAtmCaSoftPvcs = _MscFrAtmCaSoftPvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 14, 1, 6),
    _MscFrAtmCaSoftPvcs_Type()
)
mscFrAtmCaSoftPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaSoftPvcs.setStatus("mandatory")
_MscFrAtmCaAccountingOptionsTable_Object = MibTable
mscFrAtmCaAccountingOptionsTable = _MscFrAtmCaAccountingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 15)
)
if mibBuilder.loadTexts:
    mscFrAtmCaAccountingOptionsTable.setStatus("mandatory")
_MscFrAtmCaAccountingOptionsEntry_Object = MibTableRow
mscFrAtmCaAccountingOptionsEntry = _MscFrAtmCaAccountingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 15, 1)
)
mscFrAtmCaAccountingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaAccountingOptionsEntry.setStatus("mandatory")


class _MscFrAtmCaAccountClass_Type(Unsigned32):
    """Custom type mscFrAtmCaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrAtmCaAccountClass_Type.__name__ = "Unsigned32"
_MscFrAtmCaAccountClass_Object = MibTableColumn
mscFrAtmCaAccountClass = _MscFrAtmCaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 15, 1, 1),
    _MscFrAtmCaAccountClass_Type()
)
mscFrAtmCaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaAccountClass.setStatus("mandatory")


class _MscFrAtmCaAccountCollection_Type(OctetString):
    """Custom type mscFrAtmCaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrAtmCaAccountCollection_Type.__name__ = "OctetString"
_MscFrAtmCaAccountCollection_Object = MibTableColumn
mscFrAtmCaAccountCollection = _MscFrAtmCaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 15, 1, 2),
    _MscFrAtmCaAccountCollection_Type()
)
mscFrAtmCaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaAccountCollection.setStatus("mandatory")


class _MscFrAtmCaServiceExchange_Type(Unsigned32):
    """Custom type mscFrAtmCaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrAtmCaServiceExchange_Type.__name__ = "Unsigned32"
_MscFrAtmCaServiceExchange_Object = MibTableColumn
mscFrAtmCaServiceExchange = _MscFrAtmCaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 15, 1, 3),
    _MscFrAtmCaServiceExchange_Type()
)
mscFrAtmCaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaServiceExchange.setStatus("mandatory")
_MscFrAtmCaBwPoolTable_Object = MibTable
mscFrAtmCaBwPoolTable = _MscFrAtmCaBwPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 365)
)
if mibBuilder.loadTexts:
    mscFrAtmCaBwPoolTable.setStatus("mandatory")
_MscFrAtmCaBwPoolEntry_Object = MibTableRow
mscFrAtmCaBwPoolEntry = _MscFrAtmCaBwPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 365, 1)
)
mscFrAtmCaBwPoolEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaBwPoolIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaBwPoolEntry.setStatus("mandatory")


class _MscFrAtmCaBwPoolIndex_Type(Integer32):
    """Custom type mscFrAtmCaBwPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaBwPoolIndex_Type.__name__ = "Integer32"
_MscFrAtmCaBwPoolIndex_Object = MibTableColumn
mscFrAtmCaBwPoolIndex = _MscFrAtmCaBwPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 365, 1, 1),
    _MscFrAtmCaBwPoolIndex_Type()
)
mscFrAtmCaBwPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaBwPoolIndex.setStatus("mandatory")


class _MscFrAtmCaBwPoolValue_Type(Unsigned32):
    """Custom type mscFrAtmCaBwPoolValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrAtmCaBwPoolValue_Type.__name__ = "Unsigned32"
_MscFrAtmCaBwPoolValue_Object = MibTableColumn
mscFrAtmCaBwPoolValue = _MscFrAtmCaBwPoolValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 365, 1, 2),
    _MscFrAtmCaBwPoolValue_Type()
)
mscFrAtmCaBwPoolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCaBwPoolValue.setStatus("mandatory")
_MscFrAtmCaPoolProvBwTable_Object = MibTable
mscFrAtmCaPoolProvBwTable = _MscFrAtmCaPoolProvBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 366)
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolProvBwTable.setStatus("mandatory")
_MscFrAtmCaPoolProvBwEntry_Object = MibTableRow
mscFrAtmCaPoolProvBwEntry = _MscFrAtmCaPoolProvBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 366, 1)
)
mscFrAtmCaPoolProvBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaPoolProvBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolProvBwEntry.setStatus("mandatory")


class _MscFrAtmCaPoolProvBwIndex_Type(Integer32):
    """Custom type mscFrAtmCaPoolProvBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaPoolProvBwIndex_Type.__name__ = "Integer32"
_MscFrAtmCaPoolProvBwIndex_Object = MibTableColumn
mscFrAtmCaPoolProvBwIndex = _MscFrAtmCaPoolProvBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 366, 1, 1),
    _MscFrAtmCaPoolProvBwIndex_Type()
)
mscFrAtmCaPoolProvBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolProvBwIndex.setStatus("mandatory")


class _MscFrAtmCaPoolProvBwValue_Type(Gauge32):
    """Custom type mscFrAtmCaPoolProvBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrAtmCaPoolProvBwValue_Type.__name__ = "Gauge32"
_MscFrAtmCaPoolProvBwValue_Object = MibTableColumn
mscFrAtmCaPoolProvBwValue = _MscFrAtmCaPoolProvBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 366, 1, 2),
    _MscFrAtmCaPoolProvBwValue_Type()
)
mscFrAtmCaPoolProvBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolProvBwValue.setStatus("mandatory")
_MscFrAtmCaPoolAvailBwTable_Object = MibTable
mscFrAtmCaPoolAvailBwTable = _MscFrAtmCaPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 367)
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAvailBwTable.setStatus("mandatory")
_MscFrAtmCaPoolAvailBwEntry_Object = MibTableRow
mscFrAtmCaPoolAvailBwEntry = _MscFrAtmCaPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 367, 1)
)
mscFrAtmCaPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAvailBwEntry.setStatus("mandatory")


class _MscFrAtmCaPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrAtmCaPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrAtmCaPoolAvailBwIndex_Object = MibTableColumn
mscFrAtmCaPoolAvailBwIndex = _MscFrAtmCaPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 367, 1, 1),
    _MscFrAtmCaPoolAvailBwIndex_Type()
)
mscFrAtmCaPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAvailBwIndex.setStatus("mandatory")


class _MscFrAtmCaPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrAtmCaPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrAtmCaPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrAtmCaPoolAvailBwValue_Object = MibTableColumn
mscFrAtmCaPoolAvailBwValue = _MscFrAtmCaPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 367, 1, 2),
    _MscFrAtmCaPoolAvailBwValue_Type()
)
mscFrAtmCaPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAvailBwValue.setStatus("mandatory")
_MscFrAtmCaPoolAdmitBwTable_Object = MibTable
mscFrAtmCaPoolAdmitBwTable = _MscFrAtmCaPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 380)
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAdmitBwTable.setStatus("mandatory")
_MscFrAtmCaPoolAdmitBwEntry_Object = MibTableRow
mscFrAtmCaPoolAdmitBwEntry = _MscFrAtmCaPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 380, 1)
)
mscFrAtmCaPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmCaPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrAtmCaPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrAtmCaPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrAtmCaPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrAtmCaPoolAdmitBwIndex_Object = MibTableColumn
mscFrAtmCaPoolAdmitBwIndex = _MscFrAtmCaPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 380, 1, 1),
    _MscFrAtmCaPoolAdmitBwIndex_Type()
)
mscFrAtmCaPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrAtmCaPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrAtmCaPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrAtmCaPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrAtmCaPoolAdmitBwValue_Object = MibTableColumn
mscFrAtmCaPoolAdmitBwValue = _MscFrAtmCaPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 7, 380, 1, 2),
    _MscFrAtmCaPoolAdmitBwValue_Type()
)
mscFrAtmCaPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmCaPoolAdmitBwValue.setStatus("mandatory")
_MscFrAtmCidDataTable_Object = MibTable
mscFrAtmCidDataTable = _MscFrAtmCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 10)
)
if mibBuilder.loadTexts:
    mscFrAtmCidDataTable.setStatus("mandatory")
_MscFrAtmCidDataEntry_Object = MibTableRow
mscFrAtmCidDataEntry = _MscFrAtmCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 10, 1)
)
mscFrAtmCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmCidDataEntry.setStatus("mandatory")


class _MscFrAtmCustomerIdentifier_Type(Unsigned32):
    """Custom type mscFrAtmCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscFrAtmCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscFrAtmCustomerIdentifier_Object = MibTableColumn
mscFrAtmCustomerIdentifier = _MscFrAtmCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 10, 1, 1),
    _MscFrAtmCustomerIdentifier_Type()
)
mscFrAtmCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmCustomerIdentifier.setStatus("mandatory")
_MscFrAtmStateTable_Object = MibTable
mscFrAtmStateTable = _MscFrAtmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11)
)
if mibBuilder.loadTexts:
    mscFrAtmStateTable.setStatus("mandatory")
_MscFrAtmStateEntry_Object = MibTableRow
mscFrAtmStateEntry = _MscFrAtmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1)
)
mscFrAtmStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmStateEntry.setStatus("mandatory")


class _MscFrAtmAdminState_Type(Integer32):
    """Custom type mscFrAtmAdminState based on Integer32"""
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


_MscFrAtmAdminState_Type.__name__ = "Integer32"
_MscFrAtmAdminState_Object = MibTableColumn
mscFrAtmAdminState = _MscFrAtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 1),
    _MscFrAtmAdminState_Type()
)
mscFrAtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAdminState.setStatus("mandatory")


class _MscFrAtmOperationalState_Type(Integer32):
    """Custom type mscFrAtmOperationalState based on Integer32"""
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


_MscFrAtmOperationalState_Type.__name__ = "Integer32"
_MscFrAtmOperationalState_Object = MibTableColumn
mscFrAtmOperationalState = _MscFrAtmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 2),
    _MscFrAtmOperationalState_Type()
)
mscFrAtmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmOperationalState.setStatus("mandatory")


class _MscFrAtmUsageState_Type(Integer32):
    """Custom type mscFrAtmUsageState based on Integer32"""
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


_MscFrAtmUsageState_Type.__name__ = "Integer32"
_MscFrAtmUsageState_Object = MibTableColumn
mscFrAtmUsageState = _MscFrAtmUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 3),
    _MscFrAtmUsageState_Type()
)
mscFrAtmUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmUsageState.setStatus("mandatory")


class _MscFrAtmAvailabilityStatus_Type(OctetString):
    """Custom type mscFrAtmAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrAtmAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrAtmAvailabilityStatus_Object = MibTableColumn
mscFrAtmAvailabilityStatus = _MscFrAtmAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 4),
    _MscFrAtmAvailabilityStatus_Type()
)
mscFrAtmAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAvailabilityStatus.setStatus("mandatory")


class _MscFrAtmProceduralStatus_Type(OctetString):
    """Custom type mscFrAtmProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrAtmProceduralStatus_Type.__name__ = "OctetString"
_MscFrAtmProceduralStatus_Object = MibTableColumn
mscFrAtmProceduralStatus = _MscFrAtmProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 5),
    _MscFrAtmProceduralStatus_Type()
)
mscFrAtmProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmProceduralStatus.setStatus("mandatory")


class _MscFrAtmControlStatus_Type(OctetString):
    """Custom type mscFrAtmControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrAtmControlStatus_Type.__name__ = "OctetString"
_MscFrAtmControlStatus_Object = MibTableColumn
mscFrAtmControlStatus = _MscFrAtmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 6),
    _MscFrAtmControlStatus_Type()
)
mscFrAtmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmControlStatus.setStatus("mandatory")


class _MscFrAtmAlarmStatus_Type(OctetString):
    """Custom type mscFrAtmAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrAtmAlarmStatus_Type.__name__ = "OctetString"
_MscFrAtmAlarmStatus_Object = MibTableColumn
mscFrAtmAlarmStatus = _MscFrAtmAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 7),
    _MscFrAtmAlarmStatus_Type()
)
mscFrAtmAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmAlarmStatus.setStatus("mandatory")


class _MscFrAtmStandbyStatus_Type(Integer32):
    """Custom type mscFrAtmStandbyStatus based on Integer32"""
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


_MscFrAtmStandbyStatus_Type.__name__ = "Integer32"
_MscFrAtmStandbyStatus_Object = MibTableColumn
mscFrAtmStandbyStatus = _MscFrAtmStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 8),
    _MscFrAtmStandbyStatus_Type()
)
mscFrAtmStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmStandbyStatus.setStatus("mandatory")


class _MscFrAtmUnknownStatus_Type(Integer32):
    """Custom type mscFrAtmUnknownStatus based on Integer32"""
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


_MscFrAtmUnknownStatus_Type.__name__ = "Integer32"
_MscFrAtmUnknownStatus_Object = MibTableColumn
mscFrAtmUnknownStatus = _MscFrAtmUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 11, 1, 9),
    _MscFrAtmUnknownStatus_Type()
)
mscFrAtmUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmUnknownStatus.setStatus("mandatory")
_MscFrAtmStatsTable_Object = MibTable
mscFrAtmStatsTable = _MscFrAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 12)
)
if mibBuilder.loadTexts:
    mscFrAtmStatsTable.setStatus("mandatory")
_MscFrAtmStatsEntry_Object = MibTableRow
mscFrAtmStatsEntry = _MscFrAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 12, 1)
)
mscFrAtmStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmStatsEntry.setStatus("mandatory")


class _MscFrAtmLastUnknownDlci_Type(Unsigned32):
    """Custom type mscFrAtmLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFrAtmLastUnknownDlci_Type.__name__ = "Unsigned32"
_MscFrAtmLastUnknownDlci_Object = MibTableColumn
mscFrAtmLastUnknownDlci = _MscFrAtmLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 12, 1, 1),
    _MscFrAtmLastUnknownDlci_Type()
)
mscFrAtmLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmLastUnknownDlci.setStatus("mandatory")
_MscFrAtmUnknownDlciFramesFromIf_Type = Counter32
_MscFrAtmUnknownDlciFramesFromIf_Object = MibTableColumn
mscFrAtmUnknownDlciFramesFromIf = _MscFrAtmUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 12, 1, 2),
    _MscFrAtmUnknownDlciFramesFromIf_Type()
)
mscFrAtmUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmUnknownDlciFramesFromIf.setStatus("mandatory")
_MscFrAtmInvalidHeaderFramesFromIf_Type = Counter32
_MscFrAtmInvalidHeaderFramesFromIf_Object = MibTableColumn
mscFrAtmInvalidHeaderFramesFromIf = _MscFrAtmInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 12, 1, 3),
    _MscFrAtmInvalidHeaderFramesFromIf_Type()
)
mscFrAtmInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmInvalidHeaderFramesFromIf.setStatus("mandatory")
_MscFrAtmIfEntryTable_Object = MibTable
mscFrAtmIfEntryTable = _MscFrAtmIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 13)
)
if mibBuilder.loadTexts:
    mscFrAtmIfEntryTable.setStatus("mandatory")
_MscFrAtmIfEntryEntry_Object = MibTableRow
mscFrAtmIfEntryEntry = _MscFrAtmIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 13, 1)
)
mscFrAtmIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmIfEntryEntry.setStatus("mandatory")


class _MscFrAtmIfAdminStatus_Type(Integer32):
    """Custom type mscFrAtmIfAdminStatus based on Integer32"""
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


_MscFrAtmIfAdminStatus_Type.__name__ = "Integer32"
_MscFrAtmIfAdminStatus_Object = MibTableColumn
mscFrAtmIfAdminStatus = _MscFrAtmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 13, 1, 1),
    _MscFrAtmIfAdminStatus_Type()
)
mscFrAtmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmIfAdminStatus.setStatus("mandatory")


class _MscFrAtmIfIndex_Type(InterfaceIndex):
    """Custom type mscFrAtmIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrAtmIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrAtmIfIndex_Object = MibTableColumn
mscFrAtmIfIndex = _MscFrAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 13, 1, 2),
    _MscFrAtmIfIndex_Type()
)
mscFrAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmIfIndex.setStatus("mandatory")
_MscFrAtmOperStatusTable_Object = MibTable
mscFrAtmOperStatusTable = _MscFrAtmOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 14)
)
if mibBuilder.loadTexts:
    mscFrAtmOperStatusTable.setStatus("mandatory")
_MscFrAtmOperStatusEntry_Object = MibTableRow
mscFrAtmOperStatusEntry = _MscFrAtmOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 14, 1)
)
mscFrAtmOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmOperStatusEntry.setStatus("mandatory")


class _MscFrAtmSnmpOperStatus_Type(Integer32):
    """Custom type mscFrAtmSnmpOperStatus based on Integer32"""
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


_MscFrAtmSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrAtmSnmpOperStatus_Object = MibTableColumn
mscFrAtmSnmpOperStatus = _MscFrAtmSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 14, 1, 1),
    _MscFrAtmSnmpOperStatus_Type()
)
mscFrAtmSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmSnmpOperStatus.setStatus("mandatory")
_MscFrAtmEmissionPriorityQsTable_Object = MibTable
mscFrAtmEmissionPriorityQsTable = _MscFrAtmEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 15)
)
if mibBuilder.loadTexts:
    mscFrAtmEmissionPriorityQsTable.setStatus("mandatory")
_MscFrAtmEmissionPriorityQsEntry_Object = MibTableRow
mscFrAtmEmissionPriorityQsEntry = _MscFrAtmEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 15, 1)
)
mscFrAtmEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmEmissionPriorityQsEntry.setStatus("mandatory")


class _MscFrAtmNumberOfEmissionQs_Type(Unsigned32):
    """Custom type mscFrAtmNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_MscFrAtmNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_MscFrAtmNumberOfEmissionQs_Object = MibTableColumn
mscFrAtmNumberOfEmissionQs = _MscFrAtmNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 15, 1, 1),
    _MscFrAtmNumberOfEmissionQs_Type()
)
mscFrAtmNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrAtmNumberOfEmissionQs.setStatus("mandatory")
_MscFrAtmFrmToIfByQueueTable_Object = MibTable
mscFrAtmFrmToIfByQueueTable = _MscFrAtmFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 341)
)
if mibBuilder.loadTexts:
    mscFrAtmFrmToIfByQueueTable.setStatus("mandatory")
_MscFrAtmFrmToIfByQueueEntry_Object = MibTableRow
mscFrAtmFrmToIfByQueueEntry = _MscFrAtmFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 341, 1)
)
mscFrAtmFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmFrmToIfByQueueEntry.setStatus("mandatory")


class _MscFrAtmFrmToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrAtmFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrAtmFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrAtmFrmToIfByQueueIndex_Object = MibTableColumn
mscFrAtmFrmToIfByQueueIndex = _MscFrAtmFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 341, 1, 1),
    _MscFrAtmFrmToIfByQueueIndex_Type()
)
mscFrAtmFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmFrmToIfByQueueIndex.setStatus("mandatory")


class _MscFrAtmFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrAtmFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrAtmFrmToIfByQueueValue_Object = MibTableColumn
mscFrAtmFrmToIfByQueueValue = _MscFrAtmFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 341, 1, 2),
    _MscFrAtmFrmToIfByQueueValue_Type()
)
mscFrAtmFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmFrmToIfByQueueValue.setStatus("mandatory")
_MscFrAtmOctetToIfByQueueTable_Object = MibTable
mscFrAtmOctetToIfByQueueTable = _MscFrAtmOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 342)
)
if mibBuilder.loadTexts:
    mscFrAtmOctetToIfByQueueTable.setStatus("mandatory")
_MscFrAtmOctetToIfByQueueEntry_Object = MibTableRow
mscFrAtmOctetToIfByQueueEntry = _MscFrAtmOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 342, 1)
)
mscFrAtmOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB", "mscFrAtmOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrAtmOctetToIfByQueueEntry.setStatus("mandatory")


class _MscFrAtmOctetToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrAtmOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrAtmOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrAtmOctetToIfByQueueIndex_Object = MibTableColumn
mscFrAtmOctetToIfByQueueIndex = _MscFrAtmOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 342, 1, 1),
    _MscFrAtmOctetToIfByQueueIndex_Type()
)
mscFrAtmOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrAtmOctetToIfByQueueIndex.setStatus("mandatory")


class _MscFrAtmOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrAtmOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrAtmOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrAtmOctetToIfByQueueValue_Object = MibTableColumn
mscFrAtmOctetToIfByQueueValue = _MscFrAtmOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 72, 342, 1, 2),
    _MscFrAtmOctetToIfByQueueValue_Type()
)
mscFrAtmOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrAtmOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayAtmMIB_ObjectIdentity = ObjectIdentity
frameRelayAtmMIB = _FrameRelayAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51)
)
_FrameRelayAtmGroup_ObjectIdentity = ObjectIdentity
frameRelayAtmGroup = _FrameRelayAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 1)
)
_FrameRelayAtmGroupCA_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupCA = _FrameRelayAtmGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 1, 1)
)
_FrameRelayAtmGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupCA02 = _FrameRelayAtmGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 1, 1, 3)
)
_FrameRelayAtmGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupCA02A = _FrameRelayAtmGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 1, 1, 3, 2)
)
_FrameRelayAtmCapabilities_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilities = _FrameRelayAtmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 3)
)
_FrameRelayAtmCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesCA = _FrameRelayAtmCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 3, 1)
)
_FrameRelayAtmCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesCA02 = _FrameRelayAtmCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 3, 1, 3)
)
_FrameRelayAtmCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesCA02A = _FrameRelayAtmCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 51, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayAtmMIB",
    **{"mscFrAtm": mscFrAtm,
       "mscFrAtmRowStatusTable": mscFrAtmRowStatusTable,
       "mscFrAtmRowStatusEntry": mscFrAtmRowStatusEntry,
       "mscFrAtmRowStatus": mscFrAtmRowStatus,
       "mscFrAtmComponentName": mscFrAtmComponentName,
       "mscFrAtmStorageType": mscFrAtmStorageType,
       "mscFrAtmIndex": mscFrAtmIndex,
       "mscFrAtmFramer": mscFrAtmFramer,
       "mscFrAtmFramerRowStatusTable": mscFrAtmFramerRowStatusTable,
       "mscFrAtmFramerRowStatusEntry": mscFrAtmFramerRowStatusEntry,
       "mscFrAtmFramerRowStatus": mscFrAtmFramerRowStatus,
       "mscFrAtmFramerComponentName": mscFrAtmFramerComponentName,
       "mscFrAtmFramerStorageType": mscFrAtmFramerStorageType,
       "mscFrAtmFramerIndex": mscFrAtmFramerIndex,
       "mscFrAtmFramerProvTable": mscFrAtmFramerProvTable,
       "mscFrAtmFramerProvEntry": mscFrAtmFramerProvEntry,
       "mscFrAtmFramerInterfaceName": mscFrAtmFramerInterfaceName,
       "mscFrAtmFramerLinkTable": mscFrAtmFramerLinkTable,
       "mscFrAtmFramerLinkEntry": mscFrAtmFramerLinkEntry,
       "mscFrAtmFramerDataInversion": mscFrAtmFramerDataInversion,
       "mscFrAtmFramerFrameCrcType": mscFrAtmFramerFrameCrcType,
       "mscFrAtmFramerFlagsBetweenFrames": mscFrAtmFramerFlagsBetweenFrames,
       "mscFrAtmFramerStateTable": mscFrAtmFramerStateTable,
       "mscFrAtmFramerStateEntry": mscFrAtmFramerStateEntry,
       "mscFrAtmFramerAdminState": mscFrAtmFramerAdminState,
       "mscFrAtmFramerOperationalState": mscFrAtmFramerOperationalState,
       "mscFrAtmFramerUsageState": mscFrAtmFramerUsageState,
       "mscFrAtmFramerStatsTable": mscFrAtmFramerStatsTable,
       "mscFrAtmFramerStatsEntry": mscFrAtmFramerStatsEntry,
       "mscFrAtmFramerFrmToIf": mscFrAtmFramerFrmToIf,
       "mscFrAtmFramerFrmFromIf": mscFrAtmFramerFrmFromIf,
       "mscFrAtmFramerOctetFromIf": mscFrAtmFramerOctetFromIf,
       "mscFrAtmFramerAborts": mscFrAtmFramerAborts,
       "mscFrAtmFramerCrcErrors": mscFrAtmFramerCrcErrors,
       "mscFrAtmFramerLrcErrors": mscFrAtmFramerLrcErrors,
       "mscFrAtmFramerNonOctetErrors": mscFrAtmFramerNonOctetErrors,
       "mscFrAtmFramerOverruns": mscFrAtmFramerOverruns,
       "mscFrAtmFramerUnderruns": mscFrAtmFramerUnderruns,
       "mscFrAtmFramerLargeFrmErrors": mscFrAtmFramerLargeFrmErrors,
       "mscFrAtmFramerFrmModeErrors": mscFrAtmFramerFrmModeErrors,
       "mscFrAtmFramerFrmToIf64": mscFrAtmFramerFrmToIf64,
       "mscFrAtmFramerFrmFromIf64": mscFrAtmFramerFrmFromIf64,
       "mscFrAtmFramerOctetFromIf64": mscFrAtmFramerOctetFromIf64,
       "mscFrAtmFramerUtilTable": mscFrAtmFramerUtilTable,
       "mscFrAtmFramerUtilEntry": mscFrAtmFramerUtilEntry,
       "mscFrAtmFramerNormPrioLinkUtilToIf": mscFrAtmFramerNormPrioLinkUtilToIf,
       "mscFrAtmFramerNormPrioLinkUtilFromIf": mscFrAtmFramerNormPrioLinkUtilFromIf,
       "mscFrAtmLmi": mscFrAtmLmi,
       "mscFrAtmLmiRowStatusTable": mscFrAtmLmiRowStatusTable,
       "mscFrAtmLmiRowStatusEntry": mscFrAtmLmiRowStatusEntry,
       "mscFrAtmLmiRowStatus": mscFrAtmLmiRowStatus,
       "mscFrAtmLmiComponentName": mscFrAtmLmiComponentName,
       "mscFrAtmLmiStorageType": mscFrAtmLmiStorageType,
       "mscFrAtmLmiIndex": mscFrAtmLmiIndex,
       "mscFrAtmLmiParmsTable": mscFrAtmLmiParmsTable,
       "mscFrAtmLmiParmsEntry": mscFrAtmLmiParmsEntry,
       "mscFrAtmLmiProcedures": mscFrAtmLmiProcedures,
       "mscFrAtmLmiAsyncStatusReport": mscFrAtmLmiAsyncStatusReport,
       "mscFrAtmLmiErrorEventThreshold": mscFrAtmLmiErrorEventThreshold,
       "mscFrAtmLmiEventCount": mscFrAtmLmiEventCount,
       "mscFrAtmLmiCheckPointTimer": mscFrAtmLmiCheckPointTimer,
       "mscFrAtmLmiMessageCountTimer": mscFrAtmLmiMessageCountTimer,
       "mscFrAtmLmiIgnoreActiveBit": mscFrAtmLmiIgnoreActiveBit,
       "mscFrAtmLmiSide": mscFrAtmLmiSide,
       "mscFrAtmLmiPvcConfigParmsInFsr": mscFrAtmLmiPvcConfigParmsInFsr,
       "mscFrAtmLmiStateTable": mscFrAtmLmiStateTable,
       "mscFrAtmLmiStateEntry": mscFrAtmLmiStateEntry,
       "mscFrAtmLmiAdminState": mscFrAtmLmiAdminState,
       "mscFrAtmLmiOperationalState": mscFrAtmLmiOperationalState,
       "mscFrAtmLmiUsageState": mscFrAtmLmiUsageState,
       "mscFrAtmLmiPsiTable": mscFrAtmLmiPsiTable,
       "mscFrAtmLmiPsiEntry": mscFrAtmLmiPsiEntry,
       "mscFrAtmLmiProtocolStatus": mscFrAtmLmiProtocolStatus,
       "mscFrAtmLmiOpProcedures": mscFrAtmLmiOpProcedures,
       "mscFrAtmLmiStatsTable": mscFrAtmLmiStatsTable,
       "mscFrAtmLmiStatsEntry": mscFrAtmLmiStatsEntry,
       "mscFrAtmLmiKeepAliveStatusToIf": mscFrAtmLmiKeepAliveStatusToIf,
       "mscFrAtmLmiFullStatusToIf": mscFrAtmLmiFullStatusToIf,
       "mscFrAtmLmiKeepAliveStatusEnqFromIf": mscFrAtmLmiKeepAliveStatusEnqFromIf,
       "mscFrAtmLmiFullStatusEnqFromIf": mscFrAtmLmiFullStatusEnqFromIf,
       "mscFrAtmLmiNetworkSideEventHistory": mscFrAtmLmiNetworkSideEventHistory,
       "mscFrAtmLmiProtocolErrors": mscFrAtmLmiProtocolErrors,
       "mscFrAtmLmiUnexpectedIes": mscFrAtmLmiUnexpectedIes,
       "mscFrAtmLmiSequenceErrors": mscFrAtmLmiSequenceErrors,
       "mscFrAtmLmiUnexpectedReports": mscFrAtmLmiUnexpectedReports,
       "mscFrAtmLmiPollingVerifTimeouts": mscFrAtmLmiPollingVerifTimeouts,
       "mscFrAtmLmiKeepAliveEnqToIf": mscFrAtmLmiKeepAliveEnqToIf,
       "mscFrAtmLmiFullStatusEnqToIf": mscFrAtmLmiFullStatusEnqToIf,
       "mscFrAtmLmiUserSideEventHistory": mscFrAtmLmiUserSideEventHistory,
       "mscFrAtmLmiStatusSequenceErrors": mscFrAtmLmiStatusSequenceErrors,
       "mscFrAtmLmiNoStatusReportCount": mscFrAtmLmiNoStatusReportCount,
       "mscFrAtmLmiUspParmsTable": mscFrAtmLmiUspParmsTable,
       "mscFrAtmLmiUspParmsEntry": mscFrAtmLmiUspParmsEntry,
       "mscFrAtmLmiFullStatusPollingCycles": mscFrAtmLmiFullStatusPollingCycles,
       "mscFrAtmLmiLinkVerificationTimer": mscFrAtmLmiLinkVerificationTimer,
       "mscFrAtmDlci": mscFrAtmDlci,
       "mscFrAtmDlciRowStatusTable": mscFrAtmDlciRowStatusTable,
       "mscFrAtmDlciRowStatusEntry": mscFrAtmDlciRowStatusEntry,
       "mscFrAtmDlciRowStatus": mscFrAtmDlciRowStatus,
       "mscFrAtmDlciComponentName": mscFrAtmDlciComponentName,
       "mscFrAtmDlciStorageType": mscFrAtmDlciStorageType,
       "mscFrAtmDlciIndex": mscFrAtmDlciIndex,
       "mscFrAtmDlciSp": mscFrAtmDlciSp,
       "mscFrAtmDlciSpRowStatusTable": mscFrAtmDlciSpRowStatusTable,
       "mscFrAtmDlciSpRowStatusEntry": mscFrAtmDlciSpRowStatusEntry,
       "mscFrAtmDlciSpRowStatus": mscFrAtmDlciSpRowStatus,
       "mscFrAtmDlciSpComponentName": mscFrAtmDlciSpComponentName,
       "mscFrAtmDlciSpStorageType": mscFrAtmDlciSpStorageType,
       "mscFrAtmDlciSpIndex": mscFrAtmDlciSpIndex,
       "mscFrAtmDlciSpProvTable": mscFrAtmDlciSpProvTable,
       "mscFrAtmDlciSpProvEntry": mscFrAtmDlciSpProvEntry,
       "mscFrAtmDlciSpMaximumFrameSize": mscFrAtmDlciSpMaximumFrameSize,
       "mscFrAtmDlciSpRateEnforcement": mscFrAtmDlciSpRateEnforcement,
       "mscFrAtmDlciSpCommittedInformationRate": mscFrAtmDlciSpCommittedInformationRate,
       "mscFrAtmDlciSpCommittedBurstSize": mscFrAtmDlciSpCommittedBurstSize,
       "mscFrAtmDlciSpExcessBurstSize": mscFrAtmDlciSpExcessBurstSize,
       "mscFrAtmDlciSpMeasurementInterval": mscFrAtmDlciSpMeasurementInterval,
       "mscFrAtmDlciSpEmissionPriorityToIf": mscFrAtmDlciSpEmissionPriorityToIf,
       "mscFrAtmDlciSpEmissionPrioToIf": mscFrAtmDlciSpEmissionPrioToIf,
       "mscFrAtmDlciSpAccounting": mscFrAtmDlciSpAccounting,
       "mscFrAtmDlciSiwf": mscFrAtmDlciSiwf,
       "mscFrAtmDlciSiwfRowStatusTable": mscFrAtmDlciSiwfRowStatusTable,
       "mscFrAtmDlciSiwfRowStatusEntry": mscFrAtmDlciSiwfRowStatusEntry,
       "mscFrAtmDlciSiwfRowStatus": mscFrAtmDlciSiwfRowStatus,
       "mscFrAtmDlciSiwfComponentName": mscFrAtmDlciSiwfComponentName,
       "mscFrAtmDlciSiwfStorageType": mscFrAtmDlciSiwfStorageType,
       "mscFrAtmDlciSiwfIndex": mscFrAtmDlciSiwfIndex,
       "mscFrAtmDlciSiwfSd": mscFrAtmDlciSiwfSd,
       "mscFrAtmDlciSiwfSdRowStatusTable": mscFrAtmDlciSiwfSdRowStatusTable,
       "mscFrAtmDlciSiwfSdRowStatusEntry": mscFrAtmDlciSiwfSdRowStatusEntry,
       "mscFrAtmDlciSiwfSdRowStatus": mscFrAtmDlciSiwfSdRowStatus,
       "mscFrAtmDlciSiwfSdComponentName": mscFrAtmDlciSiwfSdComponentName,
       "mscFrAtmDlciSiwfSdStorageType": mscFrAtmDlciSiwfSdStorageType,
       "mscFrAtmDlciSiwfSdIndex": mscFrAtmDlciSiwfSdIndex,
       "mscFrAtmDlciSiwfSdProvTable": mscFrAtmDlciSiwfSdProvTable,
       "mscFrAtmDlciSiwfSdProvEntry": mscFrAtmDlciSiwfSdProvEntry,
       "mscFrAtmDlciSiwfSdMode": mscFrAtmDlciSiwfSdMode,
       "mscFrAtmDlciSiwfSdDeToClpMapping": mscFrAtmDlciSiwfSdDeToClpMapping,
       "mscFrAtmDlciSiwfSdClpToDeMapping": mscFrAtmDlciSiwfSdClpToDeMapping,
       "mscFrAtmDlciSiwfSdFecnToEfciMapping": mscFrAtmDlciSiwfSdFecnToEfciMapping,
       "mscFrAtmDlciSiwfSdCrToUuMapping": mscFrAtmDlciSiwfSdCrToUuMapping,
       "mscFrAtmDlciSiwfNPvc": mscFrAtmDlciSiwfNPvc,
       "mscFrAtmDlciSiwfNPvcRowStatusTable": mscFrAtmDlciSiwfNPvcRowStatusTable,
       "mscFrAtmDlciSiwfNPvcRowStatusEntry": mscFrAtmDlciSiwfNPvcRowStatusEntry,
       "mscFrAtmDlciSiwfNPvcRowStatus": mscFrAtmDlciSiwfNPvcRowStatus,
       "mscFrAtmDlciSiwfNPvcComponentName": mscFrAtmDlciSiwfNPvcComponentName,
       "mscFrAtmDlciSiwfNPvcStorageType": mscFrAtmDlciSiwfNPvcStorageType,
       "mscFrAtmDlciSiwfNPvcIndex": mscFrAtmDlciSiwfNPvcIndex,
       "mscFrAtmDlciSiwfNPvcProvTable": mscFrAtmDlciSiwfNPvcProvTable,
       "mscFrAtmDlciSiwfNPvcProvEntry": mscFrAtmDlciSiwfNPvcProvEntry,
       "mscFrAtmDlciSiwfNPvcAtmConnection": mscFrAtmDlciSiwfNPvcAtmConnection,
       "mscFrAtmDlciSiwfNPvcCorrelationTag": mscFrAtmDlciSiwfNPvcCorrelationTag,
       "mscFrAtmDlciSiwfNPvcSiwfNpvcOpTable": mscFrAtmDlciSiwfNPvcSiwfNpvcOpTable,
       "mscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry": mscFrAtmDlciSiwfNPvcSiwfNpvcOpEntry,
       "mscFrAtmDlciSiwfNPvcConnectionToAtm": mscFrAtmDlciSiwfNPvcConnectionToAtm,
       "mscFrAtmDlciSiwfSPvc": mscFrAtmDlciSiwfSPvc,
       "mscFrAtmDlciSiwfSPvcRowStatusTable": mscFrAtmDlciSiwfSPvcRowStatusTable,
       "mscFrAtmDlciSiwfSPvcRowStatusEntry": mscFrAtmDlciSiwfSPvcRowStatusEntry,
       "mscFrAtmDlciSiwfSPvcRowStatus": mscFrAtmDlciSiwfSPvcRowStatus,
       "mscFrAtmDlciSiwfSPvcComponentName": mscFrAtmDlciSiwfSPvcComponentName,
       "mscFrAtmDlciSiwfSPvcStorageType": mscFrAtmDlciSiwfSPvcStorageType,
       "mscFrAtmDlciSiwfSPvcIndex": mscFrAtmDlciSiwfSPvcIndex,
       "mscFrAtmDlciSiwfSPvcProvTable": mscFrAtmDlciSiwfSPvcProvTable,
       "mscFrAtmDlciSiwfSPvcProvEntry": mscFrAtmDlciSiwfSPvcProvEntry,
       "mscFrAtmDlciSiwfSPvcRemoteAddress": mscFrAtmDlciSiwfSPvcRemoteAddress,
       "mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier": mscFrAtmDlciSiwfSPvcRemoteConnectionIdentifier,
       "mscFrAtmDlciSiwfSPvcCorrelationTag": mscFrAtmDlciSiwfSPvcCorrelationTag,
       "mscFrAtmDlciSiwfQoS": mscFrAtmDlciSiwfQoS,
       "mscFrAtmDlciSiwfQoSRowStatusTable": mscFrAtmDlciSiwfQoSRowStatusTable,
       "mscFrAtmDlciSiwfQoSRowStatusEntry": mscFrAtmDlciSiwfQoSRowStatusEntry,
       "mscFrAtmDlciSiwfQoSRowStatus": mscFrAtmDlciSiwfQoSRowStatus,
       "mscFrAtmDlciSiwfQoSComponentName": mscFrAtmDlciSiwfQoSComponentName,
       "mscFrAtmDlciSiwfQoSStorageType": mscFrAtmDlciSiwfQoSStorageType,
       "mscFrAtmDlciSiwfQoSIndex": mscFrAtmDlciSiwfQoSIndex,
       "mscFrAtmDlciSiwfQoSProvTable": mscFrAtmDlciSiwfQoSProvTable,
       "mscFrAtmDlciSiwfQoSProvEntry": mscFrAtmDlciSiwfQoSProvEntry,
       "mscFrAtmDlciSiwfQoSEmissionPriorityToIf": mscFrAtmDlciSiwfQoSEmissionPriorityToIf,
       "mscFrAtmDlciSiwfQoSTransferPriority": mscFrAtmDlciSiwfQoSTransferPriority,
       "mscFrAtmDlciSiwfAtmCon": mscFrAtmDlciSiwfAtmCon,
       "mscFrAtmDlciSiwfAtmConRowStatusTable": mscFrAtmDlciSiwfAtmConRowStatusTable,
       "mscFrAtmDlciSiwfAtmConRowStatusEntry": mscFrAtmDlciSiwfAtmConRowStatusEntry,
       "mscFrAtmDlciSiwfAtmConRowStatus": mscFrAtmDlciSiwfAtmConRowStatus,
       "mscFrAtmDlciSiwfAtmConComponentName": mscFrAtmDlciSiwfAtmConComponentName,
       "mscFrAtmDlciSiwfAtmConStorageType": mscFrAtmDlciSiwfAtmConStorageType,
       "mscFrAtmDlciSiwfAtmConIndex": mscFrAtmDlciSiwfAtmConIndex,
       "mscFrAtmDlciSiwfAtmConOperTable": mscFrAtmDlciSiwfAtmConOperTable,
       "mscFrAtmDlciSiwfAtmConOperEntry": mscFrAtmDlciSiwfAtmConOperEntry,
       "mscFrAtmDlciSiwfAtmConNextHop": mscFrAtmDlciSiwfAtmConNextHop,
       "mscFrAtmDlciSiwfConnOpTable": mscFrAtmDlciSiwfConnOpTable,
       "mscFrAtmDlciSiwfConnOpEntry": mscFrAtmDlciSiwfConnOpEntry,
       "mscFrAtmDlciSiwfDiscardPriority": mscFrAtmDlciSiwfDiscardPriority,
       "mscFrAtmDlciSiwfAtmServiceCategory": mscFrAtmDlciSiwfAtmServiceCategory,
       "mscFrAtmDlciSiwfTrafficParmConvPolicy": mscFrAtmDlciSiwfTrafficParmConvPolicy,
       "mscFrAtmDlciSiwfAvgFrameSize": mscFrAtmDlciSiwfAvgFrameSize,
       "mscFrAtmDlciSiwfRemoteAddress": mscFrAtmDlciSiwfRemoteAddress,
       "mscFrAtmDlciSiwfRemoteConnectionIdentifier": mscFrAtmDlciSiwfRemoteConnectionIdentifier,
       "mscFrAtmDlciSiwfSdOpTable": mscFrAtmDlciSiwfSdOpTable,
       "mscFrAtmDlciSiwfSdOpEntry": mscFrAtmDlciSiwfSdOpEntry,
       "mscFrAtmDlciSiwfMode": mscFrAtmDlciSiwfMode,
       "mscFrAtmDlciSiwfDeToClpMapping": mscFrAtmDlciSiwfDeToClpMapping,
       "mscFrAtmDlciSiwfClpToDeMapping": mscFrAtmDlciSiwfClpToDeMapping,
       "mscFrAtmDlciSiwfFecnToEfciMapping": mscFrAtmDlciSiwfFecnToEfciMapping,
       "mscFrAtmDlciSiwfCrToUuMapping": mscFrAtmDlciSiwfCrToUuMapping,
       "mscFrAtmDlciSiwfTransferPriority": mscFrAtmDlciSiwfTransferPriority,
       "mscFrAtmDlciSiwfAssignedBandwidthPool": mscFrAtmDlciSiwfAssignedBandwidthPool,
       "mscFrAtmDlciSiwfSiwfSpvcOpTable": mscFrAtmDlciSiwfSiwfSpvcOpTable,
       "mscFrAtmDlciSiwfSiwfSpvcOpEntry": mscFrAtmDlciSiwfSiwfSpvcOpEntry,
       "mscFrAtmDlciSiwfPeakCellRate0": mscFrAtmDlciSiwfPeakCellRate0,
       "mscFrAtmDlciSiwfPeakCellRate01": mscFrAtmDlciSiwfPeakCellRate01,
       "mscFrAtmDlciSiwfSustainedCellRate0": mscFrAtmDlciSiwfSustainedCellRate0,
       "mscFrAtmDlciSiwfSustainedCellRate01": mscFrAtmDlciSiwfSustainedCellRate01,
       "mscFrAtmDlciSiwfMaximumBurstSize0": mscFrAtmDlciSiwfMaximumBurstSize0,
       "mscFrAtmDlciSiwfMaximumBurstSize01": mscFrAtmDlciSiwfMaximumBurstSize01,
       "mscFrAtmDlciSiwfEquivalentBitRate": mscFrAtmDlciSiwfEquivalentBitRate,
       "mscFrAtmDlciSiwfType": mscFrAtmDlciSiwfType,
       "mscFrAtmDlciSiwfVccClearCause": mscFrAtmDlciSiwfVccClearCause,
       "mscFrAtmDlciSiwfVccCauseDiag": mscFrAtmDlciSiwfVccCauseDiag,
       "mscFrAtmDlciSiwfStatsTable": mscFrAtmDlciSiwfStatsTable,
       "mscFrAtmDlciSiwfStatsEntry": mscFrAtmDlciSiwfStatsEntry,
       "mscFrAtmDlciSiwfUnknown1490Frames": mscFrAtmDlciSiwfUnknown1490Frames,
       "mscFrAtmDlciSiwfInvalid1490Frames": mscFrAtmDlciSiwfInvalid1490Frames,
       "mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader": mscFrAtmDlciSiwfLastUnknown1490ProtocolHeader,
       "mscFrAtmDlciSiwfUnknown1483Frames": mscFrAtmDlciSiwfUnknown1483Frames,
       "mscFrAtmDlciSiwfInvalid1483Frames": mscFrAtmDlciSiwfInvalid1483Frames,
       "mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader": mscFrAtmDlciSiwfLastUnknown1483ProtocolHeader,
       "mscFrAtmDlciNiwf": mscFrAtmDlciNiwf,
       "mscFrAtmDlciNiwfRowStatusTable": mscFrAtmDlciNiwfRowStatusTable,
       "mscFrAtmDlciNiwfRowStatusEntry": mscFrAtmDlciNiwfRowStatusEntry,
       "mscFrAtmDlciNiwfRowStatus": mscFrAtmDlciNiwfRowStatus,
       "mscFrAtmDlciNiwfComponentName": mscFrAtmDlciNiwfComponentName,
       "mscFrAtmDlciNiwfStorageType": mscFrAtmDlciNiwfStorageType,
       "mscFrAtmDlciNiwfIndex": mscFrAtmDlciNiwfIndex,
       "mscFrAtmDlciNiwfSpvc": mscFrAtmDlciNiwfSpvc,
       "mscFrAtmDlciNiwfSpvcRowStatusTable": mscFrAtmDlciNiwfSpvcRowStatusTable,
       "mscFrAtmDlciNiwfSpvcRowStatusEntry": mscFrAtmDlciNiwfSpvcRowStatusEntry,
       "mscFrAtmDlciNiwfSpvcRowStatus": mscFrAtmDlciNiwfSpvcRowStatus,
       "mscFrAtmDlciNiwfSpvcComponentName": mscFrAtmDlciNiwfSpvcComponentName,
       "mscFrAtmDlciNiwfSpvcStorageType": mscFrAtmDlciNiwfSpvcStorageType,
       "mscFrAtmDlciNiwfSpvcIndex": mscFrAtmDlciNiwfSpvcIndex,
       "mscFrAtmDlciNiwfSpvcProvTable": mscFrAtmDlciNiwfSpvcProvTable,
       "mscFrAtmDlciNiwfSpvcProvEntry": mscFrAtmDlciNiwfSpvcProvEntry,
       "mscFrAtmDlciNiwfSpvcRemoteAddress": mscFrAtmDlciNiwfSpvcRemoteAddress,
       "mscFrAtmDlciNiwfSpvcRemoteDlci": mscFrAtmDlciNiwfSpvcRemoteDlci,
       "mscFrAtmDlciNiwfSpvcCorrelationTag": mscFrAtmDlciNiwfSpvcCorrelationTag,
       "mscFrAtmDlciNiwfNd": mscFrAtmDlciNiwfNd,
       "mscFrAtmDlciNiwfNdRowStatusTable": mscFrAtmDlciNiwfNdRowStatusTable,
       "mscFrAtmDlciNiwfNdRowStatusEntry": mscFrAtmDlciNiwfNdRowStatusEntry,
       "mscFrAtmDlciNiwfNdRowStatus": mscFrAtmDlciNiwfNdRowStatus,
       "mscFrAtmDlciNiwfNdComponentName": mscFrAtmDlciNiwfNdComponentName,
       "mscFrAtmDlciNiwfNdStorageType": mscFrAtmDlciNiwfNdStorageType,
       "mscFrAtmDlciNiwfNdIndex": mscFrAtmDlciNiwfNdIndex,
       "mscFrAtmDlciNiwfNdProvTable": mscFrAtmDlciNiwfNdProvTable,
       "mscFrAtmDlciNiwfNdProvEntry": mscFrAtmDlciNiwfNdProvEntry,
       "mscFrAtmDlciNiwfNdDeToClpMapping": mscFrAtmDlciNiwfNdDeToClpMapping,
       "mscFrAtmDlciNiwfNdClpToDeMapping": mscFrAtmDlciNiwfNdClpToDeMapping,
       "mscFrAtmDlciNiwfNdTransferPriority": mscFrAtmDlciNiwfNdTransferPriority,
       "mscFrAtmDlciNiwfQoS": mscFrAtmDlciNiwfQoS,
       "mscFrAtmDlciNiwfQoSRowStatusTable": mscFrAtmDlciNiwfQoSRowStatusTable,
       "mscFrAtmDlciNiwfQoSRowStatusEntry": mscFrAtmDlciNiwfQoSRowStatusEntry,
       "mscFrAtmDlciNiwfQoSRowStatus": mscFrAtmDlciNiwfQoSRowStatus,
       "mscFrAtmDlciNiwfQoSComponentName": mscFrAtmDlciNiwfQoSComponentName,
       "mscFrAtmDlciNiwfQoSStorageType": mscFrAtmDlciNiwfQoSStorageType,
       "mscFrAtmDlciNiwfQoSIndex": mscFrAtmDlciNiwfQoSIndex,
       "mscFrAtmDlciNiwfQoSProvTable": mscFrAtmDlciNiwfQoSProvTable,
       "mscFrAtmDlciNiwfQoSProvEntry": mscFrAtmDlciNiwfQoSProvEntry,
       "mscFrAtmDlciNiwfQoSEmissionPriorityToIf": mscFrAtmDlciNiwfQoSEmissionPriorityToIf,
       "mscFrAtmDlciNiwfQoSTransferPriority": mscFrAtmDlciNiwfQoSTransferPriority,
       "mscFrAtmDlciNiwfOperTable": mscFrAtmDlciNiwfOperTable,
       "mscFrAtmDlciNiwfOperEntry": mscFrAtmDlciNiwfOperEntry,
       "mscFrAtmDlciNiwfDeToClpMapping": mscFrAtmDlciNiwfDeToClpMapping,
       "mscFrAtmDlciNiwfClpToDeMapping": mscFrAtmDlciNiwfClpToDeMapping,
       "mscFrAtmDlciNiwfTransferPriority": mscFrAtmDlciNiwfTransferPriority,
       "mscFrAtmDlciNiwfAtmServiceCategory": mscFrAtmDlciNiwfAtmServiceCategory,
       "mscFrAtmDlciNiwfTrafficParmConvPolicy": mscFrAtmDlciNiwfTrafficParmConvPolicy,
       "mscFrAtmDlciNiwfAvgFrameSize": mscFrAtmDlciNiwfAvgFrameSize,
       "mscFrAtmDlciNiwfEquivalentBitRate": mscFrAtmDlciNiwfEquivalentBitRate,
       "mscFrAtmDlciNiwfAtmDlci": mscFrAtmDlciNiwfAtmDlci,
       "mscFrAtmDlciNiwfAssignedBandwidthPool": mscFrAtmDlciNiwfAssignedBandwidthPool,
       "mscFrAtmDlciEgSp": mscFrAtmDlciEgSp,
       "mscFrAtmDlciEgSpRowStatusTable": mscFrAtmDlciEgSpRowStatusTable,
       "mscFrAtmDlciEgSpRowStatusEntry": mscFrAtmDlciEgSpRowStatusEntry,
       "mscFrAtmDlciEgSpRowStatus": mscFrAtmDlciEgSpRowStatus,
       "mscFrAtmDlciEgSpComponentName": mscFrAtmDlciEgSpComponentName,
       "mscFrAtmDlciEgSpStorageType": mscFrAtmDlciEgSpStorageType,
       "mscFrAtmDlciEgSpIndex": mscFrAtmDlciEgSpIndex,
       "mscFrAtmDlciEgSpProvTable": mscFrAtmDlciEgSpProvTable,
       "mscFrAtmDlciEgSpProvEntry": mscFrAtmDlciEgSpProvEntry,
       "mscFrAtmDlciEgSpCommittedInformationRate": mscFrAtmDlciEgSpCommittedInformationRate,
       "mscFrAtmDlciEgSpCommittedBurstSize": mscFrAtmDlciEgSpCommittedBurstSize,
       "mscFrAtmDlciEgSpExcessBurstSize": mscFrAtmDlciEgSpExcessBurstSize,
       "mscFrAtmDlciEgSpMeasurementInterval": mscFrAtmDlciEgSpMeasurementInterval,
       "mscFrAtmDlciStateTable": mscFrAtmDlciStateTable,
       "mscFrAtmDlciStateEntry": mscFrAtmDlciStateEntry,
       "mscFrAtmDlciAdminState": mscFrAtmDlciAdminState,
       "mscFrAtmDlciOperationalState": mscFrAtmDlciOperationalState,
       "mscFrAtmDlciUsageState": mscFrAtmDlciUsageState,
       "mscFrAtmDlciABitTable": mscFrAtmDlciABitTable,
       "mscFrAtmDlciABitEntry": mscFrAtmDlciABitEntry,
       "mscFrAtmDlciABitStatusToIf": mscFrAtmDlciABitStatusToIf,
       "mscFrAtmDlciABitReasonToIf": mscFrAtmDlciABitReasonToIf,
       "mscFrAtmDlciABitStatusFromIf": mscFrAtmDlciABitStatusFromIf,
       "mscFrAtmDlciABitReasonFromIf": mscFrAtmDlciABitReasonFromIf,
       "mscFrAtmDlciSpOpTable": mscFrAtmDlciSpOpTable,
       "mscFrAtmDlciSpOpEntry": mscFrAtmDlciSpOpEntry,
       "mscFrAtmDlciMaximumFrameSize": mscFrAtmDlciMaximumFrameSize,
       "mscFrAtmDlciRateEnforcement": mscFrAtmDlciRateEnforcement,
       "mscFrAtmDlciCommittedInformationRate": mscFrAtmDlciCommittedInformationRate,
       "mscFrAtmDlciCommittedBurstSize": mscFrAtmDlciCommittedBurstSize,
       "mscFrAtmDlciExcessBurstSize": mscFrAtmDlciExcessBurstSize,
       "mscFrAtmDlciMeasurementInterval": mscFrAtmDlciMeasurementInterval,
       "mscFrAtmDlciEmissionPriorityToIf": mscFrAtmDlciEmissionPriorityToIf,
       "mscFrAtmDlciDlciType": mscFrAtmDlciDlciType,
       "mscFrAtmDlciTroubled": mscFrAtmDlciTroubled,
       "mscFrAtmDlciTroubledReason": mscFrAtmDlciTroubledReason,
       "mscFrAtmDlciStatsTable": mscFrAtmDlciStatsTable,
       "mscFrAtmDlciStatsEntry": mscFrAtmDlciStatsEntry,
       "mscFrAtmDlciFrmToIf": mscFrAtmDlciFrmToIf,
       "mscFrAtmDlciFecnFrmToIf": mscFrAtmDlciFecnFrmToIf,
       "mscFrAtmDlciBecnFrmToIf": mscFrAtmDlciBecnFrmToIf,
       "mscFrAtmDlciDeFrmToIf": mscFrAtmDlciDeFrmToIf,
       "mscFrAtmDlciDiscCongestedToIf": mscFrAtmDlciDiscCongestedToIf,
       "mscFrAtmDlciDiscDeCongestedToIf": mscFrAtmDlciDiscDeCongestedToIf,
       "mscFrAtmDlciFrmFromIf": mscFrAtmDlciFrmFromIf,
       "mscFrAtmDlciFecnFrmFromIf": mscFrAtmDlciFecnFrmFromIf,
       "mscFrAtmDlciBecnFrmFromIf": mscFrAtmDlciBecnFrmFromIf,
       "mscFrAtmDlciEfciFrmFromNetwork": mscFrAtmDlciEfciFrmFromNetwork,
       "mscFrAtmDlciDeFrmFromIf": mscFrAtmDlciDeFrmFromIf,
       "mscFrAtmDlciExcessFrmFromIf": mscFrAtmDlciExcessFrmFromIf,
       "mscFrAtmDlciDiscExcessFromIf": mscFrAtmDlciDiscExcessFromIf,
       "mscFrAtmDlciDiscFrameAbit": mscFrAtmDlciDiscFrameAbit,
       "mscFrAtmDlciDiscCongestedFromIf": mscFrAtmDlciDiscCongestedFromIf,
       "mscFrAtmDlciDiscDeCongestedFromIf": mscFrAtmDlciDiscDeCongestedFromIf,
       "mscFrAtmDlciErrorShortFrmFromIf": mscFrAtmDlciErrorShortFrmFromIf,
       "mscFrAtmDlciErrorLongFrmFromIf": mscFrAtmDlciErrorLongFrmFromIf,
       "mscFrAtmDlciBecnFrmSetByService": mscFrAtmDlciBecnFrmSetByService,
       "mscFrAtmDlciBytesToIf": mscFrAtmDlciBytesToIf,
       "mscFrAtmDlciDeBytesToIf": mscFrAtmDlciDeBytesToIf,
       "mscFrAtmDlciDiscCongestedToIfBytes": mscFrAtmDlciDiscCongestedToIfBytes,
       "mscFrAtmDlciDiscDeCongestedToIfBytes": mscFrAtmDlciDiscDeCongestedToIfBytes,
       "mscFrAtmDlciBytesFromIf": mscFrAtmDlciBytesFromIf,
       "mscFrAtmDlciDeBytesFromIf": mscFrAtmDlciDeBytesFromIf,
       "mscFrAtmDlciExcessBytesFromIf": mscFrAtmDlciExcessBytesFromIf,
       "mscFrAtmDlciDiscExcessFromIfBytes": mscFrAtmDlciDiscExcessFromIfBytes,
       "mscFrAtmDlciDiscByteAbit": mscFrAtmDlciDiscByteAbit,
       "mscFrAtmDlciDiscCongestedFromIfBytes": mscFrAtmDlciDiscCongestedFromIfBytes,
       "mscFrAtmDlciDiscDeCongestedFromIfBytes": mscFrAtmDlciDiscDeCongestedFromIfBytes,
       "mscFrAtmDlciErrorShortBytesFromIf": mscFrAtmDlciErrorShortBytesFromIf,
       "mscFrAtmDlciErrorLongBytesFromIf": mscFrAtmDlciErrorLongBytesFromIf,
       "mscFrAtmDlciCalldTable": mscFrAtmDlciCalldTable,
       "mscFrAtmDlciCalldEntry": mscFrAtmDlciCalldEntry,
       "mscFrAtmDlciAccountingEnabled": mscFrAtmDlciAccountingEnabled,
       "mscFrAtmDlciAccountingEnd": mscFrAtmDlciAccountingEnd,
       "mscFrAtmDlciCorrelationTag": mscFrAtmDlciCorrelationTag,
       "mscFrAtmDlciIntTable": mscFrAtmDlciIntTable,
       "mscFrAtmDlciIntEntry": mscFrAtmDlciIntEntry,
       "mscFrAtmDlciStartTime": mscFrAtmDlciStartTime,
       "mscFrAtmDlciTotalIngressBytes": mscFrAtmDlciTotalIngressBytes,
       "mscFrAtmDlciTotalEgressBytes": mscFrAtmDlciTotalEgressBytes,
       "mscFrAtmDlciEirIngressBytes": mscFrAtmDlciEirIngressBytes,
       "mscFrAtmDlciEirEgressBytes": mscFrAtmDlciEirEgressBytes,
       "mscFrAtmDlciDiscardedBytes": mscFrAtmDlciDiscardedBytes,
       "mscFrAtmDlciTotalIngressFrames": mscFrAtmDlciTotalIngressFrames,
       "mscFrAtmDlciTotalEgressFrames": mscFrAtmDlciTotalEgressFrames,
       "mscFrAtmDlciEirIngressFrames": mscFrAtmDlciEirIngressFrames,
       "mscFrAtmDlciEirEgressFrames": mscFrAtmDlciEirEgressFrames,
       "mscFrAtmDlciDiscardedFrames": mscFrAtmDlciDiscardedFrames,
       "mscFrAtmDlciElapsedDifference": mscFrAtmDlciElapsedDifference,
       "mscFrAtmVFramer": mscFrAtmVFramer,
       "mscFrAtmVFramerRowStatusTable": mscFrAtmVFramerRowStatusTable,
       "mscFrAtmVFramerRowStatusEntry": mscFrAtmVFramerRowStatusEntry,
       "mscFrAtmVFramerRowStatus": mscFrAtmVFramerRowStatus,
       "mscFrAtmVFramerComponentName": mscFrAtmVFramerComponentName,
       "mscFrAtmVFramerStorageType": mscFrAtmVFramerStorageType,
       "mscFrAtmVFramerIndex": mscFrAtmVFramerIndex,
       "mscFrAtmVFramerProvTable": mscFrAtmVFramerProvTable,
       "mscFrAtmVFramerProvEntry": mscFrAtmVFramerProvEntry,
       "mscFrAtmVFramerOtherVirtualFramer": mscFrAtmVFramerOtherVirtualFramer,
       "mscFrAtmVFramerLogicalProcessor": mscFrAtmVFramerLogicalProcessor,
       "mscFrAtmVFramerStateTable": mscFrAtmVFramerStateTable,
       "mscFrAtmVFramerStateEntry": mscFrAtmVFramerStateEntry,
       "mscFrAtmVFramerAdminState": mscFrAtmVFramerAdminState,
       "mscFrAtmVFramerOperationalState": mscFrAtmVFramerOperationalState,
       "mscFrAtmVFramerUsageState": mscFrAtmVFramerUsageState,
       "mscFrAtmVFramerStatsTable": mscFrAtmVFramerStatsTable,
       "mscFrAtmVFramerStatsEntry": mscFrAtmVFramerStatsEntry,
       "mscFrAtmVFramerFrmToOtherVFramer": mscFrAtmVFramerFrmToOtherVFramer,
       "mscFrAtmVFramerFrmFromOtherVFramer": mscFrAtmVFramerFrmFromOtherVFramer,
       "mscFrAtmVFramerOctetFromOtherVFramer": mscFrAtmVFramerOctetFromOtherVFramer,
       "mscFrAtmAddr": mscFrAtmAddr,
       "mscFrAtmAddrRowStatusTable": mscFrAtmAddrRowStatusTable,
       "mscFrAtmAddrRowStatusEntry": mscFrAtmAddrRowStatusEntry,
       "mscFrAtmAddrRowStatus": mscFrAtmAddrRowStatus,
       "mscFrAtmAddrComponentName": mscFrAtmAddrComponentName,
       "mscFrAtmAddrStorageType": mscFrAtmAddrStorageType,
       "mscFrAtmAddrIndex": mscFrAtmAddrIndex,
       "mscFrAtmAddrProvTable": mscFrAtmAddrProvTable,
       "mscFrAtmAddrProvEntry": mscFrAtmAddrProvEntry,
       "mscFrAtmAddrAddress": mscFrAtmAddrAddress,
       "mscFrAtmAddrAddrOpTable": mscFrAtmAddrAddrOpTable,
       "mscFrAtmAddrAddrOpEntry": mscFrAtmAddrAddrOpEntry,
       "mscFrAtmAddrMyAddress": mscFrAtmAddrMyAddress,
       "mscFrAtmCa": mscFrAtmCa,
       "mscFrAtmCaRowStatusTable": mscFrAtmCaRowStatusTable,
       "mscFrAtmCaRowStatusEntry": mscFrAtmCaRowStatusEntry,
       "mscFrAtmCaRowStatus": mscFrAtmCaRowStatus,
       "mscFrAtmCaComponentName": mscFrAtmCaComponentName,
       "mscFrAtmCaStorageType": mscFrAtmCaStorageType,
       "mscFrAtmCaIndex": mscFrAtmCaIndex,
       "mscFrAtmCaTpm": mscFrAtmCaTpm,
       "mscFrAtmCaTpmRowStatusTable": mscFrAtmCaTpmRowStatusTable,
       "mscFrAtmCaTpmRowStatusEntry": mscFrAtmCaTpmRowStatusEntry,
       "mscFrAtmCaTpmRowStatus": mscFrAtmCaTpmRowStatus,
       "mscFrAtmCaTpmComponentName": mscFrAtmCaTpmComponentName,
       "mscFrAtmCaTpmStorageType": mscFrAtmCaTpmStorageType,
       "mscFrAtmCaTpmIndex": mscFrAtmCaTpmIndex,
       "mscFrAtmCaTpmProvTable": mscFrAtmCaTpmProvTable,
       "mscFrAtmCaTpmProvEntry": mscFrAtmCaTpmProvEntry,
       "mscFrAtmCaTpmAssignedBandwidthPool": mscFrAtmCaTpmAssignedBandwidthPool,
       "mscFrAtmCaTpmTrafficParmConvPolicy": mscFrAtmCaTpmTrafficParmConvPolicy,
       "mscFrAtmCaTpmAverageFrameSize": mscFrAtmCaTpmAverageFrameSize,
       "mscFrAtmCaProvTable": mscFrAtmCaProvTable,
       "mscFrAtmCaProvEntry": mscFrAtmCaProvEntry,
       "mscFrAtmCaCallAdmissionControl": mscFrAtmCaCallAdmissionControl,
       "mscFrAtmCaOverrideLinkRate": mscFrAtmCaOverrideLinkRate,
       "mscFrAtmCaSdTable": mscFrAtmCaSdTable,
       "mscFrAtmCaSdEntry": mscFrAtmCaSdEntry,
       "mscFrAtmCaSdMode": mscFrAtmCaSdMode,
       "mscFrAtmCaSdDeToClpMapping": mscFrAtmCaSdDeToClpMapping,
       "mscFrAtmCaSdClpToDeMapping": mscFrAtmCaSdClpToDeMapping,
       "mscFrAtmCaSdFecnToEfciMapping": mscFrAtmCaSdFecnToEfciMapping,
       "mscFrAtmCaSdCrToUuMapping": mscFrAtmCaSdCrToUuMapping,
       "mscFrAtmCaNdTable": mscFrAtmCaNdTable,
       "mscFrAtmCaNdEntry": mscFrAtmCaNdEntry,
       "mscFrAtmCaNdDeToClpMapping": mscFrAtmCaNdDeToClpMapping,
       "mscFrAtmCaNdClpToDeMapping": mscFrAtmCaNdClpToDeMapping,
       "mscFrAtmCaIfQoSTable": mscFrAtmCaIfQoSTable,
       "mscFrAtmCaIfQoSEntry": mscFrAtmCaIfQoSEntry,
       "mscFrAtmCaSiwfEmissionPriorityToIf": mscFrAtmCaSiwfEmissionPriorityToIf,
       "mscFrAtmCaSiwfTransferPriority": mscFrAtmCaSiwfTransferPriority,
       "mscFrAtmCaNiwfEmissionPriorityToIf": mscFrAtmCaNiwfEmissionPriorityToIf,
       "mscFrAtmCaNiwfTransferPriority": mscFrAtmCaNiwfTransferPriority,
       "mscFrAtmCaOpTable": mscFrAtmCaOpTable,
       "mscFrAtmCaOpEntry": mscFrAtmCaOpEntry,
       "mscFrAtmCaLinkRate": mscFrAtmCaLinkRate,
       "mscFrAtmCaNailedUpPvcs": mscFrAtmCaNailedUpPvcs,
       "mscFrAtmCaTroubledDlcis": mscFrAtmCaTroubledDlcis,
       "mscFrAtmCaSoftPvcs": mscFrAtmCaSoftPvcs,
       "mscFrAtmCaAccountingOptionsTable": mscFrAtmCaAccountingOptionsTable,
       "mscFrAtmCaAccountingOptionsEntry": mscFrAtmCaAccountingOptionsEntry,
       "mscFrAtmCaAccountClass": mscFrAtmCaAccountClass,
       "mscFrAtmCaAccountCollection": mscFrAtmCaAccountCollection,
       "mscFrAtmCaServiceExchange": mscFrAtmCaServiceExchange,
       "mscFrAtmCaBwPoolTable": mscFrAtmCaBwPoolTable,
       "mscFrAtmCaBwPoolEntry": mscFrAtmCaBwPoolEntry,
       "mscFrAtmCaBwPoolIndex": mscFrAtmCaBwPoolIndex,
       "mscFrAtmCaBwPoolValue": mscFrAtmCaBwPoolValue,
       "mscFrAtmCaPoolProvBwTable": mscFrAtmCaPoolProvBwTable,
       "mscFrAtmCaPoolProvBwEntry": mscFrAtmCaPoolProvBwEntry,
       "mscFrAtmCaPoolProvBwIndex": mscFrAtmCaPoolProvBwIndex,
       "mscFrAtmCaPoolProvBwValue": mscFrAtmCaPoolProvBwValue,
       "mscFrAtmCaPoolAvailBwTable": mscFrAtmCaPoolAvailBwTable,
       "mscFrAtmCaPoolAvailBwEntry": mscFrAtmCaPoolAvailBwEntry,
       "mscFrAtmCaPoolAvailBwIndex": mscFrAtmCaPoolAvailBwIndex,
       "mscFrAtmCaPoolAvailBwValue": mscFrAtmCaPoolAvailBwValue,
       "mscFrAtmCaPoolAdmitBwTable": mscFrAtmCaPoolAdmitBwTable,
       "mscFrAtmCaPoolAdmitBwEntry": mscFrAtmCaPoolAdmitBwEntry,
       "mscFrAtmCaPoolAdmitBwIndex": mscFrAtmCaPoolAdmitBwIndex,
       "mscFrAtmCaPoolAdmitBwValue": mscFrAtmCaPoolAdmitBwValue,
       "mscFrAtmCidDataTable": mscFrAtmCidDataTable,
       "mscFrAtmCidDataEntry": mscFrAtmCidDataEntry,
       "mscFrAtmCustomerIdentifier": mscFrAtmCustomerIdentifier,
       "mscFrAtmStateTable": mscFrAtmStateTable,
       "mscFrAtmStateEntry": mscFrAtmStateEntry,
       "mscFrAtmAdminState": mscFrAtmAdminState,
       "mscFrAtmOperationalState": mscFrAtmOperationalState,
       "mscFrAtmUsageState": mscFrAtmUsageState,
       "mscFrAtmAvailabilityStatus": mscFrAtmAvailabilityStatus,
       "mscFrAtmProceduralStatus": mscFrAtmProceduralStatus,
       "mscFrAtmControlStatus": mscFrAtmControlStatus,
       "mscFrAtmAlarmStatus": mscFrAtmAlarmStatus,
       "mscFrAtmStandbyStatus": mscFrAtmStandbyStatus,
       "mscFrAtmUnknownStatus": mscFrAtmUnknownStatus,
       "mscFrAtmStatsTable": mscFrAtmStatsTable,
       "mscFrAtmStatsEntry": mscFrAtmStatsEntry,
       "mscFrAtmLastUnknownDlci": mscFrAtmLastUnknownDlci,
       "mscFrAtmUnknownDlciFramesFromIf": mscFrAtmUnknownDlciFramesFromIf,
       "mscFrAtmInvalidHeaderFramesFromIf": mscFrAtmInvalidHeaderFramesFromIf,
       "mscFrAtmIfEntryTable": mscFrAtmIfEntryTable,
       "mscFrAtmIfEntryEntry": mscFrAtmIfEntryEntry,
       "mscFrAtmIfAdminStatus": mscFrAtmIfAdminStatus,
       "mscFrAtmIfIndex": mscFrAtmIfIndex,
       "mscFrAtmOperStatusTable": mscFrAtmOperStatusTable,
       "mscFrAtmOperStatusEntry": mscFrAtmOperStatusEntry,
       "mscFrAtmSnmpOperStatus": mscFrAtmSnmpOperStatus,
       "mscFrAtmEmissionPriorityQsTable": mscFrAtmEmissionPriorityQsTable,
       "mscFrAtmEmissionPriorityQsEntry": mscFrAtmEmissionPriorityQsEntry,
       "mscFrAtmNumberOfEmissionQs": mscFrAtmNumberOfEmissionQs,
       "mscFrAtmFrmToIfByQueueTable": mscFrAtmFrmToIfByQueueTable,
       "mscFrAtmFrmToIfByQueueEntry": mscFrAtmFrmToIfByQueueEntry,
       "mscFrAtmFrmToIfByQueueIndex": mscFrAtmFrmToIfByQueueIndex,
       "mscFrAtmFrmToIfByQueueValue": mscFrAtmFrmToIfByQueueValue,
       "mscFrAtmOctetToIfByQueueTable": mscFrAtmOctetToIfByQueueTable,
       "mscFrAtmOctetToIfByQueueEntry": mscFrAtmOctetToIfByQueueEntry,
       "mscFrAtmOctetToIfByQueueIndex": mscFrAtmOctetToIfByQueueIndex,
       "mscFrAtmOctetToIfByQueueValue": mscFrAtmOctetToIfByQueueValue,
       "frameRelayAtmMIB": frameRelayAtmMIB,
       "frameRelayAtmGroup": frameRelayAtmGroup,
       "frameRelayAtmGroupCA": frameRelayAtmGroupCA,
       "frameRelayAtmGroupCA02": frameRelayAtmGroupCA02,
       "frameRelayAtmGroupCA02A": frameRelayAtmGroupCA02A,
       "frameRelayAtmCapabilities": frameRelayAtmCapabilities,
       "frameRelayAtmCapabilitiesCA": frameRelayAtmCapabilitiesCA,
       "frameRelayAtmCapabilitiesCA02": frameRelayAtmCapabilitiesCA02,
       "frameRelayAtmCapabilitiesCA02A": frameRelayAtmCapabilitiesCA02A}
)
