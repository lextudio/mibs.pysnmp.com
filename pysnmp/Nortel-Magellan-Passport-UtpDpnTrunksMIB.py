# SNMP MIB module (Nortel-Magellan-Passport-UtpDpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-UtpDpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:31 2024
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

(dpnGate,
 dpnGateIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-DpnTrunksMIB",
    "dpnGate",
    "dpnGateIndex")

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

_DpnGateUtp_ObjectIdentity = ObjectIdentity
dpnGateUtp = _DpnGateUtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2)
)
_DpnGateUtpRowStatusTable_Object = MibTable
dpnGateUtpRowStatusTable = _DpnGateUtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1)
)
if mibBuilder.loadTexts:
    dpnGateUtpRowStatusTable.setStatus("mandatory")
_DpnGateUtpRowStatusEntry_Object = MibTableRow
dpnGateUtpRowStatusEntry = _DpnGateUtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1)
)
dpnGateUtpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpRowStatusEntry.setStatus("mandatory")
_DpnGateUtpRowStatus_Type = RowStatus
_DpnGateUtpRowStatus_Object = MibTableColumn
dpnGateUtpRowStatus = _DpnGateUtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 1),
    _DpnGateUtpRowStatus_Type()
)
dpnGateUtpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpRowStatus.setStatus("mandatory")
_DpnGateUtpComponentName_Type = DisplayString
_DpnGateUtpComponentName_Object = MibTableColumn
dpnGateUtpComponentName = _DpnGateUtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 2),
    _DpnGateUtpComponentName_Type()
)
dpnGateUtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpComponentName.setStatus("mandatory")
_DpnGateUtpStorageType_Type = StorageType
_DpnGateUtpStorageType_Object = MibTableColumn
dpnGateUtpStorageType = _DpnGateUtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 4),
    _DpnGateUtpStorageType_Type()
)
dpnGateUtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpStorageType.setStatus("mandatory")
_DpnGateUtpIndex_Type = NonReplicated
_DpnGateUtpIndex_Object = MibTableColumn
dpnGateUtpIndex = _DpnGateUtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 1, 1, 10),
    _DpnGateUtpIndex_Type()
)
dpnGateUtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateUtpIndex.setStatus("mandatory")
_DpnGateUtpFramer_ObjectIdentity = ObjectIdentity
dpnGateUtpFramer = _DpnGateUtpFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2)
)
_DpnGateUtpFramerRowStatusTable_Object = MibTable
dpnGateUtpFramerRowStatusTable = _DpnGateUtpFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerRowStatusTable.setStatus("mandatory")
_DpnGateUtpFramerRowStatusEntry_Object = MibTableRow
dpnGateUtpFramerRowStatusEntry = _DpnGateUtpFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1)
)
dpnGateUtpFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerRowStatusEntry.setStatus("mandatory")
_DpnGateUtpFramerRowStatus_Type = RowStatus
_DpnGateUtpFramerRowStatus_Object = MibTableColumn
dpnGateUtpFramerRowStatus = _DpnGateUtpFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 1),
    _DpnGateUtpFramerRowStatus_Type()
)
dpnGateUtpFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerRowStatus.setStatus("mandatory")
_DpnGateUtpFramerComponentName_Type = DisplayString
_DpnGateUtpFramerComponentName_Object = MibTableColumn
dpnGateUtpFramerComponentName = _DpnGateUtpFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 2),
    _DpnGateUtpFramerComponentName_Type()
)
dpnGateUtpFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerComponentName.setStatus("mandatory")
_DpnGateUtpFramerStorageType_Type = StorageType
_DpnGateUtpFramerStorageType_Object = MibTableColumn
dpnGateUtpFramerStorageType = _DpnGateUtpFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 4),
    _DpnGateUtpFramerStorageType_Type()
)
dpnGateUtpFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerStorageType.setStatus("mandatory")
_DpnGateUtpFramerIndex_Type = NonReplicated
_DpnGateUtpFramerIndex_Object = MibTableColumn
dpnGateUtpFramerIndex = _DpnGateUtpFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 1, 1, 10),
    _DpnGateUtpFramerIndex_Type()
)
dpnGateUtpFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateUtpFramerIndex.setStatus("mandatory")
_DpnGateUtpFramerProvTable_Object = MibTable
dpnGateUtpFramerProvTable = _DpnGateUtpFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerProvTable.setStatus("mandatory")
_DpnGateUtpFramerProvEntry_Object = MibTableRow
dpnGateUtpFramerProvEntry = _DpnGateUtpFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10, 1)
)
dpnGateUtpFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerProvEntry.setStatus("mandatory")
_DpnGateUtpFramerInterfaceName_Type = Link
_DpnGateUtpFramerInterfaceName_Object = MibTableColumn
dpnGateUtpFramerInterfaceName = _DpnGateUtpFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 10, 1, 1),
    _DpnGateUtpFramerInterfaceName_Type()
)
dpnGateUtpFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerInterfaceName.setStatus("mandatory")
_DpnGateUtpFramerLinkTable_Object = MibTable
dpnGateUtpFramerLinkTable = _DpnGateUtpFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerLinkTable.setStatus("mandatory")
_DpnGateUtpFramerLinkEntry_Object = MibTableRow
dpnGateUtpFramerLinkEntry = _DpnGateUtpFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1)
)
dpnGateUtpFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerLinkEntry.setStatus("mandatory")


