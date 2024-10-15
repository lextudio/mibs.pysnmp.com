# SNMP MIB module (Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:12 2024
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

(mscDpnGate,
 mscDpnGateIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-DpnTrunksMIB",
    "mscDpnGate",
    "mscDpnGateIndex")

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

_MscDpnGateUtp_ObjectIdentity = ObjectIdentity
mscDpnGateUtp = _MscDpnGateUtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2)
)
_MscDpnGateUtpRowStatusTable_Object = MibTable
mscDpnGateUtpRowStatusTable = _MscDpnGateUtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpRowStatusTable.setStatus("mandatory")
_MscDpnGateUtpRowStatusEntry_Object = MibTableRow
mscDpnGateUtpRowStatusEntry = _MscDpnGateUtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1, 1)
)
mscDpnGateUtpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpRowStatusEntry.setStatus("mandatory")
_MscDpnGateUtpRowStatus_Type = RowStatus
_MscDpnGateUtpRowStatus_Object = MibTableColumn
mscDpnGateUtpRowStatus = _MscDpnGateUtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1, 1, 1),
    _MscDpnGateUtpRowStatus_Type()
)
mscDpnGateUtpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpRowStatus.setStatus("mandatory")
_MscDpnGateUtpComponentName_Type = DisplayString
_MscDpnGateUtpComponentName_Object = MibTableColumn
mscDpnGateUtpComponentName = _MscDpnGateUtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1, 1, 2),
    _MscDpnGateUtpComponentName_Type()
)
mscDpnGateUtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpComponentName.setStatus("mandatory")
_MscDpnGateUtpStorageType_Type = StorageType
_MscDpnGateUtpStorageType_Object = MibTableColumn
mscDpnGateUtpStorageType = _MscDpnGateUtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1, 1, 4),
    _MscDpnGateUtpStorageType_Type()
)
mscDpnGateUtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpStorageType.setStatus("mandatory")
_MscDpnGateUtpIndex_Type = NonReplicated
_MscDpnGateUtpIndex_Object = MibTableColumn
mscDpnGateUtpIndex = _MscDpnGateUtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 1, 1, 10),
    _MscDpnGateUtpIndex_Type()
)
mscDpnGateUtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateUtpIndex.setStatus("mandatory")
_MscDpnGateUtpFramer_ObjectIdentity = ObjectIdentity
mscDpnGateUtpFramer = _MscDpnGateUtpFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2)
)
_MscDpnGateUtpFramerRowStatusTable_Object = MibTable
mscDpnGateUtpFramerRowStatusTable = _MscDpnGateUtpFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerRowStatusTable.setStatus("mandatory")
_MscDpnGateUtpFramerRowStatusEntry_Object = MibTableRow
mscDpnGateUtpFramerRowStatusEntry = _MscDpnGateUtpFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1, 1)
)
mscDpnGateUtpFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerRowStatusEntry.setStatus("mandatory")
_MscDpnGateUtpFramerRowStatus_Type = RowStatus
_MscDpnGateUtpFramerRowStatus_Object = MibTableColumn
mscDpnGateUtpFramerRowStatus = _MscDpnGateUtpFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1, 1, 1),
    _MscDpnGateUtpFramerRowStatus_Type()
)
mscDpnGateUtpFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerRowStatus.setStatus("mandatory")
_MscDpnGateUtpFramerComponentName_Type = DisplayString
_MscDpnGateUtpFramerComponentName_Object = MibTableColumn
mscDpnGateUtpFramerComponentName = _MscDpnGateUtpFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1, 1, 2),
    _MscDpnGateUtpFramerComponentName_Type()
)
mscDpnGateUtpFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerComponentName.setStatus("mandatory")
_MscDpnGateUtpFramerStorageType_Type = StorageType
_MscDpnGateUtpFramerStorageType_Object = MibTableColumn
mscDpnGateUtpFramerStorageType = _MscDpnGateUtpFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1, 1, 4),
    _MscDpnGateUtpFramerStorageType_Type()
)
mscDpnGateUtpFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerStorageType.setStatus("mandatory")
_MscDpnGateUtpFramerIndex_Type = NonReplicated
_MscDpnGateUtpFramerIndex_Object = MibTableColumn
mscDpnGateUtpFramerIndex = _MscDpnGateUtpFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 1, 1, 10),
    _MscDpnGateUtpFramerIndex_Type()
)
mscDpnGateUtpFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerIndex.setStatus("mandatory")
_MscDpnGateUtpFramerProvTable_Object = MibTable
mscDpnGateUtpFramerProvTable = _MscDpnGateUtpFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerProvTable.setStatus("mandatory")
_MscDpnGateUtpFramerProvEntry_Object = MibTableRow
mscDpnGateUtpFramerProvEntry = _MscDpnGateUtpFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 10, 1)
)
mscDpnGateUtpFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerProvEntry.setStatus("mandatory")
_MscDpnGateUtpFramerInterfaceName_Type = Link
_MscDpnGateUtpFramerInterfaceName_Object = MibTableColumn
mscDpnGateUtpFramerInterfaceName = _MscDpnGateUtpFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 10, 1, 1),
    _MscDpnGateUtpFramerInterfaceName_Type()
)
mscDpnGateUtpFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerInterfaceName.setStatus("mandatory")
_MscDpnGateUtpFramerLinkTable_Object = MibTable
mscDpnGateUtpFramerLinkTable = _MscDpnGateUtpFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerLinkTable.setStatus("mandatory")
_MscDpnGateUtpFramerLinkEntry_Object = MibTableRow
mscDpnGateUtpFramerLinkEntry = _MscDpnGateUtpFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11, 1)
)
mscDpnGateUtpFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerLinkEntry.setStatus("mandatory")


