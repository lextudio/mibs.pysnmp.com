# SNMP MIB module (Nortel-MsCarrier-MscPassport-HdlcTransparentMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-HdlcTransparentMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:34 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
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

_MscHtds_ObjectIdentity = ObjectIdentity
mscHtds = _MscHtds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82)
)
_MscHtdsRowStatusTable_Object = MibTable
mscHtdsRowStatusTable = _MscHtdsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1)
)
if mibBuilder.loadTexts:
    mscHtdsRowStatusTable.setStatus("mandatory")
_MscHtdsRowStatusEntry_Object = MibTableRow
mscHtdsRowStatusEntry = _MscHtdsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1, 1)
)
mscHtdsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsRowStatusEntry.setStatus("mandatory")
_MscHtdsRowStatus_Type = RowStatus
_MscHtdsRowStatus_Object = MibTableColumn
mscHtdsRowStatus = _MscHtdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1, 1, 1),
    _MscHtdsRowStatus_Type()
)
mscHtdsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsRowStatus.setStatus("mandatory")
_MscHtdsComponentName_Type = DisplayString
_MscHtdsComponentName_Object = MibTableColumn
mscHtdsComponentName = _MscHtdsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1, 1, 2),
    _MscHtdsComponentName_Type()
)
mscHtdsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsComponentName.setStatus("mandatory")
_MscHtdsStorageType_Type = StorageType
_MscHtdsStorageType_Object = MibTableColumn
mscHtdsStorageType = _MscHtdsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1, 1, 4),
    _MscHtdsStorageType_Type()
)
mscHtdsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsStorageType.setStatus("mandatory")