class _DpnGateUtpFramerFramingType_Type(Integer32):
    """Custom type dpnGateUtpFramerFramingType based on Integer32"""
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


_DpnGateUtpFramerFramingType_Type.__name__ = "Integer32"
_DpnGateUtpFramerFramingType_Object = MibTableColumn
dpnGateUtpFramerFramingType = _DpnGateUtpFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 1),
    _DpnGateUtpFramerFramingType_Type()
)
dpnGateUtpFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFramingType.setStatus("mandatory")


class _DpnGateUtpFramerDataInversion_Type(Integer32):
    """Custom type dpnGateUtpFramerDataInversion based on Integer32"""
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


_DpnGateUtpFramerDataInversion_Type.__name__ = "Integer32"
_DpnGateUtpFramerDataInversion_Object = MibTableColumn
dpnGateUtpFramerDataInversion = _DpnGateUtpFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 2),
    _DpnGateUtpFramerDataInversion_Type()
)
dpnGateUtpFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerDataInversion.setStatus("mandatory")


class _DpnGateUtpFramerFrameCrcType_Type(Integer32):
    """Custom type dpnGateUtpFramerFrameCrcType based on Integer32"""
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


_DpnGateUtpFramerFrameCrcType_Type.__name__ = "Integer32"
_DpnGateUtpFramerFrameCrcType_Object = MibTableColumn
dpnGateUtpFramerFrameCrcType = _DpnGateUtpFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 3),
    _DpnGateUtpFramerFrameCrcType_Type()
)
dpnGateUtpFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFrameCrcType.setStatus("mandatory")


class _DpnGateUtpFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type dpnGateUtpFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DpnGateUtpFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_DpnGateUtpFramerFlagsBetweenFrames_Object = MibTableColumn
dpnGateUtpFramerFlagsBetweenFrames = _DpnGateUtpFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 11, 1, 4),
    _DpnGateUtpFramerFlagsBetweenFrames_Type()
)
dpnGateUtpFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFlagsBetweenFrames.setStatus("mandatory")
_DpnGateUtpFramerStateTable_Object = MibTable
dpnGateUtpFramerStateTable = _DpnGateUtpFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerStateTable.setStatus("mandatory")
_DpnGateUtpFramerStateEntry_Object = MibTableRow
dpnGateUtpFramerStateEntry = _DpnGateUtpFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1)
)
dpnGateUtpFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerStateEntry.setStatus("mandatory")


class _DpnGateUtpFramerAdminState_Type(Integer32):
    """Custom type dpnGateUtpFramerAdminState based on Integer32"""
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


_DpnGateUtpFramerAdminState_Type.__name__ = "Integer32"
_DpnGateUtpFramerAdminState_Object = MibTableColumn
dpnGateUtpFramerAdminState = _DpnGateUtpFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 1),
    _DpnGateUtpFramerAdminState_Type()
)
dpnGateUtpFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerAdminState.setStatus("mandatory")


class _DpnGateUtpFramerOperationalState_Type(Integer32):
    """Custom type dpnGateUtpFramerOperationalState based on Integer32"""
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


_DpnGateUtpFramerOperationalState_Type.__name__ = "Integer32"
_DpnGateUtpFramerOperationalState_Object = MibTableColumn
dpnGateUtpFramerOperationalState = _DpnGateUtpFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 2),
    _DpnGateUtpFramerOperationalState_Type()
)
dpnGateUtpFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerOperationalState.setStatus("mandatory")


class _DpnGateUtpFramerUsageState_Type(Integer32):
    """Custom type dpnGateUtpFramerUsageState based on Integer32"""
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