class _MscDpnGateUtpFramerFramingType_Type(Integer32):
    """Custom type mscDpnGateUtpFramerFramingType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("hdlc", 0)
    )


_MscDpnGateUtpFramerFramingType_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerFramingType_Object = MibTableColumn
mscDpnGateUtpFramerFramingType = _MscDpnGateUtpFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11, 1, 1),
    _MscDpnGateUtpFramerFramingType_Type()
)
mscDpnGateUtpFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFramingType.setStatus("mandatory")


class _MscDpnGateUtpFramerDataInversion_Type(Integer32):
    """Custom type mscDpnGateUtpFramerDataInversion based on Integer32"""
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


_MscDpnGateUtpFramerDataInversion_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerDataInversion_Object = MibTableColumn
mscDpnGateUtpFramerDataInversion = _MscDpnGateUtpFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11, 1, 2),
    _MscDpnGateUtpFramerDataInversion_Type()
)
mscDpnGateUtpFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerDataInversion.setStatus("mandatory")


class _MscDpnGateUtpFramerFrameCrcType_Type(Integer32):
    """Custom type mscDpnGateUtpFramerFrameCrcType based on Integer32"""
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


_MscDpnGateUtpFramerFrameCrcType_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerFrameCrcType_Object = MibTableColumn
mscDpnGateUtpFramerFrameCrcType = _MscDpnGateUtpFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11, 1, 3),
    _MscDpnGateUtpFramerFrameCrcType_Type()
)
mscDpnGateUtpFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrameCrcType.setStatus("mandatory")


class _MscDpnGateUtpFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscDpnGateUtpFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscDpnGateUtpFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscDpnGateUtpFramerFlagsBetweenFrames_Object = MibTableColumn
mscDpnGateUtpFramerFlagsBetweenFrames = _MscDpnGateUtpFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 11, 1, 4),
    _MscDpnGateUtpFramerFlagsBetweenFrames_Type()
)
mscDpnGateUtpFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFlagsBetweenFrames.setStatus("mandatory")
_MscDpnGateUtpFramerStateTable_Object = MibTable
mscDpnGateUtpFramerStateTable = _MscDpnGateUtpFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerStateTable.setStatus("mandatory")
_MscDpnGateUtpFramerStateEntry_Object = MibTableRow
mscDpnGateUtpFramerStateEntry = _MscDpnGateUtpFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 12, 1)
)
mscDpnGateUtpFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerStateEntry.setStatus("mandatory")


class _MscDpnGateUtpFramerAdminState_Type(Integer32):
    """Custom type mscDpnGateUtpFramerAdminState based on Integer32"""
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


_MscDpnGateUtpFramerAdminState_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerAdminState_Object = MibTableColumn
mscDpnGateUtpFramerAdminState = _MscDpnGateUtpFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 12, 1, 1),
    _MscDpnGateUtpFramerAdminState_Type()
)
mscDpnGateUtpFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerAdminState.setStatus("mandatory")


class _MscDpnGateUtpFramerOperationalState_Type(Integer32):
    """Custom type mscDpnGateUtpFramerOperationalState based on Integer32"""
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


_MscDpnGateUtpFramerOperationalState_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerOperationalState_Object = MibTableColumn
mscDpnGateUtpFramerOperationalState = _MscDpnGateUtpFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 12, 1, 2),
    _MscDpnGateUtpFramerOperationalState_Type()
)
mscDpnGateUtpFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerOperationalState.setStatus("mandatory")


class _MscDpnGateUtpFramerUsageState_Type(Integer32):
    """Custom type mscDpnGateUtpFramerUsageState based on Integer32"""
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


_MscDpnGateUtpFramerUsageState_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerUsageState_Object = MibTableColumn
mscDpnGateUtpFramerUsageState = _MscDpnGateUtpFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 12, 1, 3),
    _MscDpnGateUtpFramerUsageState_Type()
)
mscDpnGateUtpFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUsageState.setStatus("mandatory")
_MscDpnGateUtpFramerStatsTable_Object = MibTable
mscDpnGateUtpFramerStatsTable = _MscDpnGateUtpFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerStatsTable.setStatus("mandatory")
_MscDpnGateUtpFramerStatsEntry_Object = MibTableRow
mscDpnGateUtpFramerStatsEntry = _MscDpnGateUtpFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1)
)
mscDpnGateUtpFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerStatsEntry.setStatus("mandatory")
_MscDpnGateUtpFramerFrmToIf_Type = Counter32
_MscDpnGateUtpFramerFrmToIf_Object = MibTableColumn
mscDpnGateUtpFramerFrmToIf = _MscDpnGateUtpFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 1),
    _MscDpnGateUtpFramerFrmToIf_Type()
)
mscDpnGateUtpFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrmToIf.setStatus("obsolete")
_MscDpnGateUtpFramerFrmFromIf_Type = Counter32
_MscDpnGateUtpFramerFrmFromIf_Object = MibTableColumn
mscDpnGateUtpFramerFrmFromIf = _MscDpnGateUtpFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 2),
    _MscDpnGateUtpFramerFrmFromIf_Type()
)
mscDpnGateUtpFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrmFromIf.setStatus("obsolete")
_MscDpnGateUtpFramerOctetFromIf_Type = Counter32
_MscDpnGateUtpFramerOctetFromIf_Object = MibTableColumn
mscDpnGateUtpFramerOctetFromIf = _MscDpnGateUtpFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 3),
    _MscDpnGateUtpFramerOctetFromIf_Type()
)
mscDpnGateUtpFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerOctetFromIf.setStatus("obsolete")
_MscDpnGateUtpFramerAborts_Type = Counter32
_MscDpnGateUtpFramerAborts_Object = MibTableColumn
mscDpnGateUtpFramerAborts = _MscDpnGateUtpFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 4),
    _MscDpnGateUtpFramerAborts_Type()
)
mscDpnGateUtpFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerAborts.setStatus("mandatory")
_MscDpnGateUtpFramerCrcErrors_Type = Counter32
_MscDpnGateUtpFramerCrcErrors_Object = MibTableColumn
mscDpnGateUtpFramerCrcErrors = _MscDpnGateUtpFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 5),
    _MscDpnGateUtpFramerCrcErrors_Type()
)
mscDpnGateUtpFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerCrcErrors.setStatus("mandatory")
_MscDpnGateUtpFramerLrcErrors_Type = Counter32
_MscDpnGateUtpFramerLrcErrors_Object = MibTableColumn
mscDpnGateUtpFramerLrcErrors = _MscDpnGateUtpFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 6),
    _MscDpnGateUtpFramerLrcErrors_Type()
)
mscDpnGateUtpFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerLrcErrors.setStatus("mandatory")
_MscDpnGateUtpFramerNonOctetErrors_Type = Counter32
_MscDpnGateUtpFramerNonOctetErrors_Object = MibTableColumn
mscDpnGateUtpFramerNonOctetErrors = _MscDpnGateUtpFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 7),
    _MscDpnGateUtpFramerNonOctetErrors_Type()
)
mscDpnGateUtpFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerNonOctetErrors.setStatus("mandatory")
_MscDpnGateUtpFramerOverruns_Type = Counter32
_MscDpnGateUtpFramerOverruns_Object = MibTableColumn
mscDpnGateUtpFramerOverruns = _MscDpnGateUtpFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 8),
    _MscDpnGateUtpFramerOverruns_Type()
)
mscDpnGateUtpFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerOverruns.setStatus("mandatory")
_MscDpnGateUtpFramerUnderruns_Type = Counter32
_MscDpnGateUtpFramerUnderruns_Object = MibTableColumn
mscDpnGateUtpFramerUnderruns = _MscDpnGateUtpFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 9),
    _MscDpnGateUtpFramerUnderruns_Type()
)
mscDpnGateUtpFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUnderruns.setStatus("mandatory")
_MscDpnGateUtpFramerLargeFrmErrors_Type = Counter32
_MscDpnGateUtpFramerLargeFrmErrors_Object = MibTableColumn
mscDpnGateUtpFramerLargeFrmErrors = _MscDpnGateUtpFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 10),
    _MscDpnGateUtpFramerLargeFrmErrors_Type()
)
mscDpnGateUtpFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerLargeFrmErrors.setStatus("mandatory")
_MscDpnGateUtpFramerFrmModeErrors_Type = Counter32
_MscDpnGateUtpFramerFrmModeErrors_Object = MibTableColumn
mscDpnGateUtpFramerFrmModeErrors = _MscDpnGateUtpFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 11),
    _MscDpnGateUtpFramerFrmModeErrors_Type()
)
mscDpnGateUtpFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrmModeErrors.setStatus("mandatory")
_MscDpnGateUtpFramerOutOfSequenceFrm_Type = Counter32
_MscDpnGateUtpFramerOutOfSequenceFrm_Object = MibTableColumn
mscDpnGateUtpFramerOutOfSequenceFrm = _MscDpnGateUtpFramerOutOfSequenceFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 12),
    _MscDpnGateUtpFramerOutOfSequenceFrm_Type()
)
mscDpnGateUtpFramerOutOfSequenceFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerOutOfSequenceFrm.setStatus("mandatory")
_MscDpnGateUtpFramerRepeatedFrm_Type = Counter32
_MscDpnGateUtpFramerRepeatedFrm_Object = MibTableColumn
mscDpnGateUtpFramerRepeatedFrm = _MscDpnGateUtpFramerRepeatedFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 13),
    _MscDpnGateUtpFramerRepeatedFrm_Type()
)
mscDpnGateUtpFramerRepeatedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerRepeatedFrm.setStatus("mandatory")
_MscDpnGateUtpFramerFrmToIf64_Type = PassportCounter64
_MscDpnGateUtpFramerFrmToIf64_Object = MibTableColumn
mscDpnGateUtpFramerFrmToIf64 = _MscDpnGateUtpFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 14),
    _MscDpnGateUtpFramerFrmToIf64_Type()
)
mscDpnGateUtpFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrmToIf64.setStatus("mandatory")
_MscDpnGateUtpFramerFrmFromIf64_Type = PassportCounter64
_MscDpnGateUtpFramerFrmFromIf64_Object = MibTableColumn
mscDpnGateUtpFramerFrmFromIf64 = _MscDpnGateUtpFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 15),
    _MscDpnGateUtpFramerFrmFromIf64_Type()
)
mscDpnGateUtpFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerFrmFromIf64.setStatus("mandatory")
_MscDpnGateUtpFramerOctetFromIf64_Type = PassportCounter64
_MscDpnGateUtpFramerOctetFromIf64_Object = MibTableColumn
mscDpnGateUtpFramerOctetFromIf64 = _MscDpnGateUtpFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 13, 1, 16),
    _MscDpnGateUtpFramerOctetFromIf64_Type()
)
mscDpnGateUtpFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerOctetFromIf64.setStatus("mandatory")
_MscDpnGateUtpFramerUtilTable_Object = MibTable
mscDpnGateUtpFramerUtilTable = _MscDpnGateUtpFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUtilTable.setStatus("mandatory")
_MscDpnGateUtpFramerUtilEntry_Object = MibTableRow
mscDpnGateUtpFramerUtilEntry = _MscDpnGateUtpFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14, 1)
)
mscDpnGateUtpFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUtilEntry.setStatus("mandatory")


class _MscDpnGateUtpFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscDpnGateUtpFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscDpnGateUtpFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscDpnGateUtpFramerNormPrioLinkUtilToIf = _MscDpnGateUtpFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14, 1, 1),
    _MscDpnGateUtpFramerNormPrioLinkUtilToIf_Type()
)
mscDpnGateUtpFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscDpnGateUtpFramerHighPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscDpnGateUtpFramerHighPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerHighPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscDpnGateUtpFramerHighPrioLinkUtilToIf_Object = MibTableColumn
mscDpnGateUtpFramerHighPrioLinkUtilToIf = _MscDpnGateUtpFramerHighPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14, 1, 2),
    _MscDpnGateUtpFramerHighPrioLinkUtilToIf_Type()
)
mscDpnGateUtpFramerHighPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerHighPrioLinkUtilToIf.setStatus("mandatory")


class _MscDpnGateUtpFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscDpnGateUtpFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscDpnGateUtpFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscDpnGateUtpFramerNormPrioLinkUtilFromIf = _MscDpnGateUtpFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14, 1, 3),
    _MscDpnGateUtpFramerNormPrioLinkUtilFromIf_Type()
)
mscDpnGateUtpFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerNormPrioLinkUtilFromIf.setStatus("mandatory")


class _MscDpnGateUtpFramerHighPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscDpnGateUtpFramerHighPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerHighPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscDpnGateUtpFramerHighPrioLinkUtilFromIf_Object = MibTableColumn
mscDpnGateUtpFramerHighPrioLinkUtilFromIf = _MscDpnGateUtpFramerHighPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 14, 1, 4),
    _MscDpnGateUtpFramerHighPrioLinkUtilFromIf_Type()
)
mscDpnGateUtpFramerHighPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerHighPrioLinkUtilFromIf.setStatus("mandatory")
_MscDpnGateUtpFramerUtilThresholdTable_Object = MibTable
mscDpnGateUtpFramerUtilThresholdTable = _MscDpnGateUtpFramerUtilThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUtilThresholdTable.setStatus("mandatory")
_MscDpnGateUtpFramerUtilThresholdEntry_Object = MibTableRow
mscDpnGateUtpFramerUtilThresholdEntry = _MscDpnGateUtpFramerUtilThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15, 1)
)
mscDpnGateUtpFramerUtilThresholdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerUtilThresholdEntry.setStatus("mandatory")


class _MscDpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDpnGateUtpFramerMinorLinkUtilAlarmThreshold_Object = MibTableColumn
mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold = _MscDpnGateUtpFramerMinorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15, 1, 1),
    _MscDpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type()
)
mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscDpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDpnGateUtpFramerMajorLinkUtilAlarmThreshold_Object = MibTableColumn
mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold = _MscDpnGateUtpFramerMajorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15, 1, 2),
    _MscDpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type()
)
mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_MscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Object = MibTableColumn
mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold = _MscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15, 1, 3),
    _MscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type()
)
mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold.setStatus("mandatory")


class _MscDpnGateUtpFramerLinkUtilAlarmStatus_Type(Integer32):
    """Custom type mscDpnGateUtpFramerLinkUtilAlarmStatus based on Integer32"""
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


_MscDpnGateUtpFramerLinkUtilAlarmStatus_Type.__name__ = "Integer32"
_MscDpnGateUtpFramerLinkUtilAlarmStatus_Object = MibTableColumn
mscDpnGateUtpFramerLinkUtilAlarmStatus = _MscDpnGateUtpFramerLinkUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 2, 15, 1, 4),
    _MscDpnGateUtpFramerLinkUtilAlarmStatus_Type()
)
mscDpnGateUtpFramerLinkUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpFramerLinkUtilAlarmStatus.setStatus("mandatory")
_MscDpnGateUtpProvTable_Object = MibTable
mscDpnGateUtpProvTable = _MscDpnGateUtpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpProvTable.setStatus("mandatory")
_MscDpnGateUtpProvEntry_Object = MibTableRow
mscDpnGateUtpProvEntry = _MscDpnGateUtpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 10, 1)
)
mscDpnGateUtpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpProvEntry.setStatus("mandatory")


class _MscDpnGateUtpMaximumErroredInterval_Type(Unsigned32):
    """Custom type mscDpnGateUtpMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_MscDpnGateUtpMaximumErroredInterval_Type.__name__ = "Unsigned32"