class _MscHtdsIndex_Type(Integer32):
    """Custom type mscHtdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscHtdsIndex_Type.__name__ = "Integer32"
_MscHtdsIndex_Object = MibTableColumn
mscHtdsIndex = _MscHtdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 1, 1, 10),
    _MscHtdsIndex_Type()
)
mscHtdsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHtdsIndex.setStatus("mandatory")
_MscHtdsFramer_ObjectIdentity = ObjectIdentity
mscHtdsFramer = _MscHtdsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2)
)
_MscHtdsFramerRowStatusTable_Object = MibTable
mscHtdsFramerRowStatusTable = _MscHtdsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1)
)
if mibBuilder.loadTexts:
    mscHtdsFramerRowStatusTable.setStatus("mandatory")
_MscHtdsFramerRowStatusEntry_Object = MibTableRow
mscHtdsFramerRowStatusEntry = _MscHtdsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1, 1)
)
mscHtdsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerRowStatusEntry.setStatus("mandatory")
_MscHtdsFramerRowStatus_Type = RowStatus
_MscHtdsFramerRowStatus_Object = MibTableColumn
mscHtdsFramerRowStatus = _MscHtdsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1, 1, 1),
    _MscHtdsFramerRowStatus_Type()
)
mscHtdsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerRowStatus.setStatus("mandatory")
_MscHtdsFramerComponentName_Type = DisplayString
_MscHtdsFramerComponentName_Object = MibTableColumn
mscHtdsFramerComponentName = _MscHtdsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1, 1, 2),
    _MscHtdsFramerComponentName_Type()
)
mscHtdsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerComponentName.setStatus("mandatory")
_MscHtdsFramerStorageType_Type = StorageType
_MscHtdsFramerStorageType_Object = MibTableColumn
mscHtdsFramerStorageType = _MscHtdsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1, 1, 4),
    _MscHtdsFramerStorageType_Type()
)
mscHtdsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerStorageType.setStatus("mandatory")
_MscHtdsFramerIndex_Type = NonReplicated
_MscHtdsFramerIndex_Object = MibTableColumn
mscHtdsFramerIndex = _MscHtdsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 1, 1, 10),
    _MscHtdsFramerIndex_Type()
)
mscHtdsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHtdsFramerIndex.setStatus("mandatory")
_MscHtdsFramerProvTable_Object = MibTable
mscHtdsFramerProvTable = _MscHtdsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 10)
)
if mibBuilder.loadTexts:
    mscHtdsFramerProvTable.setStatus("mandatory")
_MscHtdsFramerProvEntry_Object = MibTableRow
mscHtdsFramerProvEntry = _MscHtdsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 10, 1)
)
mscHtdsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerProvEntry.setStatus("mandatory")
_MscHtdsFramerInterfaceName_Type = Link
_MscHtdsFramerInterfaceName_Object = MibTableColumn
mscHtdsFramerInterfaceName = _MscHtdsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 10, 1, 1),
    _MscHtdsFramerInterfaceName_Type()
)
mscHtdsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerInterfaceName.setStatus("mandatory")
_MscHtdsFramerLinkTable_Object = MibTable
mscHtdsFramerLinkTable = _MscHtdsFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11)
)
if mibBuilder.loadTexts:
    mscHtdsFramerLinkTable.setStatus("mandatory")
_MscHtdsFramerLinkEntry_Object = MibTableRow
mscHtdsFramerLinkEntry = _MscHtdsFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1)
)
mscHtdsFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerLinkEntry.setStatus("mandatory")


class _MscHtdsFramerDataInversion_Type(Integer32):
    """Custom type mscHtdsFramerDataInversion based on Integer32"""
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


_MscHtdsFramerDataInversion_Type.__name__ = "Integer32"
_MscHtdsFramerDataInversion_Object = MibTableColumn
mscHtdsFramerDataInversion = _MscHtdsFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1, 2),
    _MscHtdsFramerDataInversion_Type()
)
mscHtdsFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerDataInversion.setStatus("mandatory")


class _MscHtdsFramerNonOctetData_Type(Integer32):
    """Custom type mscHtdsFramerNonOctetData based on Integer32"""
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


_MscHtdsFramerNonOctetData_Type.__name__ = "Integer32"
_MscHtdsFramerNonOctetData_Object = MibTableColumn
mscHtdsFramerNonOctetData = _MscHtdsFramerNonOctetData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1, 3),
    _MscHtdsFramerNonOctetData_Type()
)
mscHtdsFramerNonOctetData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerNonOctetData.setStatus("mandatory")


class _MscHtdsFramerFrameCrcType_Type(Integer32):
    """Custom type mscHtdsFramerFrameCrcType based on Integer32"""
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


_MscHtdsFramerFrameCrcType_Type.__name__ = "Integer32"
_MscHtdsFramerFrameCrcType_Object = MibTableColumn
mscHtdsFramerFrameCrcType = _MscHtdsFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1, 4),
    _MscHtdsFramerFrameCrcType_Type()
)
mscHtdsFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerFrameCrcType.setStatus("mandatory")


class _MscHtdsFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscHtdsFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscHtdsFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscHtdsFramerFlagsBetweenFrames_Object = MibTableColumn
mscHtdsFramerFlagsBetweenFrames = _MscHtdsFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1, 5),
    _MscHtdsFramerFlagsBetweenFrames_Type()
)
mscHtdsFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerFlagsBetweenFrames.setStatus("mandatory")


class _MscHtdsFramerLineSignalTransport_Type(Integer32):
    """Custom type mscHtdsFramerLineSignalTransport based on Integer32"""
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


_MscHtdsFramerLineSignalTransport_Type.__name__ = "Integer32"
_MscHtdsFramerLineSignalTransport_Object = MibTableColumn
mscHtdsFramerLineSignalTransport = _MscHtdsFramerLineSignalTransport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 11, 1, 8),
    _MscHtdsFramerLineSignalTransport_Type()
)
mscHtdsFramerLineSignalTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsFramerLineSignalTransport.setStatus("mandatory")
_MscHtdsFramerStateTable_Object = MibTable
mscHtdsFramerStateTable = _MscHtdsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 12)
)
if mibBuilder.loadTexts:
    mscHtdsFramerStateTable.setStatus("mandatory")
_MscHtdsFramerStateEntry_Object = MibTableRow
mscHtdsFramerStateEntry = _MscHtdsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 12, 1)
)
mscHtdsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerStateEntry.setStatus("mandatory")


class _MscHtdsFramerAdminState_Type(Integer32):
    """Custom type mscHtdsFramerAdminState based on Integer32"""
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


_MscHtdsFramerAdminState_Type.__name__ = "Integer32"
_MscHtdsFramerAdminState_Object = MibTableColumn
mscHtdsFramerAdminState = _MscHtdsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 12, 1, 1),
    _MscHtdsFramerAdminState_Type()
)
mscHtdsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerAdminState.setStatus("mandatory")


class _MscHtdsFramerOperationalState_Type(Integer32):
    """Custom type mscHtdsFramerOperationalState based on Integer32"""
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


_MscHtdsFramerOperationalState_Type.__name__ = "Integer32"
_MscHtdsFramerOperationalState_Object = MibTableColumn
mscHtdsFramerOperationalState = _MscHtdsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 12, 1, 2),
    _MscHtdsFramerOperationalState_Type()
)
mscHtdsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerOperationalState.setStatus("mandatory")


class _MscHtdsFramerUsageState_Type(Integer32):
    """Custom type mscHtdsFramerUsageState based on Integer32"""
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


_MscHtdsFramerUsageState_Type.__name__ = "Integer32"
_MscHtdsFramerUsageState_Object = MibTableColumn
mscHtdsFramerUsageState = _MscHtdsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 12, 1, 3),
    _MscHtdsFramerUsageState_Type()
)
mscHtdsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerUsageState.setStatus("mandatory")
_MscHtdsFramerStatsTable_Object = MibTable
mscHtdsFramerStatsTable = _MscHtdsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13)
)
if mibBuilder.loadTexts:
    mscHtdsFramerStatsTable.setStatus("mandatory")
_MscHtdsFramerStatsEntry_Object = MibTableRow
mscHtdsFramerStatsEntry = _MscHtdsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1)
)
mscHtdsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerStatsEntry.setStatus("mandatory")
_MscHtdsFramerFrmToIf_Type = Counter32
_MscHtdsFramerFrmToIf_Object = MibTableColumn
mscHtdsFramerFrmToIf = _MscHtdsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 1),
    _MscHtdsFramerFrmToIf_Type()
)
mscHtdsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerFrmToIf.setStatus("mandatory")
_MscHtdsFramerFrmFromIf_Type = Counter32
_MscHtdsFramerFrmFromIf_Object = MibTableColumn
mscHtdsFramerFrmFromIf = _MscHtdsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 2),
    _MscHtdsFramerFrmFromIf_Type()
)
mscHtdsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerFrmFromIf.setStatus("mandatory")
_MscHtdsFramerOctetFromIf_Type = Counter32
_MscHtdsFramerOctetFromIf_Object = MibTableColumn
mscHtdsFramerOctetFromIf = _MscHtdsFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 3),
    _MscHtdsFramerOctetFromIf_Type()
)
mscHtdsFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerOctetFromIf.setStatus("mandatory")
_MscHtdsFramerAborts_Type = Counter32
_MscHtdsFramerAborts_Object = MibTableColumn
mscHtdsFramerAborts = _MscHtdsFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 4),
    _MscHtdsFramerAborts_Type()
)
mscHtdsFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerAborts.setStatus("mandatory")
_MscHtdsFramerCrcErrors_Type = Counter32
_MscHtdsFramerCrcErrors_Object = MibTableColumn
mscHtdsFramerCrcErrors = _MscHtdsFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 5),
    _MscHtdsFramerCrcErrors_Type()
)
mscHtdsFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerCrcErrors.setStatus("mandatory")
_MscHtdsFramerLrcErrors_Type = Counter32
_MscHtdsFramerLrcErrors_Object = MibTableColumn
mscHtdsFramerLrcErrors = _MscHtdsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 6),
    _MscHtdsFramerLrcErrors_Type()
)
mscHtdsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerLrcErrors.setStatus("mandatory")
_MscHtdsFramerNonOctetErrors_Type = Counter32
_MscHtdsFramerNonOctetErrors_Object = MibTableColumn
mscHtdsFramerNonOctetErrors = _MscHtdsFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 7),
    _MscHtdsFramerNonOctetErrors_Type()
)
mscHtdsFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerNonOctetErrors.setStatus("mandatory")
_MscHtdsFramerOverruns_Type = Counter32
_MscHtdsFramerOverruns_Object = MibTableColumn
mscHtdsFramerOverruns = _MscHtdsFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 8),
    _MscHtdsFramerOverruns_Type()
)
mscHtdsFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerOverruns.setStatus("mandatory")
_MscHtdsFramerUnderruns_Type = Counter32
_MscHtdsFramerUnderruns_Object = MibTableColumn
mscHtdsFramerUnderruns = _MscHtdsFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 9),
    _MscHtdsFramerUnderruns_Type()
)
mscHtdsFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerUnderruns.setStatus("mandatory")
_MscHtdsFramerLargeFrmErrors_Type = Counter32
_MscHtdsFramerLargeFrmErrors_Object = MibTableColumn
mscHtdsFramerLargeFrmErrors = _MscHtdsFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 13, 1, 10),
    _MscHtdsFramerLargeFrmErrors_Type()
)
mscHtdsFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerLargeFrmErrors.setStatus("mandatory")
_MscHtdsFramerUtilTable_Object = MibTable
mscHtdsFramerUtilTable = _MscHtdsFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 14)
)
if mibBuilder.loadTexts:
    mscHtdsFramerUtilTable.setStatus("mandatory")
_MscHtdsFramerUtilEntry_Object = MibTableRow
mscHtdsFramerUtilEntry = _MscHtdsFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 14, 1)
)
mscHtdsFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsFramerUtilEntry.setStatus("mandatory")


class _MscHtdsFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscHtdsFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscHtdsFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscHtdsFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscHtdsFramerNormPrioLinkUtilToIf = _MscHtdsFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 14, 1, 1),
    _MscHtdsFramerNormPrioLinkUtilToIf_Type()
)
mscHtdsFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscHtdsFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscHtdsFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscHtdsFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscHtdsFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscHtdsFramerNormPrioLinkUtilFromIf = _MscHtdsFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 2, 14, 1, 3),
    _MscHtdsFramerNormPrioLinkUtilFromIf_Type()
)
mscHtdsFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscHtdsPlc_ObjectIdentity = ObjectIdentity
mscHtdsPlc = _MscHtdsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3)
)
_MscHtdsPlcRowStatusTable_Object = MibTable
mscHtdsPlcRowStatusTable = _MscHtdsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1)
)
if mibBuilder.loadTexts:
    mscHtdsPlcRowStatusTable.setStatus("mandatory")
_MscHtdsPlcRowStatusEntry_Object = MibTableRow
mscHtdsPlcRowStatusEntry = _MscHtdsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1, 1)
)
mscHtdsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsPlcRowStatusEntry.setStatus("mandatory")
_MscHtdsPlcRowStatus_Type = RowStatus
_MscHtdsPlcRowStatus_Object = MibTableColumn
mscHtdsPlcRowStatus = _MscHtdsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1, 1, 1),
    _MscHtdsPlcRowStatus_Type()
)
mscHtdsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsPlcRowStatus.setStatus("mandatory")
_MscHtdsPlcComponentName_Type = DisplayString
_MscHtdsPlcComponentName_Object = MibTableColumn
mscHtdsPlcComponentName = _MscHtdsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1, 1, 2),
    _MscHtdsPlcComponentName_Type()
)
mscHtdsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsPlcComponentName.setStatus("mandatory")
_MscHtdsPlcStorageType_Type = StorageType
_MscHtdsPlcStorageType_Object = MibTableColumn
mscHtdsPlcStorageType = _MscHtdsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1, 1, 4),
    _MscHtdsPlcStorageType_Type()
)
mscHtdsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsPlcStorageType.setStatus("mandatory")
_MscHtdsPlcIndex_Type = NonReplicated
_MscHtdsPlcIndex_Object = MibTableColumn
mscHtdsPlcIndex = _MscHtdsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 1, 1, 10),
    _MscHtdsPlcIndex_Type()
)
mscHtdsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHtdsPlcIndex.setStatus("mandatory")
_MscHtdsPlcProvTable_Object = MibTable
mscHtdsPlcProvTable = _MscHtdsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10)
)
if mibBuilder.loadTexts:
    mscHtdsPlcProvTable.setStatus("mandatory")
_MscHtdsPlcProvEntry_Object = MibTableRow
mscHtdsPlcProvEntry = _MscHtdsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1)
)
mscHtdsPlcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsPlcProvEntry.setStatus("mandatory")


class _MscHtdsPlcRemoteName_Type(AsciiString):
    """Custom type mscHtdsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsPlcRemoteName_Type.__name__ = "AsciiString"