_DpnGateUtpFramerUsageState_Type.__name__ = "Integer32"
_DpnGateUtpFramerUsageState_Object = MibTableColumn
dpnGateUtpFramerUsageState = _DpnGateUtpFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 12, 1, 3),
    _DpnGateUtpFramerUsageState_Type()
)
dpnGateUtpFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerUsageState.setStatus("mandatory")
_DpnGateUtpFramerStatsTable_Object = MibTable
dpnGateUtpFramerStatsTable = _DpnGateUtpFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerStatsTable.setStatus("mandatory")
_DpnGateUtpFramerStatsEntry_Object = MibTableRow
dpnGateUtpFramerStatsEntry = _DpnGateUtpFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1)
)
dpnGateUtpFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerStatsEntry.setStatus("mandatory")
_DpnGateUtpFramerFrmToIf_Type = Counter32
_DpnGateUtpFramerFrmToIf_Object = MibTableColumn
dpnGateUtpFramerFrmToIf = _DpnGateUtpFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 1),
    _DpnGateUtpFramerFrmToIf_Type()
)
dpnGateUtpFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFrmToIf.setStatus("mandatory")
_DpnGateUtpFramerFrmFromIf_Type = Counter32
_DpnGateUtpFramerFrmFromIf_Object = MibTableColumn
dpnGateUtpFramerFrmFromIf = _DpnGateUtpFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 2),
    _DpnGateUtpFramerFrmFromIf_Type()
)
dpnGateUtpFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFrmFromIf.setStatus("mandatory")
_DpnGateUtpFramerOctetFromIf_Type = Counter32
_DpnGateUtpFramerOctetFromIf_Object = MibTableColumn
dpnGateUtpFramerOctetFromIf = _DpnGateUtpFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 3),
    _DpnGateUtpFramerOctetFromIf_Type()
)
dpnGateUtpFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerOctetFromIf.setStatus("mandatory")
_DpnGateUtpFramerAborts_Type = Counter32
_DpnGateUtpFramerAborts_Object = MibTableColumn
dpnGateUtpFramerAborts = _DpnGateUtpFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 4),
    _DpnGateUtpFramerAborts_Type()
)
dpnGateUtpFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerAborts.setStatus("mandatory")
_DpnGateUtpFramerCrcErrors_Type = Counter32
_DpnGateUtpFramerCrcErrors_Object = MibTableColumn
dpnGateUtpFramerCrcErrors = _DpnGateUtpFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 5),
    _DpnGateUtpFramerCrcErrors_Type()
)
dpnGateUtpFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerCrcErrors.setStatus("mandatory")
_DpnGateUtpFramerLrcErrors_Type = Counter32
_DpnGateUtpFramerLrcErrors_Object = MibTableColumn
dpnGateUtpFramerLrcErrors = _DpnGateUtpFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 6),
    _DpnGateUtpFramerLrcErrors_Type()
)
dpnGateUtpFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerLrcErrors.setStatus("mandatory")
_DpnGateUtpFramerNonOctetErrors_Type = Counter32
_DpnGateUtpFramerNonOctetErrors_Object = MibTableColumn
dpnGateUtpFramerNonOctetErrors = _DpnGateUtpFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 7),
    _DpnGateUtpFramerNonOctetErrors_Type()
)
dpnGateUtpFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerNonOctetErrors.setStatus("mandatory")
_DpnGateUtpFramerOverruns_Type = Counter32
_DpnGateUtpFramerOverruns_Object = MibTableColumn
dpnGateUtpFramerOverruns = _DpnGateUtpFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 8),
    _DpnGateUtpFramerOverruns_Type()
)
dpnGateUtpFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerOverruns.setStatus("mandatory")
_DpnGateUtpFramerUnderruns_Type = Counter32
_DpnGateUtpFramerUnderruns_Object = MibTableColumn
dpnGateUtpFramerUnderruns = _DpnGateUtpFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 9),
    _DpnGateUtpFramerUnderruns_Type()
)
dpnGateUtpFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerUnderruns.setStatus("mandatory")
_DpnGateUtpFramerLargeFrmErrors_Type = Counter32
_DpnGateUtpFramerLargeFrmErrors_Object = MibTableColumn
dpnGateUtpFramerLargeFrmErrors = _DpnGateUtpFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 10),
    _DpnGateUtpFramerLargeFrmErrors_Type()
)
dpnGateUtpFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerLargeFrmErrors.setStatus("mandatory")
_DpnGateUtpFramerFrmModeErrors_Type = Counter32
_DpnGateUtpFramerFrmModeErrors_Object = MibTableColumn
dpnGateUtpFramerFrmModeErrors = _DpnGateUtpFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 11),
    _DpnGateUtpFramerFrmModeErrors_Type()
)
dpnGateUtpFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerFrmModeErrors.setStatus("mandatory")
_DpnGateUtpFramerOutOfSequenceFrm_Type = Counter32
_DpnGateUtpFramerOutOfSequenceFrm_Object = MibTableColumn
dpnGateUtpFramerOutOfSequenceFrm = _DpnGateUtpFramerOutOfSequenceFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 12),
    _DpnGateUtpFramerOutOfSequenceFrm_Type()
)
dpnGateUtpFramerOutOfSequenceFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerOutOfSequenceFrm.setStatus("mandatory")
_DpnGateUtpFramerRepeatedFrm_Type = Counter32
_DpnGateUtpFramerRepeatedFrm_Object = MibTableColumn
dpnGateUtpFramerRepeatedFrm = _DpnGateUtpFramerRepeatedFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 13, 1, 13),
    _DpnGateUtpFramerRepeatedFrm_Type()
)
dpnGateUtpFramerRepeatedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerRepeatedFrm.setStatus("mandatory")
_DpnGateUtpFramerUtilTable_Object = MibTable
dpnGateUtpFramerUtilTable = _DpnGateUtpFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerUtilTable.setStatus("mandatory")
_DpnGateUtpFramerUtilEntry_Object = MibTableRow
dpnGateUtpFramerUtilEntry = _DpnGateUtpFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1)
)
dpnGateUtpFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerUtilEntry.setStatus("mandatory")