_MscDpnGateUtpMaximumErroredInterval_Object = MibTableColumn
mscDpnGateUtpMaximumErroredInterval = _MscDpnGateUtpMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 10, 1, 1),
    _MscDpnGateUtpMaximumErroredInterval_Type()
)
mscDpnGateUtpMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpMaximumErroredInterval.setStatus("mandatory")


class _MscDpnGateUtpReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type mscDpnGateUtpReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_MscDpnGateUtpReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_MscDpnGateUtpReceiveErrorSensitivity_Object = MibTableColumn
mscDpnGateUtpReceiveErrorSensitivity = _MscDpnGateUtpReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 10, 1, 2),
    _MscDpnGateUtpReceiveErrorSensitivity_Type()
)
mscDpnGateUtpReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateUtpReceiveErrorSensitivity.setStatus("mandatory")
_MscDpnGateUtpStateTable_Object = MibTable
mscDpnGateUtpStateTable = _MscDpnGateUtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpStateTable.setStatus("mandatory")
_MscDpnGateUtpStateEntry_Object = MibTableRow
mscDpnGateUtpStateEntry = _MscDpnGateUtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1)
)
mscDpnGateUtpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpStateEntry.setStatus("mandatory")


class _MscDpnGateUtpAdminState_Type(Integer32):
    """Custom type mscDpnGateUtpAdminState based on Integer32"""
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


