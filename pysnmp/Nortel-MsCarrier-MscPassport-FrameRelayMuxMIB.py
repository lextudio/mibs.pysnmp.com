# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:28 2024
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

(Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
    "NonReplicated",
    "PassportCounter64")

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

_MscFrMux_ObjectIdentity = ObjectIdentity
mscFrMux = _MscFrMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112)
)
_MscFrMuxRowStatusTable_Object = MibTable
mscFrMuxRowStatusTable = _MscFrMuxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1)
)
if mibBuilder.loadTexts:
    mscFrMuxRowStatusTable.setStatus("mandatory")
_MscFrMuxRowStatusEntry_Object = MibTableRow
mscFrMuxRowStatusEntry = _MscFrMuxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1, 1)
)
mscFrMuxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxRowStatusEntry.setStatus("mandatory")
_MscFrMuxRowStatus_Type = RowStatus
_MscFrMuxRowStatus_Object = MibTableColumn
mscFrMuxRowStatus = _MscFrMuxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1, 1, 1),
    _MscFrMuxRowStatus_Type()
)
mscFrMuxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxRowStatus.setStatus("mandatory")
_MscFrMuxComponentName_Type = DisplayString
_MscFrMuxComponentName_Object = MibTableColumn
mscFrMuxComponentName = _MscFrMuxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1, 1, 2),
    _MscFrMuxComponentName_Type()
)
mscFrMuxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxComponentName.setStatus("mandatory")
_MscFrMuxStorageType_Type = StorageType
_MscFrMuxStorageType_Object = MibTableColumn
mscFrMuxStorageType = _MscFrMuxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1, 1, 4),
    _MscFrMuxStorageType_Type()
)
mscFrMuxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxStorageType.setStatus("mandatory")