_MscHtdsPlcRemoteName_Object = MibTableColumn
mscHtdsPlcRemoteName = _MscHtdsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 2),
    _MscHtdsPlcRemoteName_Type()
)
mscHtdsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRemoteName.setStatus("mandatory")


class _MscHtdsPlcSetupPriority_Type(Unsigned32):
    """Custom type mscHtdsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscHtdsPlcSetupPriority_Type.__name__ = "Unsigned32"
_MscHtdsPlcSetupPriority_Object = MibTableColumn
mscHtdsPlcSetupPriority = _MscHtdsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 3),
    _MscHtdsPlcSetupPriority_Type()
)
mscHtdsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcSetupPriority.setStatus("mandatory")


class _MscHtdsPlcHoldingPriority_Type(Unsigned32):
    """Custom type mscHtdsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscHtdsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_MscHtdsPlcHoldingPriority_Object = MibTableColumn
mscHtdsPlcHoldingPriority = _MscHtdsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 4),
    _MscHtdsPlcHoldingPriority_Type()
)
mscHtdsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcHoldingPriority.setStatus("mandatory")


class _MscHtdsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscHtdsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscHtdsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscHtdsPlcRequiredTxBandwidth_Object = MibTableColumn
mscHtdsPlcRequiredTxBandwidth = _MscHtdsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 5),
    _MscHtdsPlcRequiredTxBandwidth_Type()
)
mscHtdsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRequiredTxBandwidth.setStatus("mandatory")


class _MscHtdsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscHtdsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscHtdsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscHtdsPlcRequiredRxBandwidth_Object = MibTableColumn
mscHtdsPlcRequiredRxBandwidth = _MscHtdsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 6),
    _MscHtdsPlcRequiredRxBandwidth_Type()
)
mscHtdsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRequiredRxBandwidth.setStatus("mandatory")


class _MscHtdsPlcRequiredTrafficType_Type(Integer32):
    """Custom type mscHtdsPlcRequiredTrafficType based on Integer32"""
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


_MscHtdsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_MscHtdsPlcRequiredTrafficType_Object = MibTableColumn
mscHtdsPlcRequiredTrafficType = _MscHtdsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 7),
    _MscHtdsPlcRequiredTrafficType_Type()
)
mscHtdsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRequiredTrafficType.setStatus("mandatory")


class _MscHtdsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type mscHtdsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscHtdsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscHtdsPlcPermittedTrunkTypes_Object = MibTableColumn
mscHtdsPlcPermittedTrunkTypes = _MscHtdsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 8),
    _MscHtdsPlcPermittedTrunkTypes_Type()
)
mscHtdsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcPermittedTrunkTypes.setStatus("mandatory")


class _MscHtdsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type mscHtdsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscHtdsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_MscHtdsPlcRequiredSecurity_Object = MibTableColumn
mscHtdsPlcRequiredSecurity = _MscHtdsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 9),
    _MscHtdsPlcRequiredSecurity_Type()
)
mscHtdsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRequiredSecurity.setStatus("mandatory")


class _MscHtdsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscHtdsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscHtdsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscHtdsPlcRequiredCustomerParm_Object = MibTableColumn
mscHtdsPlcRequiredCustomerParm = _MscHtdsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 10),
    _MscHtdsPlcRequiredCustomerParm_Type()
)
mscHtdsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcRequiredCustomerParm.setStatus("mandatory")


class _MscHtdsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type mscHtdsPlcPathAttributeToMinimize based on Integer32"""
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


_MscHtdsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscHtdsPlcPathAttributeToMinimize_Object = MibTableColumn
mscHtdsPlcPathAttributeToMinimize = _MscHtdsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 11),
    _MscHtdsPlcPathAttributeToMinimize_Type()
)
mscHtdsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcPathAttributeToMinimize.setStatus("mandatory")


class _MscHtdsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscHtdsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscHtdsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscHtdsPlcMaximumAcceptableCost_Object = MibTableColumn
mscHtdsPlcMaximumAcceptableCost = _MscHtdsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 12),
    _MscHtdsPlcMaximumAcceptableCost_Type()
)
mscHtdsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcMaximumAcceptableCost.setStatus("mandatory")


class _MscHtdsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscHtdsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscHtdsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscHtdsPlcMaximumAcceptableDelay_Object = MibTableColumn
mscHtdsPlcMaximumAcceptableDelay = _MscHtdsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 13),
    _MscHtdsPlcMaximumAcceptableDelay_Type()
)
mscHtdsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _MscHtdsPlcEmissionPriority_Type(Unsigned32):
    """Custom type mscHtdsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MscHtdsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_MscHtdsPlcEmissionPriority_Object = MibTableColumn
mscHtdsPlcEmissionPriority = _MscHtdsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 14),
    _MscHtdsPlcEmissionPriority_Type()
)
mscHtdsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcEmissionPriority.setStatus("mandatory")


class _MscHtdsPlcDiscardPriority_Type(Unsigned32):
    """Custom type mscHtdsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscHtdsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_MscHtdsPlcDiscardPriority_Object = MibTableColumn
mscHtdsPlcDiscardPriority = _MscHtdsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 15),
    _MscHtdsPlcDiscardPriority_Type()
)
mscHtdsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcDiscardPriority.setStatus("mandatory")


class _MscHtdsPlcPathType_Type(Integer32):
    """Custom type mscHtdsPlcPathType based on Integer32"""
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


_MscHtdsPlcPathType_Type.__name__ = "Integer32"
_MscHtdsPlcPathType_Object = MibTableColumn
mscHtdsPlcPathType = _MscHtdsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 16),
    _MscHtdsPlcPathType_Type()
)
mscHtdsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcPathType.setStatus("mandatory")


class _MscHtdsPlcPathFailureAction_Type(Integer32):
    """Custom type mscHtdsPlcPathFailureAction based on Integer32"""
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


_MscHtdsPlcPathFailureAction_Type.__name__ = "Integer32"
_MscHtdsPlcPathFailureAction_Object = MibTableColumn
mscHtdsPlcPathFailureAction = _MscHtdsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 17),
    _MscHtdsPlcPathFailureAction_Type()
)
mscHtdsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcPathFailureAction.setStatus("mandatory")


class _MscHtdsPlcBumpPreference_Type(Integer32):
    """Custom type mscHtdsPlcBumpPreference based on Integer32"""
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


_MscHtdsPlcBumpPreference_Type.__name__ = "Integer32"
_MscHtdsPlcBumpPreference_Object = MibTableColumn
mscHtdsPlcBumpPreference = _MscHtdsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 18),
    _MscHtdsPlcBumpPreference_Type()
)
mscHtdsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcBumpPreference.setStatus("mandatory")


class _MscHtdsPlcOptimization_Type(Integer32):
    """Custom type mscHtdsPlcOptimization based on Integer32"""
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


_MscHtdsPlcOptimization_Type.__name__ = "Integer32"
_MscHtdsPlcOptimization_Object = MibTableColumn
mscHtdsPlcOptimization = _MscHtdsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 19),
    _MscHtdsPlcOptimization_Type()
)
mscHtdsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcOptimization.setStatus("mandatory")


class _MscHtdsPlcAddressToCall_Type(AsciiString):
    """Custom type mscHtdsPlcAddressToCall based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsPlcAddressToCall_Type.__name__ = "AsciiString"