_MscDpnGateUtpAdminState_Type.__name__ = "Integer32"
_MscDpnGateUtpAdminState_Object = MibTableColumn
mscDpnGateUtpAdminState = _MscDpnGateUtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 1),
    _MscDpnGateUtpAdminState_Type()
)
mscDpnGateUtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpAdminState.setStatus("mandatory")


class _MscDpnGateUtpOperationalState_Type(Integer32):
    """Custom type mscDpnGateUtpOperationalState based on Integer32"""
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


_MscDpnGateUtpOperationalState_Type.__name__ = "Integer32"
_MscDpnGateUtpOperationalState_Object = MibTableColumn
mscDpnGateUtpOperationalState = _MscDpnGateUtpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 2),
    _MscDpnGateUtpOperationalState_Type()
)
mscDpnGateUtpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpOperationalState.setStatus("mandatory")


class _MscDpnGateUtpUsageState_Type(Integer32):
    """Custom type mscDpnGateUtpUsageState based on Integer32"""
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


_MscDpnGateUtpUsageState_Type.__name__ = "Integer32"
_MscDpnGateUtpUsageState_Object = MibTableColumn
mscDpnGateUtpUsageState = _MscDpnGateUtpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 3),
    _MscDpnGateUtpUsageState_Type()
)
mscDpnGateUtpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpUsageState.setStatus("mandatory")