class _MscFrMuxIndex_Type(Integer32):
    """Custom type mscFrMuxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrMuxIndex_Type.__name__ = "Integer32"
_MscFrMuxIndex_Object = MibTableColumn
mscFrMuxIndex = _MscFrMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 1, 1, 10),
    _MscFrMuxIndex_Type()
)
mscFrMuxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrMuxIndex.setStatus("mandatory")
_MscFrMuxFramer_ObjectIdentity = ObjectIdentity
mscFrMuxFramer = _MscFrMuxFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2)
)
_MscFrMuxFramerRowStatusTable_Object = MibTable
mscFrMuxFramerRowStatusTable = _MscFrMuxFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerRowStatusTable.setStatus("mandatory")
_MscFrMuxFramerRowStatusEntry_Object = MibTableRow
mscFrMuxFramerRowStatusEntry = _MscFrMuxFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1, 1)
)
mscFrMuxFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerRowStatusEntry.setStatus("mandatory")
_MscFrMuxFramerRowStatus_Type = RowStatus
_MscFrMuxFramerRowStatus_Object = MibTableColumn
mscFrMuxFramerRowStatus = _MscFrMuxFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1, 1, 1),
    _MscFrMuxFramerRowStatus_Type()
)
mscFrMuxFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerRowStatus.setStatus("mandatory")
_MscFrMuxFramerComponentName_Type = DisplayString
_MscFrMuxFramerComponentName_Object = MibTableColumn
mscFrMuxFramerComponentName = _MscFrMuxFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1, 1, 2),
    _MscFrMuxFramerComponentName_Type()
)
mscFrMuxFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerComponentName.setStatus("mandatory")
_MscFrMuxFramerStorageType_Type = StorageType
_MscFrMuxFramerStorageType_Object = MibTableColumn
mscFrMuxFramerStorageType = _MscFrMuxFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1, 1, 4),
    _MscFrMuxFramerStorageType_Type()
)
mscFrMuxFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerStorageType.setStatus("mandatory")
_MscFrMuxFramerIndex_Type = NonReplicated
_MscFrMuxFramerIndex_Object = MibTableColumn
mscFrMuxFramerIndex = _MscFrMuxFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 1, 1, 10),
    _MscFrMuxFramerIndex_Type()
)
mscFrMuxFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrMuxFramerIndex.setStatus("mandatory")
_MscFrMuxFramerProvTable_Object = MibTable
mscFrMuxFramerProvTable = _MscFrMuxFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerProvTable.setStatus("mandatory")
_MscFrMuxFramerProvEntry_Object = MibTableRow
mscFrMuxFramerProvEntry = _MscFrMuxFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 10, 1)
)
mscFrMuxFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerProvEntry.setStatus("mandatory")
_MscFrMuxFramerInterfaceName_Type = Link
_MscFrMuxFramerInterfaceName_Object = MibTableColumn
mscFrMuxFramerInterfaceName = _MscFrMuxFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 10, 1, 1),
    _MscFrMuxFramerInterfaceName_Type()
)
mscFrMuxFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxFramerInterfaceName.setStatus("mandatory")
_MscFrMuxFramerLinkTable_Object = MibTable
mscFrMuxFramerLinkTable = _MscFrMuxFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerLinkTable.setStatus("mandatory")
_MscFrMuxFramerLinkEntry_Object = MibTableRow
mscFrMuxFramerLinkEntry = _MscFrMuxFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 11, 1)
)
mscFrMuxFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerLinkEntry.setStatus("mandatory")


class _MscFrMuxFramerDataInversion_Type(Integer32):
    """Custom type mscFrMuxFramerDataInversion based on Integer32"""
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


_MscFrMuxFramerDataInversion_Type.__name__ = "Integer32"
_MscFrMuxFramerDataInversion_Object = MibTableColumn
mscFrMuxFramerDataInversion = _MscFrMuxFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 11, 1, 2),
    _MscFrMuxFramerDataInversion_Type()
)
mscFrMuxFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxFramerDataInversion.setStatus("mandatory")


class _MscFrMuxFramerFrameCrcType_Type(Integer32):
    """Custom type mscFrMuxFramerFrameCrcType based on Integer32"""
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


_MscFrMuxFramerFrameCrcType_Type.__name__ = "Integer32"
_MscFrMuxFramerFrameCrcType_Object = MibTableColumn
mscFrMuxFramerFrameCrcType = _MscFrMuxFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 11, 1, 3),
    _MscFrMuxFramerFrameCrcType_Type()
)
mscFrMuxFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrameCrcType.setStatus("mandatory")


class _MscFrMuxFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscFrMuxFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscFrMuxFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscFrMuxFramerFlagsBetweenFrames_Object = MibTableColumn
mscFrMuxFramerFlagsBetweenFrames = _MscFrMuxFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 11, 1, 4),
    _MscFrMuxFramerFlagsBetweenFrames_Type()
)
mscFrMuxFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxFramerFlagsBetweenFrames.setStatus("mandatory")
_MscFrMuxFramerStateTable_Object = MibTable
mscFrMuxFramerStateTable = _MscFrMuxFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerStateTable.setStatus("mandatory")
_MscFrMuxFramerStateEntry_Object = MibTableRow
mscFrMuxFramerStateEntry = _MscFrMuxFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 12, 1)
)
mscFrMuxFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerStateEntry.setStatus("mandatory")


class _MscFrMuxFramerAdminState_Type(Integer32):
    """Custom type mscFrMuxFramerAdminState based on Integer32"""
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


_MscFrMuxFramerAdminState_Type.__name__ = "Integer32"
_MscFrMuxFramerAdminState_Object = MibTableColumn
mscFrMuxFramerAdminState = _MscFrMuxFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 12, 1, 1),
    _MscFrMuxFramerAdminState_Type()
)
mscFrMuxFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerAdminState.setStatus("mandatory")


class _MscFrMuxFramerOperationalState_Type(Integer32):
    """Custom type mscFrMuxFramerOperationalState based on Integer32"""
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


_MscFrMuxFramerOperationalState_Type.__name__ = "Integer32"
_MscFrMuxFramerOperationalState_Object = MibTableColumn
mscFrMuxFramerOperationalState = _MscFrMuxFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 12, 1, 2),
    _MscFrMuxFramerOperationalState_Type()
)
mscFrMuxFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerOperationalState.setStatus("mandatory")


class _MscFrMuxFramerUsageState_Type(Integer32):
    """Custom type mscFrMuxFramerUsageState based on Integer32"""
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


_MscFrMuxFramerUsageState_Type.__name__ = "Integer32"
_MscFrMuxFramerUsageState_Object = MibTableColumn
mscFrMuxFramerUsageState = _MscFrMuxFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 12, 1, 3),
    _MscFrMuxFramerUsageState_Type()
)
mscFrMuxFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerUsageState.setStatus("mandatory")
_MscFrMuxFramerStatsTable_Object = MibTable
mscFrMuxFramerStatsTable = _MscFrMuxFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerStatsTable.setStatus("mandatory")
_MscFrMuxFramerStatsEntry_Object = MibTableRow
mscFrMuxFramerStatsEntry = _MscFrMuxFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1)
)
mscFrMuxFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerStatsEntry.setStatus("mandatory")
_MscFrMuxFramerFrmToIf_Type = Counter32
_MscFrMuxFramerFrmToIf_Object = MibTableColumn
mscFrMuxFramerFrmToIf = _MscFrMuxFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 1),
    _MscFrMuxFramerFrmToIf_Type()
)
mscFrMuxFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrmToIf.setStatus("obsolete")
_MscFrMuxFramerFrmFromIf_Type = Counter32
_MscFrMuxFramerFrmFromIf_Object = MibTableColumn
mscFrMuxFramerFrmFromIf = _MscFrMuxFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 2),
    _MscFrMuxFramerFrmFromIf_Type()
)
mscFrMuxFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrmFromIf.setStatus("obsolete")
_MscFrMuxFramerOctetFromIf_Type = Counter32
_MscFrMuxFramerOctetFromIf_Object = MibTableColumn
mscFrMuxFramerOctetFromIf = _MscFrMuxFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 3),
    _MscFrMuxFramerOctetFromIf_Type()
)
mscFrMuxFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerOctetFromIf.setStatus("obsolete")
_MscFrMuxFramerAborts_Type = Counter32
_MscFrMuxFramerAborts_Object = MibTableColumn
mscFrMuxFramerAborts = _MscFrMuxFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 4),
    _MscFrMuxFramerAborts_Type()
)
mscFrMuxFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerAborts.setStatus("mandatory")
_MscFrMuxFramerCrcErrors_Type = Counter32
_MscFrMuxFramerCrcErrors_Object = MibTableColumn
mscFrMuxFramerCrcErrors = _MscFrMuxFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 5),
    _MscFrMuxFramerCrcErrors_Type()
)
mscFrMuxFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerCrcErrors.setStatus("mandatory")
_MscFrMuxFramerLrcErrors_Type = Counter32
_MscFrMuxFramerLrcErrors_Object = MibTableColumn
mscFrMuxFramerLrcErrors = _MscFrMuxFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 6),
    _MscFrMuxFramerLrcErrors_Type()
)
mscFrMuxFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerLrcErrors.setStatus("mandatory")
_MscFrMuxFramerNonOctetErrors_Type = Counter32
_MscFrMuxFramerNonOctetErrors_Object = MibTableColumn
mscFrMuxFramerNonOctetErrors = _MscFrMuxFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 7),
    _MscFrMuxFramerNonOctetErrors_Type()
)
mscFrMuxFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerNonOctetErrors.setStatus("mandatory")
_MscFrMuxFramerOverruns_Type = Counter32
_MscFrMuxFramerOverruns_Object = MibTableColumn
mscFrMuxFramerOverruns = _MscFrMuxFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 8),
    _MscFrMuxFramerOverruns_Type()
)
mscFrMuxFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerOverruns.setStatus("mandatory")
_MscFrMuxFramerUnderruns_Type = Counter32
_MscFrMuxFramerUnderruns_Object = MibTableColumn
mscFrMuxFramerUnderruns = _MscFrMuxFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 9),
    _MscFrMuxFramerUnderruns_Type()
)
mscFrMuxFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerUnderruns.setStatus("mandatory")
_MscFrMuxFramerLargeFrmErrors_Type = Counter32
_MscFrMuxFramerLargeFrmErrors_Object = MibTableColumn
mscFrMuxFramerLargeFrmErrors = _MscFrMuxFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 10),
    _MscFrMuxFramerLargeFrmErrors_Type()
)
mscFrMuxFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerLargeFrmErrors.setStatus("mandatory")
_MscFrMuxFramerFrmModeErrors_Type = Counter32
_MscFrMuxFramerFrmModeErrors_Object = MibTableColumn
mscFrMuxFramerFrmModeErrors = _MscFrMuxFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 11),
    _MscFrMuxFramerFrmModeErrors_Type()
)
mscFrMuxFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrmModeErrors.setStatus("mandatory")
_MscFrMuxFramerFrmToIf64_Type = PassportCounter64
_MscFrMuxFramerFrmToIf64_Object = MibTableColumn
mscFrMuxFramerFrmToIf64 = _MscFrMuxFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 14),
    _MscFrMuxFramerFrmToIf64_Type()
)
mscFrMuxFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrmToIf64.setStatus("mandatory")
_MscFrMuxFramerFrmFromIf64_Type = PassportCounter64
_MscFrMuxFramerFrmFromIf64_Object = MibTableColumn
mscFrMuxFramerFrmFromIf64 = _MscFrMuxFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 15),
    _MscFrMuxFramerFrmFromIf64_Type()
)
mscFrMuxFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerFrmFromIf64.setStatus("mandatory")
_MscFrMuxFramerOctetFromIf64_Type = PassportCounter64
_MscFrMuxFramerOctetFromIf64_Object = MibTableColumn
mscFrMuxFramerOctetFromIf64 = _MscFrMuxFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 13, 1, 16),
    _MscFrMuxFramerOctetFromIf64_Type()
)
mscFrMuxFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerOctetFromIf64.setStatus("mandatory")
_MscFrMuxFramerUtilTable_Object = MibTable
mscFrMuxFramerUtilTable = _MscFrMuxFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 14)
)
if mibBuilder.loadTexts:
    mscFrMuxFramerUtilTable.setStatus("mandatory")
_MscFrMuxFramerUtilEntry_Object = MibTableRow
mscFrMuxFramerUtilEntry = _MscFrMuxFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 14, 1)
)
mscFrMuxFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxFramerUtilEntry.setStatus("mandatory")


class _MscFrMuxFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscFrMuxFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrMuxFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscFrMuxFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscFrMuxFramerNormPrioLinkUtilToIf = _MscFrMuxFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 14, 1, 1),
    _MscFrMuxFramerNormPrioLinkUtilToIf_Type()
)
mscFrMuxFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscFrMuxFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscFrMuxFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrMuxFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscFrMuxFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscFrMuxFramerNormPrioLinkUtilFromIf = _MscFrMuxFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 2, 14, 1, 3),
    _MscFrMuxFramerNormPrioLinkUtilFromIf_Type()
)
mscFrMuxFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscFrMuxLmi_ObjectIdentity = ObjectIdentity
mscFrMuxLmi = _MscFrMuxLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3)
)
_MscFrMuxLmiRowStatusTable_Object = MibTable
mscFrMuxLmiRowStatusTable = _MscFrMuxLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrMuxLmiRowStatusTable.setStatus("mandatory")
_MscFrMuxLmiRowStatusEntry_Object = MibTableRow
mscFrMuxLmiRowStatusEntry = _MscFrMuxLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1, 1)
)
mscFrMuxLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxLmiRowStatusEntry.setStatus("mandatory")
_MscFrMuxLmiRowStatus_Type = RowStatus
_MscFrMuxLmiRowStatus_Object = MibTableColumn
mscFrMuxLmiRowStatus = _MscFrMuxLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1, 1, 1),
    _MscFrMuxLmiRowStatus_Type()
)
mscFrMuxLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiRowStatus.setStatus("mandatory")
_MscFrMuxLmiComponentName_Type = DisplayString
_MscFrMuxLmiComponentName_Object = MibTableColumn
mscFrMuxLmiComponentName = _MscFrMuxLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1, 1, 2),
    _MscFrMuxLmiComponentName_Type()
)
mscFrMuxLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiComponentName.setStatus("mandatory")
_MscFrMuxLmiStorageType_Type = StorageType
_MscFrMuxLmiStorageType_Object = MibTableColumn
mscFrMuxLmiStorageType = _MscFrMuxLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1, 1, 4),
    _MscFrMuxLmiStorageType_Type()
)
mscFrMuxLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiStorageType.setStatus("mandatory")
_MscFrMuxLmiIndex_Type = NonReplicated
_MscFrMuxLmiIndex_Object = MibTableColumn
mscFrMuxLmiIndex = _MscFrMuxLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 1, 1, 10),
    _MscFrMuxLmiIndex_Type()
)
mscFrMuxLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrMuxLmiIndex.setStatus("mandatory")
_MscFrMuxLmiProvTable_Object = MibTable
mscFrMuxLmiProvTable = _MscFrMuxLmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrMuxLmiProvTable.setStatus("mandatory")
_MscFrMuxLmiProvEntry_Object = MibTableRow
mscFrMuxLmiProvEntry = _MscFrMuxLmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1)
)
mscFrMuxLmiProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxLmiProvEntry.setStatus("mandatory")


class _MscFrMuxLmiProcedures_Type(Integer32):
    """Custom type mscFrMuxLmiProcedures based on Integer32"""
    defaultValue = 3

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
        *(("ansi", 2),
          ("ccitt", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_MscFrMuxLmiProcedures_Type.__name__ = "Integer32"
_MscFrMuxLmiProcedures_Object = MibTableColumn
mscFrMuxLmiProcedures = _MscFrMuxLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1, 1),
    _MscFrMuxLmiProcedures_Type()
)
mscFrMuxLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxLmiProcedures.setStatus("mandatory")


class _MscFrMuxLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mscFrMuxLmiLinkVerificationTimer based on Unsigned32"""
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


_MscFrMuxLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_MscFrMuxLmiLinkVerificationTimer_Object = MibTableColumn
mscFrMuxLmiLinkVerificationTimer = _MscFrMuxLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1, 2),
    _MscFrMuxLmiLinkVerificationTimer_Type()
)
mscFrMuxLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxLmiLinkVerificationTimer.setStatus("mandatory")


class _MscFrMuxLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mscFrMuxLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrMuxLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_MscFrMuxLmiFullStatusPollingCycles_Object = MibTableColumn
mscFrMuxLmiFullStatusPollingCycles = _MscFrMuxLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1, 3),
    _MscFrMuxLmiFullStatusPollingCycles_Type()
)
mscFrMuxLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxLmiFullStatusPollingCycles.setStatus("mandatory")


class _MscFrMuxLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mscFrMuxLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrMuxLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_MscFrMuxLmiErrorEventThreshold_Object = MibTableColumn
mscFrMuxLmiErrorEventThreshold = _MscFrMuxLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1, 4),
    _MscFrMuxLmiErrorEventThreshold_Type()
)
mscFrMuxLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxLmiErrorEventThreshold.setStatus("mandatory")


class _MscFrMuxLmiEventCount_Type(Unsigned32):
    """Custom type mscFrMuxLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrMuxLmiEventCount_Type.__name__ = "Unsigned32"
_MscFrMuxLmiEventCount_Object = MibTableColumn
mscFrMuxLmiEventCount = _MscFrMuxLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 10, 1, 5),
    _MscFrMuxLmiEventCount_Type()
)
mscFrMuxLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxLmiEventCount.setStatus("mandatory")
_MscFrMuxLmiStateTable_Object = MibTable
mscFrMuxLmiStateTable = _MscFrMuxLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrMuxLmiStateTable.setStatus("mandatory")
_MscFrMuxLmiStateEntry_Object = MibTableRow
mscFrMuxLmiStateEntry = _MscFrMuxLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 11, 1)
)
mscFrMuxLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxLmiStateEntry.setStatus("mandatory")


class _MscFrMuxLmiAdminState_Type(Integer32):
    """Custom type mscFrMuxLmiAdminState based on Integer32"""
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


_MscFrMuxLmiAdminState_Type.__name__ = "Integer32"
_MscFrMuxLmiAdminState_Object = MibTableColumn
mscFrMuxLmiAdminState = _MscFrMuxLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 11, 1, 1),
    _MscFrMuxLmiAdminState_Type()
)
mscFrMuxLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiAdminState.setStatus("mandatory")


class _MscFrMuxLmiOperationalState_Type(Integer32):
    """Custom type mscFrMuxLmiOperationalState based on Integer32"""
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


_MscFrMuxLmiOperationalState_Type.__name__ = "Integer32"
_MscFrMuxLmiOperationalState_Object = MibTableColumn
mscFrMuxLmiOperationalState = _MscFrMuxLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 11, 1, 2),
    _MscFrMuxLmiOperationalState_Type()
)
mscFrMuxLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiOperationalState.setStatus("mandatory")


class _MscFrMuxLmiUsageState_Type(Integer32):
    """Custom type mscFrMuxLmiUsageState based on Integer32"""
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


_MscFrMuxLmiUsageState_Type.__name__ = "Integer32"
_MscFrMuxLmiUsageState_Object = MibTableColumn
mscFrMuxLmiUsageState = _MscFrMuxLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 11, 1, 3),
    _MscFrMuxLmiUsageState_Type()
)
mscFrMuxLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiUsageState.setStatus("mandatory")
_MscFrMuxLmiPsiTable_Object = MibTable
mscFrMuxLmiPsiTable = _MscFrMuxLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrMuxLmiPsiTable.setStatus("mandatory")
_MscFrMuxLmiPsiEntry_Object = MibTableRow
mscFrMuxLmiPsiEntry = _MscFrMuxLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 12, 1)
)
mscFrMuxLmiPsiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxLmiPsiEntry.setStatus("mandatory")


class _MscFrMuxLmiProtocolStatus_Type(Integer32):
    """Custom type mscFrMuxLmiProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("errorCondition", 0),
          ("normalCondition", 1))
    )


_MscFrMuxLmiProtocolStatus_Type.__name__ = "Integer32"
_MscFrMuxLmiProtocolStatus_Object = MibTableColumn
mscFrMuxLmiProtocolStatus = _MscFrMuxLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 12, 1, 1),
    _MscFrMuxLmiProtocolStatus_Type()
)
mscFrMuxLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiProtocolStatus.setStatus("mandatory")
_MscFrMuxLmiStatsTable_Object = MibTable
mscFrMuxLmiStatsTable = _MscFrMuxLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13)
)
if mibBuilder.loadTexts:
    mscFrMuxLmiStatsTable.setStatus("mandatory")
_MscFrMuxLmiStatsEntry_Object = MibTableRow
mscFrMuxLmiStatsEntry = _MscFrMuxLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1)
)
mscFrMuxLmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxLmiStatsEntry.setStatus("mandatory")
_MscFrMuxLmiKeepAliveStatusEnqToIf_Type = Counter32
_MscFrMuxLmiKeepAliveStatusEnqToIf_Object = MibTableColumn
mscFrMuxLmiKeepAliveStatusEnqToIf = _MscFrMuxLmiKeepAliveStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 1),
    _MscFrMuxLmiKeepAliveStatusEnqToIf_Type()
)
mscFrMuxLmiKeepAliveStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiKeepAliveStatusEnqToIf.setStatus("mandatory")
_MscFrMuxLmiFullStatusEnqToIf_Type = Counter32
_MscFrMuxLmiFullStatusEnqToIf_Object = MibTableColumn
mscFrMuxLmiFullStatusEnqToIf = _MscFrMuxLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 2),
    _MscFrMuxLmiFullStatusEnqToIf_Type()
)
mscFrMuxLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiFullStatusEnqToIf.setStatus("mandatory")
_MscFrMuxLmiProtocolErrors_Type = Counter32
_MscFrMuxLmiProtocolErrors_Object = MibTableColumn
mscFrMuxLmiProtocolErrors = _MscFrMuxLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 3),
    _MscFrMuxLmiProtocolErrors_Type()
)
mscFrMuxLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiProtocolErrors.setStatus("mandatory")
_MscFrMuxLmiUnexpectedIes_Type = Counter32
_MscFrMuxLmiUnexpectedIes_Object = MibTableColumn
mscFrMuxLmiUnexpectedIes = _MscFrMuxLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 4),
    _MscFrMuxLmiUnexpectedIes_Type()
)
mscFrMuxLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiUnexpectedIes.setStatus("mandatory")
_MscFrMuxLmiSequenceErrors_Type = Counter32
_MscFrMuxLmiSequenceErrors_Object = MibTableColumn
mscFrMuxLmiSequenceErrors = _MscFrMuxLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 5),
    _MscFrMuxLmiSequenceErrors_Type()
)
mscFrMuxLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiSequenceErrors.setStatus("mandatory")
_MscFrMuxLmiUnexpectedReports_Type = Counter32
_MscFrMuxLmiUnexpectedReports_Object = MibTableColumn
mscFrMuxLmiUnexpectedReports = _MscFrMuxLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 6),
    _MscFrMuxLmiUnexpectedReports_Type()
)
mscFrMuxLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiUnexpectedReports.setStatus("mandatory")
_MscFrMuxLmiNoStatusReportCount_Type = Counter32
_MscFrMuxLmiNoStatusReportCount_Object = MibTableColumn
mscFrMuxLmiNoStatusReportCount = _MscFrMuxLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 3, 13, 1, 7),
    _MscFrMuxLmiNoStatusReportCount_Type()
)
mscFrMuxLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLmiNoStatusReportCount.setStatus("mandatory")
_MscFrMuxDlci_ObjectIdentity = ObjectIdentity
mscFrMuxDlci = _MscFrMuxDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4)
)
_MscFrMuxDlciRowStatusTable_Object = MibTable
mscFrMuxDlciRowStatusTable = _MscFrMuxDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciRowStatusTable.setStatus("mandatory")
_MscFrMuxDlciRowStatusEntry_Object = MibTableRow
mscFrMuxDlciRowStatusEntry = _MscFrMuxDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1, 1)
)
mscFrMuxDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciRowStatusEntry.setStatus("mandatory")
_MscFrMuxDlciRowStatus_Type = RowStatus
_MscFrMuxDlciRowStatus_Object = MibTableColumn
mscFrMuxDlciRowStatus = _MscFrMuxDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1, 1, 1),
    _MscFrMuxDlciRowStatus_Type()
)
mscFrMuxDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxDlciRowStatus.setStatus("mandatory")
_MscFrMuxDlciComponentName_Type = DisplayString
_MscFrMuxDlciComponentName_Object = MibTableColumn
mscFrMuxDlciComponentName = _MscFrMuxDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1, 1, 2),
    _MscFrMuxDlciComponentName_Type()
)
mscFrMuxDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciComponentName.setStatus("mandatory")
_MscFrMuxDlciStorageType_Type = StorageType
_MscFrMuxDlciStorageType_Object = MibTableColumn
mscFrMuxDlciStorageType = _MscFrMuxDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1, 1, 4),
    _MscFrMuxDlciStorageType_Type()
)
mscFrMuxDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciStorageType.setStatus("mandatory")