_MscHtdsPlcAddressToCall_Object = MibTableColumn
mscHtdsPlcAddressToCall = _MscHtdsPlcAddressToCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 20),
    _MscHtdsPlcAddressToCall_Type()
)
mscHtdsPlcAddressToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcAddressToCall.setStatus("mandatory")


class _MscHtdsPlcLocalAddress_Type(AsciiString):
    """Custom type mscHtdsPlcLocalAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsPlcLocalAddress_Type.__name__ = "AsciiString"
_MscHtdsPlcLocalAddress_Object = MibTableColumn
mscHtdsPlcLocalAddress = _MscHtdsPlcLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 21),
    _MscHtdsPlcLocalAddress_Type()
)
mscHtdsPlcLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcLocalAddress.setStatus("mandatory")


class _MscHtdsPlcMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type mscHtdsPlcMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscHtdsPlcMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_MscHtdsPlcMaximumAcceptableGatewayCost_Object = MibTableColumn
mscHtdsPlcMaximumAcceptableGatewayCost = _MscHtdsPlcMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 10, 1, 22),
    _MscHtdsPlcMaximumAcceptableGatewayCost_Type()
)
mscHtdsPlcMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcMaximumAcceptableGatewayCost.setStatus("mandatory")
_MscHtdsPlcMpathTable_Object = MibTable
mscHtdsPlcMpathTable = _MscHtdsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 265)
)
if mibBuilder.loadTexts:
    mscHtdsPlcMpathTable.setStatus("mandatory")
_MscHtdsPlcMpathEntry_Object = MibTableRow
mscHtdsPlcMpathEntry = _MscHtdsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 265, 1)
)
mscHtdsPlcMpathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsPlcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsPlcMpathEntry.setStatus("mandatory")


class _MscHtdsPlcMpathIndex_Type(Integer32):
    """Custom type mscHtdsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscHtdsPlcMpathIndex_Type.__name__ = "Integer32"
_MscHtdsPlcMpathIndex_Object = MibTableColumn
mscHtdsPlcMpathIndex = _MscHtdsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 265, 1, 1),
    _MscHtdsPlcMpathIndex_Type()
)
mscHtdsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHtdsPlcMpathIndex.setStatus("mandatory")


class _MscHtdsPlcMpathValue_Type(AsciiString):
    """Custom type mscHtdsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsPlcMpathValue_Type.__name__ = "AsciiString"
_MscHtdsPlcMpathValue_Object = MibTableColumn
mscHtdsPlcMpathValue = _MscHtdsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 3, 265, 1, 2),
    _MscHtdsPlcMpathValue_Type()
)
mscHtdsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsPlcMpathValue.setStatus("mandatory")
_MscHtdsLCo_ObjectIdentity = ObjectIdentity
mscHtdsLCo = _MscHtdsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4)
)
_MscHtdsLCoRowStatusTable_Object = MibTable
mscHtdsLCoRowStatusTable = _MscHtdsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1)
)
if mibBuilder.loadTexts:
    mscHtdsLCoRowStatusTable.setStatus("mandatory")
_MscHtdsLCoRowStatusEntry_Object = MibTableRow
mscHtdsLCoRowStatusEntry = _MscHtdsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1, 1)
)
mscHtdsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsLCoRowStatusEntry.setStatus("mandatory")
_MscHtdsLCoRowStatus_Type = RowStatus
_MscHtdsLCoRowStatus_Object = MibTableColumn
mscHtdsLCoRowStatus = _MscHtdsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1, 1, 1),
    _MscHtdsLCoRowStatus_Type()
)
mscHtdsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRowStatus.setStatus("mandatory")
_MscHtdsLCoComponentName_Type = DisplayString
_MscHtdsLCoComponentName_Object = MibTableColumn
mscHtdsLCoComponentName = _MscHtdsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1, 1, 2),
    _MscHtdsLCoComponentName_Type()
)
mscHtdsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoComponentName.setStatus("mandatory")
_MscHtdsLCoStorageType_Type = StorageType
_MscHtdsLCoStorageType_Object = MibTableColumn
mscHtdsLCoStorageType = _MscHtdsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1, 1, 4),
    _MscHtdsLCoStorageType_Type()
)
mscHtdsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoStorageType.setStatus("mandatory")
_MscHtdsLCoIndex_Type = NonReplicated
_MscHtdsLCoIndex_Object = MibTableColumn
mscHtdsLCoIndex = _MscHtdsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 1, 1, 10),
    _MscHtdsLCoIndex_Type()
)
mscHtdsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscHtdsLCoIndex.setStatus("mandatory")
_MscHtdsLCoPathDataTable_Object = MibTable
mscHtdsLCoPathDataTable = _MscHtdsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10)
)
if mibBuilder.loadTexts:
    mscHtdsLCoPathDataTable.setStatus("mandatory")
_MscHtdsLCoPathDataEntry_Object = MibTableRow
mscHtdsLCoPathDataEntry = _MscHtdsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1)
)
mscHtdsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsLCoPathDataEntry.setStatus("mandatory")


class _MscHtdsLCoState_Type(Integer32):
    """Custom type mscHtdsLCoState based on Integer32"""
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


_MscHtdsLCoState_Type.__name__ = "Integer32"
_MscHtdsLCoState_Object = MibTableColumn
mscHtdsLCoState = _MscHtdsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 1),
    _MscHtdsLCoState_Type()
)
mscHtdsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoState.setStatus("mandatory")


class _MscHtdsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscHtdsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscHtdsLCoOverrideRemoteName_Object = MibTableColumn
mscHtdsLCoOverrideRemoteName = _MscHtdsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 2),
    _MscHtdsLCoOverrideRemoteName_Type()
)
mscHtdsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsLCoOverrideRemoteName.setStatus("mandatory")


class _MscHtdsLCoEnd_Type(Integer32):
    """Custom type mscHtdsLCoEnd based on Integer32"""
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


_MscHtdsLCoEnd_Type.__name__ = "Integer32"
_MscHtdsLCoEnd_Object = MibTableColumn
mscHtdsLCoEnd = _MscHtdsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 3),
    _MscHtdsLCoEnd_Type()
)
mscHtdsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoEnd.setStatus("mandatory")


class _MscHtdsLCoCostMetric_Type(Unsigned32):
    """Custom type mscHtdsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscHtdsLCoCostMetric_Type.__name__ = "Unsigned32"
_MscHtdsLCoCostMetric_Object = MibTableColumn
mscHtdsLCoCostMetric = _MscHtdsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 4),
    _MscHtdsLCoCostMetric_Type()
)
mscHtdsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoCostMetric.setStatus("mandatory")


class _MscHtdsLCoDelayMetric_Type(Unsigned32):
    """Custom type mscHtdsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscHtdsLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscHtdsLCoDelayMetric_Object = MibTableColumn
mscHtdsLCoDelayMetric = _MscHtdsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 5),
    _MscHtdsLCoDelayMetric_Type()
)
mscHtdsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoDelayMetric.setStatus("mandatory")


class _MscHtdsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscHtdsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscHtdsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscHtdsLCoRoundTripDelay_Object = MibTableColumn
mscHtdsLCoRoundTripDelay = _MscHtdsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 6),
    _MscHtdsLCoRoundTripDelay_Type()
)
mscHtdsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRoundTripDelay.setStatus("mandatory")


class _MscHtdsLCoSetupPriority_Type(Unsigned32):
    """Custom type mscHtdsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscHtdsLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscHtdsLCoSetupPriority_Object = MibTableColumn