class _DpnGateUtpFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type dpnGateUtpFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_DpnGateUtpFramerNormPrioLinkUtilToIf_Object = MibTableColumn
dpnGateUtpFramerNormPrioLinkUtilToIf = _DpnGateUtpFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 1),
    _DpnGateUtpFramerNormPrioLinkUtilToIf_Type()
)
dpnGateUtpFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _DpnGateUtpFramerHighPrioLinkUtilToIf_Type(Gauge32):
    """Custom type dpnGateUtpFramerHighPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerHighPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_DpnGateUtpFramerHighPrioLinkUtilToIf_Object = MibTableColumn
dpnGateUtpFramerHighPrioLinkUtilToIf = _DpnGateUtpFramerHighPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 2),
    _DpnGateUtpFramerHighPrioLinkUtilToIf_Type()
)
dpnGateUtpFramerHighPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerHighPrioLinkUtilToIf.setStatus("mandatory")


class _DpnGateUtpFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type dpnGateUtpFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_DpnGateUtpFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
dpnGateUtpFramerNormPrioLinkUtilFromIf = _DpnGateUtpFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 3),
    _DpnGateUtpFramerNormPrioLinkUtilFromIf_Type()
)
dpnGateUtpFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerNormPrioLinkUtilFromIf.setStatus("mandatory")


class _DpnGateUtpFramerHighPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type dpnGateUtpFramerHighPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerHighPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_DpnGateUtpFramerHighPrioLinkUtilFromIf_Object = MibTableColumn
dpnGateUtpFramerHighPrioLinkUtilFromIf = _DpnGateUtpFramerHighPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 14, 1, 4),
    _DpnGateUtpFramerHighPrioLinkUtilFromIf_Type()
)
dpnGateUtpFramerHighPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFramerHighPrioLinkUtilFromIf.setStatus("mandatory")
_DpnGateUtpFramerUtilThresholdTable_Object = MibTable
dpnGateUtpFramerUtilThresholdTable = _DpnGateUtpFramerUtilThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15)
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerUtilThresholdTable.setStatus("mandatory")
_DpnGateUtpFramerUtilThresholdEntry_Object = MibTableRow
dpnGateUtpFramerUtilThresholdEntry = _DpnGateUtpFramerUtilThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1)
)
dpnGateUtpFramerUtilThresholdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpFramerIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpFramerUtilThresholdEntry.setStatus("mandatory")


class _DpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type dpnGateUtpFramerMinorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_DpnGateUtpFramerMinorLinkUtilAlarmThreshold_Object = MibTableColumn
dpnGateUtpFramerMinorLinkUtilAlarmThreshold = _DpnGateUtpFramerMinorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 1),
    _DpnGateUtpFramerMinorLinkUtilAlarmThreshold_Type()
)
dpnGateUtpFramerMinorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerMinorLinkUtilAlarmThreshold.setStatus("mandatory")


class _DpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type dpnGateUtpFramerMajorLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_DpnGateUtpFramerMajorLinkUtilAlarmThreshold_Object = MibTableColumn
dpnGateUtpFramerMajorLinkUtilAlarmThreshold = _DpnGateUtpFramerMajorLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 2),
    _DpnGateUtpFramerMajorLinkUtilAlarmThreshold_Type()
)
dpnGateUtpFramerMajorLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerMajorLinkUtilAlarmThreshold.setStatus("mandatory")


class _DpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type(Unsigned32):
    """Custom type dpnGateUtpFramerCriticalLinkUtilAlarmThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type.__name__ = "Unsigned32"
_DpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Object = MibTableColumn
dpnGateUtpFramerCriticalLinkUtilAlarmThreshold = _DpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 3),
    _DpnGateUtpFramerCriticalLinkUtilAlarmThreshold_Type()
)
dpnGateUtpFramerCriticalLinkUtilAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerCriticalLinkUtilAlarmThreshold.setStatus("mandatory")


class _DpnGateUtpFramerLinkUtilAlarmStatus_Type(Integer32):
    """Custom type dpnGateUtpFramerLinkUtilAlarmStatus based on Integer32"""
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