class _MscFrMuxDlciIndex_Type(Integer32):
    """Custom type mscFrMuxDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrMuxDlciIndex_Type.__name__ = "Integer32"
_MscFrMuxDlciIndex_Object = MibTableColumn
mscFrMuxDlciIndex = _MscFrMuxDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 1, 1, 10),
    _MscFrMuxDlciIndex_Type()
)
mscFrMuxDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrMuxDlciIndex.setStatus("mandatory")
_MscFrMuxDlciApplInfo_ObjectIdentity = ObjectIdentity
mscFrMuxDlciApplInfo = _MscFrMuxDlciApplInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2)
)
_MscFrMuxDlciApplInfoRowStatusTable_Object = MibTable
mscFrMuxDlciApplInfoRowStatusTable = _MscFrMuxDlciApplInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoRowStatusTable.setStatus("mandatory")
_MscFrMuxDlciApplInfoRowStatusEntry_Object = MibTableRow
mscFrMuxDlciApplInfoRowStatusEntry = _MscFrMuxDlciApplInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1, 1)
)
mscFrMuxDlciApplInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciApplInfoIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoRowStatusEntry.setStatus("mandatory")
_MscFrMuxDlciApplInfoRowStatus_Type = RowStatus
_MscFrMuxDlciApplInfoRowStatus_Object = MibTableColumn
mscFrMuxDlciApplInfoRowStatus = _MscFrMuxDlciApplInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1, 1, 1),
    _MscFrMuxDlciApplInfoRowStatus_Type()
)
mscFrMuxDlciApplInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoRowStatus.setStatus("mandatory")
_MscFrMuxDlciApplInfoComponentName_Type = DisplayString
_MscFrMuxDlciApplInfoComponentName_Object = MibTableColumn
mscFrMuxDlciApplInfoComponentName = _MscFrMuxDlciApplInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1, 1, 2),
    _MscFrMuxDlciApplInfoComponentName_Type()
)
mscFrMuxDlciApplInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoComponentName.setStatus("mandatory")
_MscFrMuxDlciApplInfoStorageType_Type = StorageType
_MscFrMuxDlciApplInfoStorageType_Object = MibTableColumn
mscFrMuxDlciApplInfoStorageType = _MscFrMuxDlciApplInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1, 1, 4),
    _MscFrMuxDlciApplInfoStorageType_Type()
)
mscFrMuxDlciApplInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoStorageType.setStatus("mandatory")
_MscFrMuxDlciApplInfoIndex_Type = NonReplicated
_MscFrMuxDlciApplInfoIndex_Object = MibTableColumn
mscFrMuxDlciApplInfoIndex = _MscFrMuxDlciApplInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 1, 1, 10),
    _MscFrMuxDlciApplInfoIndex_Type()
)
mscFrMuxDlciApplInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoIndex.setStatus("mandatory")
_MscFrMuxDlciApplInfoProvTable_Object = MibTable
mscFrMuxDlciApplInfoProvTable = _MscFrMuxDlciApplInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoProvTable.setStatus("mandatory")
_MscFrMuxDlciApplInfoProvEntry_Object = MibTableRow
mscFrMuxDlciApplInfoProvEntry = _MscFrMuxDlciApplInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 11, 1)
)
mscFrMuxDlciApplInfoProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciApplInfoIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoProvEntry.setStatus("mandatory")
_MscFrMuxDlciApplInfoApplicationName_Type = Link
_MscFrMuxDlciApplInfoApplicationName_Object = MibTableColumn
mscFrMuxDlciApplInfoApplicationName = _MscFrMuxDlciApplInfoApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 2, 11, 1, 1),
    _MscFrMuxDlciApplInfoApplicationName_Type()
)
mscFrMuxDlciApplInfoApplicationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplInfoApplicationName.setStatus("mandatory")
_MscFrMuxDlciOperTable_Object = MibTable
mscFrMuxDlciOperTable = _MscFrMuxDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciOperTable.setStatus("mandatory")
_MscFrMuxDlciOperEntry_Object = MibTableRow
mscFrMuxDlciOperEntry = _MscFrMuxDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 10, 1)
)
mscFrMuxDlciOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciOperEntry.setStatus("mandatory")
_MscFrMuxDlciApplicationName_Type = RowPointer
_MscFrMuxDlciApplicationName_Object = MibTableColumn
mscFrMuxDlciApplicationName = _MscFrMuxDlciApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 10, 1, 1),
    _MscFrMuxDlciApplicationName_Type()
)
mscFrMuxDlciApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciApplicationName.setStatus("mandatory")
_MscFrMuxDlciStateTable_Object = MibTable
mscFrMuxDlciStateTable = _MscFrMuxDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciStateTable.setStatus("mandatory")
_MscFrMuxDlciStateEntry_Object = MibTableRow
mscFrMuxDlciStateEntry = _MscFrMuxDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 11, 1)
)
mscFrMuxDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciStateEntry.setStatus("mandatory")


class _MscFrMuxDlciAdminState_Type(Integer32):
    """Custom type mscFrMuxDlciAdminState based on Integer32"""
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


_MscFrMuxDlciAdminState_Type.__name__ = "Integer32"
_MscFrMuxDlciAdminState_Object = MibTableColumn
mscFrMuxDlciAdminState = _MscFrMuxDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 11, 1, 1),
    _MscFrMuxDlciAdminState_Type()
)
mscFrMuxDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciAdminState.setStatus("mandatory")


class _MscFrMuxDlciOperationalState_Type(Integer32):
    """Custom type mscFrMuxDlciOperationalState based on Integer32"""
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


_MscFrMuxDlciOperationalState_Type.__name__ = "Integer32"
_MscFrMuxDlciOperationalState_Object = MibTableColumn
mscFrMuxDlciOperationalState = _MscFrMuxDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 11, 1, 2),
    _MscFrMuxDlciOperationalState_Type()
)
mscFrMuxDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciOperationalState.setStatus("mandatory")


class _MscFrMuxDlciUsageState_Type(Integer32):
    """Custom type mscFrMuxDlciUsageState based on Integer32"""
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


_MscFrMuxDlciUsageState_Type.__name__ = "Integer32"
_MscFrMuxDlciUsageState_Object = MibTableColumn
mscFrMuxDlciUsageState = _MscFrMuxDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 11, 1, 3),
    _MscFrMuxDlciUsageState_Type()
)
mscFrMuxDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciUsageState.setStatus("mandatory")
_MscFrMuxDlciAbitTable_Object = MibTable
mscFrMuxDlciAbitTable = _MscFrMuxDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 12)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciAbitTable.setStatus("mandatory")
_MscFrMuxDlciAbitEntry_Object = MibTableRow
mscFrMuxDlciAbitEntry = _MscFrMuxDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 12, 1)
)
mscFrMuxDlciAbitEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciAbitEntry.setStatus("mandatory")


class _MscFrMuxDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscFrMuxDlciABitStatusFromIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_MscFrMuxDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscFrMuxDlciABitStatusFromIf_Object = MibTableColumn
mscFrMuxDlciABitStatusFromIf = _MscFrMuxDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 12, 1, 1),
    _MscFrMuxDlciABitStatusFromIf_Type()
)
mscFrMuxDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciABitStatusFromIf.setStatus("mandatory")
_MscFrMuxDlciStatsTable_Object = MibTable
mscFrMuxDlciStatsTable = _MscFrMuxDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13)
)
if mibBuilder.loadTexts:
    mscFrMuxDlciStatsTable.setStatus("mandatory")
_MscFrMuxDlciStatsEntry_Object = MibTableRow
mscFrMuxDlciStatsEntry = _MscFrMuxDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1)
)
mscFrMuxDlciStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxDlciStatsEntry.setStatus("mandatory")
_MscFrMuxDlciFrmToIf_Type = Counter32
_MscFrMuxDlciFrmToIf_Object = MibTableColumn
mscFrMuxDlciFrmToIf = _MscFrMuxDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 1),
    _MscFrMuxDlciFrmToIf_Type()
)
mscFrMuxDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciFrmToIf.setStatus("mandatory")
_MscFrMuxDlciBytesToIf_Type = PassportCounter64
_MscFrMuxDlciBytesToIf_Object = MibTableColumn
mscFrMuxDlciBytesToIf = _MscFrMuxDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 2),
    _MscFrMuxDlciBytesToIf_Type()
)
mscFrMuxDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciBytesToIf.setStatus("mandatory")
_MscFrMuxDlciFrmFromIf_Type = Counter32
_MscFrMuxDlciFrmFromIf_Object = MibTableColumn
mscFrMuxDlciFrmFromIf = _MscFrMuxDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 3),
    _MscFrMuxDlciFrmFromIf_Type()
)
mscFrMuxDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciFrmFromIf.setStatus("mandatory")
_MscFrMuxDlciDeFrmFromIf_Type = Counter32
_MscFrMuxDlciDeFrmFromIf_Object = MibTableColumn
mscFrMuxDlciDeFrmFromIf = _MscFrMuxDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 4),
    _MscFrMuxDlciDeFrmFromIf_Type()
)
mscFrMuxDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDeFrmFromIf.setStatus("mandatory")
_MscFrMuxDlciBytesFromIf_Type = PassportCounter64
_MscFrMuxDlciBytesFromIf_Object = MibTableColumn
mscFrMuxDlciBytesFromIf = _MscFrMuxDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 5),
    _MscFrMuxDlciBytesFromIf_Type()
)
mscFrMuxDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciBytesFromIf.setStatus("mandatory")
_MscFrMuxDlciDeBytesFromIf_Type = PassportCounter64
_MscFrMuxDlciDeBytesFromIf_Object = MibTableColumn
mscFrMuxDlciDeBytesFromIf = _MscFrMuxDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 6),
    _MscFrMuxDlciDeBytesFromIf_Type()
)
mscFrMuxDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDeBytesFromIf.setStatus("mandatory")
_MscFrMuxDlciFecnFrmToIf_Type = Counter32
_MscFrMuxDlciFecnFrmToIf_Object = MibTableColumn
mscFrMuxDlciFecnFrmToIf = _MscFrMuxDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 7),
    _MscFrMuxDlciFecnFrmToIf_Type()
)
mscFrMuxDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciFecnFrmToIf.setStatus("mandatory")
_MscFrMuxDlciFecnFrmFromIf_Type = Counter32
_MscFrMuxDlciFecnFrmFromIf_Object = MibTableColumn
mscFrMuxDlciFecnFrmFromIf = _MscFrMuxDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 8),
    _MscFrMuxDlciFecnFrmFromIf_Type()
)
mscFrMuxDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciFecnFrmFromIf.setStatus("mandatory")
_MscFrMuxDlciBecnFrmToIf_Type = Counter32
_MscFrMuxDlciBecnFrmToIf_Object = MibTableColumn
mscFrMuxDlciBecnFrmToIf = _MscFrMuxDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 9),
    _MscFrMuxDlciBecnFrmToIf_Type()
)
mscFrMuxDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciBecnFrmToIf.setStatus("mandatory")
_MscFrMuxDlciBecnFrmFromIf_Type = Counter32
_MscFrMuxDlciBecnFrmFromIf_Object = MibTableColumn
mscFrMuxDlciBecnFrmFromIf = _MscFrMuxDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 10),
    _MscFrMuxDlciBecnFrmFromIf_Type()
)
mscFrMuxDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciBecnFrmFromIf.setStatus("mandatory")
_MscFrMuxDlciDiscCongestedFromIf_Type = Counter32
_MscFrMuxDlciDiscCongestedFromIf_Object = MibTableColumn
mscFrMuxDlciDiscCongestedFromIf = _MscFrMuxDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 11),
    _MscFrMuxDlciDiscCongestedFromIf_Type()
)
mscFrMuxDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDiscCongestedFromIf.setStatus("mandatory")
_MscFrMuxDlciDiscCongestedFromIfBytes_Type = Counter32
_MscFrMuxDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mscFrMuxDlciDiscCongestedFromIfBytes = _MscFrMuxDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 12),
    _MscFrMuxDlciDiscCongestedFromIfBytes_Type()
)
mscFrMuxDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDiscCongestedFromIfBytes.setStatus("mandatory")
_MscFrMuxDlciDiscDeCongestedFromIf_Type = Counter32
_MscFrMuxDlciDiscDeCongestedFromIf_Object = MibTableColumn
mscFrMuxDlciDiscDeCongestedFromIf = _MscFrMuxDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 13),
    _MscFrMuxDlciDiscDeCongestedFromIf_Type()
)
mscFrMuxDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDiscDeCongestedFromIf.setStatus("mandatory")
_MscFrMuxDlciDiscDeCongestedFromIfBytes_Type = Counter32
_MscFrMuxDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mscFrMuxDlciDiscDeCongestedFromIfBytes = _MscFrMuxDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 14),
    _MscFrMuxDlciDiscDeCongestedFromIfBytes_Type()
)
mscFrMuxDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")
_MscFrMuxDlciErrorShortFrmFromIf_Type = Counter32
_MscFrMuxDlciErrorShortFrmFromIf_Object = MibTableColumn
mscFrMuxDlciErrorShortFrmFromIf = _MscFrMuxDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 15),
    _MscFrMuxDlciErrorShortFrmFromIf_Type()
)
mscFrMuxDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciErrorShortFrmFromIf.setStatus("mandatory")
_MscFrMuxDlciErrorLongFrmFromIf_Type = Counter32
_MscFrMuxDlciErrorLongFrmFromIf_Object = MibTableColumn
mscFrMuxDlciErrorLongFrmFromIf = _MscFrMuxDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 4, 13, 1, 16),
    _MscFrMuxDlciErrorLongFrmFromIf_Type()
)
mscFrMuxDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxDlciErrorLongFrmFromIf.setStatus("mandatory")
_MscFrMuxOperStatusTable_Object = MibTable
mscFrMuxOperStatusTable = _MscFrMuxOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 8)
)
if mibBuilder.loadTexts:
    mscFrMuxOperStatusTable.setStatus("mandatory")
_MscFrMuxOperStatusEntry_Object = MibTableRow
mscFrMuxOperStatusEntry = _MscFrMuxOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 8, 1)
)
mscFrMuxOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxOperStatusEntry.setStatus("mandatory")


class _MscFrMuxSnmpOperStatus_Type(Integer32):
    """Custom type mscFrMuxSnmpOperStatus based on Integer32"""
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


_MscFrMuxSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrMuxSnmpOperStatus_Object = MibTableColumn
mscFrMuxSnmpOperStatus = _MscFrMuxSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 8, 1, 1),
    _MscFrMuxSnmpOperStatus_Type()
)
mscFrMuxSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxSnmpOperStatus.setStatus("mandatory")
_MscFrMuxIfEntryTable_Object = MibTable
mscFrMuxIfEntryTable = _MscFrMuxIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 9)
)
if mibBuilder.loadTexts:
    mscFrMuxIfEntryTable.setStatus("mandatory")
_MscFrMuxIfEntryEntry_Object = MibTableRow
mscFrMuxIfEntryEntry = _MscFrMuxIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 9, 1)
)
mscFrMuxIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxIfEntryEntry.setStatus("mandatory")


class _MscFrMuxIfAdminStatus_Type(Integer32):
    """Custom type mscFrMuxIfAdminStatus based on Integer32"""
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


_MscFrMuxIfAdminStatus_Type.__name__ = "Integer32"
_MscFrMuxIfAdminStatus_Object = MibTableColumn
mscFrMuxIfAdminStatus = _MscFrMuxIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 9, 1, 1),
    _MscFrMuxIfAdminStatus_Type()
)
mscFrMuxIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxIfAdminStatus.setStatus("mandatory")


class _MscFrMuxIfIndex_Type(InterfaceIndex):
    """Custom type mscFrMuxIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrMuxIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrMuxIfIndex_Object = MibTableColumn