mscHtdsLCoSetupPriority = _MscHtdsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 7),
    _MscHtdsLCoSetupPriority_Type()
)
mscHtdsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoSetupPriority.setStatus("mandatory")


class _MscHtdsLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscHtdsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscHtdsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscHtdsLCoHoldingPriority_Object = MibTableColumn
mscHtdsLCoHoldingPriority = _MscHtdsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 8),
    _MscHtdsLCoHoldingPriority_Type()
)
mscHtdsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoHoldingPriority.setStatus("mandatory")


class _MscHtdsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscHtdsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscHtdsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscHtdsLCoRequiredTxBandwidth_Object = MibTableColumn
mscHtdsLCoRequiredTxBandwidth = _MscHtdsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 9),
    _MscHtdsLCoRequiredTxBandwidth_Type()
)
mscHtdsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscHtdsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscHtdsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscHtdsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscHtdsLCoRequiredRxBandwidth_Object = MibTableColumn
mscHtdsLCoRequiredRxBandwidth = _MscHtdsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 10),
    _MscHtdsLCoRequiredRxBandwidth_Type()
)
mscHtdsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscHtdsLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscHtdsLCoRequiredTrafficType based on Integer32"""
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


_MscHtdsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscHtdsLCoRequiredTrafficType_Object = MibTableColumn
mscHtdsLCoRequiredTrafficType = _MscHtdsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 11),
    _MscHtdsLCoRequiredTrafficType_Type()
)
mscHtdsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRequiredTrafficType.setStatus("mandatory")


class _MscHtdsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscHtdsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscHtdsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscHtdsLCoPermittedTrunkTypes_Object = MibTableColumn
mscHtdsLCoPermittedTrunkTypes = _MscHtdsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 12),
    _MscHtdsLCoPermittedTrunkTypes_Type()
)
mscHtdsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscHtdsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscHtdsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscHtdsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscHtdsLCoRequiredSecurity_Object = MibTableColumn
mscHtdsLCoRequiredSecurity = _MscHtdsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 13),
    _MscHtdsLCoRequiredSecurity_Type()
)
mscHtdsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRequiredSecurity.setStatus("mandatory")


class _MscHtdsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscHtdsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscHtdsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscHtdsLCoRequiredCustomerParameter_Object = MibTableColumn
mscHtdsLCoRequiredCustomerParameter = _MscHtdsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 14),
    _MscHtdsLCoRequiredCustomerParameter_Type()
)
mscHtdsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscHtdsLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscHtdsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscHtdsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscHtdsLCoEmissionPriority_Object = MibTableColumn
mscHtdsLCoEmissionPriority = _MscHtdsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 15),
    _MscHtdsLCoEmissionPriority_Type()
)
mscHtdsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoEmissionPriority.setStatus("mandatory")


class _MscHtdsLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscHtdsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscHtdsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscHtdsLCoDiscardPriority_Object = MibTableColumn
mscHtdsLCoDiscardPriority = _MscHtdsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 16),
    _MscHtdsLCoDiscardPriority_Type()
)
mscHtdsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoDiscardPriority.setStatus("mandatory")


class _MscHtdsLCoPathType_Type(Integer32):
    """Custom type mscHtdsLCoPathType based on Integer32"""
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


_MscHtdsLCoPathType_Type.__name__ = "Integer32"
_MscHtdsLCoPathType_Object = MibTableColumn
mscHtdsLCoPathType = _MscHtdsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 17),
    _MscHtdsLCoPathType_Type()
)
mscHtdsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPathType.setStatus("mandatory")


class _MscHtdsLCoRetryCount_Type(Unsigned32):
    """Custom type mscHtdsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscHtdsLCoRetryCount_Type.__name__ = "Unsigned32"
_MscHtdsLCoRetryCount_Object = MibTableColumn
mscHtdsLCoRetryCount = _MscHtdsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 18),
    _MscHtdsLCoRetryCount_Type()
)
mscHtdsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoRetryCount.setStatus("mandatory")


class _MscHtdsLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscHtdsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscHtdsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscHtdsLCoPathFailureCount_Object = MibTableColumn
mscHtdsLCoPathFailureCount = _MscHtdsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 19),
    _MscHtdsLCoPathFailureCount_Type()
)
mscHtdsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPathFailureCount.setStatus("mandatory")


class _MscHtdsLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscHtdsLCoReasonForNoRoute based on Integer32"""
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


_MscHtdsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscHtdsLCoReasonForNoRoute_Object = MibTableColumn
mscHtdsLCoReasonForNoRoute = _MscHtdsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 20),
    _MscHtdsLCoReasonForNoRoute_Type()
)
mscHtdsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoReasonForNoRoute.setStatus("mandatory")


class _MscHtdsLCoLastTearDownReason_Type(Integer32):
    """Custom type mscHtdsLCoLastTearDownReason based on Integer32"""
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


_MscHtdsLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscHtdsLCoLastTearDownReason_Object = MibTableColumn
mscHtdsLCoLastTearDownReason = _MscHtdsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 21),
    _MscHtdsLCoLastTearDownReason_Type()
)
mscHtdsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoLastTearDownReason.setStatus("mandatory")


class _MscHtdsLCoPathFailureAction_Type(Integer32):
    """Custom type mscHtdsLCoPathFailureAction based on Integer32"""
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


_MscHtdsLCoPathFailureAction_Type.__name__ = "Integer32"
_MscHtdsLCoPathFailureAction_Object = MibTableColumn
mscHtdsLCoPathFailureAction = _MscHtdsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 22),
    _MscHtdsLCoPathFailureAction_Type()
)
mscHtdsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPathFailureAction.setStatus("mandatory")


class _MscHtdsLCoBumpPreference_Type(Integer32):
    """Custom type mscHtdsLCoBumpPreference based on Integer32"""
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


_MscHtdsLCoBumpPreference_Type.__name__ = "Integer32"
_MscHtdsLCoBumpPreference_Object = MibTableColumn
mscHtdsLCoBumpPreference = _MscHtdsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 23),
    _MscHtdsLCoBumpPreference_Type()
)
mscHtdsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoBumpPreference.setStatus("mandatory")


class _MscHtdsLCoOptimization_Type(Integer32):
    """Custom type mscHtdsLCoOptimization based on Integer32"""
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


_MscHtdsLCoOptimization_Type.__name__ = "Integer32"
_MscHtdsLCoOptimization_Object = MibTableColumn
mscHtdsLCoOptimization = _MscHtdsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 24),
    _MscHtdsLCoOptimization_Type()
)
mscHtdsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoOptimization.setStatus("mandatory")


class _MscHtdsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscHtdsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscHtdsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscHtdsLCoPathUpDateTime_Object = MibTableColumn
mscHtdsLCoPathUpDateTime = _MscHtdsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 10, 1, 25),
    _MscHtdsLCoPathUpDateTime_Type()
)
mscHtdsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPathUpDateTime.setStatus("mandatory")
_MscHtdsLCoStatsTable_Object = MibTable
mscHtdsLCoStatsTable = _MscHtdsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11)
)
if mibBuilder.loadTexts:
    mscHtdsLCoStatsTable.setStatus("mandatory")
_MscHtdsLCoStatsEntry_Object = MibTableRow
mscHtdsLCoStatsEntry = _MscHtdsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11, 1)
)
mscHtdsLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsLCoStatsEntry.setStatus("mandatory")
_MscHtdsLCoPktsToNetwork_Type = PassportCounter64
_MscHtdsLCoPktsToNetwork_Object = MibTableColumn
mscHtdsLCoPktsToNetwork = _MscHtdsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11, 1, 1),
    _MscHtdsLCoPktsToNetwork_Type()
)
mscHtdsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPktsToNetwork.setStatus("mandatory")
_MscHtdsLCoBytesToNetwork_Type = PassportCounter64
_MscHtdsLCoBytesToNetwork_Object = MibTableColumn
mscHtdsLCoBytesToNetwork = _MscHtdsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11, 1, 2),
    _MscHtdsLCoBytesToNetwork_Type()
)
mscHtdsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoBytesToNetwork.setStatus("mandatory")
_MscHtdsLCoPktsFromNetwork_Type = PassportCounter64
_MscHtdsLCoPktsFromNetwork_Object = MibTableColumn
mscHtdsLCoPktsFromNetwork = _MscHtdsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11, 1, 3),
    _MscHtdsLCoPktsFromNetwork_Type()
)
mscHtdsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPktsFromNetwork.setStatus("mandatory")
_MscHtdsLCoBytesFromNetwork_Type = PassportCounter64
_MscHtdsLCoBytesFromNetwork_Object = MibTableColumn
mscHtdsLCoBytesFromNetwork = _MscHtdsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 11, 1, 4),
    _MscHtdsLCoBytesFromNetwork_Type()
)
mscHtdsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoBytesFromNetwork.setStatus("mandatory")
_MscHtdsLCoPathTable_Object = MibTable
mscHtdsLCoPathTable = _MscHtdsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 264)
)
if mibBuilder.loadTexts:
    mscHtdsLCoPathTable.setStatus("mandatory")
_MscHtdsLCoPathEntry_Object = MibTableRow
mscHtdsLCoPathEntry = _MscHtdsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 264, 1)
)
mscHtdsLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscHtdsLCoPathEntry.setStatus("mandatory")


class _MscHtdsLCoPathValue_Type(AsciiString):
    """Custom type mscHtdsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscHtdsLCoPathValue_Type.__name__ = "AsciiString"