_DpnGateUtpFramerLinkUtilAlarmStatus_Type.__name__ = "Integer32"
_DpnGateUtpFramerLinkUtilAlarmStatus_Object = MibTableColumn
dpnGateUtpFramerLinkUtilAlarmStatus = _DpnGateUtpFramerLinkUtilAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 2, 15, 1, 4),
    _DpnGateUtpFramerLinkUtilAlarmStatus_Type()
)
dpnGateUtpFramerLinkUtilAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpFramerLinkUtilAlarmStatus.setStatus("mandatory")
_DpnGateUtpProvTable_Object = MibTable
dpnGateUtpProvTable = _DpnGateUtpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10)
)
if mibBuilder.loadTexts:
    dpnGateUtpProvTable.setStatus("mandatory")
_DpnGateUtpProvEntry_Object = MibTableRow
dpnGateUtpProvEntry = _DpnGateUtpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1)
)
dpnGateUtpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpProvEntry.setStatus("mandatory")


class _DpnGateUtpMaximumErroredInterval_Type(Unsigned32):
    """Custom type dpnGateUtpMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_DpnGateUtpMaximumErroredInterval_Type.__name__ = "Unsigned32"
_DpnGateUtpMaximumErroredInterval_Object = MibTableColumn
dpnGateUtpMaximumErroredInterval = _DpnGateUtpMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1, 1),
    _DpnGateUtpMaximumErroredInterval_Type()
)
dpnGateUtpMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpMaximumErroredInterval.setStatus("mandatory")


class _DpnGateUtpReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type dpnGateUtpReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_DpnGateUtpReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_DpnGateUtpReceiveErrorSensitivity_Object = MibTableColumn
dpnGateUtpReceiveErrorSensitivity = _DpnGateUtpReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 10, 1, 2),
    _DpnGateUtpReceiveErrorSensitivity_Type()
)
dpnGateUtpReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateUtpReceiveErrorSensitivity.setStatus("mandatory")
_DpnGateUtpStateTable_Object = MibTable
dpnGateUtpStateTable = _DpnGateUtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11)
)
if mibBuilder.loadTexts:
    dpnGateUtpStateTable.setStatus("mandatory")
_DpnGateUtpStateEntry_Object = MibTableRow
dpnGateUtpStateEntry = _DpnGateUtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1)
)
dpnGateUtpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpStateEntry.setStatus("mandatory")


class _DpnGateUtpAdminState_Type(Integer32):
    """Custom type dpnGateUtpAdminState based on Integer32"""
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


_DpnGateUtpAdminState_Type.__name__ = "Integer32"
_DpnGateUtpAdminState_Object = MibTableColumn
dpnGateUtpAdminState = _DpnGateUtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 1),
    _DpnGateUtpAdminState_Type()
)
dpnGateUtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpAdminState.setStatus("mandatory")


class _DpnGateUtpOperationalState_Type(Integer32):
    """Custom type dpnGateUtpOperationalState based on Integer32"""
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


_DpnGateUtpOperationalState_Type.__name__ = "Integer32"
_DpnGateUtpOperationalState_Object = MibTableColumn
dpnGateUtpOperationalState = _DpnGateUtpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 2),
    _DpnGateUtpOperationalState_Type()
)
dpnGateUtpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpOperationalState.setStatus("mandatory")


class _DpnGateUtpUsageState_Type(Integer32):
    """Custom type dpnGateUtpUsageState based on Integer32"""
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


_DpnGateUtpUsageState_Type.__name__ = "Integer32"
_DpnGateUtpUsageState_Object = MibTableColumn
dpnGateUtpUsageState = _DpnGateUtpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 3),
    _DpnGateUtpUsageState_Type()
)
dpnGateUtpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpUsageState.setStatus("mandatory")


class _DpnGateUtpAvailabilityStatus_Type(OctetString):
    """Custom type dpnGateUtpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DpnGateUtpAvailabilityStatus_Type.__name__ = "OctetString"
_DpnGateUtpAvailabilityStatus_Object = MibTableColumn
dpnGateUtpAvailabilityStatus = _DpnGateUtpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 4),
    _DpnGateUtpAvailabilityStatus_Type()
)
dpnGateUtpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpAvailabilityStatus.setStatus("mandatory")


class _DpnGateUtpProceduralStatus_Type(OctetString):
    """Custom type dpnGateUtpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateUtpProceduralStatus_Type.__name__ = "OctetString"
_DpnGateUtpProceduralStatus_Object = MibTableColumn
dpnGateUtpProceduralStatus = _DpnGateUtpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 5),
    _DpnGateUtpProceduralStatus_Type()
)
dpnGateUtpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpProceduralStatus.setStatus("mandatory")


class _DpnGateUtpControlStatus_Type(OctetString):
    """Custom type dpnGateUtpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateUtpControlStatus_Type.__name__ = "OctetString"
_DpnGateUtpControlStatus_Object = MibTableColumn
dpnGateUtpControlStatus = _DpnGateUtpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 6),
    _DpnGateUtpControlStatus_Type()
)
dpnGateUtpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpControlStatus.setStatus("mandatory")