class _MscDpnGateUtpAvailabilityStatus_Type(OctetString):
    """Custom type mscDpnGateUtpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscDpnGateUtpAvailabilityStatus_Type.__name__ = "OctetString"
_MscDpnGateUtpAvailabilityStatus_Object = MibTableColumn
mscDpnGateUtpAvailabilityStatus = _MscDpnGateUtpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 4),
    _MscDpnGateUtpAvailabilityStatus_Type()
)
mscDpnGateUtpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpAvailabilityStatus.setStatus("mandatory")


class _MscDpnGateUtpProceduralStatus_Type(OctetString):
    """Custom type mscDpnGateUtpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateUtpProceduralStatus_Type.__name__ = "OctetString"
_MscDpnGateUtpProceduralStatus_Object = MibTableColumn
mscDpnGateUtpProceduralStatus = _MscDpnGateUtpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 5),
    _MscDpnGateUtpProceduralStatus_Type()
)
mscDpnGateUtpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpProceduralStatus.setStatus("mandatory")


class _MscDpnGateUtpControlStatus_Type(OctetString):
    """Custom type mscDpnGateUtpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateUtpControlStatus_Type.__name__ = "OctetString"
_MscDpnGateUtpControlStatus_Object = MibTableColumn
mscDpnGateUtpControlStatus = _MscDpnGateUtpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 6),
    _MscDpnGateUtpControlStatus_Type()
)
mscDpnGateUtpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpControlStatus.setStatus("mandatory")


class _MscDpnGateUtpAlarmStatus_Type(OctetString):
    """Custom type mscDpnGateUtpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateUtpAlarmStatus_Type.__name__ = "OctetString"