mscFrMuxIfIndex = _MscFrMuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 9, 1, 2),
    _MscFrMuxIfIndex_Type()
)
mscFrMuxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxIfIndex.setStatus("mandatory")
_MscFrMuxCidDataTable_Object = MibTable
mscFrMuxCidDataTable = _MscFrMuxCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 10)
)
if mibBuilder.loadTexts:
    mscFrMuxCidDataTable.setStatus("mandatory")
_MscFrMuxCidDataEntry_Object = MibTableRow
mscFrMuxCidDataEntry = _MscFrMuxCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 10, 1)
)
mscFrMuxCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxCidDataEntry.setStatus("mandatory")


class _MscFrMuxCustomerIdentifier_Type(Unsigned32):
    """Custom type mscFrMuxCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscFrMuxCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscFrMuxCustomerIdentifier_Object = MibTableColumn
mscFrMuxCustomerIdentifier = _MscFrMuxCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 10, 1, 1),
    _MscFrMuxCustomerIdentifier_Type()
)
mscFrMuxCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrMuxCustomerIdentifier.setStatus("mandatory")
_MscFrMuxStateTable_Object = MibTable
mscFrMuxStateTable = _MscFrMuxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11)
)
if mibBuilder.loadTexts:
    mscFrMuxStateTable.setStatus("mandatory")
_MscFrMuxStateEntry_Object = MibTableRow
mscFrMuxStateEntry = _MscFrMuxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1)
)
mscFrMuxStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxStateEntry.setStatus("mandatory")


class _MscFrMuxAdminState_Type(Integer32):
    """Custom type mscFrMuxAdminState based on Integer32"""
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


_MscFrMuxAdminState_Type.__name__ = "Integer32"
_MscFrMuxAdminState_Object = MibTableColumn
mscFrMuxAdminState = _MscFrMuxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 1),
    _MscFrMuxAdminState_Type()
)
mscFrMuxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxAdminState.setStatus("mandatory")


class _MscFrMuxOperationalState_Type(Integer32):
    """Custom type mscFrMuxOperationalState based on Integer32"""
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


_MscFrMuxOperationalState_Type.__name__ = "Integer32"
_MscFrMuxOperationalState_Object = MibTableColumn
mscFrMuxOperationalState = _MscFrMuxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 2),
    _MscFrMuxOperationalState_Type()
)
mscFrMuxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxOperationalState.setStatus("mandatory")


class _MscFrMuxUsageState_Type(Integer32):
    """Custom type mscFrMuxUsageState based on Integer32"""
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


_MscFrMuxUsageState_Type.__name__ = "Integer32"
_MscFrMuxUsageState_Object = MibTableColumn
mscFrMuxUsageState = _MscFrMuxUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 3),
    _MscFrMuxUsageState_Type()
)
mscFrMuxUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxUsageState.setStatus("mandatory")


class _MscFrMuxAvailabilityStatus_Type(OctetString):
    """Custom type mscFrMuxAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrMuxAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrMuxAvailabilityStatus_Object = MibTableColumn