_MscHtdsLCoPathValue_Object = MibTableColumn
mscHtdsLCoPathValue = _MscHtdsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 4, 264, 1, 1),
    _MscHtdsLCoPathValue_Type()
)
mscHtdsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsLCoPathValue.setStatus("mandatory")
_MscHtdsCidDataTable_Object = MibTable
mscHtdsCidDataTable = _MscHtdsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 10)
)
if mibBuilder.loadTexts:
    mscHtdsCidDataTable.setStatus("mandatory")
_MscHtdsCidDataEntry_Object = MibTableRow
mscHtdsCidDataEntry = _MscHtdsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 10, 1)
)
mscHtdsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsCidDataEntry.setStatus("mandatory")


class _MscHtdsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscHtdsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscHtdsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscHtdsCustomerIdentifier_Object = MibTableColumn
mscHtdsCustomerIdentifier = _MscHtdsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 10, 1, 1),
    _MscHtdsCustomerIdentifier_Type()
)
mscHtdsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsCustomerIdentifier.setStatus("mandatory")
_MscHtdsIfEntryTable_Object = MibTable
mscHtdsIfEntryTable = _MscHtdsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 11)
)
if mibBuilder.loadTexts:
    mscHtdsIfEntryTable.setStatus("mandatory")
_MscHtdsIfEntryEntry_Object = MibTableRow
mscHtdsIfEntryEntry = _MscHtdsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 11, 1)
)
mscHtdsIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsIfEntryEntry.setStatus("mandatory")


class _MscHtdsIfAdminStatus_Type(Integer32):
    """Custom type mscHtdsIfAdminStatus based on Integer32"""
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


_MscHtdsIfAdminStatus_Type.__name__ = "Integer32"
_MscHtdsIfAdminStatus_Object = MibTableColumn
mscHtdsIfAdminStatus = _MscHtdsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 11, 1, 1),
    _MscHtdsIfAdminStatus_Type()
)
mscHtdsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscHtdsIfAdminStatus.setStatus("mandatory")


class _MscHtdsIfIndex_Type(InterfaceIndex):
    """Custom type mscHtdsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscHtdsIfIndex_Type.__name__ = "InterfaceIndex"
_MscHtdsIfIndex_Object = MibTableColumn
mscHtdsIfIndex = _MscHtdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 11, 1, 2),
    _MscHtdsIfIndex_Type()
)
mscHtdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsIfIndex.setStatus("mandatory")
_MscHtdsOperStatusTable_Object = MibTable
mscHtdsOperStatusTable = _MscHtdsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 12)
)
if mibBuilder.loadTexts:
    mscHtdsOperStatusTable.setStatus("mandatory")
_MscHtdsOperStatusEntry_Object = MibTableRow
mscHtdsOperStatusEntry = _MscHtdsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 12, 1)
)
mscHtdsOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsOperStatusEntry.setStatus("mandatory")


class _MscHtdsSnmpOperStatus_Type(Integer32):
    """Custom type mscHtdsSnmpOperStatus based on Integer32"""
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


_MscHtdsSnmpOperStatus_Type.__name__ = "Integer32"
_MscHtdsSnmpOperStatus_Object = MibTableColumn
mscHtdsSnmpOperStatus = _MscHtdsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 12, 1, 1),
    _MscHtdsSnmpOperStatus_Type()
)
mscHtdsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsSnmpOperStatus.setStatus("mandatory")
_MscHtdsStateTable_Object = MibTable
mscHtdsStateTable = _MscHtdsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13)
)
if mibBuilder.loadTexts:
    mscHtdsStateTable.setStatus("mandatory")
_MscHtdsStateEntry_Object = MibTableRow
mscHtdsStateEntry = _MscHtdsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1)
)
mscHtdsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB", "mscHtdsIndex"),
)
if mibBuilder.loadTexts:
    mscHtdsStateEntry.setStatus("mandatory")


class _MscHtdsAdminState_Type(Integer32):
    """Custom type mscHtdsAdminState based on Integer32"""
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


_MscHtdsAdminState_Type.__name__ = "Integer32"
_MscHtdsAdminState_Object = MibTableColumn
mscHtdsAdminState = _MscHtdsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 1),
    _MscHtdsAdminState_Type()
)
mscHtdsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsAdminState.setStatus("mandatory")


class _MscHtdsOperationalState_Type(Integer32):
    """Custom type mscHtdsOperationalState based on Integer32"""
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


_MscHtdsOperationalState_Type.__name__ = "Integer32"
_MscHtdsOperationalState_Object = MibTableColumn
mscHtdsOperationalState = _MscHtdsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 2),
    _MscHtdsOperationalState_Type()
)
mscHtdsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsOperationalState.setStatus("mandatory")


class _MscHtdsUsageState_Type(Integer32):
    """Custom type mscHtdsUsageState based on Integer32"""
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


_MscHtdsUsageState_Type.__name__ = "Integer32"
_MscHtdsUsageState_Object = MibTableColumn
mscHtdsUsageState = _MscHtdsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 3),
    _MscHtdsUsageState_Type()
)
mscHtdsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsUsageState.setStatus("mandatory")


class _MscHtdsAvailabilityStatus_Type(OctetString):
    """Custom type mscHtdsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscHtdsAvailabilityStatus_Type.__name__ = "OctetString"
_MscHtdsAvailabilityStatus_Object = MibTableColumn
mscHtdsAvailabilityStatus = _MscHtdsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 4),
    _MscHtdsAvailabilityStatus_Type()
)
mscHtdsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsAvailabilityStatus.setStatus("mandatory")


class _MscHtdsProceduralStatus_Type(OctetString):
    """Custom type mscHtdsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscHtdsProceduralStatus_Type.__name__ = "OctetString"
_MscHtdsProceduralStatus_Object = MibTableColumn
mscHtdsProceduralStatus = _MscHtdsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 5),
    _MscHtdsProceduralStatus_Type()
)
mscHtdsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsProceduralStatus.setStatus("mandatory")


class _MscHtdsControlStatus_Type(OctetString):
    """Custom type mscHtdsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscHtdsControlStatus_Type.__name__ = "OctetString"
_MscHtdsControlStatus_Object = MibTableColumn
mscHtdsControlStatus = _MscHtdsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 6),
    _MscHtdsControlStatus_Type()
)
mscHtdsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsControlStatus.setStatus("mandatory")