_MscDpnGateUtpAlarmStatus_Object = MibTableColumn
mscDpnGateUtpAlarmStatus = _MscDpnGateUtpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 7),
    _MscDpnGateUtpAlarmStatus_Type()
)
mscDpnGateUtpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpAlarmStatus.setStatus("mandatory")


class _MscDpnGateUtpStandbyStatus_Type(Integer32):
    """Custom type mscDpnGateUtpStandbyStatus based on Integer32"""
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


_MscDpnGateUtpStandbyStatus_Type.__name__ = "Integer32"
_MscDpnGateUtpStandbyStatus_Object = MibTableColumn
mscDpnGateUtpStandbyStatus = _MscDpnGateUtpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 8),
    _MscDpnGateUtpStandbyStatus_Type()
)
mscDpnGateUtpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpStandbyStatus.setStatus("mandatory")


class _MscDpnGateUtpUnknownStatus_Type(Integer32):
    """Custom type mscDpnGateUtpUnknownStatus based on Integer32"""
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


_MscDpnGateUtpUnknownStatus_Type.__name__ = "Integer32"
_MscDpnGateUtpUnknownStatus_Object = MibTableColumn
mscDpnGateUtpUnknownStatus = _MscDpnGateUtpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 11, 1, 9),
    _MscDpnGateUtpUnknownStatus_Type()
)
mscDpnGateUtpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpUnknownStatus.setStatus("mandatory")
_MscDpnGateUtpOpTable_Object = MibTable
mscDpnGateUtpOpTable = _MscDpnGateUtpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 12)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpOpTable.setStatus("mandatory")
_MscDpnGateUtpOpEntry_Object = MibTableRow
mscDpnGateUtpOpEntry = _MscDpnGateUtpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 12, 1)
)
mscDpnGateUtpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpOpEntry.setStatus("mandatory")