mscFrMuxAvailabilityStatus = _MscFrMuxAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 4),
    _MscFrMuxAvailabilityStatus_Type()
)
mscFrMuxAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxAvailabilityStatus.setStatus("mandatory")


class _MscFrMuxProceduralStatus_Type(OctetString):
    """Custom type mscFrMuxProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrMuxProceduralStatus_Type.__name__ = "OctetString"
_MscFrMuxProceduralStatus_Object = MibTableColumn
mscFrMuxProceduralStatus = _MscFrMuxProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 5),
    _MscFrMuxProceduralStatus_Type()
)
mscFrMuxProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxProceduralStatus.setStatus("mandatory")


class _MscFrMuxControlStatus_Type(OctetString):
    """Custom type mscFrMuxControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrMuxControlStatus_Type.__name__ = "OctetString"
_MscFrMuxControlStatus_Object = MibTableColumn
mscFrMuxControlStatus = _MscFrMuxControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 6),
    _MscFrMuxControlStatus_Type()
)
mscFrMuxControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxControlStatus.setStatus("mandatory")


class _MscFrMuxAlarmStatus_Type(OctetString):
    """Custom type mscFrMuxAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrMuxAlarmStatus_Type.__name__ = "OctetString"
_MscFrMuxAlarmStatus_Object = MibTableColumn
mscFrMuxAlarmStatus = _MscFrMuxAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 7),
    _MscFrMuxAlarmStatus_Type()
)
mscFrMuxAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxAlarmStatus.setStatus("mandatory")


class _MscFrMuxStandbyStatus_Type(Integer32):
    """Custom type mscFrMuxStandbyStatus based on Integer32"""
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


_MscFrMuxStandbyStatus_Type.__name__ = "Integer32"
_MscFrMuxStandbyStatus_Object = MibTableColumn
mscFrMuxStandbyStatus = _MscFrMuxStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 8),
    _MscFrMuxStandbyStatus_Type()
)
mscFrMuxStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxStandbyStatus.setStatus("mandatory")


class _MscFrMuxUnknownStatus_Type(Integer32):
    """Custom type mscFrMuxUnknownStatus based on Integer32"""
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


_MscFrMuxUnknownStatus_Type.__name__ = "Integer32"
_MscFrMuxUnknownStatus_Object = MibTableColumn
mscFrMuxUnknownStatus = _MscFrMuxUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 11, 1, 9),
    _MscFrMuxUnknownStatus_Type()
)
mscFrMuxUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxUnknownStatus.setStatus("mandatory")
_MscFrMuxStatsTable_Object = MibTable
mscFrMuxStatsTable = _MscFrMuxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12)
)
if mibBuilder.loadTexts:
    mscFrMuxStatsTable.setStatus("mandatory")
_MscFrMuxStatsEntry_Object = MibTableRow
mscFrMuxStatsEntry = _MscFrMuxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12, 1)
)
mscFrMuxStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB", "mscFrMuxIndex"),
)
if mibBuilder.loadTexts:
    mscFrMuxStatsEntry.setStatus("mandatory")


class _MscFrMuxLastUnknownDlci_Type(Unsigned32):
    """Custom type mscFrMuxLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFrMuxLastUnknownDlci_Type.__name__ = "Unsigned32"