class _DpnGateUtpAlarmStatus_Type(OctetString):
    """Custom type dpnGateUtpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateUtpAlarmStatus_Type.__name__ = "OctetString"
_DpnGateUtpAlarmStatus_Object = MibTableColumn
dpnGateUtpAlarmStatus = _DpnGateUtpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 7),
    _DpnGateUtpAlarmStatus_Type()
)
dpnGateUtpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpAlarmStatus.setStatus("mandatory")


class _DpnGateUtpStandbyStatus_Type(Integer32):
    """Custom type dpnGateUtpStandbyStatus based on Integer32"""
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


_DpnGateUtpStandbyStatus_Type.__name__ = "Integer32"
_DpnGateUtpStandbyStatus_Object = MibTableColumn
dpnGateUtpStandbyStatus = _DpnGateUtpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 8),
    _DpnGateUtpStandbyStatus_Type()
)
dpnGateUtpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpStandbyStatus.setStatus("mandatory")


class _DpnGateUtpUnknownStatus_Type(Integer32):
    """Custom type dpnGateUtpUnknownStatus based on Integer32"""
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


_DpnGateUtpUnknownStatus_Type.__name__ = "Integer32"
_DpnGateUtpUnknownStatus_Object = MibTableColumn
dpnGateUtpUnknownStatus = _DpnGateUtpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 11, 1, 9),
    _DpnGateUtpUnknownStatus_Type()
)
dpnGateUtpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpUnknownStatus.setStatus("mandatory")
_DpnGateUtpOpTable_Object = MibTable
dpnGateUtpOpTable = _DpnGateUtpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12)
)
if mibBuilder.loadTexts:
    dpnGateUtpOpTable.setStatus("mandatory")
_DpnGateUtpOpEntry_Object = MibTableRow
dpnGateUtpOpEntry = _DpnGateUtpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12, 1)
)
dpnGateUtpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpOpEntry.setStatus("mandatory")


class _DpnGateUtpRoundTripDelay_Type(Gauge32):
    """Custom type dpnGateUtpRoundTripDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DpnGateUtpRoundTripDelay_Type.__name__ = "Gauge32"
_DpnGateUtpRoundTripDelay_Object = MibTableColumn
dpnGateUtpRoundTripDelay = _DpnGateUtpRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 12, 1, 1),
    _DpnGateUtpRoundTripDelay_Type()
)
dpnGateUtpRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpRoundTripDelay.setStatus("mandatory")
_DpnGateUtpStatsTable_Object = MibTable
dpnGateUtpStatsTable = _DpnGateUtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13)
)
if mibBuilder.loadTexts:
    dpnGateUtpStatsTable.setStatus("mandatory")
_DpnGateUtpStatsEntry_Object = MibTableRow
dpnGateUtpStatsEntry = _DpnGateUtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1)
)
dpnGateUtpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-UtpDpnTrunksMIB", "dpnGateUtpIndex"),
)
if mibBuilder.loadTexts:
    dpnGateUtpStatsEntry.setStatus("mandatory")