class _MscDpnGateUtpRoundTripDelay_Type(Gauge32):
    """Custom type mscDpnGateUtpRoundTripDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscDpnGateUtpRoundTripDelay_Type.__name__ = "Gauge32"
_MscDpnGateUtpRoundTripDelay_Object = MibTableColumn
mscDpnGateUtpRoundTripDelay = _MscDpnGateUtpRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 12, 1, 1),
    _MscDpnGateUtpRoundTripDelay_Type()
)
mscDpnGateUtpRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpRoundTripDelay.setStatus("mandatory")
_MscDpnGateUtpStatsTable_Object = MibTable
mscDpnGateUtpStatsTable = _MscDpnGateUtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13)
)
if mibBuilder.loadTexts:
    mscDpnGateUtpStatsTable.setStatus("mandatory")
_MscDpnGateUtpStatsEntry_Object = MibTableRow
mscDpnGateUtpStatsEntry = _MscDpnGateUtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1)
)
mscDpnGateUtpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB", "mscDpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateUtpStatsEntry.setStatus("mandatory")
_MscDpnGateUtpDiscardBadFromIf_Type = Counter32
_MscDpnGateUtpDiscardBadFromIf_Object = MibTableColumn
mscDpnGateUtpDiscardBadFromIf = _MscDpnGateUtpDiscardBadFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1, 1),
    _MscDpnGateUtpDiscardBadFromIf_Type()
)
mscDpnGateUtpDiscardBadFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpDiscardBadFromIf.setStatus("mandatory")
_MscDpnGateUtpDiscardExcessToIf_Type = Counter32
_MscDpnGateUtpDiscardExcessToIf_Object = MibTableColumn
mscDpnGateUtpDiscardExcessToIf = _MscDpnGateUtpDiscardExcessToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1, 2),
    _MscDpnGateUtpDiscardExcessToIf_Type()
)
mscDpnGateUtpDiscardExcessToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpDiscardExcessToIf.setStatus("mandatory")
_MscDpnGateUtpFrmRexmtToIf_Type = Counter32
_MscDpnGateUtpFrmRexmtToIf_Object = MibTableColumn
mscDpnGateUtpFrmRexmtToIf = _MscDpnGateUtpFrmRexmtToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1, 3),
    _MscDpnGateUtpFrmRexmtToIf_Type()
)
mscDpnGateUtpFrmRexmtToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpFrmRexmtToIf.setStatus("mandatory")
_MscDpnGateUtpAreYouThereModeEntries_Type = Counter32
_MscDpnGateUtpAreYouThereModeEntries_Object = MibTableColumn
mscDpnGateUtpAreYouThereModeEntries = _MscDpnGateUtpAreYouThereModeEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1, 4),
    _MscDpnGateUtpAreYouThereModeEntries_Type()
)
mscDpnGateUtpAreYouThereModeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpAreYouThereModeEntries.setStatus("mandatory")
_MscDpnGateUtpWindowClosures_Type = Counter32
_MscDpnGateUtpWindowClosures_Object = MibTableColumn
mscDpnGateUtpWindowClosures = _MscDpnGateUtpWindowClosures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 2, 13, 1, 5),
    _MscDpnGateUtpWindowClosures_Type()
)
mscDpnGateUtpWindowClosures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateUtpWindowClosures.setStatus("mandatory")
_UtpDpnTrunksMIB_ObjectIdentity = ObjectIdentity
utpDpnTrunksMIB = _UtpDpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67)
)
_UtpDpnTrunksGroup_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroup = _UtpDpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 1)
)
_UtpDpnTrunksGroupCA_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupCA = _UtpDpnTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 1, 1)
)
_UtpDpnTrunksGroupCA02_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupCA02 = _UtpDpnTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 1, 1, 3)
)
_UtpDpnTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupCA02A = _UtpDpnTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 1, 1, 3, 2)
)
_UtpDpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilities = _UtpDpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 3)
)
_UtpDpnTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesCA = _UtpDpnTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 3, 1)
)
_UtpDpnTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesCA02 = _UtpDpnTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 3, 1, 3)
)
_UtpDpnTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesCA02A = _UtpDpnTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 67, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-UtpDpnTrunksMIB",
    **{"mscDpnGateUtp": mscDpnGateUtp,
       "mscDpnGateUtpRowStatusTable": mscDpnGateUtpRowStatusTable,
       "mscDpnGateUtpRowStatusEntry": mscDpnGateUtpRowStatusEntry,
       "mscDpnGateUtpRowStatus": mscDpnGateUtpRowStatus,
       "mscDpnGateUtpComponentName": mscDpnGateUtpComponentName,
       "mscDpnGateUtpStorageType": mscDpnGateUtpStorageType,
       "mscDpnGateUtpIndex": mscDpnGateUtpIndex,
       "mscDpnGateUtpFramer": mscDpnGateUtpFramer,
       "mscDpnGateUtpFramerRowStatusTable": mscDpnGateUtpFramerRowStatusTable,
       "mscDpnGateUtpFramerRowStatusEntry": mscDpnGateUtpFramerRowStatusEntry,
       "mscDpnGateUtpFramerRowStatus": mscDpnGateUtpFramerRowStatus,
       "mscDpnGateUtpFramerComponentName": mscDpnGateUtpFramerComponentName,
       "mscDpnGateUtpFramerStorageType": mscDpnGateUtpFramerStorageType,
       "mscDpnGateUtpFramerIndex": mscDpnGateUtpFramerIndex,
       "mscDpnGateUtpFramerProvTable": mscDpnGateUtpFramerProvTable,
       "mscDpnGateUtpFramerProvEntry": mscDpnGateUtpFramerProvEntry,
       "mscDpnGateUtpFramerInterfaceName": mscDpnGateUtpFramerInterfaceName,
       "mscDpnGateUtpFramerLinkTable": mscDpnGateUtpFramerLinkTable,
       "mscDpnGateUtpFramerLinkEntry": mscDpnGateUtpFramerLinkEntry,
       "mscDpnGateUtpFramerFramingType": mscDpnGateUtpFramerFramingType,
       "mscDpnGateUtpFramerDataInversion": mscDpnGateUtpFramerDataInversion,
       "mscDpnGateUtpFramerFrameCrcType": mscDpnGateUtpFramerFrameCrcType,
       "mscDpnGateUtpFramerFlagsBetweenFrames": mscDpnGateUtpFramerFlagsBetweenFrames,
       "mscDpnGateUtpFramerStateTable": mscDpnGateUtpFramerStateTable,
       "mscDpnGateUtpFramerStateEntry": mscDpnGateUtpFramerStateEntry,
       "mscDpnGateUtpFramerAdminState": mscDpnGateUtpFramerAdminState,
       "mscDpnGateUtpFramerOperationalState": mscDpnGateUtpFramerOperationalState,
       "mscDpnGateUtpFramerUsageState": mscDpnGateUtpFramerUsageState,
       "mscDpnGateUtpFramerStatsTable": mscDpnGateUtpFramerStatsTable,
       "mscDpnGateUtpFramerStatsEntry": mscDpnGateUtpFramerStatsEntry,
       "mscDpnGateUtpFramerFrmToIf": mscDpnGateUtpFramerFrmToIf,
       "mscDpnGateUtpFramerFrmFromIf": mscDpnGateUtpFramerFrmFromIf,
       "mscDpnGateUtpFramerOctetFromIf": mscDpnGateUtpFramerOctetFromIf,
       "mscDpnGateUtpFramerAborts": mscDpnGateUtpFramerAborts,
       "mscDpnGateUtpFramerCrcErrors": mscDpnGateUtpFramerCrcErrors,
       "mscDpnGateUtpFramerLrcErrors": mscDpnGateUtpFramerLrcErrors,
       "mscDpnGateUtpFramerNonOctetErrors": mscDpnGateUtpFramerNonOctetErrors,
       "mscDpnGateUtpFramerOverruns": mscDpnGateUtpFramerOverruns,
       "mscDpnGateUtpFramerUnderruns": mscDpnGateUtpFramerUnderruns,
       "mscDpnGateUtpFramerLargeFrmErrors": mscDpnGateUtpFramerLargeFrmErrors,
       "mscDpnGateUtpFramerFrmModeErrors": mscDpnGateUtpFramerFrmModeErrors,
       "mscDpnGateUtpFramerOutOfSequenceFrm": mscDpnGateUtpFramerOutOfSequenceFrm,
       "mscDpnGateUtpFramerRepeatedFrm": mscDpnGateUtpFramerRepeatedFrm,
       "mscDpnGateUtpFramerFrmToIf64": mscDpnGateUtpFramerFrmToIf64,
       "mscDpnGateUtpFramerFrmFromIf64": mscDpnGateUtpFramerFrmFromIf64,
       "mscDpnGateUtpFramerOctetFromIf64": mscDpnGateUtpFramerOctetFromIf64,
       "mscDpnGateUtpFramerUtilTable": mscDpnGateUtpFramerUtilTable,
       "mscDpnGateUtpFramerUtilEntry": mscDpnGateUtpFramerUtilEntry,
       "mscDpnGateUtpFramerNormPrioLinkUtilToIf": mscDpnGateUtpFramerNormPrioLinkUtilToIf,
       "mscDpnGateUtpFramerHighPrioLinkUtilToIf": mscDpnGateUtpFramerHighPrioLinkUtilToIf,
       "mscDpnGateUtpFramerNormPrioLinkUtilFromIf": mscDpnGateUtpFramerNormPrioLinkUtilFromIf,
       "mscDpnGateUtpFramerHighPrioLinkUtilFromIf": mscDpnGateUtpFramerHighPrioLinkUtilFromIf,
       "mscDpnGateUtpFramerUtilThresholdTable": mscDpnGateUtpFramerUtilThresholdTable,
       "mscDpnGateUtpFramerUtilThresholdEntry": mscDpnGateUtpFramerUtilThresholdEntry,
       "mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold": mscDpnGateUtpFramerMinorLinkUtilAlarmThreshold,
       "mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold": mscDpnGateUtpFramerMajorLinkUtilAlarmThreshold,
       "mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold": mscDpnGateUtpFramerCriticalLinkUtilAlarmThreshold,
       "mscDpnGateUtpFramerLinkUtilAlarmStatus": mscDpnGateUtpFramerLinkUtilAlarmStatus,
       "mscDpnGateUtpProvTable": mscDpnGateUtpProvTable,
       "mscDpnGateUtpProvEntry": mscDpnGateUtpProvEntry,
       "mscDpnGateUtpMaximumErroredInterval": mscDpnGateUtpMaximumErroredInterval,
       "mscDpnGateUtpReceiveErrorSensitivity": mscDpnGateUtpReceiveErrorSensitivity,
       "mscDpnGateUtpStateTable": mscDpnGateUtpStateTable,
       "mscDpnGateUtpStateEntry": mscDpnGateUtpStateEntry,
       "mscDpnGateUtpAdminState": mscDpnGateUtpAdminState,
       "mscDpnGateUtpOperationalState": mscDpnGateUtpOperationalState,
       "mscDpnGateUtpUsageState": mscDpnGateUtpUsageState,
       "mscDpnGateUtpAvailabilityStatus": mscDpnGateUtpAvailabilityStatus,
       "mscDpnGateUtpProceduralStatus": mscDpnGateUtpProceduralStatus,
       "mscDpnGateUtpControlStatus": mscDpnGateUtpControlStatus,
       "mscDpnGateUtpAlarmStatus": mscDpnGateUtpAlarmStatus,
       "mscDpnGateUtpStandbyStatus": mscDpnGateUtpStandbyStatus,
       "mscDpnGateUtpUnknownStatus": mscDpnGateUtpUnknownStatus,
       "mscDpnGateUtpOpTable": mscDpnGateUtpOpTable,
       "mscDpnGateUtpOpEntry": mscDpnGateUtpOpEntry,
       "mscDpnGateUtpRoundTripDelay": mscDpnGateUtpRoundTripDelay,
       "mscDpnGateUtpStatsTable": mscDpnGateUtpStatsTable,
       "mscDpnGateUtpStatsEntry": mscDpnGateUtpStatsEntry,
       "mscDpnGateUtpDiscardBadFromIf": mscDpnGateUtpDiscardBadFromIf,
       "mscDpnGateUtpDiscardExcessToIf": mscDpnGateUtpDiscardExcessToIf,
       "mscDpnGateUtpFrmRexmtToIf": mscDpnGateUtpFrmRexmtToIf,
       "mscDpnGateUtpAreYouThereModeEntries": mscDpnGateUtpAreYouThereModeEntries,
       "mscDpnGateUtpWindowClosures": mscDpnGateUtpWindowClosures,
       "utpDpnTrunksMIB": utpDpnTrunksMIB,
       "utpDpnTrunksGroup": utpDpnTrunksGroup,
       "utpDpnTrunksGroupCA": utpDpnTrunksGroupCA,
       "utpDpnTrunksGroupCA02": utpDpnTrunksGroupCA02,
       "utpDpnTrunksGroupCA02A": utpDpnTrunksGroupCA02A,
       "utpDpnTrunksCapabilities": utpDpnTrunksCapabilities,
       "utpDpnTrunksCapabilitiesCA": utpDpnTrunksCapabilitiesCA,
       "utpDpnTrunksCapabilitiesCA02": utpDpnTrunksCapabilitiesCA02,
       "utpDpnTrunksCapabilitiesCA02A": utpDpnTrunksCapabilitiesCA02A}
)