_MscFrMuxLastUnknownDlci_Object = MibTableColumn
mscFrMuxLastUnknownDlci = _MscFrMuxLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12, 1, 1),
    _MscFrMuxLastUnknownDlci_Type()
)
mscFrMuxLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxLastUnknownDlci.setStatus("mandatory")
_MscFrMuxUnknownDlciFramesFromIf_Type = Counter32
_MscFrMuxUnknownDlciFramesFromIf_Object = MibTableColumn
mscFrMuxUnknownDlciFramesFromIf = _MscFrMuxUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12, 1, 2),
    _MscFrMuxUnknownDlciFramesFromIf_Type()
)
mscFrMuxUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxUnknownDlciFramesFromIf.setStatus("mandatory")
_MscFrMuxInvalidHeaderFramesFromIf_Type = Counter32
_MscFrMuxInvalidHeaderFramesFromIf_Object = MibTableColumn
mscFrMuxInvalidHeaderFramesFromIf = _MscFrMuxInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12, 1, 3),
    _MscFrMuxInvalidHeaderFramesFromIf_Type()
)
mscFrMuxInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxInvalidHeaderFramesFromIf.setStatus("mandatory")
_MscFrMuxTimeFramerCongested_Type = Counter32
_MscFrMuxTimeFramerCongested_Object = MibTableColumn
mscFrMuxTimeFramerCongested = _MscFrMuxTimeFramerCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 112, 12, 1, 4),
    _MscFrMuxTimeFramerCongested_Type()
)
mscFrMuxTimeFramerCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrMuxTimeFramerCongested.setStatus("mandatory")
_FrameRelayMuxMIB_ObjectIdentity = ObjectIdentity
frameRelayMuxMIB = _FrameRelayMuxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38)
)
_FrameRelayMuxGroup_ObjectIdentity = ObjectIdentity
frameRelayMuxGroup = _FrameRelayMuxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 1)
)
_FrameRelayMuxGroupCA_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupCA = _FrameRelayMuxGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 1, 1)
)
_FrameRelayMuxGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupCA02 = _FrameRelayMuxGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 1, 1, 3)
)
_FrameRelayMuxGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupCA02A = _FrameRelayMuxGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 1, 1, 3, 2)
)
_FrameRelayMuxCapabilities_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilities = _FrameRelayMuxCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 3)
)
_FrameRelayMuxCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesCA = _FrameRelayMuxCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 3, 1)
)
_FrameRelayMuxCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesCA02 = _FrameRelayMuxCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 3, 1, 3)
)
_FrameRelayMuxCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesCA02A = _FrameRelayMuxCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 38, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayMuxMIB",
    **{"mscFrMux": mscFrMux,
       "mscFrMuxRowStatusTable": mscFrMuxRowStatusTable,
       "mscFrMuxRowStatusEntry": mscFrMuxRowStatusEntry,
       "mscFrMuxRowStatus": mscFrMuxRowStatus,
       "mscFrMuxComponentName": mscFrMuxComponentName,
       "mscFrMuxStorageType": mscFrMuxStorageType,
       "mscFrMuxIndex": mscFrMuxIndex,
       "mscFrMuxFramer": mscFrMuxFramer,
       "mscFrMuxFramerRowStatusTable": mscFrMuxFramerRowStatusTable,
       "mscFrMuxFramerRowStatusEntry": mscFrMuxFramerRowStatusEntry,
       "mscFrMuxFramerRowStatus": mscFrMuxFramerRowStatus,
       "mscFrMuxFramerComponentName": mscFrMuxFramerComponentName,
       "mscFrMuxFramerStorageType": mscFrMuxFramerStorageType,
       "mscFrMuxFramerIndex": mscFrMuxFramerIndex,
       "mscFrMuxFramerProvTable": mscFrMuxFramerProvTable,
       "mscFrMuxFramerProvEntry": mscFrMuxFramerProvEntry,
       "mscFrMuxFramerInterfaceName": mscFrMuxFramerInterfaceName,
       "mscFrMuxFramerLinkTable": mscFrMuxFramerLinkTable,
       "mscFrMuxFramerLinkEntry": mscFrMuxFramerLinkEntry,
       "mscFrMuxFramerDataInversion": mscFrMuxFramerDataInversion,
       "mscFrMuxFramerFrameCrcType": mscFrMuxFramerFrameCrcType,
       "mscFrMuxFramerFlagsBetweenFrames": mscFrMuxFramerFlagsBetweenFrames,
       "mscFrMuxFramerStateTable": mscFrMuxFramerStateTable,
       "mscFrMuxFramerStateEntry": mscFrMuxFramerStateEntry,
       "mscFrMuxFramerAdminState": mscFrMuxFramerAdminState,
       "mscFrMuxFramerOperationalState": mscFrMuxFramerOperationalState,
       "mscFrMuxFramerUsageState": mscFrMuxFramerUsageState,
       "mscFrMuxFramerStatsTable": mscFrMuxFramerStatsTable,
       "mscFrMuxFramerStatsEntry": mscFrMuxFramerStatsEntry,
       "mscFrMuxFramerFrmToIf": mscFrMuxFramerFrmToIf,
       "mscFrMuxFramerFrmFromIf": mscFrMuxFramerFrmFromIf,
       "mscFrMuxFramerOctetFromIf": mscFrMuxFramerOctetFromIf,
       "mscFrMuxFramerAborts": mscFrMuxFramerAborts,
       "mscFrMuxFramerCrcErrors": mscFrMuxFramerCrcErrors,
       "mscFrMuxFramerLrcErrors": mscFrMuxFramerLrcErrors,
       "mscFrMuxFramerNonOctetErrors": mscFrMuxFramerNonOctetErrors,
       "mscFrMuxFramerOverruns": mscFrMuxFramerOverruns,
       "mscFrMuxFramerUnderruns": mscFrMuxFramerUnderruns,
       "mscFrMuxFramerLargeFrmErrors": mscFrMuxFramerLargeFrmErrors,
       "mscFrMuxFramerFrmModeErrors": mscFrMuxFramerFrmModeErrors,
       "mscFrMuxFramerFrmToIf64": mscFrMuxFramerFrmToIf64,
       "mscFrMuxFramerFrmFromIf64": mscFrMuxFramerFrmFromIf64,
       "mscFrMuxFramerOctetFromIf64": mscFrMuxFramerOctetFromIf64,
       "mscFrMuxFramerUtilTable": mscFrMuxFramerUtilTable,
       "mscFrMuxFramerUtilEntry": mscFrMuxFramerUtilEntry,
       "mscFrMuxFramerNormPrioLinkUtilToIf": mscFrMuxFramerNormPrioLinkUtilToIf,
       "mscFrMuxFramerNormPrioLinkUtilFromIf": mscFrMuxFramerNormPrioLinkUtilFromIf,
       "mscFrMuxLmi": mscFrMuxLmi,
       "mscFrMuxLmiRowStatusTable": mscFrMuxLmiRowStatusTable,
       "mscFrMuxLmiRowStatusEntry": mscFrMuxLmiRowStatusEntry,
       "mscFrMuxLmiRowStatus": mscFrMuxLmiRowStatus,
       "mscFrMuxLmiComponentName": mscFrMuxLmiComponentName,
       "mscFrMuxLmiStorageType": mscFrMuxLmiStorageType,
       "mscFrMuxLmiIndex": mscFrMuxLmiIndex,
       "mscFrMuxLmiProvTable": mscFrMuxLmiProvTable,
       "mscFrMuxLmiProvEntry": mscFrMuxLmiProvEntry,
       "mscFrMuxLmiProcedures": mscFrMuxLmiProcedures,
       "mscFrMuxLmiLinkVerificationTimer": mscFrMuxLmiLinkVerificationTimer,
       "mscFrMuxLmiFullStatusPollingCycles": mscFrMuxLmiFullStatusPollingCycles,
       "mscFrMuxLmiErrorEventThreshold": mscFrMuxLmiErrorEventThreshold,
       "mscFrMuxLmiEventCount": mscFrMuxLmiEventCount,
       "mscFrMuxLmiStateTable": mscFrMuxLmiStateTable,
       "mscFrMuxLmiStateEntry": mscFrMuxLmiStateEntry,
       "mscFrMuxLmiAdminState": mscFrMuxLmiAdminState,
       "mscFrMuxLmiOperationalState": mscFrMuxLmiOperationalState,
       "mscFrMuxLmiUsageState": mscFrMuxLmiUsageState,
       "mscFrMuxLmiPsiTable": mscFrMuxLmiPsiTable,
       "mscFrMuxLmiPsiEntry": mscFrMuxLmiPsiEntry,
       "mscFrMuxLmiProtocolStatus": mscFrMuxLmiProtocolStatus,
       "mscFrMuxLmiStatsTable": mscFrMuxLmiStatsTable,
       "mscFrMuxLmiStatsEntry": mscFrMuxLmiStatsEntry,
       "mscFrMuxLmiKeepAliveStatusEnqToIf": mscFrMuxLmiKeepAliveStatusEnqToIf,
       "mscFrMuxLmiFullStatusEnqToIf": mscFrMuxLmiFullStatusEnqToIf,
       "mscFrMuxLmiProtocolErrors": mscFrMuxLmiProtocolErrors,
       "mscFrMuxLmiUnexpectedIes": mscFrMuxLmiUnexpectedIes,
       "mscFrMuxLmiSequenceErrors": mscFrMuxLmiSequenceErrors,
       "mscFrMuxLmiUnexpectedReports": mscFrMuxLmiUnexpectedReports,
       "mscFrMuxLmiNoStatusReportCount": mscFrMuxLmiNoStatusReportCount,
       "mscFrMuxDlci": mscFrMuxDlci,
       "mscFrMuxDlciRowStatusTable": mscFrMuxDlciRowStatusTable,
       "mscFrMuxDlciRowStatusEntry": mscFrMuxDlciRowStatusEntry,
       "mscFrMuxDlciRowStatus": mscFrMuxDlciRowStatus,
       "mscFrMuxDlciComponentName": mscFrMuxDlciComponentName,
       "mscFrMuxDlciStorageType": mscFrMuxDlciStorageType,
       "mscFrMuxDlciIndex": mscFrMuxDlciIndex,
       "mscFrMuxDlciApplInfo": mscFrMuxDlciApplInfo,
       "mscFrMuxDlciApplInfoRowStatusTable": mscFrMuxDlciApplInfoRowStatusTable,
       "mscFrMuxDlciApplInfoRowStatusEntry": mscFrMuxDlciApplInfoRowStatusEntry,
       "mscFrMuxDlciApplInfoRowStatus": mscFrMuxDlciApplInfoRowStatus,
       "mscFrMuxDlciApplInfoComponentName": mscFrMuxDlciApplInfoComponentName,
       "mscFrMuxDlciApplInfoStorageType": mscFrMuxDlciApplInfoStorageType,
       "mscFrMuxDlciApplInfoIndex": mscFrMuxDlciApplInfoIndex,
       "mscFrMuxDlciApplInfoProvTable": mscFrMuxDlciApplInfoProvTable,
       "mscFrMuxDlciApplInfoProvEntry": mscFrMuxDlciApplInfoProvEntry,
       "mscFrMuxDlciApplInfoApplicationName": mscFrMuxDlciApplInfoApplicationName,
       "mscFrMuxDlciOperTable": mscFrMuxDlciOperTable,
       "mscFrMuxDlciOperEntry": mscFrMuxDlciOperEntry,
       "mscFrMuxDlciApplicationName": mscFrMuxDlciApplicationName,
       "mscFrMuxDlciStateTable": mscFrMuxDlciStateTable,
       "mscFrMuxDlciStateEntry": mscFrMuxDlciStateEntry,
       "mscFrMuxDlciAdminState": mscFrMuxDlciAdminState,
       "mscFrMuxDlciOperationalState": mscFrMuxDlciOperationalState,
       "mscFrMuxDlciUsageState": mscFrMuxDlciUsageState,
       "mscFrMuxDlciAbitTable": mscFrMuxDlciAbitTable,
       "mscFrMuxDlciAbitEntry": mscFrMuxDlciAbitEntry,
       "mscFrMuxDlciABitStatusFromIf": mscFrMuxDlciABitStatusFromIf,
       "mscFrMuxDlciStatsTable": mscFrMuxDlciStatsTable,
       "mscFrMuxDlciStatsEntry": mscFrMuxDlciStatsEntry,
       "mscFrMuxDlciFrmToIf": mscFrMuxDlciFrmToIf,
       "mscFrMuxDlciBytesToIf": mscFrMuxDlciBytesToIf,
       "mscFrMuxDlciFrmFromIf": mscFrMuxDlciFrmFromIf,
       "mscFrMuxDlciDeFrmFromIf": mscFrMuxDlciDeFrmFromIf,
       "mscFrMuxDlciBytesFromIf": mscFrMuxDlciBytesFromIf,
       "mscFrMuxDlciDeBytesFromIf": mscFrMuxDlciDeBytesFromIf,
       "mscFrMuxDlciFecnFrmToIf": mscFrMuxDlciFecnFrmToIf,
       "mscFrMuxDlciFecnFrmFromIf": mscFrMuxDlciFecnFrmFromIf,
       "mscFrMuxDlciBecnFrmToIf": mscFrMuxDlciBecnFrmToIf,
       "mscFrMuxDlciBecnFrmFromIf": mscFrMuxDlciBecnFrmFromIf,
       "mscFrMuxDlciDiscCongestedFromIf": mscFrMuxDlciDiscCongestedFromIf,
       "mscFrMuxDlciDiscCongestedFromIfBytes": mscFrMuxDlciDiscCongestedFromIfBytes,
       "mscFrMuxDlciDiscDeCongestedFromIf": mscFrMuxDlciDiscDeCongestedFromIf,
       "mscFrMuxDlciDiscDeCongestedFromIfBytes": mscFrMuxDlciDiscDeCongestedFromIfBytes,
       "mscFrMuxDlciErrorShortFrmFromIf": mscFrMuxDlciErrorShortFrmFromIf,
       "mscFrMuxDlciErrorLongFrmFromIf": mscFrMuxDlciErrorLongFrmFromIf,
       "mscFrMuxOperStatusTable": mscFrMuxOperStatusTable,
       "mscFrMuxOperStatusEntry": mscFrMuxOperStatusEntry,
       "mscFrMuxSnmpOperStatus": mscFrMuxSnmpOperStatus,
       "mscFrMuxIfEntryTable": mscFrMuxIfEntryTable,
       "mscFrMuxIfEntryEntry": mscFrMuxIfEntryEntry,
       "mscFrMuxIfAdminStatus": mscFrMuxIfAdminStatus,
       "mscFrMuxIfIndex": mscFrMuxIfIndex,
       "mscFrMuxCidDataTable": mscFrMuxCidDataTable,
       "mscFrMuxCidDataEntry": mscFrMuxCidDataEntry,
       "mscFrMuxCustomerIdentifier": mscFrMuxCustomerIdentifier,
       "mscFrMuxStateTable": mscFrMuxStateTable,
       "mscFrMuxStateEntry": mscFrMuxStateEntry,
       "mscFrMuxAdminState": mscFrMuxAdminState,
       "mscFrMuxOperationalState": mscFrMuxOperationalState,
       "mscFrMuxUsageState": mscFrMuxUsageState,
       "mscFrMuxAvailabilityStatus": mscFrMuxAvailabilityStatus,
       "mscFrMuxProceduralStatus": mscFrMuxProceduralStatus,
       "mscFrMuxControlStatus": mscFrMuxControlStatus,
       "mscFrMuxAlarmStatus": mscFrMuxAlarmStatus,
       "mscFrMuxStandbyStatus": mscFrMuxStandbyStatus,
       "mscFrMuxUnknownStatus": mscFrMuxUnknownStatus,
       "mscFrMuxStatsTable": mscFrMuxStatsTable,
       "mscFrMuxStatsEntry": mscFrMuxStatsEntry,
       "mscFrMuxLastUnknownDlci": mscFrMuxLastUnknownDlci,
       "mscFrMuxUnknownDlciFramesFromIf": mscFrMuxUnknownDlciFramesFromIf,
       "mscFrMuxInvalidHeaderFramesFromIf": mscFrMuxInvalidHeaderFramesFromIf,
       "mscFrMuxTimeFramerCongested": mscFrMuxTimeFramerCongested,
       "frameRelayMuxMIB": frameRelayMuxMIB,
       "frameRelayMuxGroup": frameRelayMuxGroup,
       "frameRelayMuxGroupCA": frameRelayMuxGroupCA,
       "frameRelayMuxGroupCA02": frameRelayMuxGroupCA02,
       "frameRelayMuxGroupCA02A": frameRelayMuxGroupCA02A,
       "frameRelayMuxCapabilities": frameRelayMuxCapabilities,
       "frameRelayMuxCapabilitiesCA": frameRelayMuxCapabilitiesCA,
       "frameRelayMuxCapabilitiesCA02": frameRelayMuxCapabilitiesCA02,
       "frameRelayMuxCapabilitiesCA02A": frameRelayMuxCapabilitiesCA02A}
)