class _MscHtdsAlarmStatus_Type(OctetString):
    """Custom type mscHtdsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscHtdsAlarmStatus_Type.__name__ = "OctetString"
_MscHtdsAlarmStatus_Object = MibTableColumn
mscHtdsAlarmStatus = _MscHtdsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 7),
    _MscHtdsAlarmStatus_Type()
)
mscHtdsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsAlarmStatus.setStatus("mandatory")


class _MscHtdsStandbyStatus_Type(Integer32):
    """Custom type mscHtdsStandbyStatus based on Integer32"""
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


_MscHtdsStandbyStatus_Type.__name__ = "Integer32"
_MscHtdsStandbyStatus_Object = MibTableColumn
mscHtdsStandbyStatus = _MscHtdsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 8),
    _MscHtdsStandbyStatus_Type()
)
mscHtdsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsStandbyStatus.setStatus("mandatory")


class _MscHtdsUnknownStatus_Type(Integer32):
    """Custom type mscHtdsUnknownStatus based on Integer32"""
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


_MscHtdsUnknownStatus_Type.__name__ = "Integer32"
_MscHtdsUnknownStatus_Object = MibTableColumn
mscHtdsUnknownStatus = _MscHtdsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 82, 13, 1, 9),
    _MscHtdsUnknownStatus_Type()
)
mscHtdsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscHtdsUnknownStatus.setStatus("mandatory")
_HdlcTransparentMIB_ObjectIdentity = ObjectIdentity
hdlcTransparentMIB = _HdlcTransparentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47)
)
_HdlcTransparentGroup_ObjectIdentity = ObjectIdentity
hdlcTransparentGroup = _HdlcTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 1)
)
_HdlcTransparentGroupCA_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupCA = _HdlcTransparentGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 1, 1)
)
_HdlcTransparentGroupCA02_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupCA02 = _HdlcTransparentGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 1, 1, 3)
)
_HdlcTransparentGroupCA02A_ObjectIdentity = ObjectIdentity
hdlcTransparentGroupCA02A = _HdlcTransparentGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 1, 1, 3, 2)
)
_HdlcTransparentCapabilities_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilities = _HdlcTransparentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 3)
)
_HdlcTransparentCapabilitiesCA_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesCA = _HdlcTransparentCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 3, 1)
)
_HdlcTransparentCapabilitiesCA02_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesCA02 = _HdlcTransparentCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 3, 1, 3)
)
_HdlcTransparentCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
hdlcTransparentCapabilitiesCA02A = _HdlcTransparentCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 47, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-HdlcTransparentMIB",
    **{"mscHtds": mscHtds,
       "mscHtdsRowStatusTable": mscHtdsRowStatusTable,
       "mscHtdsRowStatusEntry": mscHtdsRowStatusEntry,
       "mscHtdsRowStatus": mscHtdsRowStatus,
       "mscHtdsComponentName": mscHtdsComponentName,
       "mscHtdsStorageType": mscHtdsStorageType,
       "mscHtdsIndex": mscHtdsIndex,
       "mscHtdsFramer": mscHtdsFramer,
       "mscHtdsFramerRowStatusTable": mscHtdsFramerRowStatusTable,
       "mscHtdsFramerRowStatusEntry": mscHtdsFramerRowStatusEntry,
       "mscHtdsFramerRowStatus": mscHtdsFramerRowStatus,
       "mscHtdsFramerComponentName": mscHtdsFramerComponentName,
       "mscHtdsFramerStorageType": mscHtdsFramerStorageType,
       "mscHtdsFramerIndex": mscHtdsFramerIndex,
       "mscHtdsFramerProvTable": mscHtdsFramerProvTable,
       "mscHtdsFramerProvEntry": mscHtdsFramerProvEntry,
       "mscHtdsFramerInterfaceName": mscHtdsFramerInterfaceName,
       "mscHtdsFramerLinkTable": mscHtdsFramerLinkTable,
       "mscHtdsFramerLinkEntry": mscHtdsFramerLinkEntry,
       "mscHtdsFramerDataInversion": mscHtdsFramerDataInversion,
       "mscHtdsFramerNonOctetData": mscHtdsFramerNonOctetData,
       "mscHtdsFramerFrameCrcType": mscHtdsFramerFrameCrcType,
       "mscHtdsFramerFlagsBetweenFrames": mscHtdsFramerFlagsBetweenFrames,
       "mscHtdsFramerLineSignalTransport": mscHtdsFramerLineSignalTransport,
       "mscHtdsFramerStateTable": mscHtdsFramerStateTable,
       "mscHtdsFramerStateEntry": mscHtdsFramerStateEntry,
       "mscHtdsFramerAdminState": mscHtdsFramerAdminState,
       "mscHtdsFramerOperationalState": mscHtdsFramerOperationalState,
       "mscHtdsFramerUsageState": mscHtdsFramerUsageState,
       "mscHtdsFramerStatsTable": mscHtdsFramerStatsTable,
       "mscHtdsFramerStatsEntry": mscHtdsFramerStatsEntry,
       "mscHtdsFramerFrmToIf": mscHtdsFramerFrmToIf,
       "mscHtdsFramerFrmFromIf": mscHtdsFramerFrmFromIf,
       "mscHtdsFramerOctetFromIf": mscHtdsFramerOctetFromIf,
       "mscHtdsFramerAborts": mscHtdsFramerAborts,
       "mscHtdsFramerCrcErrors": mscHtdsFramerCrcErrors,
       "mscHtdsFramerLrcErrors": mscHtdsFramerLrcErrors,
       "mscHtdsFramerNonOctetErrors": mscHtdsFramerNonOctetErrors,
       "mscHtdsFramerOverruns": mscHtdsFramerOverruns,
       "mscHtdsFramerUnderruns": mscHtdsFramerUnderruns,
       "mscHtdsFramerLargeFrmErrors": mscHtdsFramerLargeFrmErrors,
       "mscHtdsFramerUtilTable": mscHtdsFramerUtilTable,
       "mscHtdsFramerUtilEntry": mscHtdsFramerUtilEntry,
       "mscHtdsFramerNormPrioLinkUtilToIf": mscHtdsFramerNormPrioLinkUtilToIf,
       "mscHtdsFramerNormPrioLinkUtilFromIf": mscHtdsFramerNormPrioLinkUtilFromIf,
       "mscHtdsPlc": mscHtdsPlc,
       "mscHtdsPlcRowStatusTable": mscHtdsPlcRowStatusTable,
       "mscHtdsPlcRowStatusEntry": mscHtdsPlcRowStatusEntry,
       "mscHtdsPlcRowStatus": mscHtdsPlcRowStatus,
       "mscHtdsPlcComponentName": mscHtdsPlcComponentName,
       "mscHtdsPlcStorageType": mscHtdsPlcStorageType,
       "mscHtdsPlcIndex": mscHtdsPlcIndex,
       "mscHtdsPlcProvTable": mscHtdsPlcProvTable,
       "mscHtdsPlcProvEntry": mscHtdsPlcProvEntry,
       "mscHtdsPlcRemoteName": mscHtdsPlcRemoteName,
       "mscHtdsPlcSetupPriority": mscHtdsPlcSetupPriority,
       "mscHtdsPlcHoldingPriority": mscHtdsPlcHoldingPriority,
       "mscHtdsPlcRequiredTxBandwidth": mscHtdsPlcRequiredTxBandwidth,
       "mscHtdsPlcRequiredRxBandwidth": mscHtdsPlcRequiredRxBandwidth,
       "mscHtdsPlcRequiredTrafficType": mscHtdsPlcRequiredTrafficType,
       "mscHtdsPlcPermittedTrunkTypes": mscHtdsPlcPermittedTrunkTypes,
       "mscHtdsPlcRequiredSecurity": mscHtdsPlcRequiredSecurity,
       "mscHtdsPlcRequiredCustomerParm": mscHtdsPlcRequiredCustomerParm,
       "mscHtdsPlcPathAttributeToMinimize": mscHtdsPlcPathAttributeToMinimize,
       "mscHtdsPlcMaximumAcceptableCost": mscHtdsPlcMaximumAcceptableCost,
       "mscHtdsPlcMaximumAcceptableDelay": mscHtdsPlcMaximumAcceptableDelay,
       "mscHtdsPlcEmissionPriority": mscHtdsPlcEmissionPriority,
       "mscHtdsPlcDiscardPriority": mscHtdsPlcDiscardPriority,
       "mscHtdsPlcPathType": mscHtdsPlcPathType,
       "mscHtdsPlcPathFailureAction": mscHtdsPlcPathFailureAction,
       "mscHtdsPlcBumpPreference": mscHtdsPlcBumpPreference,
       "mscHtdsPlcOptimization": mscHtdsPlcOptimization,
       "mscHtdsPlcAddressToCall": mscHtdsPlcAddressToCall,
       "mscHtdsPlcLocalAddress": mscHtdsPlcLocalAddress,
       "mscHtdsPlcMaximumAcceptableGatewayCost": mscHtdsPlcMaximumAcceptableGatewayCost,
       "mscHtdsPlcMpathTable": mscHtdsPlcMpathTable,
       "mscHtdsPlcMpathEntry": mscHtdsPlcMpathEntry,
       "mscHtdsPlcMpathIndex": mscHtdsPlcMpathIndex,
       "mscHtdsPlcMpathValue": mscHtdsPlcMpathValue,
       "mscHtdsLCo": mscHtdsLCo,
       "mscHtdsLCoRowStatusTable": mscHtdsLCoRowStatusTable,
       "mscHtdsLCoRowStatusEntry": mscHtdsLCoRowStatusEntry,
       "mscHtdsLCoRowStatus": mscHtdsLCoRowStatus,
       "mscHtdsLCoComponentName": mscHtdsLCoComponentName,
       "mscHtdsLCoStorageType": mscHtdsLCoStorageType,
       "mscHtdsLCoIndex": mscHtdsLCoIndex,
       "mscHtdsLCoPathDataTable": mscHtdsLCoPathDataTable,
       "mscHtdsLCoPathDataEntry": mscHtdsLCoPathDataEntry,
       "mscHtdsLCoState": mscHtdsLCoState,
       "mscHtdsLCoOverrideRemoteName": mscHtdsLCoOverrideRemoteName,
       "mscHtdsLCoEnd": mscHtdsLCoEnd,
       "mscHtdsLCoCostMetric": mscHtdsLCoCostMetric,
       "mscHtdsLCoDelayMetric": mscHtdsLCoDelayMetric,
       "mscHtdsLCoRoundTripDelay": mscHtdsLCoRoundTripDelay,
       "mscHtdsLCoSetupPriority": mscHtdsLCoSetupPriority,
       "mscHtdsLCoHoldingPriority": mscHtdsLCoHoldingPriority,
       "mscHtdsLCoRequiredTxBandwidth": mscHtdsLCoRequiredTxBandwidth,
       "mscHtdsLCoRequiredRxBandwidth": mscHtdsLCoRequiredRxBandwidth,
       "mscHtdsLCoRequiredTrafficType": mscHtdsLCoRequiredTrafficType,
       "mscHtdsLCoPermittedTrunkTypes": mscHtdsLCoPermittedTrunkTypes,
       "mscHtdsLCoRequiredSecurity": mscHtdsLCoRequiredSecurity,
       "mscHtdsLCoRequiredCustomerParameter": mscHtdsLCoRequiredCustomerParameter,
       "mscHtdsLCoEmissionPriority": mscHtdsLCoEmissionPriority,
       "mscHtdsLCoDiscardPriority": mscHtdsLCoDiscardPriority,
       "mscHtdsLCoPathType": mscHtdsLCoPathType,
       "mscHtdsLCoRetryCount": mscHtdsLCoRetryCount,
       "mscHtdsLCoPathFailureCount": mscHtdsLCoPathFailureCount,
       "mscHtdsLCoReasonForNoRoute": mscHtdsLCoReasonForNoRoute,
       "mscHtdsLCoLastTearDownReason": mscHtdsLCoLastTearDownReason,
       "mscHtdsLCoPathFailureAction": mscHtdsLCoPathFailureAction,
       "mscHtdsLCoBumpPreference": mscHtdsLCoBumpPreference,
       "mscHtdsLCoOptimization": mscHtdsLCoOptimization,
       "mscHtdsLCoPathUpDateTime": mscHtdsLCoPathUpDateTime,
       "mscHtdsLCoStatsTable": mscHtdsLCoStatsTable,
       "mscHtdsLCoStatsEntry": mscHtdsLCoStatsEntry,
       "mscHtdsLCoPktsToNetwork": mscHtdsLCoPktsToNetwork,
       "mscHtdsLCoBytesToNetwork": mscHtdsLCoBytesToNetwork,
       "mscHtdsLCoPktsFromNetwork": mscHtdsLCoPktsFromNetwork,
       "mscHtdsLCoBytesFromNetwork": mscHtdsLCoBytesFromNetwork,
       "mscHtdsLCoPathTable": mscHtdsLCoPathTable,
       "mscHtdsLCoPathEntry": mscHtdsLCoPathEntry,
       "mscHtdsLCoPathValue": mscHtdsLCoPathValue,
       "mscHtdsCidDataTable": mscHtdsCidDataTable,
       "mscHtdsCidDataEntry": mscHtdsCidDataEntry,
       "mscHtdsCustomerIdentifier": mscHtdsCustomerIdentifier,
       "mscHtdsIfEntryTable": mscHtdsIfEntryTable,
       "mscHtdsIfEntryEntry": mscHtdsIfEntryEntry,
       "mscHtdsIfAdminStatus": mscHtdsIfAdminStatus,
       "mscHtdsIfIndex": mscHtdsIfIndex,
       "mscHtdsOperStatusTable": mscHtdsOperStatusTable,
       "mscHtdsOperStatusEntry": mscHtdsOperStatusEntry,
       "mscHtdsSnmpOperStatus": mscHtdsSnmpOperStatus,
       "mscHtdsStateTable": mscHtdsStateTable,
       "mscHtdsStateEntry": mscHtdsStateEntry,
       "mscHtdsAdminState": mscHtdsAdminState,
       "mscHtdsOperationalState": mscHtdsOperationalState,
       "mscHtdsUsageState": mscHtdsUsageState,
       "mscHtdsAvailabilityStatus": mscHtdsAvailabilityStatus,
       "mscHtdsProceduralStatus": mscHtdsProceduralStatus,
       "mscHtdsControlStatus": mscHtdsControlStatus,
       "mscHtdsAlarmStatus": mscHtdsAlarmStatus,
       "mscHtdsStandbyStatus": mscHtdsStandbyStatus,
       "mscHtdsUnknownStatus": mscHtdsUnknownStatus,
       "hdlcTransparentMIB": hdlcTransparentMIB,
       "hdlcTransparentGroup": hdlcTransparentGroup,
       "hdlcTransparentGroupCA": hdlcTransparentGroupCA,
       "hdlcTransparentGroupCA02": hdlcTransparentGroupCA02,
       "hdlcTransparentGroupCA02A": hdlcTransparentGroupCA02A,
       "hdlcTransparentCapabilities": hdlcTransparentCapabilities,
       "hdlcTransparentCapabilitiesCA": hdlcTransparentCapabilitiesCA,
       "hdlcTransparentCapabilitiesCA02": hdlcTransparentCapabilitiesCA02,
       "hdlcTransparentCapabilitiesCA02A": hdlcTransparentCapabilitiesCA02A}
)