_DpnGateUtpDiscardBadFromIf_Type = Counter32
_DpnGateUtpDiscardBadFromIf_Object = MibTableColumn
dpnGateUtpDiscardBadFromIf = _DpnGateUtpDiscardBadFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 1),
    _DpnGateUtpDiscardBadFromIf_Type()
)
dpnGateUtpDiscardBadFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpDiscardBadFromIf.setStatus("mandatory")
_DpnGateUtpDiscardExcessToIf_Type = Counter32
_DpnGateUtpDiscardExcessToIf_Object = MibTableColumn
dpnGateUtpDiscardExcessToIf = _DpnGateUtpDiscardExcessToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 2),
    _DpnGateUtpDiscardExcessToIf_Type()
)
dpnGateUtpDiscardExcessToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpDiscardExcessToIf.setStatus("mandatory")
_DpnGateUtpFrmRexmtToIf_Type = Counter32
_DpnGateUtpFrmRexmtToIf_Object = MibTableColumn
dpnGateUtpFrmRexmtToIf = _DpnGateUtpFrmRexmtToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 3),
    _DpnGateUtpFrmRexmtToIf_Type()
)
dpnGateUtpFrmRexmtToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpFrmRexmtToIf.setStatus("mandatory")
_DpnGateUtpAreYouThereModeEntries_Type = Counter32
_DpnGateUtpAreYouThereModeEntries_Object = MibTableColumn
dpnGateUtpAreYouThereModeEntries = _DpnGateUtpAreYouThereModeEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 4),
    _DpnGateUtpAreYouThereModeEntries_Type()
)
dpnGateUtpAreYouThereModeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpAreYouThereModeEntries.setStatus("mandatory")
_DpnGateUtpWindowClosures_Type = Counter32
_DpnGateUtpWindowClosures_Object = MibTableColumn
dpnGateUtpWindowClosures = _DpnGateUtpWindowClosures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 2, 13, 1, 5),
    _DpnGateUtpWindowClosures_Type()
)
dpnGateUtpWindowClosures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateUtpWindowClosures.setStatus("mandatory")
_UtpDpnTrunksMIB_ObjectIdentity = ObjectIdentity
utpDpnTrunksMIB = _UtpDpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67)
)
_UtpDpnTrunksGroup_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroup = _UtpDpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1)
)
_UtpDpnTrunksGroupBE_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupBE = _UtpDpnTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5)
)
_UtpDpnTrunksGroupBE00_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupBE00 = _UtpDpnTrunksGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5, 1)
)
_UtpDpnTrunksGroupBE00A_ObjectIdentity = ObjectIdentity
utpDpnTrunksGroupBE00A = _UtpDpnTrunksGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 1, 5, 1, 2)
)
_UtpDpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilities = _UtpDpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3)
)
_UtpDpnTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesBE = _UtpDpnTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5)
)
_UtpDpnTrunksCapabilitiesBE00_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesBE00 = _UtpDpnTrunksCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5, 1)
)
_UtpDpnTrunksCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
utpDpnTrunksCapabilitiesBE00A = _UtpDpnTrunksCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 67, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-UtpDpnTrunksMIB",
    **{"dpnGateUtp": dpnGateUtp,
       "dpnGateUtpRowStatusTable": dpnGateUtpRowStatusTable,
       "dpnGateUtpRowStatusEntry": dpnGateUtpRowStatusEntry,
       "dpnGateUtpRowStatus": dpnGateUtpRowStatus,
       "dpnGateUtpComponentName": dpnGateUtpComponentName,
       "dpnGateUtpStorageType": dpnGateUtpStorageType,
       "dpnGateUtpIndex": dpnGateUtpIndex,
       "dpnGateUtpFramer": dpnGateUtpFramer,
       "dpnGateUtpFramerRowStatusTable": dpnGateUtpFramerRowStatusTable,
       "dpnGateUtpFramerRowStatusEntry": dpnGateUtpFramerRowStatusEntry,
       "dpnGateUtpFramerRowStatus": dpnGateUtpFramerRowStatus,
       "dpnGateUtpFramerComponentName": dpnGateUtpFramerComponentName,
       "dpnGateUtpFramerStorageType": dpnGateUtpFramerStorageType,
       "dpnGateUtpFramerIndex": dpnGateUtpFramerIndex,
       "dpnGateUtpFramerProvTable": dpnGateUtpFramerProvTable,
       "dpnGateUtpFramerProvEntry": dpnGateUtpFramerProvEntry,
       "dpnGateUtpFramerInterfaceName": dpnGateUtpFramerInterfaceName,
       "dpnGateUtpFramerLinkTable": dpnGateUtpFramerLinkTable,
       "dpnGateUtpFramerLinkEntry": dpnGateUtpFramerLinkEntry,
       "dpnGateUtpFramerFramingType": dpnGateUtpFramerFramingType,
       "dpnGateUtpFramerDataInversion": dpnGateUtpFramerDataInversion,
       "dpnGateUtpFramerFrameCrcType": dpnGateUtpFramerFrameCrcType,
       "dpnGateUtpFramerFlagsBetweenFrames": dpnGateUtpFramerFlagsBetweenFrames,
       "dpnGateUtpFramerStateTable": dpnGateUtpFramerStateTable,
       "dpnGateUtpFramerStateEntry": dpnGateUtpFramerStateEntry,
       "dpnGateUtpFramerAdminState": dpnGateUtpFramerAdminState,
       "dpnGateUtpFramerOperationalState": dpnGateUtpFramerOperationalState,
       "dpnGateUtpFramerUsageState": dpnGateUtpFramerUsageState,
       "dpnGateUtpFramerStatsTable": dpnGateUtpFramerStatsTable,
       "dpnGateUtpFramerStatsEntry": dpnGateUtpFramerStatsEntry,
       "dpnGateUtpFramerFrmToIf": dpnGateUtpFramerFrmToIf,
       "dpnGateUtpFramerFrmFromIf": dpnGateUtpFramerFrmFromIf,
       "dpnGateUtpFramerOctetFromIf": dpnGateUtpFramerOctetFromIf,
       "dpnGateUtpFramerAborts": dpnGateUtpFramerAborts,
       "dpnGateUtpFramerCrcErrors": dpnGateUtpFramerCrcErrors,
       "dpnGateUtpFramerLrcErrors": dpnGateUtpFramerLrcErrors,
       "dpnGateUtpFramerNonOctetErrors": dpnGateUtpFramerNonOctetErrors,
       "dpnGateUtpFramerOverruns": dpnGateUtpFramerOverruns,
       "dpnGateUtpFramerUnderruns": dpnGateUtpFramerUnderruns,
       "dpnGateUtpFramerLargeFrmErrors": dpnGateUtpFramerLargeFrmErrors,
       "dpnGateUtpFramerFrmModeErrors": dpnGateUtpFramerFrmModeErrors,
       "dpnGateUtpFramerOutOfSequenceFrm": dpnGateUtpFramerOutOfSequenceFrm,
       "dpnGateUtpFramerRepeatedFrm": dpnGateUtpFramerRepeatedFrm,
       "dpnGateUtpFramerUtilTable": dpnGateUtpFramerUtilTable,
       "dpnGateUtpFramerUtilEntry": dpnGateUtpFramerUtilEntry,
       "dpnGateUtpFramerNormPrioLinkUtilToIf": dpnGateUtpFramerNormPrioLinkUtilToIf,
       "dpnGateUtpFramerHighPrioLinkUtilToIf": dpnGateUtpFramerHighPrioLinkUtilToIf,
       "dpnGateUtpFramerNormPrioLinkUtilFromIf": dpnGateUtpFramerNormPrioLinkUtilFromIf,
       "dpnGateUtpFramerHighPrioLinkUtilFromIf": dpnGateUtpFramerHighPrioLinkUtilFromIf,
       "dpnGateUtpFramerUtilThresholdTable": dpnGateUtpFramerUtilThresholdTable,
       "dpnGateUtpFramerUtilThresholdEntry": dpnGateUtpFramerUtilThresholdEntry,
       "dpnGateUtpFramerMinorLinkUtilAlarmThreshold": dpnGateUtpFramerMinorLinkUtilAlarmThreshold,
       "dpnGateUtpFramerMajorLinkUtilAlarmThreshold": dpnGateUtpFramerMajorLinkUtilAlarmThreshold,
       "dpnGateUtpFramerCriticalLinkUtilAlarmThreshold": dpnGateUtpFramerCriticalLinkUtilAlarmThreshold,
       "dpnGateUtpFramerLinkUtilAlarmStatus": dpnGateUtpFramerLinkUtilAlarmStatus,
       "dpnGateUtpProvTable": dpnGateUtpProvTable,
       "dpnGateUtpProvEntry": dpnGateUtpProvEntry,
       "dpnGateUtpMaximumErroredInterval": dpnGateUtpMaximumErroredInterval,
       "dpnGateUtpReceiveErrorSensitivity": dpnGateUtpReceiveErrorSensitivity,
       "dpnGateUtpStateTable": dpnGateUtpStateTable,
       "dpnGateUtpStateEntry": dpnGateUtpStateEntry,
       "dpnGateUtpAdminState": dpnGateUtpAdminState,
       "dpnGateUtpOperationalState": dpnGateUtpOperationalState,
       "dpnGateUtpUsageState": dpnGateUtpUsageState,
       "dpnGateUtpAvailabilityStatus": dpnGateUtpAvailabilityStatus,
       "dpnGateUtpProceduralStatus": dpnGateUtpProceduralStatus,
       "dpnGateUtpControlStatus": dpnGateUtpControlStatus,
       "dpnGateUtpAlarmStatus": dpnGateUtpAlarmStatus,
       "dpnGateUtpStandbyStatus": dpnGateUtpStandbyStatus,
       "dpnGateUtpUnknownStatus": dpnGateUtpUnknownStatus,
       "dpnGateUtpOpTable": dpnGateUtpOpTable,
       "dpnGateUtpOpEntry": dpnGateUtpOpEntry,
       "dpnGateUtpRoundTripDelay": dpnGateUtpRoundTripDelay,
       "dpnGateUtpStatsTable": dpnGateUtpStatsTable,
       "dpnGateUtpStatsEntry": dpnGateUtpStatsEntry,
       "dpnGateUtpDiscardBadFromIf": dpnGateUtpDiscardBadFromIf,
       "dpnGateUtpDiscardExcessToIf": dpnGateUtpDiscardExcessToIf,
       "dpnGateUtpFrmRexmtToIf": dpnGateUtpFrmRexmtToIf,
       "dpnGateUtpAreYouThereModeEntries": dpnGateUtpAreYouThereModeEntries,
       "dpnGateUtpWindowClosures": dpnGateUtpWindowClosures,
       "utpDpnTrunksMIB": utpDpnTrunksMIB,
       "utpDpnTrunksGroup": utpDpnTrunksGroup,
       "utpDpnTrunksGroupBE": utpDpnTrunksGroupBE,
       "utpDpnTrunksGroupBE00": utpDpnTrunksGroupBE00,
       "utpDpnTrunksGroupBE00A": utpDpnTrunksGroupBE00A,
       "utpDpnTrunksCapabilities": utpDpnTrunksCapabilities,
       "utpDpnTrunksCapabilitiesBE": utpDpnTrunksCapabilitiesBE,
       "utpDpnTrunksCapabilitiesBE00": utpDpnTrunksCapabilitiesBE00,
       "utpDpnTrunksCapabilitiesBE00A": utpDpnTrunksCapabilitiesBE00A}
)
