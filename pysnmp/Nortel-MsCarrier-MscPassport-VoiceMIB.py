# SNMP MIB module (Nortel-MsCarrier-MscPassport-VoiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VoiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:21 2024
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
 FixedPoint1,
 HexString,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "FixedPoint1",
    "HexString",
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

_MscVs_ObjectIdentity = ObjectIdentity
mscVs = _MscVs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80)
)
_MscVsRowStatusTable_Object = MibTable
mscVsRowStatusTable = _MscVsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1)
)
if mibBuilder.loadTexts:
    mscVsRowStatusTable.setStatus("mandatory")
_MscVsRowStatusEntry_Object = MibTableRow
mscVsRowStatusEntry = _MscVsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1, 1)
)
mscVsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsRowStatusEntry.setStatus("mandatory")
_MscVsRowStatus_Type = RowStatus
_MscVsRowStatus_Object = MibTableColumn
mscVsRowStatus = _MscVsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1, 1, 1),
    _MscVsRowStatus_Type()
)
mscVsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsRowStatus.setStatus("mandatory")
_MscVsComponentName_Type = DisplayString
_MscVsComponentName_Object = MibTableColumn
mscVsComponentName = _MscVsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1, 1, 2),
    _MscVsComponentName_Type()
)
mscVsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsComponentName.setStatus("mandatory")
_MscVsStorageType_Type = StorageType
_MscVsStorageType_Object = MibTableColumn
mscVsStorageType = _MscVsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1, 1, 4),
    _MscVsStorageType_Type()
)
mscVsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsStorageType.setStatus("mandatory")


class _MscVsIndex_Type(Integer32):
    """Custom type mscVsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVsIndex_Type.__name__ = "Integer32"
_MscVsIndex_Object = MibTableColumn
mscVsIndex = _MscVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 1, 1, 10),
    _MscVsIndex_Type()
)
mscVsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsIndex.setStatus("mandatory")
_MscVsFramer_ObjectIdentity = ObjectIdentity
mscVsFramer = _MscVsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2)
)
_MscVsFramerRowStatusTable_Object = MibTable
mscVsFramerRowStatusTable = _MscVsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1)
)
if mibBuilder.loadTexts:
    mscVsFramerRowStatusTable.setStatus("mandatory")
_MscVsFramerRowStatusEntry_Object = MibTableRow
mscVsFramerRowStatusEntry = _MscVsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1, 1)
)
mscVsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerRowStatusEntry.setStatus("mandatory")
_MscVsFramerRowStatus_Type = RowStatus
_MscVsFramerRowStatus_Object = MibTableColumn
mscVsFramerRowStatus = _MscVsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1, 1, 1),
    _MscVsFramerRowStatus_Type()
)
mscVsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerRowStatus.setStatus("mandatory")
_MscVsFramerComponentName_Type = DisplayString
_MscVsFramerComponentName_Object = MibTableColumn
mscVsFramerComponentName = _MscVsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1, 1, 2),
    _MscVsFramerComponentName_Type()
)
mscVsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerComponentName.setStatus("mandatory")
_MscVsFramerStorageType_Type = StorageType
_MscVsFramerStorageType_Object = MibTableColumn
mscVsFramerStorageType = _MscVsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1, 1, 4),
    _MscVsFramerStorageType_Type()
)
mscVsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerStorageType.setStatus("mandatory")
_MscVsFramerIndex_Type = NonReplicated
_MscVsFramerIndex_Object = MibTableColumn
mscVsFramerIndex = _MscVsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 1, 1, 10),
    _MscVsFramerIndex_Type()
)
mscVsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerIndex.setStatus("mandatory")
_MscVsFramerVfpDebug_ObjectIdentity = ObjectIdentity
mscVsFramerVfpDebug = _MscVsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5)
)
_MscVsFramerVfpDebugRowStatusTable_Object = MibTable
mscVsFramerVfpDebugRowStatusTable = _MscVsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_MscVsFramerVfpDebugRowStatusEntry_Object = MibTableRow
mscVsFramerVfpDebugRowStatusEntry = _MscVsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1, 1)
)
mscVsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_MscVsFramerVfpDebugRowStatus_Type = RowStatus
_MscVsFramerVfpDebugRowStatus_Object = MibTableColumn
mscVsFramerVfpDebugRowStatus = _MscVsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1, 1, 1),
    _MscVsFramerVfpDebugRowStatus_Type()
)
mscVsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugRowStatus.setStatus("mandatory")
_MscVsFramerVfpDebugComponentName_Type = DisplayString
_MscVsFramerVfpDebugComponentName_Object = MibTableColumn
mscVsFramerVfpDebugComponentName = _MscVsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1, 1, 2),
    _MscVsFramerVfpDebugComponentName_Type()
)
mscVsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugComponentName.setStatus("mandatory")
_MscVsFramerVfpDebugStorageType_Type = StorageType
_MscVsFramerVfpDebugStorageType_Object = MibTableColumn
mscVsFramerVfpDebugStorageType = _MscVsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1, 1, 4),
    _MscVsFramerVfpDebugStorageType_Type()
)
mscVsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugStorageType.setStatus("mandatory")
_MscVsFramerVfpDebugIndex_Type = NonReplicated
_MscVsFramerVfpDebugIndex_Object = MibTableColumn
mscVsFramerVfpDebugIndex = _MscVsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 5, 1, 1, 10),
    _MscVsFramerVfpDebugIndex_Type()
)
mscVsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerVfpDebugIndex.setStatus("mandatory")
_MscVsFramerMvpDebug_ObjectIdentity = ObjectIdentity
mscVsFramerMvpDebug = _MscVsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6)
)
_MscVsFramerMvpDebugRowStatusTable_Object = MibTable
mscVsFramerMvpDebugRowStatusTable = _MscVsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_MscVsFramerMvpDebugRowStatusEntry_Object = MibTableRow
mscVsFramerMvpDebugRowStatusEntry = _MscVsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1, 1)
)
mscVsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_MscVsFramerMvpDebugRowStatus_Type = RowStatus
_MscVsFramerMvpDebugRowStatus_Object = MibTableColumn
mscVsFramerMvpDebugRowStatus = _MscVsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1, 1, 1),
    _MscVsFramerMvpDebugRowStatus_Type()
)
mscVsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugRowStatus.setStatus("mandatory")
_MscVsFramerMvpDebugComponentName_Type = DisplayString
_MscVsFramerMvpDebugComponentName_Object = MibTableColumn
mscVsFramerMvpDebugComponentName = _MscVsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1, 1, 2),
    _MscVsFramerMvpDebugComponentName_Type()
)
mscVsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugComponentName.setStatus("mandatory")
_MscVsFramerMvpDebugStorageType_Type = StorageType
_MscVsFramerMvpDebugStorageType_Object = MibTableColumn
mscVsFramerMvpDebugStorageType = _MscVsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1, 1, 4),
    _MscVsFramerMvpDebugStorageType_Type()
)
mscVsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugStorageType.setStatus("mandatory")
_MscVsFramerMvpDebugIndex_Type = NonReplicated
_MscVsFramerMvpDebugIndex_Object = MibTableColumn
mscVsFramerMvpDebugIndex = _MscVsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 6, 1, 1, 10),
    _MscVsFramerMvpDebugIndex_Type()
)
mscVsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerMvpDebugIndex.setStatus("mandatory")
_MscVsFramerPcmCapture_ObjectIdentity = ObjectIdentity
mscVsFramerPcmCapture = _MscVsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7)
)
_MscVsFramerPcmCaptureRowStatusTable_Object = MibTable
mscVsFramerPcmCaptureRowStatusTable = _MscVsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_MscVsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
mscVsFramerPcmCaptureRowStatusEntry = _MscVsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1, 1)
)
mscVsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_MscVsFramerPcmCaptureRowStatus_Type = RowStatus
_MscVsFramerPcmCaptureRowStatus_Object = MibTableColumn
mscVsFramerPcmCaptureRowStatus = _MscVsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1, 1, 1),
    _MscVsFramerPcmCaptureRowStatus_Type()
)
mscVsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureRowStatus.setStatus("mandatory")
_MscVsFramerPcmCaptureComponentName_Type = DisplayString
_MscVsFramerPcmCaptureComponentName_Object = MibTableColumn
mscVsFramerPcmCaptureComponentName = _MscVsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1, 1, 2),
    _MscVsFramerPcmCaptureComponentName_Type()
)
mscVsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureComponentName.setStatus("mandatory")
_MscVsFramerPcmCaptureStorageType_Type = StorageType
_MscVsFramerPcmCaptureStorageType_Object = MibTableColumn
mscVsFramerPcmCaptureStorageType = _MscVsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1, 1, 4),
    _MscVsFramerPcmCaptureStorageType_Type()
)
mscVsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureStorageType.setStatus("mandatory")
_MscVsFramerPcmCaptureIndex_Type = NonReplicated
_MscVsFramerPcmCaptureIndex_Object = MibTableColumn
mscVsFramerPcmCaptureIndex = _MscVsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 7, 1, 1, 10),
    _MscVsFramerPcmCaptureIndex_Type()
)
mscVsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerPcmCaptureIndex.setStatus("mandatory")
_MscVsFramerProvTable_Object = MibTable
mscVsFramerProvTable = _MscVsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 10)
)
if mibBuilder.loadTexts:
    mscVsFramerProvTable.setStatus("mandatory")
_MscVsFramerProvEntry_Object = MibTableRow
mscVsFramerProvEntry = _MscVsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 10, 1)
)
mscVsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerProvEntry.setStatus("mandatory")
_MscVsFramerInterfaceName_Type = Link
_MscVsFramerInterfaceName_Object = MibTableColumn
mscVsFramerInterfaceName = _MscVsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 10, 1, 1),
    _MscVsFramerInterfaceName_Type()
)
mscVsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerInterfaceName.setStatus("mandatory")
_MscVsFramerCoderTable_Object = MibTable
mscVsFramerCoderTable = _MscVsFramerCoderTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12)
)
if mibBuilder.loadTexts:
    mscVsFramerCoderTable.setStatus("mandatory")
_MscVsFramerCoderEntry_Object = MibTableRow
mscVsFramerCoderEntry = _MscVsFramerCoderEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1)
)
mscVsFramerCoderEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerCoderEntry.setStatus("mandatory")


class _MscVsFramerMaxVoiceBitRate_Type(Integer32):
    """Custom type mscVsFramerMaxVoiceBitRate based on Integer32"""
    defaultValue = 0

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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerMaxVoiceBitRate_Type.__name__ = "Integer32"
_MscVsFramerMaxVoiceBitRate_Object = MibTableColumn
mscVsFramerMaxVoiceBitRate = _MscVsFramerMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 1),
    _MscVsFramerMaxVoiceBitRate_Type()
)
mscVsFramerMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerMaxVoiceBitRate.setStatus("mandatory")


class _MscVsFramerMinVoiceBitRate_Type(Integer32):
    """Custom type mscVsFramerMinVoiceBitRate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerMinVoiceBitRate_Type.__name__ = "Integer32"
_MscVsFramerMinVoiceBitRate_Object = MibTableColumn
mscVsFramerMinVoiceBitRate = _MscVsFramerMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 2),
    _MscVsFramerMinVoiceBitRate_Type()
)
mscVsFramerMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerMinVoiceBitRate.setStatus("mandatory")


class _MscVsFramerMaxModemBitRate_Type(Integer32):
    """Custom type mscVsFramerMaxModemBitRate based on Integer32"""
    defaultValue = 0

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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerMaxModemBitRate_Type.__name__ = "Integer32"
_MscVsFramerMaxModemBitRate_Object = MibTableColumn
mscVsFramerMaxModemBitRate = _MscVsFramerMaxModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 3),
    _MscVsFramerMaxModemBitRate_Type()
)
mscVsFramerMaxModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerMaxModemBitRate.setStatus("mandatory")


class _MscVsFramerMinModemBitRate_Type(Integer32):
    """Custom type mscVsFramerMinModemBitRate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerMinModemBitRate_Type.__name__ = "Integer32"
_MscVsFramerMinModemBitRate_Object = MibTableColumn
mscVsFramerMinModemBitRate = _MscVsFramerMinModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 4),
    _MscVsFramerMinModemBitRate_Type()
)
mscVsFramerMinModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerMinModemBitRate.setStatus("mandatory")


class _MscVsFramerAudioGain_Type(Integer32):
    """Custom type mscVsFramerAudioGain based on Integer32"""
    defaultValue = 3

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
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("minus1", 15),
          ("minus10", 9),
          ("minus11", 8),
          ("minus12", 7),
          ("minus2", 2),
          ("minus3", 14),
          ("minus4", 1),
          ("minus5", 13),
          ("minus6", 0),
          ("minus7", 12),
          ("minus8", 11),
          ("minus9", 10),
          ("n0", 3),
          ("n1", 16),
          ("n10", 22),
          ("n11", 23),
          ("n12", 24),
          ("n2", 4),
          ("n3", 17),
          ("n4", 5),
          ("n5", 18),
          ("n6", 6),
          ("n7", 19),
          ("n8", 20),
          ("n9", 21))
    )


_MscVsFramerAudioGain_Type.__name__ = "Integer32"
_MscVsFramerAudioGain_Object = MibTableColumn
mscVsFramerAudioGain = _MscVsFramerAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 5),
    _MscVsFramerAudioGain_Type()
)
mscVsFramerAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerAudioGain.setStatus("obsolete")


class _MscVsFramerSilenceSuppression_Type(Integer32):
    """Custom type mscVsFramerSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("casIdleCode", 5),
          ("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_MscVsFramerSilenceSuppression_Type.__name__ = "Integer32"
_MscVsFramerSilenceSuppression_Object = MibTableColumn
mscVsFramerSilenceSuppression = _MscVsFramerSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 6),
    _MscVsFramerSilenceSuppression_Type()
)
mscVsFramerSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerSilenceSuppression.setStatus("mandatory")


class _MscVsFramerEchoCancellation_Type(Integer32):
    """Custom type mscVsFramerEchoCancellation based on Integer32"""
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


_MscVsFramerEchoCancellation_Type.__name__ = "Integer32"
_MscVsFramerEchoCancellation_Object = MibTableColumn
mscVsFramerEchoCancellation = _MscVsFramerEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 7),
    _MscVsFramerEchoCancellation_Type()
)
mscVsFramerEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEchoCancellation.setStatus("mandatory")


class _MscVsFramerALawConversion_Type(Integer32):
    """Custom type mscVsFramerALawConversion based on Integer32"""
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


_MscVsFramerALawConversion_Type.__name__ = "Integer32"
_MscVsFramerALawConversion_Object = MibTableColumn
mscVsFramerALawConversion = _MscVsFramerALawConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 9),
    _MscVsFramerALawConversion_Type()
)
mscVsFramerALawConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerALawConversion.setStatus("mandatory")


class _MscVsFramerVoiceEncoding_Type(Integer32):
    """Custom type mscVsFramerVoiceEncoding based on Integer32"""
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
        *(("g711G726", 0),
          ("g728at16", 1),
          ("g729at8", 2))
    )


_MscVsFramerVoiceEncoding_Type.__name__ = "Integer32"
_MscVsFramerVoiceEncoding_Object = MibTableColumn
mscVsFramerVoiceEncoding = _MscVsFramerVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 11),
    _MscVsFramerVoiceEncoding_Type()
)
mscVsFramerVoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerVoiceEncoding.setStatus("mandatory")


class _MscVsFramerFaxEncoding_Type(Integer32):
    """Custom type mscVsFramerFaxEncoding based on Integer32"""
    defaultValue = 0

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
        *(("faxRelayG711G726", 2),
          ("faxRelayOnly", 1),
          ("g711G726", 0),
          ("useVoiceEncoding", 3))
    )


_MscVsFramerFaxEncoding_Type.__name__ = "Integer32"
_MscVsFramerFaxEncoding_Object = MibTableColumn
mscVsFramerFaxEncoding = _MscVsFramerFaxEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 12),
    _MscVsFramerFaxEncoding_Type()
)
mscVsFramerFaxEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerFaxEncoding.setStatus("mandatory")


class _MscVsFramerTandemPassThrough_Type(Integer32):
    """Custom type mscVsFramerTandemPassThrough based on Integer32"""
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


_MscVsFramerTandemPassThrough_Type.__name__ = "Integer32"
_MscVsFramerTandemPassThrough_Object = MibTableColumn
mscVsFramerTandemPassThrough = _MscVsFramerTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 13),
    _MscVsFramerTandemPassThrough_Type()
)
mscVsFramerTandemPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerTandemPassThrough.setStatus("mandatory")


class _MscVsFramerInsertedOutputDelay_Type(Integer32):
    """Custom type mscVsFramerInsertedOutputDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              15,
              22,
              30,
              35,
              40,
              45,
              50,
              75,
              100,
              125,
              150)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("n100", 100),
          ("n125", 125),
          ("n15", 15),
          ("n150", 150),
          ("n22", 22),
          ("n30", 30),
          ("n35", 35),
          ("n40", 40),
          ("n45", 45),
          ("n5", 5),
          ("n50", 50),
          ("n75", 75))
    )


_MscVsFramerInsertedOutputDelay_Type.__name__ = "Integer32"
_MscVsFramerInsertedOutputDelay_Object = MibTableColumn
mscVsFramerInsertedOutputDelay = _MscVsFramerInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 14),
    _MscVsFramerInsertedOutputDelay_Type()
)
mscVsFramerInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerInsertedOutputDelay.setStatus("mandatory")


class _MscVsFramerEgressAudioGain_Type(Integer32):
    """Custom type mscVsFramerEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscVsFramerEgressAudioGain_Type.__name__ = "Integer32"
_MscVsFramerEgressAudioGain_Object = MibTableColumn
mscVsFramerEgressAudioGain = _MscVsFramerEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 15),
    _MscVsFramerEgressAudioGain_Type()
)
mscVsFramerEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEgressAudioGain.setStatus("obsolete")


class _MscVsFramerFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type mscVsFramerFaxIdleSuppressionG711G726 based on Integer32"""
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


_MscVsFramerFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_MscVsFramerFaxIdleSuppressionG711G726_Object = MibTableColumn
mscVsFramerFaxIdleSuppressionG711G726 = _MscVsFramerFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 16),
    _MscVsFramerFaxIdleSuppressionG711G726_Type()
)
mscVsFramerFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerFaxIdleSuppressionG711G726.setStatus("mandatory")


class _MscVsFramerEndOfCallPattern_Type(Integer32):
    """Custom type mscVsFramerEndOfCallPattern based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a0", 160),
          ("a1", 161),
          ("a2", 162),
          ("a3", 163),
          ("a4", 164),
          ("a5", 165),
          ("a6", 166),
          ("a7", 167),
          ("a8", 168),
          ("a9", 169),
          ("aa", 170),
          ("ab", 171),
          ("ac", 172),
          ("ad", 173),
          ("ae", 174),
          ("af", 175),
          ("b0", 176),
          ("b1", 177),
          ("b2", 178),
          ("b3", 179),
          ("b4", 180),
          ("b5", 181),
          ("b6", 182),
          ("b7", 183),
          ("b8", 184),
          ("b9", 185),
          ("ba", 186),
          ("bb", 187),
          ("bc", 188),
          ("bd", 189),
          ("be", 190),
          ("bf", 191),
          ("c0", 192),
          ("c1", 193),
          ("c2", 194),
          ("c3", 195),
          ("c4", 196),
          ("c5", 197),
          ("c6", 198),
          ("c7", 199),
          ("c8", 200),
          ("c9", 201),
          ("ca", 202),
          ("cb", 203),
          ("cc", 204),
          ("cd", 205),
          ("ce", 206),
          ("cf", 207),
          ("d0", 208),
          ("d1", 209),
          ("d2", 210),
          ("d3", 211),
          ("d4", 212),
          ("d5", 213),
          ("d6", 214),
          ("d7", 215),
          ("d8", 216),
          ("d9", 217),
          ("da", 218),
          ("db", 219),
          ("dc", 220),
          ("dd", 221),
          ("de", 222),
          ("df", 223),
          ("e0", 224),
          ("e1", 225),
          ("e2", 226),
          ("e3", 227),
          ("e4", 228),
          ("e5", 229),
          ("e6", 230),
          ("e7", 231),
          ("e8", 232),
          ("e9", 233),
          ("ea", 234),
          ("eb", 235),
          ("ec", 236),
          ("ed", 237),
          ("ee", 238),
          ("ef", 239),
          ("f0", 240),
          ("f1", 241),
          ("f2", 242),
          ("f3", 243),
          ("f4", 244),
          ("f5", 245),
          ("f6", 246),
          ("f7", 247),
          ("f8", 248),
          ("f9", 249),
          ("fa", 250),
          ("fb", 251),
          ("fc", 252),
          ("fd", 253),
          ("fe", 254),
          ("ff", 255),
          ("n01", 1),
          ("n02", 2),
          ("n03", 3),
          ("n04", 4),
          ("n05", 5),
          ("n06", 6),
          ("n07", 7),
          ("n08", 8),
          ("n09", 9),
          ("n0a", 10),
          ("n0b", 11),
          ("n0c", 12),
          ("n0d", 13),
          ("n0e", 14),
          ("n0f", 15),
          ("n10", 16),
          ("n11", 17),
          ("n12", 18),
          ("n13", 19),
          ("n14", 20),
          ("n15", 21),
          ("n16", 22),
          ("n17", 23),
          ("n18", 24),
          ("n19", 25),
          ("n1a", 26),
          ("n1b", 27),
          ("n1c", 28),
          ("n1d", 29),
          ("n1e", 30),
          ("n1f", 31),
          ("n20", 32),
          ("n21", 33),
          ("n22", 34),
          ("n23", 35),
          ("n24", 36),
          ("n25", 37),
          ("n26", 38),
          ("n27", 39),
          ("n28", 40),
          ("n29", 41),
          ("n2a", 42),
          ("n2b", 43),
          ("n2c", 44),
          ("n2d", 45),
          ("n2e", 46),
          ("n2f", 47),
          ("n30", 48),
          ("n31", 49),
          ("n32", 50),
          ("n33", 51),
          ("n34", 52),
          ("n35", 53),
          ("n36", 54),
          ("n37", 55),
          ("n38", 56),
          ("n39", 57),
          ("n3a", 58),
          ("n3b", 59),
          ("n3c", 60),
          ("n3d", 61),
          ("n3e", 62),
          ("n3f", 63),
          ("n40", 64),
          ("n41", 65),
          ("n42", 66),
          ("n43", 67),
          ("n44", 68),
          ("n45", 69),
          ("n46", 70),
          ("n47", 71),
          ("n48", 72),
          ("n49", 73),
          ("n4a", 74),
          ("n4b", 75),
          ("n4c", 76),
          ("n4d", 77),
          ("n4e", 78),
          ("n4f", 79),
          ("n50", 80),
          ("n51", 81),
          ("n52", 82),
          ("n53", 83),
          ("n54", 84),
          ("n55", 85),
          ("n56", 86),
          ("n57", 87),
          ("n58", 88),
          ("n59", 89),
          ("n5a", 90),
          ("n5b", 91),
          ("n5c", 92),
          ("n5d", 93),
          ("n5e", 94),
          ("n5f", 95),
          ("n60", 96),
          ("n61", 97),
          ("n62", 98),
          ("n63", 99),
          ("n64", 100),
          ("n65", 101),
          ("n66", 102),
          ("n67", 103),
          ("n68", 104),
          ("n69", 105),
          ("n6a", 106),
          ("n6b", 107),
          ("n6c", 108),
          ("n6d", 109),
          ("n6e", 110),
          ("n6f", 111),
          ("n70", 112),
          ("n71", 113),
          ("n72", 114),
          ("n73", 115),
          ("n74", 116),
          ("n75", 117),
          ("n76", 118),
          ("n77", 119),
          ("n78", 120),
          ("n79", 121),
          ("n7a", 122),
          ("n7b", 123),
          ("n7c", 124),
          ("n7d", 125),
          ("n7e", 126),
          ("n7f", 127),
          ("n80", 128),
          ("n81", 129),
          ("n82", 130),
          ("n83", 131),
          ("n84", 132),
          ("n85", 133),
          ("n86", 134),
          ("n87", 135),
          ("n88", 136),
          ("n89", 137),
          ("n8a", 138),
          ("n8b", 139),
          ("n8c", 140),
          ("n8d", 141),
          ("n8e", 142),
          ("n8f", 143),
          ("n90", 144),
          ("n91", 145),
          ("n92", 146),
          ("n93", 147),
          ("n94", 148),
          ("n95", 149),
          ("n96", 150),
          ("n97", 151),
          ("n98", 152),
          ("n99", 153),
          ("n9a", 154),
          ("n9b", 155),
          ("n9c", 156),
          ("n9d", 157),
          ("n9e", 158),
          ("n9f", 159),
          ("standard", 0))
    )


_MscVsFramerEndOfCallPattern_Type.__name__ = "Integer32"
_MscVsFramerEndOfCallPattern_Object = MibTableColumn
mscVsFramerEndOfCallPattern = _MscVsFramerEndOfCallPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 17),
    _MscVsFramerEndOfCallPattern_Type()
)
mscVsFramerEndOfCallPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEndOfCallPattern.setStatus("mandatory")


class _MscVsFramerIngressAudioGain_Type(Integer32):
    """Custom type mscVsFramerIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscVsFramerIngressAudioGain_Type.__name__ = "Integer32"
_MscVsFramerIngressAudioGain_Object = MibTableColumn
mscVsFramerIngressAudioGain = _MscVsFramerIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 18),
    _MscVsFramerIngressAudioGain_Type()
)
mscVsFramerIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerIngressAudioGain.setStatus("mandatory")


class _MscVsFramerEgressGain_Type(Integer32):
    """Custom type mscVsFramerEgressGain based on Integer32"""
    defaultValue = 3

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
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("minus1", 15),
          ("minus10", 9),
          ("minus11", 8),
          ("minus12", 7),
          ("minus2", 2),
          ("minus3", 14),
          ("minus4", 1),
          ("minus5", 13),
          ("minus6", 0),
          ("minus7", 12),
          ("minus8", 11),
          ("minus9", 10),
          ("n0", 3),
          ("n1", 16),
          ("n10", 22),
          ("n11", 23),
          ("n12", 24),
          ("n2", 4),
          ("n3", 17),
          ("n4", 5),
          ("n5", 18),
          ("n6", 6),
          ("n7", 19),
          ("n8", 20),
          ("n9", 21))
    )


_MscVsFramerEgressGain_Type.__name__ = "Integer32"
_MscVsFramerEgressGain_Object = MibTableColumn
mscVsFramerEgressGain = _MscVsFramerEgressGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 19),
    _MscVsFramerEgressGain_Type()
)
mscVsFramerEgressGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEgressGain.setStatus("mandatory")


class _MscVsFramerComfortNoiseCap_Type(Integer32):
    """Custom type mscVsFramerComfortNoiseCap based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-78, -78),
        ValueRangeConstraint(-65, -65),
        ValueRangeConstraint(-60, -60),
        ValueRangeConstraint(-54, -54),
        ValueRangeConstraint(-52, -52),
        ValueRangeConstraint(-50, -50),
        ValueRangeConstraint(-48, -48),
        ValueRangeConstraint(-46, -46),
        ValueRangeConstraint(-44, -44),
        ValueRangeConstraint(-42, -42),
        ValueRangeConstraint(-40, -40),
    )


_MscVsFramerComfortNoiseCap_Type.__name__ = "Integer32"
_MscVsFramerComfortNoiseCap_Object = MibTableColumn
mscVsFramerComfortNoiseCap = _MscVsFramerComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 20),
    _MscVsFramerComfortNoiseCap_Type()
)
mscVsFramerComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerComfortNoiseCap.setStatus("mandatory")


class _MscVsFramerEchoTailDelay_Type(Unsigned32):
    """Custom type mscVsFramerEchoTailDelay based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
    )


_MscVsFramerEchoTailDelay_Type.__name__ = "Unsigned32"
_MscVsFramerEchoTailDelay_Object = MibTableColumn
mscVsFramerEchoTailDelay = _MscVsFramerEchoTailDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 21),
    _MscVsFramerEchoTailDelay_Type()
)
mscVsFramerEchoTailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEchoTailDelay.setStatus("mandatory")


class _MscVsFramerEchoReturnLoss_Type(Unsigned32):
    """Custom type mscVsFramerEchoReturnLoss based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(6, 6),
    )


_MscVsFramerEchoReturnLoss_Type.__name__ = "Unsigned32"
_MscVsFramerEchoReturnLoss_Object = MibTableColumn
mscVsFramerEchoReturnLoss = _MscVsFramerEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 22),
    _MscVsFramerEchoReturnLoss_Type()
)
mscVsFramerEchoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEchoReturnLoss.setStatus("mandatory")


class _MscVsFramerDtmfRegeneration_Type(Integer32):
    """Custom type mscVsFramerDtmfRegeneration based on Integer32"""
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


_MscVsFramerDtmfRegeneration_Type.__name__ = "Integer32"
_MscVsFramerDtmfRegeneration_Object = MibTableColumn
mscVsFramerDtmfRegeneration = _MscVsFramerDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 34),
    _MscVsFramerDtmfRegeneration_Type()
)
mscVsFramerDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerDtmfRegeneration.setStatus("mandatory")


class _MscVsFramerSpeechHangoverTime_Type(Integer32):
    """Custom type mscVsFramerSpeechHangoverTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_MscVsFramerSpeechHangoverTime_Type.__name__ = "Integer32"
_MscVsFramerSpeechHangoverTime_Object = MibTableColumn
mscVsFramerSpeechHangoverTime = _MscVsFramerSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 35),
    _MscVsFramerSpeechHangoverTime_Type()
)
mscVsFramerSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerSpeechHangoverTime.setStatus("mandatory")


class _MscVsFramerFaxHangoverTimeG711G726_Type(Integer32):
    """Custom type mscVsFramerFaxHangoverTimeG711G726 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 20000),
    )


_MscVsFramerFaxHangoverTimeG711G726_Type.__name__ = "Integer32"
_MscVsFramerFaxHangoverTimeG711G726_Object = MibTableColumn
mscVsFramerFaxHangoverTimeG711G726 = _MscVsFramerFaxHangoverTimeG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 36),
    _MscVsFramerFaxHangoverTimeG711G726_Type()
)
mscVsFramerFaxHangoverTimeG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerFaxHangoverTimeG711G726.setStatus("mandatory")


class _MscVsFramerModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type mscVsFramerModemFaxSpeechDiscrim based on Integer32"""
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


_MscVsFramerModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_MscVsFramerModemFaxSpeechDiscrim_Object = MibTableColumn
mscVsFramerModemFaxSpeechDiscrim = _MscVsFramerModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 37),
    _MscVsFramerModemFaxSpeechDiscrim_Type()
)
mscVsFramerModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerModemFaxSpeechDiscrim.setStatus("mandatory")


class _MscVsFramerV17EncodedAsG711G726_Type(Integer32):
    """Custom type mscVsFramerV17EncodedAsG711G726 based on Integer32"""
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


_MscVsFramerV17EncodedAsG711G726_Type.__name__ = "Integer32"
_MscVsFramerV17EncodedAsG711G726_Object = MibTableColumn
mscVsFramerV17EncodedAsG711G726 = _MscVsFramerV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 39),
    _MscVsFramerV17EncodedAsG711G726_Type()
)
mscVsFramerV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerV17EncodedAsG711G726.setStatus("mandatory")


class _MscVsFramerEcanBypassMode_Type(Integer32):
    """Custom type mscVsFramerEcanBypassMode based on Integer32"""
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
        *(("g164", 0),
          ("g165", 1),
          ("never", 2))
    )


_MscVsFramerEcanBypassMode_Type.__name__ = "Integer32"
_MscVsFramerEcanBypassMode_Object = MibTableColumn
mscVsFramerEcanBypassMode = _MscVsFramerEcanBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 40),
    _MscVsFramerEcanBypassMode_Type()
)
mscVsFramerEcanBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerEcanBypassMode.setStatus("mandatory")


class _MscVsFramerMaxFaxRelayRate_Type(FixedPoint1):
    """Custom type mscVsFramerMaxFaxRelayRate based on FixedPoint1"""
    defaultValue = 144

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(144, 144),
    )


_MscVsFramerMaxFaxRelayRate_Type.__name__ = "FixedPoint1"
_MscVsFramerMaxFaxRelayRate_Object = MibTableColumn
mscVsFramerMaxFaxRelayRate = _MscVsFramerMaxFaxRelayRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 12, 1, 41),
    _MscVsFramerMaxFaxRelayRate_Type()
)
mscVsFramerMaxFaxRelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerMaxFaxRelayRate.setStatus("mandatory")
_MscVsFramerSignalTable_Object = MibTable
mscVsFramerSignalTable = _MscVsFramerSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13)
)
if mibBuilder.loadTexts:
    mscVsFramerSignalTable.setStatus("mandatory")
_MscVsFramerSignalEntry_Object = MibTableRow
mscVsFramerSignalEntry = _MscVsFramerSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1)
)
mscVsFramerSignalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerSignalEntry.setStatus("mandatory")


class _MscVsFramerTransmitBusyYellow_Type(Integer32):
    """Custom type mscVsFramerTransmitBusyYellow based on Integer32"""
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


_MscVsFramerTransmitBusyYellow_Type.__name__ = "Integer32"
_MscVsFramerTransmitBusyYellow_Object = MibTableColumn
mscVsFramerTransmitBusyYellow = _MscVsFramerTransmitBusyYellow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 1),
    _MscVsFramerTransmitBusyYellow_Type()
)
mscVsFramerTransmitBusyYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerTransmitBusyYellow.setStatus("mandatory")


class _MscVsFramerTransportSignalling_Type(Integer32):
    """Custom type mscVsFramerTransportSignalling based on Integer32"""
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


_MscVsFramerTransportSignalling_Type.__name__ = "Integer32"
_MscVsFramerTransportSignalling_Object = MibTableColumn
mscVsFramerTransportSignalling = _MscVsFramerTransportSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 2),
    _MscVsFramerTransportSignalling_Type()
)
mscVsFramerTransportSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerTransportSignalling.setStatus("obsolete")


class _MscVsFramerInterpretSignalling_Type(Integer32):
    """Custom type mscVsFramerInterpretSignalling based on Integer32"""
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


_MscVsFramerInterpretSignalling_Type.__name__ = "Integer32"
_MscVsFramerInterpretSignalling_Object = MibTableColumn
mscVsFramerInterpretSignalling = _MscVsFramerInterpretSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 3),
    _MscVsFramerInterpretSignalling_Type()
)
mscVsFramerInterpretSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerInterpretSignalling.setStatus("obsolete")


class _MscVsFramerInvertBits_Type(Integer32):
    """Custom type mscVsFramerInvertBits based on Integer32"""
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


_MscVsFramerInvertBits_Type.__name__ = "Integer32"
_MscVsFramerInvertBits_Object = MibTableColumn
mscVsFramerInvertBits = _MscVsFramerInvertBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 4),
    _MscVsFramerInvertBits_Type()
)
mscVsFramerInvertBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerInvertBits.setStatus("mandatory")


class _MscVsFramerSignalBits_Type(Integer32):
    """Custom type mscVsFramerSignalBits based on Integer32"""
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
        *(("a", 0),
          ("aB", 1),
          ("aBCD", 2))
    )


_MscVsFramerSignalBits_Type.__name__ = "Integer32"
_MscVsFramerSignalBits_Object = MibTableColumn
mscVsFramerSignalBits = _MscVsFramerSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 5),
    _MscVsFramerSignalBits_Type()
)
mscVsFramerSignalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerSignalBits.setStatus("mandatory")


class _MscVsFramerTransmitCasYellow_Type(Integer32):
    """Custom type mscVsFramerTransmitCasYellow based on Integer32"""
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


_MscVsFramerTransmitCasYellow_Type.__name__ = "Integer32"
_MscVsFramerTransmitCasYellow_Object = MibTableColumn
mscVsFramerTransmitCasYellow = _MscVsFramerTransmitCasYellow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 7),
    _MscVsFramerTransmitCasYellow_Type()
)
mscVsFramerTransmitCasYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerTransmitCasYellow.setStatus("mandatory")


class _MscVsFramerCasSignalling_Type(Integer32):
    """Custom type mscVsFramerCasSignalling based on Integer32"""
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
        *(("interpret", 2),
          ("none", 0),
          ("transparent", 1))
    )


_MscVsFramerCasSignalling_Type.__name__ = "Integer32"
_MscVsFramerCasSignalling_Object = MibTableColumn
mscVsFramerCasSignalling = _MscVsFramerCasSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 13, 1, 8),
    _MscVsFramerCasSignalling_Type()
)
mscVsFramerCasSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerCasSignalling.setStatus("mandatory")
_MscVsFramerStateTable_Object = MibTable
mscVsFramerStateTable = _MscVsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 14)
)
if mibBuilder.loadTexts:
    mscVsFramerStateTable.setStatus("mandatory")
_MscVsFramerStateEntry_Object = MibTableRow
mscVsFramerStateEntry = _MscVsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 14, 1)
)
mscVsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerStateEntry.setStatus("mandatory")


class _MscVsFramerAdminState_Type(Integer32):
    """Custom type mscVsFramerAdminState based on Integer32"""
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


_MscVsFramerAdminState_Type.__name__ = "Integer32"
_MscVsFramerAdminState_Object = MibTableColumn
mscVsFramerAdminState = _MscVsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 14, 1, 1),
    _MscVsFramerAdminState_Type()
)
mscVsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerAdminState.setStatus("mandatory")


class _MscVsFramerOperationalState_Type(Integer32):
    """Custom type mscVsFramerOperationalState based on Integer32"""
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


_MscVsFramerOperationalState_Type.__name__ = "Integer32"
_MscVsFramerOperationalState_Object = MibTableColumn
mscVsFramerOperationalState = _MscVsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 14, 1, 2),
    _MscVsFramerOperationalState_Type()
)
mscVsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerOperationalState.setStatus("mandatory")


class _MscVsFramerUsageState_Type(Integer32):
    """Custom type mscVsFramerUsageState based on Integer32"""
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


_MscVsFramerUsageState_Type.__name__ = "Integer32"
_MscVsFramerUsageState_Object = MibTableColumn
mscVsFramerUsageState = _MscVsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 14, 1, 3),
    _MscVsFramerUsageState_Type()
)
mscVsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerUsageState.setStatus("mandatory")
_MscVsFramerStatsTable_Object = MibTable
mscVsFramerStatsTable = _MscVsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15)
)
if mibBuilder.loadTexts:
    mscVsFramerStatsTable.setStatus("mandatory")
_MscVsFramerStatsEntry_Object = MibTableRow
mscVsFramerStatsEntry = _MscVsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1)
)
mscVsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerStatsEntry.setStatus("mandatory")
_MscVsFramerTotalCells_Type = Counter32
_MscVsFramerTotalCells_Object = MibTableColumn
mscVsFramerTotalCells = _MscVsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 1),
    _MscVsFramerTotalCells_Type()
)
mscVsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerTotalCells.setStatus("mandatory")
_MscVsFramerAudioCells_Type = Counter32
_MscVsFramerAudioCells_Object = MibTableColumn
mscVsFramerAudioCells = _MscVsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 2),
    _MscVsFramerAudioCells_Type()
)
mscVsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerAudioCells.setStatus("mandatory")
_MscVsFramerSilenceCells_Type = Counter32
_MscVsFramerSilenceCells_Object = MibTableColumn
mscVsFramerSilenceCells = _MscVsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 4),
    _MscVsFramerSilenceCells_Type()
)
mscVsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerSilenceCells.setStatus("mandatory")
_MscVsFramerModemCells_Type = Counter32
_MscVsFramerModemCells_Object = MibTableColumn
mscVsFramerModemCells = _MscVsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 5),
    _MscVsFramerModemCells_Type()
)
mscVsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerModemCells.setStatus("obsolete")


class _MscVsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type mscVsFramerCurrentEncodingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_MscVsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_MscVsFramerCurrentEncodingRate_Object = MibTableColumn
mscVsFramerCurrentEncodingRate = _MscVsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 6),
    _MscVsFramerCurrentEncodingRate_Type()
)
mscVsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerCurrentEncodingRate.setStatus("obsolete")
_MscVsFramerLrcErrors_Type = Counter32
_MscVsFramerLrcErrors_Object = MibTableColumn
mscVsFramerLrcErrors = _MscVsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 7),
    _MscVsFramerLrcErrors_Type()
)
mscVsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerLrcErrors.setStatus("mandatory")
_MscVsFramerFrmLostInNetwork_Type = Counter32
_MscVsFramerFrmLostInNetwork_Object = MibTableColumn
mscVsFramerFrmLostInNetwork = _MscVsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 8),
    _MscVsFramerFrmLostInNetwork_Type()
)
mscVsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFrmLostInNetwork.setStatus("mandatory")
_MscVsFramerFrmUnderRuns_Type = Counter32
_MscVsFramerFrmUnderRuns_Object = MibTableColumn
mscVsFramerFrmUnderRuns = _MscVsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 9),
    _MscVsFramerFrmUnderRuns_Type()
)
mscVsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFrmUnderRuns.setStatus("mandatory")
_MscVsFramerFrmDumped_Type = Counter32
_MscVsFramerFrmDumped_Object = MibTableColumn
mscVsFramerFrmDumped = _MscVsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 10),
    _MscVsFramerFrmDumped_Type()
)
mscVsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFrmDumped.setStatus("mandatory")
_MscVsFramerModemSilenceCells_Type = Counter32
_MscVsFramerModemSilenceCells_Object = MibTableColumn
mscVsFramerModemSilenceCells = _MscVsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 26),
    _MscVsFramerModemSilenceCells_Type()
)
mscVsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerModemSilenceCells.setStatus("obsolete")


class _MscVsFramerTptStatus_Type(Integer32):
    """Custom type mscVsFramerTptStatus based on Integer32"""
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
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0),
          ("rejected", 1))
    )


_MscVsFramerTptStatus_Type.__name__ = "Integer32"
_MscVsFramerTptStatus_Object = MibTableColumn
mscVsFramerTptStatus = _MscVsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 27),
    _MscVsFramerTptStatus_Type()
)
mscVsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerTptStatus.setStatus("obsolete")


class _MscVsFramerCurrentEncoding_Type(Integer32):
    """Custom type mscVsFramerCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_MscVsFramerCurrentEncoding_Type.__name__ = "Integer32"
_MscVsFramerCurrentEncoding_Object = MibTableColumn
mscVsFramerCurrentEncoding = _MscVsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 28),
    _MscVsFramerCurrentEncoding_Type()
)
mscVsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerCurrentEncoding.setStatus("obsolete")


class _MscVsFramerRecentIngressLineSamples_Type(HexString):
    """Custom type mscVsFramerRecentIngressLineSamples based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVsFramerRecentIngressLineSamples_Type.__name__ = "HexString"
_MscVsFramerRecentIngressLineSamples_Object = MibTableColumn
mscVsFramerRecentIngressLineSamples = _MscVsFramerRecentIngressLineSamples_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 29),
    _MscVsFramerRecentIngressLineSamples_Type()
)
mscVsFramerRecentIngressLineSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerRecentIngressLineSamples.setStatus("obsolete")


class _MscVsFramerSentMinVoiceG711G726Rate_Type(Integer32):
    """Custom type mscVsFramerSentMinVoiceG711G726Rate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerSentMinVoiceG711G726Rate_Type.__name__ = "Integer32"
_MscVsFramerSentMinVoiceG711G726Rate_Object = MibTableColumn
mscVsFramerSentMinVoiceG711G726Rate = _MscVsFramerSentMinVoiceG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 30),
    _MscVsFramerSentMinVoiceG711G726Rate_Type()
)
mscVsFramerSentMinVoiceG711G726Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerSentMinVoiceG711G726Rate.setStatus("obsolete")


class _MscVsFramerSentMinModemFaxG711G726Rate_Type(Integer32):
    """Custom type mscVsFramerSentMinModemFaxG711G726Rate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVsFramerSentMinModemFaxG711G726Rate_Type.__name__ = "Integer32"
_MscVsFramerSentMinModemFaxG711G726Rate_Object = MibTableColumn
mscVsFramerSentMinModemFaxG711G726Rate = _MscVsFramerSentMinModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 31),
    _MscVsFramerSentMinModemFaxG711G726Rate_Type()
)
mscVsFramerSentMinModemFaxG711G726Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerSentMinModemFaxG711G726Rate.setStatus("obsolete")


class _MscVsFramerSentFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type mscVsFramerSentFaxIdleSuppressionG711G726 based on Integer32"""
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


_MscVsFramerSentFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_MscVsFramerSentFaxIdleSuppressionG711G726_Object = MibTableColumn
mscVsFramerSentFaxIdleSuppressionG711G726 = _MscVsFramerSentFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 32),
    _MscVsFramerSentFaxIdleSuppressionG711G726_Type()
)
mscVsFramerSentFaxIdleSuppressionG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerSentFaxIdleSuppressionG711G726.setStatus("obsolete")


class _MscVsFramerSentSilenceSuppression_Type(Integer32):
    """Custom type mscVsFramerSentSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("casIdleCode", 5),
          ("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_MscVsFramerSentSilenceSuppression_Type.__name__ = "Integer32"
_MscVsFramerSentSilenceSuppression_Object = MibTableColumn
mscVsFramerSentSilenceSuppression = _MscVsFramerSentSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 33),
    _MscVsFramerSentSilenceSuppression_Type()
)
mscVsFramerSentSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerSentSilenceSuppression.setStatus("obsolete")
_MscVsFramerFaxRelayCells_Type = Counter32
_MscVsFramerFaxRelayCells_Object = MibTableColumn
mscVsFramerFaxRelayCells = _MscVsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 42),
    _MscVsFramerFaxRelayCells_Type()
)
mscVsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFaxRelayCells.setStatus("mandatory")
_MscVsFramerModemFaxCells_Type = Counter32
_MscVsFramerModemFaxCells_Object = MibTableColumn
mscVsFramerModemFaxCells = _MscVsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 43),
    _MscVsFramerModemFaxCells_Type()
)
mscVsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerModemFaxCells.setStatus("mandatory")
_MscVsFramerFaxIdleCells_Type = Counter32
_MscVsFramerFaxIdleCells_Object = MibTableColumn
mscVsFramerFaxIdleCells = _MscVsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 15, 1, 44),
    _MscVsFramerFaxIdleCells_Type()
)
mscVsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFaxIdleCells.setStatus("mandatory")
_MscVsFramerNegTable_Object = MibTable
mscVsFramerNegTable = _MscVsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16)
)
if mibBuilder.loadTexts:
    mscVsFramerNegTable.setStatus("mandatory")
_MscVsFramerNegEntry_Object = MibTableRow
mscVsFramerNegEntry = _MscVsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1)
)
mscVsFramerNegEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerNegEntry.setStatus("mandatory")


class _MscVsFramerNegotiatedIgSilenceSuppression_Type(Integer32):
    """Custom type mscVsFramerNegotiatedIgSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("casIdleCode", 5),
          ("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_MscVsFramerNegotiatedIgSilenceSuppression_Type.__name__ = "Integer32"
_MscVsFramerNegotiatedIgSilenceSuppression_Object = MibTableColumn
mscVsFramerNegotiatedIgSilenceSuppression = _MscVsFramerNegotiatedIgSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1, 1),
    _MscVsFramerNegotiatedIgSilenceSuppression_Type()
)
mscVsFramerNegotiatedIgSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNegotiatedIgSilenceSuppression.setStatus("mandatory")


class _MscVsFramerNegotiatedIgFisG711G726_Type(Integer32):
    """Custom type mscVsFramerNegotiatedIgFisG711G726 based on Integer32"""
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


_MscVsFramerNegotiatedIgFisG711G726_Type.__name__ = "Integer32"
_MscVsFramerNegotiatedIgFisG711G726_Object = MibTableColumn
mscVsFramerNegotiatedIgFisG711G726 = _MscVsFramerNegotiatedIgFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1, 2),
    _MscVsFramerNegotiatedIgFisG711G726_Type()
)
mscVsFramerNegotiatedIgFisG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNegotiatedIgFisG711G726.setStatus("mandatory")


class _MscVsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type mscVsFramerNegotiatedDtmfRegeneration based on Integer32"""
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


_MscVsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_MscVsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
mscVsFramerNegotiatedDtmfRegeneration = _MscVsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1, 3),
    _MscVsFramerNegotiatedDtmfRegeneration_Type()
)
mscVsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _MscVsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type mscVsFramerNegotiatedV17AsG711G726 based on Integer32"""
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


_MscVsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_MscVsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
mscVsFramerNegotiatedV17AsG711G726 = _MscVsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1, 4),
    _MscVsFramerNegotiatedV17AsG711G726_Type()
)
mscVsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _MscVsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type mscVsFramerNegotiatedTandemPassThrough based on Integer32"""
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


_MscVsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_MscVsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
mscVsFramerNegotiatedTandemPassThrough = _MscVsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 16, 1, 5),
    _MscVsFramerNegotiatedTandemPassThrough_Type()
)
mscVsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_MscVsFramerOperTable_Object = MibTable
mscVsFramerOperTable = _MscVsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17)
)
if mibBuilder.loadTexts:
    mscVsFramerOperTable.setStatus("mandatory")
_MscVsFramerOperEntry_Object = MibTableRow
mscVsFramerOperEntry = _MscVsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17, 1)
)
mscVsFramerOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerOperEntry.setStatus("mandatory")


class _MscVsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type mscVsFramerOpCurrentEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              32,
              33,
              64,
              65,
              66,
              67,
              255)
        )
    )
    namedValues = NamedValues(
        *(("faxRelay", 64),
          ("g711", 5),
          ("g723", 3),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17", 67),
          ("v22", 32),
          ("v22bis", 33),
          ("v27", 65),
          ("v29", 66))
    )


_MscVsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_MscVsFramerOpCurrentEncoding_Object = MibTableColumn
mscVsFramerOpCurrentEncoding = _MscVsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17, 1, 1),
    _MscVsFramerOpCurrentEncoding_Type()
)
mscVsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerOpCurrentEncoding.setStatus("mandatory")


class _MscVsFramerCurrentRate_Type(Integer32):
    """Custom type mscVsFramerCurrentRate based on Integer32"""
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
          ("n03", 15),
          ("n12", 14),
          ("n120", 7),
          ("n144", 6),
          ("n160", 4),
          ("n24", 13),
          ("n240", 3),
          ("n320", 2),
          ("n48", 12),
          ("n53", 11),
          ("n63", 10),
          ("n640", 1),
          ("n72", 9),
          ("n80", 5),
          ("n96", 8))
    )


_MscVsFramerCurrentRate_Type.__name__ = "Integer32"
_MscVsFramerCurrentRate_Object = MibTableColumn
mscVsFramerCurrentRate = _MscVsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17, 1, 2),
    _MscVsFramerCurrentRate_Type()
)
mscVsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerCurrentRate.setStatus("mandatory")


class _MscVsFramerOpTptStatus_Type(Integer32):
    """Custom type mscVsFramerOpTptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("monitoring", 2),
          ("operating", 0))
    )


_MscVsFramerOpTptStatus_Type.__name__ = "Integer32"
_MscVsFramerOpTptStatus_Object = MibTableColumn
mscVsFramerOpTptStatus = _MscVsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17, 1, 3),
    _MscVsFramerOpTptStatus_Type()
)
mscVsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerOpTptStatus.setStatus("mandatory")


class _MscVsFramerOpRecentIngressLineSamples_Type(HexString):
    """Custom type mscVsFramerOpRecentIngressLineSamples based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVsFramerOpRecentIngressLineSamples_Type.__name__ = "HexString"
_MscVsFramerOpRecentIngressLineSamples_Object = MibTableColumn
mscVsFramerOpRecentIngressLineSamples = _MscVsFramerOpRecentIngressLineSamples_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 17, 1, 4),
    _MscVsFramerOpRecentIngressLineSamples_Type()
)
mscVsFramerOpRecentIngressLineSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerOpRecentIngressLineSamples.setStatus("mandatory")
_MscVsFramerIdleCodeTable_Object = MibTable
mscVsFramerIdleCodeTable = _MscVsFramerIdleCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 204)
)
if mibBuilder.loadTexts:
    mscVsFramerIdleCodeTable.setStatus("mandatory")
_MscVsFramerIdleCodeEntry_Object = MibTableRow
mscVsFramerIdleCodeEntry = _MscVsFramerIdleCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 204, 1)
)
mscVsFramerIdleCodeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIdleCodeIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerIdleCodeEntry.setStatus("mandatory")


class _MscVsFramerIdleCodeIndex_Type(Integer32):
    """Custom type mscVsFramerIdleCodeIndex based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3))
    )


_MscVsFramerIdleCodeIndex_Type.__name__ = "Integer32"
_MscVsFramerIdleCodeIndex_Object = MibTableColumn
mscVsFramerIdleCodeIndex = _MscVsFramerIdleCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 204, 1, 1),
    _MscVsFramerIdleCodeIndex_Type()
)
mscVsFramerIdleCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerIdleCodeIndex.setStatus("mandatory")


class _MscVsFramerIdleCodeValue_Type(Unsigned32):
    """Custom type mscVsFramerIdleCodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscVsFramerIdleCodeValue_Type.__name__ = "Unsigned32"
_MscVsFramerIdleCodeValue_Object = MibTableColumn
mscVsFramerIdleCodeValue = _MscVsFramerIdleCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 204, 1, 2),
    _MscVsFramerIdleCodeValue_Type()
)
mscVsFramerIdleCodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerIdleCodeValue.setStatus("mandatory")
_MscVsFramerSeizeCodeTable_Object = MibTable
mscVsFramerSeizeCodeTable = _MscVsFramerSeizeCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 205)
)
if mibBuilder.loadTexts:
    mscVsFramerSeizeCodeTable.setStatus("mandatory")
_MscVsFramerSeizeCodeEntry_Object = MibTableRow
mscVsFramerSeizeCodeEntry = _MscVsFramerSeizeCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 205, 1)
)
mscVsFramerSeizeCodeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerSeizeCodeIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerSeizeCodeEntry.setStatus("mandatory")


class _MscVsFramerSeizeCodeIndex_Type(Integer32):
    """Custom type mscVsFramerSeizeCodeIndex based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3))
    )


_MscVsFramerSeizeCodeIndex_Type.__name__ = "Integer32"
_MscVsFramerSeizeCodeIndex_Object = MibTableColumn
mscVsFramerSeizeCodeIndex = _MscVsFramerSeizeCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 205, 1, 1),
    _MscVsFramerSeizeCodeIndex_Type()
)
mscVsFramerSeizeCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerSeizeCodeIndex.setStatus("mandatory")


class _MscVsFramerSeizeCodeValue_Type(Unsigned32):
    """Custom type mscVsFramerSeizeCodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscVsFramerSeizeCodeValue_Type.__name__ = "Unsigned32"
_MscVsFramerSeizeCodeValue_Object = MibTableColumn
mscVsFramerSeizeCodeValue = _MscVsFramerSeizeCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 205, 1, 2),
    _MscVsFramerSeizeCodeValue_Type()
)
mscVsFramerSeizeCodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsFramerSeizeCodeValue.setStatus("mandatory")
_MscVsFramerFrmToNetworkTable_Object = MibTable
mscVsFramerFrmToNetworkTable = _MscVsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 206)
)
if mibBuilder.loadTexts:
    mscVsFramerFrmToNetworkTable.setStatus("mandatory")
_MscVsFramerFrmToNetworkEntry_Object = MibTableRow
mscVsFramerFrmToNetworkEntry = _MscVsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 206, 1)
)
mscVsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerFrmToNetworkEntry.setStatus("mandatory")


class _MscVsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type mscVsFramerFrmToNetworkIndex based on Integer32"""
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
        *(("n16KbitS", 3),
          ("n24KbitS", 2),
          ("n32KbitS", 1),
          ("n64KbitS", 0),
          ("n8KbitS", 4))
    )


_MscVsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_MscVsFramerFrmToNetworkIndex_Object = MibTableColumn
mscVsFramerFrmToNetworkIndex = _MscVsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 206, 1, 1),
    _MscVsFramerFrmToNetworkIndex_Type()
)
mscVsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerFrmToNetworkIndex.setStatus("mandatory")
_MscVsFramerFrmToNetworkValue_Type = Counter32
_MscVsFramerFrmToNetworkValue_Object = MibTableColumn
mscVsFramerFrmToNetworkValue = _MscVsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 206, 1, 2),
    _MscVsFramerFrmToNetworkValue_Type()
)
mscVsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerFrmToNetworkValue.setStatus("mandatory")
_MscVsFramerNEncodingTable_Object = MibTable
mscVsFramerNEncodingTable = _MscVsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 438)
)
if mibBuilder.loadTexts:
    mscVsFramerNEncodingTable.setStatus("mandatory")
_MscVsFramerNEncodingEntry_Object = MibTableRow
mscVsFramerNEncodingEntry = _MscVsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 438, 1)
)
mscVsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerNEncodingEntry.setStatus("mandatory")


class _MscVsFramerNEncodingIndex_Type(Integer32):
    """Custom type mscVsFramerNEncodingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_MscVsFramerNEncodingIndex_Type.__name__ = "Integer32"
_MscVsFramerNEncodingIndex_Object = MibTableColumn
mscVsFramerNEncodingIndex = _MscVsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 438, 1, 1),
    _MscVsFramerNEncodingIndex_Type()
)
mscVsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerNEncodingIndex.setStatus("mandatory")


class _MscVsFramerNEncodingValue_Type(Integer32):
    """Custom type mscVsFramerNEncodingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              31,
              64,
              68,
              255)
        )
    )
    namedValues = NamedValues(
        *(("g711", 5),
          ("g711G726", 31),
          ("g726", 4),
          ("g728", 2),
          ("g729", 1),
          ("none", 255),
          ("v17V29V27Relay", 68),
          ("v29V27Relay", 64))
    )


_MscVsFramerNEncodingValue_Type.__name__ = "Integer32"
_MscVsFramerNEncodingValue_Object = MibTableColumn
mscVsFramerNEncodingValue = _MscVsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 438, 1, 2),
    _MscVsFramerNEncodingValue_Type()
)
mscVsFramerNEncodingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNEncodingValue.setStatus("mandatory")
_MscVsFramerNRatesTable_Object = MibTable
mscVsFramerNRatesTable = _MscVsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 439)
)
if mibBuilder.loadTexts:
    mscVsFramerNRatesTable.setStatus("mandatory")
_MscVsFramerNRatesEntry_Object = MibTableRow
mscVsFramerNRatesEntry = _MscVsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 439, 1)
)
mscVsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerNRatesTrafficIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVsFramerNRatesEntry.setStatus("mandatory")


class _MscVsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type mscVsFramerNRatesTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fax", 2),
          ("modemFax", 1),
          ("voice", 0))
    )


_MscVsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_MscVsFramerNRatesTrafficIndex_Object = MibTableColumn
mscVsFramerNRatesTrafficIndex = _MscVsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 439, 1, 1),
    _MscVsFramerNRatesTrafficIndex_Type()
)
mscVsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerNRatesTrafficIndex.setStatus("mandatory")


class _MscVsFramerNRatesRateIndex_Type(Integer32):
    """Custom type mscVsFramerNRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_MscVsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_MscVsFramerNRatesRateIndex_Object = MibTableColumn
mscVsFramerNRatesRateIndex = _MscVsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 439, 1, 2),
    _MscVsFramerNRatesRateIndex_Type()
)
mscVsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsFramerNRatesRateIndex.setStatus("mandatory")


class _MscVsFramerNRatesValue_Type(Integer32):
    """Custom type mscVsFramerNRatesValue based on Integer32"""
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
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("n00", 0),
          ("n03", 1),
          ("n12", 2),
          ("n120", 7),
          ("n144", 8),
          ("n160", 67),
          ("n24", 3),
          ("n240", 68),
          ("n320", 69),
          ("n48", 4),
          ("n640", 70),
          ("n72", 5),
          ("n80", 66),
          ("n96", 6))
    )


_MscVsFramerNRatesValue_Type.__name__ = "Integer32"
_MscVsFramerNRatesValue_Object = MibTableColumn
mscVsFramerNRatesValue = _MscVsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 2, 439, 1, 3),
    _MscVsFramerNRatesValue_Type()
)
mscVsFramerNRatesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsFramerNRatesValue.setStatus("mandatory")
_MscVsPlc_ObjectIdentity = ObjectIdentity
mscVsPlc = _MscVsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3)
)
_MscVsPlcRowStatusTable_Object = MibTable
mscVsPlcRowStatusTable = _MscVsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1)
)
if mibBuilder.loadTexts:
    mscVsPlcRowStatusTable.setStatus("mandatory")
_MscVsPlcRowStatusEntry_Object = MibTableRow
mscVsPlcRowStatusEntry = _MscVsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1, 1)
)
mscVsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscVsPlcRowStatusEntry.setStatus("mandatory")
_MscVsPlcRowStatus_Type = RowStatus
_MscVsPlcRowStatus_Object = MibTableColumn
mscVsPlcRowStatus = _MscVsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1, 1, 1),
    _MscVsPlcRowStatus_Type()
)
mscVsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsPlcRowStatus.setStatus("mandatory")
_MscVsPlcComponentName_Type = DisplayString
_MscVsPlcComponentName_Object = MibTableColumn
mscVsPlcComponentName = _MscVsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1, 1, 2),
    _MscVsPlcComponentName_Type()
)
mscVsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsPlcComponentName.setStatus("mandatory")
_MscVsPlcStorageType_Type = StorageType
_MscVsPlcStorageType_Object = MibTableColumn
mscVsPlcStorageType = _MscVsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1, 1, 4),
    _MscVsPlcStorageType_Type()
)
mscVsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsPlcStorageType.setStatus("mandatory")
_MscVsPlcIndex_Type = NonReplicated
_MscVsPlcIndex_Object = MibTableColumn
mscVsPlcIndex = _MscVsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 1, 1, 10),
    _MscVsPlcIndex_Type()
)
mscVsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsPlcIndex.setStatus("mandatory")
_MscVsPlcProvTable_Object = MibTable
mscVsPlcProvTable = _MscVsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10)
)
if mibBuilder.loadTexts:
    mscVsPlcProvTable.setStatus("mandatory")
_MscVsPlcProvEntry_Object = MibTableRow
mscVsPlcProvEntry = _MscVsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1)
)
mscVsPlcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscVsPlcProvEntry.setStatus("mandatory")


class _MscVsPlcRemoteName_Type(AsciiString):
    """Custom type mscVsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsPlcRemoteName_Type.__name__ = "AsciiString"
_MscVsPlcRemoteName_Object = MibTableColumn
mscVsPlcRemoteName = _MscVsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 2),
    _MscVsPlcRemoteName_Type()
)
mscVsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRemoteName.setStatus("mandatory")


class _MscVsPlcSetupPriority_Type(Unsigned32):
    """Custom type mscVsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsPlcSetupPriority_Type.__name__ = "Unsigned32"
_MscVsPlcSetupPriority_Object = MibTableColumn
mscVsPlcSetupPriority = _MscVsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 3),
    _MscVsPlcSetupPriority_Type()
)
mscVsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcSetupPriority.setStatus("mandatory")


class _MscVsPlcHoldingPriority_Type(Unsigned32):
    """Custom type mscVsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_MscVsPlcHoldingPriority_Object = MibTableColumn
mscVsPlcHoldingPriority = _MscVsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 4),
    _MscVsPlcHoldingPriority_Type()
)
mscVsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcHoldingPriority.setStatus("mandatory")


class _MscVsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscVsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscVsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscVsPlcRequiredTxBandwidth_Object = MibTableColumn
mscVsPlcRequiredTxBandwidth = _MscVsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 5),
    _MscVsPlcRequiredTxBandwidth_Type()
)
mscVsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRequiredTxBandwidth.setStatus("mandatory")


class _MscVsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscVsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscVsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscVsPlcRequiredRxBandwidth_Object = MibTableColumn
mscVsPlcRequiredRxBandwidth = _MscVsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 6),
    _MscVsPlcRequiredRxBandwidth_Type()
)
mscVsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRequiredRxBandwidth.setStatus("mandatory")


class _MscVsPlcRequiredTrafficType_Type(Integer32):
    """Custom type mscVsPlcRequiredTrafficType based on Integer32"""
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


_MscVsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_MscVsPlcRequiredTrafficType_Object = MibTableColumn
mscVsPlcRequiredTrafficType = _MscVsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 7),
    _MscVsPlcRequiredTrafficType_Type()
)
mscVsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRequiredTrafficType.setStatus("mandatory")


class _MscVsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type mscVsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscVsPlcPermittedTrunkTypes_Object = MibTableColumn
mscVsPlcPermittedTrunkTypes = _MscVsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 8),
    _MscVsPlcPermittedTrunkTypes_Type()
)
mscVsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcPermittedTrunkTypes.setStatus("mandatory")


class _MscVsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type mscVsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_MscVsPlcRequiredSecurity_Object = MibTableColumn
mscVsPlcRequiredSecurity = _MscVsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 9),
    _MscVsPlcRequiredSecurity_Type()
)
mscVsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRequiredSecurity.setStatus("mandatory")


class _MscVsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscVsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscVsPlcRequiredCustomerParm_Object = MibTableColumn
mscVsPlcRequiredCustomerParm = _MscVsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 10),
    _MscVsPlcRequiredCustomerParm_Type()
)
mscVsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcRequiredCustomerParm.setStatus("mandatory")


class _MscVsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type mscVsPlcPathAttributeToMinimize based on Integer32"""
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


_MscVsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscVsPlcPathAttributeToMinimize_Object = MibTableColumn
mscVsPlcPathAttributeToMinimize = _MscVsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 11),
    _MscVsPlcPathAttributeToMinimize_Type()
)
mscVsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcPathAttributeToMinimize.setStatus("mandatory")


class _MscVsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscVsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscVsPlcMaximumAcceptableCost_Object = MibTableColumn
mscVsPlcMaximumAcceptableCost = _MscVsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 12),
    _MscVsPlcMaximumAcceptableCost_Type()
)
mscVsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcMaximumAcceptableCost.setStatus("mandatory")


class _MscVsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscVsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscVsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscVsPlcMaximumAcceptableDelay_Object = MibTableColumn
mscVsPlcMaximumAcceptableDelay = _MscVsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 13),
    _MscVsPlcMaximumAcceptableDelay_Type()
)
mscVsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _MscVsPlcEmissionPriority_Type(Unsigned32):
    """Custom type mscVsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscVsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_MscVsPlcEmissionPriority_Object = MibTableColumn
mscVsPlcEmissionPriority = _MscVsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 14),
    _MscVsPlcEmissionPriority_Type()
)
mscVsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcEmissionPriority.setStatus("mandatory")


class _MscVsPlcDiscardPriority_Type(Unsigned32):
    """Custom type mscVsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscVsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_MscVsPlcDiscardPriority_Object = MibTableColumn
mscVsPlcDiscardPriority = _MscVsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 15),
    _MscVsPlcDiscardPriority_Type()
)
mscVsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcDiscardPriority.setStatus("mandatory")


class _MscVsPlcPathType_Type(Integer32):
    """Custom type mscVsPlcPathType based on Integer32"""
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


_MscVsPlcPathType_Type.__name__ = "Integer32"
_MscVsPlcPathType_Object = MibTableColumn
mscVsPlcPathType = _MscVsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 16),
    _MscVsPlcPathType_Type()
)
mscVsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcPathType.setStatus("mandatory")


class _MscVsPlcPathFailureAction_Type(Integer32):
    """Custom type mscVsPlcPathFailureAction based on Integer32"""
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


_MscVsPlcPathFailureAction_Type.__name__ = "Integer32"
_MscVsPlcPathFailureAction_Object = MibTableColumn
mscVsPlcPathFailureAction = _MscVsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 17),
    _MscVsPlcPathFailureAction_Type()
)
mscVsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcPathFailureAction.setStatus("mandatory")


class _MscVsPlcBumpPreference_Type(Integer32):
    """Custom type mscVsPlcBumpPreference based on Integer32"""
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


_MscVsPlcBumpPreference_Type.__name__ = "Integer32"
_MscVsPlcBumpPreference_Object = MibTableColumn
mscVsPlcBumpPreference = _MscVsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 18),
    _MscVsPlcBumpPreference_Type()
)
mscVsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcBumpPreference.setStatus("mandatory")


class _MscVsPlcOptimization_Type(Integer32):
    """Custom type mscVsPlcOptimization based on Integer32"""
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


_MscVsPlcOptimization_Type.__name__ = "Integer32"
_MscVsPlcOptimization_Object = MibTableColumn
mscVsPlcOptimization = _MscVsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 19),
    _MscVsPlcOptimization_Type()
)
mscVsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcOptimization.setStatus("mandatory")


class _MscVsPlcAddressToCall_Type(AsciiString):
    """Custom type mscVsPlcAddressToCall based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsPlcAddressToCall_Type.__name__ = "AsciiString"
_MscVsPlcAddressToCall_Object = MibTableColumn
mscVsPlcAddressToCall = _MscVsPlcAddressToCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 20),
    _MscVsPlcAddressToCall_Type()
)
mscVsPlcAddressToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcAddressToCall.setStatus("mandatory")


class _MscVsPlcLocalAddress_Type(AsciiString):
    """Custom type mscVsPlcLocalAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsPlcLocalAddress_Type.__name__ = "AsciiString"
_MscVsPlcLocalAddress_Object = MibTableColumn
mscVsPlcLocalAddress = _MscVsPlcLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 21),
    _MscVsPlcLocalAddress_Type()
)
mscVsPlcLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcLocalAddress.setStatus("mandatory")


class _MscVsPlcMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type mscVsPlcMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsPlcMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_MscVsPlcMaximumAcceptableGatewayCost_Object = MibTableColumn
mscVsPlcMaximumAcceptableGatewayCost = _MscVsPlcMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 10, 1, 22),
    _MscVsPlcMaximumAcceptableGatewayCost_Type()
)
mscVsPlcMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcMaximumAcceptableGatewayCost.setStatus("mandatory")
_MscVsPlcMpathTable_Object = MibTable
mscVsPlcMpathTable = _MscVsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 207)
)
if mibBuilder.loadTexts:
    mscVsPlcMpathTable.setStatus("mandatory")
_MscVsPlcMpathEntry_Object = MibTableRow
mscVsPlcMpathEntry = _MscVsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 207, 1)
)
mscVsPlcMpathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsPlcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    mscVsPlcMpathEntry.setStatus("mandatory")


class _MscVsPlcMpathIndex_Type(Integer32):
    """Custom type mscVsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscVsPlcMpathIndex_Type.__name__ = "Integer32"
_MscVsPlcMpathIndex_Object = MibTableColumn
mscVsPlcMpathIndex = _MscVsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 207, 1, 1),
    _MscVsPlcMpathIndex_Type()
)
mscVsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsPlcMpathIndex.setStatus("mandatory")


class _MscVsPlcMpathValue_Type(AsciiString):
    """Custom type mscVsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsPlcMpathValue_Type.__name__ = "AsciiString"
_MscVsPlcMpathValue_Object = MibTableColumn
mscVsPlcMpathValue = _MscVsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 3, 207, 1, 2),
    _MscVsPlcMpathValue_Type()
)
mscVsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsPlcMpathValue.setStatus("mandatory")
_MscVsLCo_ObjectIdentity = ObjectIdentity
mscVsLCo = _MscVsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4)
)
_MscVsLCoRowStatusTable_Object = MibTable
mscVsLCoRowStatusTable = _MscVsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1)
)
if mibBuilder.loadTexts:
    mscVsLCoRowStatusTable.setStatus("mandatory")
_MscVsLCoRowStatusEntry_Object = MibTableRow
mscVsLCoRowStatusEntry = _MscVsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1, 1)
)
mscVsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsLCoRowStatusEntry.setStatus("mandatory")
_MscVsLCoRowStatus_Type = RowStatus
_MscVsLCoRowStatus_Object = MibTableColumn
mscVsLCoRowStatus = _MscVsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1, 1, 1),
    _MscVsLCoRowStatus_Type()
)
mscVsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRowStatus.setStatus("mandatory")
_MscVsLCoComponentName_Type = DisplayString
_MscVsLCoComponentName_Object = MibTableColumn
mscVsLCoComponentName = _MscVsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1, 1, 2),
    _MscVsLCoComponentName_Type()
)
mscVsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoComponentName.setStatus("mandatory")
_MscVsLCoStorageType_Type = StorageType
_MscVsLCoStorageType_Object = MibTableColumn
mscVsLCoStorageType = _MscVsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1, 1, 4),
    _MscVsLCoStorageType_Type()
)
mscVsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoStorageType.setStatus("mandatory")
_MscVsLCoIndex_Type = NonReplicated
_MscVsLCoIndex_Object = MibTableColumn
mscVsLCoIndex = _MscVsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 1, 1, 10),
    _MscVsLCoIndex_Type()
)
mscVsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsLCoIndex.setStatus("mandatory")
_MscVsLCoPathDataTable_Object = MibTable
mscVsLCoPathDataTable = _MscVsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10)
)
if mibBuilder.loadTexts:
    mscVsLCoPathDataTable.setStatus("mandatory")
_MscVsLCoPathDataEntry_Object = MibTableRow
mscVsLCoPathDataEntry = _MscVsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1)
)
mscVsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsLCoPathDataEntry.setStatus("mandatory")


class _MscVsLCoState_Type(Integer32):
    """Custom type mscVsLCoState based on Integer32"""
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


_MscVsLCoState_Type.__name__ = "Integer32"
_MscVsLCoState_Object = MibTableColumn
mscVsLCoState = _MscVsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 1),
    _MscVsLCoState_Type()
)
mscVsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoState.setStatus("mandatory")


class _MscVsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscVsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscVsLCoOverrideRemoteName_Object = MibTableColumn
mscVsLCoOverrideRemoteName = _MscVsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 2),
    _MscVsLCoOverrideRemoteName_Type()
)
mscVsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsLCoOverrideRemoteName.setStatus("mandatory")


class _MscVsLCoEnd_Type(Integer32):
    """Custom type mscVsLCoEnd based on Integer32"""
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


_MscVsLCoEnd_Type.__name__ = "Integer32"
_MscVsLCoEnd_Object = MibTableColumn
mscVsLCoEnd = _MscVsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 3),
    _MscVsLCoEnd_Type()
)
mscVsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoEnd.setStatus("mandatory")


class _MscVsLCoCostMetric_Type(Unsigned32):
    """Custom type mscVsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsLCoCostMetric_Type.__name__ = "Unsigned32"
_MscVsLCoCostMetric_Object = MibTableColumn
mscVsLCoCostMetric = _MscVsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 4),
    _MscVsLCoCostMetric_Type()
)
mscVsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoCostMetric.setStatus("mandatory")


class _MscVsLCoDelayMetric_Type(Unsigned32):
    """Custom type mscVsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscVsLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscVsLCoDelayMetric_Object = MibTableColumn
mscVsLCoDelayMetric = _MscVsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 5),
    _MscVsLCoDelayMetric_Type()
)
mscVsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoDelayMetric.setStatus("mandatory")


class _MscVsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscVsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscVsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscVsLCoRoundTripDelay_Object = MibTableColumn
mscVsLCoRoundTripDelay = _MscVsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 6),
    _MscVsLCoRoundTripDelay_Type()
)
mscVsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRoundTripDelay.setStatus("mandatory")


class _MscVsLCoSetupPriority_Type(Unsigned32):
    """Custom type mscVsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscVsLCoSetupPriority_Object = MibTableColumn
mscVsLCoSetupPriority = _MscVsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 7),
    _MscVsLCoSetupPriority_Type()
)
mscVsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoSetupPriority.setStatus("mandatory")


class _MscVsLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscVsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscVsLCoHoldingPriority_Object = MibTableColumn
mscVsLCoHoldingPriority = _MscVsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 8),
    _MscVsLCoHoldingPriority_Type()
)
mscVsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoHoldingPriority.setStatus("mandatory")


class _MscVsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscVsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscVsLCoRequiredTxBandwidth_Object = MibTableColumn
mscVsLCoRequiredTxBandwidth = _MscVsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 9),
    _MscVsLCoRequiredTxBandwidth_Type()
)
mscVsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscVsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscVsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscVsLCoRequiredRxBandwidth_Object = MibTableColumn
mscVsLCoRequiredRxBandwidth = _MscVsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 10),
    _MscVsLCoRequiredRxBandwidth_Type()
)
mscVsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscVsLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscVsLCoRequiredTrafficType based on Integer32"""
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


_MscVsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscVsLCoRequiredTrafficType_Object = MibTableColumn
mscVsLCoRequiredTrafficType = _MscVsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 11),
    _MscVsLCoRequiredTrafficType_Type()
)
mscVsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRequiredTrafficType.setStatus("mandatory")


class _MscVsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscVsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscVsLCoPermittedTrunkTypes_Object = MibTableColumn
mscVsLCoPermittedTrunkTypes = _MscVsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 12),
    _MscVsLCoPermittedTrunkTypes_Type()
)
mscVsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscVsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscVsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscVsLCoRequiredSecurity_Object = MibTableColumn
mscVsLCoRequiredSecurity = _MscVsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 13),
    _MscVsLCoRequiredSecurity_Type()
)
mscVsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRequiredSecurity.setStatus("mandatory")


class _MscVsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscVsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscVsLCoRequiredCustomerParameter_Object = MibTableColumn
mscVsLCoRequiredCustomerParameter = _MscVsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 14),
    _MscVsLCoRequiredCustomerParameter_Type()
)
mscVsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscVsLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscVsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscVsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscVsLCoEmissionPriority_Object = MibTableColumn
mscVsLCoEmissionPriority = _MscVsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 15),
    _MscVsLCoEmissionPriority_Type()
)
mscVsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoEmissionPriority.setStatus("mandatory")


class _MscVsLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscVsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscVsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscVsLCoDiscardPriority_Object = MibTableColumn
mscVsLCoDiscardPriority = _MscVsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 16),
    _MscVsLCoDiscardPriority_Type()
)
mscVsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoDiscardPriority.setStatus("mandatory")


class _MscVsLCoPathType_Type(Integer32):
    """Custom type mscVsLCoPathType based on Integer32"""
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


_MscVsLCoPathType_Type.__name__ = "Integer32"
_MscVsLCoPathType_Object = MibTableColumn
mscVsLCoPathType = _MscVsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 17),
    _MscVsLCoPathType_Type()
)
mscVsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPathType.setStatus("mandatory")


class _MscVsLCoRetryCount_Type(Unsigned32):
    """Custom type mscVsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVsLCoRetryCount_Type.__name__ = "Unsigned32"
_MscVsLCoRetryCount_Object = MibTableColumn
mscVsLCoRetryCount = _MscVsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 18),
    _MscVsLCoRetryCount_Type()
)
mscVsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoRetryCount.setStatus("mandatory")


class _MscVsLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscVsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscVsLCoPathFailureCount_Object = MibTableColumn
mscVsLCoPathFailureCount = _MscVsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 19),
    _MscVsLCoPathFailureCount_Type()
)
mscVsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPathFailureCount.setStatus("mandatory")


class _MscVsLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscVsLCoReasonForNoRoute based on Integer32"""
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


_MscVsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscVsLCoReasonForNoRoute_Object = MibTableColumn
mscVsLCoReasonForNoRoute = _MscVsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 20),
    _MscVsLCoReasonForNoRoute_Type()
)
mscVsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoReasonForNoRoute.setStatus("mandatory")


class _MscVsLCoLastTearDownReason_Type(Integer32):
    """Custom type mscVsLCoLastTearDownReason based on Integer32"""
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


_MscVsLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscVsLCoLastTearDownReason_Object = MibTableColumn
mscVsLCoLastTearDownReason = _MscVsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 21),
    _MscVsLCoLastTearDownReason_Type()
)
mscVsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoLastTearDownReason.setStatus("mandatory")


class _MscVsLCoPathFailureAction_Type(Integer32):
    """Custom type mscVsLCoPathFailureAction based on Integer32"""
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


_MscVsLCoPathFailureAction_Type.__name__ = "Integer32"
_MscVsLCoPathFailureAction_Object = MibTableColumn
mscVsLCoPathFailureAction = _MscVsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 22),
    _MscVsLCoPathFailureAction_Type()
)
mscVsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPathFailureAction.setStatus("mandatory")


class _MscVsLCoBumpPreference_Type(Integer32):
    """Custom type mscVsLCoBumpPreference based on Integer32"""
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


_MscVsLCoBumpPreference_Type.__name__ = "Integer32"
_MscVsLCoBumpPreference_Object = MibTableColumn
mscVsLCoBumpPreference = _MscVsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 23),
    _MscVsLCoBumpPreference_Type()
)
mscVsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoBumpPreference.setStatus("mandatory")


class _MscVsLCoOptimization_Type(Integer32):
    """Custom type mscVsLCoOptimization based on Integer32"""
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


_MscVsLCoOptimization_Type.__name__ = "Integer32"
_MscVsLCoOptimization_Object = MibTableColumn
mscVsLCoOptimization = _MscVsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 24),
    _MscVsLCoOptimization_Type()
)
mscVsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoOptimization.setStatus("mandatory")


class _MscVsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscVsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscVsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscVsLCoPathUpDateTime_Object = MibTableColumn
mscVsLCoPathUpDateTime = _MscVsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 10, 1, 25),
    _MscVsLCoPathUpDateTime_Type()
)
mscVsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPathUpDateTime.setStatus("mandatory")
_MscVsLCoStatsTable_Object = MibTable
mscVsLCoStatsTable = _MscVsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11)
)
if mibBuilder.loadTexts:
    mscVsLCoStatsTable.setStatus("mandatory")
_MscVsLCoStatsEntry_Object = MibTableRow
mscVsLCoStatsEntry = _MscVsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11, 1)
)
mscVsLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsLCoStatsEntry.setStatus("mandatory")
_MscVsLCoPktsToNetwork_Type = PassportCounter64
_MscVsLCoPktsToNetwork_Object = MibTableColumn
mscVsLCoPktsToNetwork = _MscVsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11, 1, 1),
    _MscVsLCoPktsToNetwork_Type()
)
mscVsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPktsToNetwork.setStatus("mandatory")
_MscVsLCoBytesToNetwork_Type = PassportCounter64
_MscVsLCoBytesToNetwork_Object = MibTableColumn
mscVsLCoBytesToNetwork = _MscVsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11, 1, 2),
    _MscVsLCoBytesToNetwork_Type()
)
mscVsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoBytesToNetwork.setStatus("mandatory")
_MscVsLCoPktsFromNetwork_Type = PassportCounter64
_MscVsLCoPktsFromNetwork_Object = MibTableColumn
mscVsLCoPktsFromNetwork = _MscVsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11, 1, 3),
    _MscVsLCoPktsFromNetwork_Type()
)
mscVsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPktsFromNetwork.setStatus("mandatory")
_MscVsLCoBytesFromNetwork_Type = PassportCounter64
_MscVsLCoBytesFromNetwork_Object = MibTableColumn
mscVsLCoBytesFromNetwork = _MscVsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 11, 1, 4),
    _MscVsLCoBytesFromNetwork_Type()
)
mscVsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoBytesFromNetwork.setStatus("mandatory")
_MscVsLCoPathTable_Object = MibTable
mscVsLCoPathTable = _MscVsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 264)
)
if mibBuilder.loadTexts:
    mscVsLCoPathTable.setStatus("mandatory")
_MscVsLCoPathEntry_Object = MibTableRow
mscVsLCoPathEntry = _MscVsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 264, 1)
)
mscVsLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscVsLCoPathEntry.setStatus("mandatory")


class _MscVsLCoPathValue_Type(AsciiString):
    """Custom type mscVsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsLCoPathValue_Type.__name__ = "AsciiString"
_MscVsLCoPathValue_Object = MibTableColumn
mscVsLCoPathValue = _MscVsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 4, 264, 1, 1),
    _MscVsLCoPathValue_Type()
)
mscVsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsLCoPathValue.setStatus("mandatory")
_MscVsCidDataTable_Object = MibTable
mscVsCidDataTable = _MscVsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 10)
)
if mibBuilder.loadTexts:
    mscVsCidDataTable.setStatus("mandatory")
_MscVsCidDataEntry_Object = MibTableRow
mscVsCidDataEntry = _MscVsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 10, 1)
)
mscVsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsCidDataEntry.setStatus("mandatory")


class _MscVsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscVsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscVsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscVsCustomerIdentifier_Object = MibTableColumn
mscVsCustomerIdentifier = _MscVsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 10, 1, 1),
    _MscVsCustomerIdentifier_Type()
)
mscVsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsCustomerIdentifier.setStatus("mandatory")
_MscVsIfEntryTable_Object = MibTable
mscVsIfEntryTable = _MscVsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 11)
)
if mibBuilder.loadTexts:
    mscVsIfEntryTable.setStatus("mandatory")
_MscVsIfEntryEntry_Object = MibTableRow
mscVsIfEntryEntry = _MscVsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 11, 1)
)
mscVsIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsIfEntryEntry.setStatus("mandatory")


class _MscVsIfAdminStatus_Type(Integer32):
    """Custom type mscVsIfAdminStatus based on Integer32"""
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


_MscVsIfAdminStatus_Type.__name__ = "Integer32"
_MscVsIfAdminStatus_Object = MibTableColumn
mscVsIfAdminStatus = _MscVsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 11, 1, 1),
    _MscVsIfAdminStatus_Type()
)
mscVsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsIfAdminStatus.setStatus("mandatory")


class _MscVsIfIndex_Type(InterfaceIndex):
    """Custom type mscVsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVsIfIndex_Type.__name__ = "InterfaceIndex"
_MscVsIfIndex_Object = MibTableColumn
mscVsIfIndex = _MscVsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 11, 1, 2),
    _MscVsIfIndex_Type()
)
mscVsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsIfIndex.setStatus("mandatory")
_MscVsOperStatusTable_Object = MibTable
mscVsOperStatusTable = _MscVsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 12)
)
if mibBuilder.loadTexts:
    mscVsOperStatusTable.setStatus("mandatory")
_MscVsOperStatusEntry_Object = MibTableRow
mscVsOperStatusEntry = _MscVsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 12, 1)
)
mscVsOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsOperStatusEntry.setStatus("mandatory")


class _MscVsSnmpOperStatus_Type(Integer32):
    """Custom type mscVsSnmpOperStatus based on Integer32"""
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


_MscVsSnmpOperStatus_Type.__name__ = "Integer32"
_MscVsSnmpOperStatus_Object = MibTableColumn
mscVsSnmpOperStatus = _MscVsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 12, 1, 1),
    _MscVsSnmpOperStatus_Type()
)
mscVsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsSnmpOperStatus.setStatus("mandatory")
_MscVsStateTable_Object = MibTable
mscVsStateTable = _MscVsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13)
)
if mibBuilder.loadTexts:
    mscVsStateTable.setStatus("mandatory")
_MscVsStateEntry_Object = MibTableRow
mscVsStateEntry = _MscVsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1)
)
mscVsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsStateEntry.setStatus("mandatory")


class _MscVsAdminState_Type(Integer32):
    """Custom type mscVsAdminState based on Integer32"""
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


_MscVsAdminState_Type.__name__ = "Integer32"
_MscVsAdminState_Object = MibTableColumn
mscVsAdminState = _MscVsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 1),
    _MscVsAdminState_Type()
)
mscVsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsAdminState.setStatus("mandatory")


class _MscVsOperationalState_Type(Integer32):
    """Custom type mscVsOperationalState based on Integer32"""
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


_MscVsOperationalState_Type.__name__ = "Integer32"
_MscVsOperationalState_Object = MibTableColumn
mscVsOperationalState = _MscVsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 2),
    _MscVsOperationalState_Type()
)
mscVsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsOperationalState.setStatus("mandatory")


class _MscVsUsageState_Type(Integer32):
    """Custom type mscVsUsageState based on Integer32"""
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


_MscVsUsageState_Type.__name__ = "Integer32"
_MscVsUsageState_Object = MibTableColumn
mscVsUsageState = _MscVsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 3),
    _MscVsUsageState_Type()
)
mscVsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsUsageState.setStatus("mandatory")


class _MscVsAvailabilityStatus_Type(OctetString):
    """Custom type mscVsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVsAvailabilityStatus_Type.__name__ = "OctetString"
_MscVsAvailabilityStatus_Object = MibTableColumn
mscVsAvailabilityStatus = _MscVsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 4),
    _MscVsAvailabilityStatus_Type()
)
mscVsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsAvailabilityStatus.setStatus("mandatory")


class _MscVsProceduralStatus_Type(OctetString):
    """Custom type mscVsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsProceduralStatus_Type.__name__ = "OctetString"
_MscVsProceduralStatus_Object = MibTableColumn
mscVsProceduralStatus = _MscVsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 5),
    _MscVsProceduralStatus_Type()
)
mscVsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsProceduralStatus.setStatus("mandatory")


class _MscVsControlStatus_Type(OctetString):
    """Custom type mscVsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsControlStatus_Type.__name__ = "OctetString"
_MscVsControlStatus_Object = MibTableColumn
mscVsControlStatus = _MscVsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 6),
    _MscVsControlStatus_Type()
)
mscVsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsControlStatus.setStatus("mandatory")


class _MscVsAlarmStatus_Type(OctetString):
    """Custom type mscVsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsAlarmStatus_Type.__name__ = "OctetString"
_MscVsAlarmStatus_Object = MibTableColumn
mscVsAlarmStatus = _MscVsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 7),
    _MscVsAlarmStatus_Type()
)
mscVsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsAlarmStatus.setStatus("mandatory")


class _MscVsStandbyStatus_Type(Integer32):
    """Custom type mscVsStandbyStatus based on Integer32"""
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


_MscVsStandbyStatus_Type.__name__ = "Integer32"
_MscVsStandbyStatus_Object = MibTableColumn
mscVsStandbyStatus = _MscVsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 8),
    _MscVsStandbyStatus_Type()
)
mscVsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsStandbyStatus.setStatus("mandatory")


class _MscVsUnknownStatus_Type(Integer32):
    """Custom type mscVsUnknownStatus based on Integer32"""
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


_MscVsUnknownStatus_Type.__name__ = "Integer32"
_MscVsUnknownStatus_Object = MibTableColumn
mscVsUnknownStatus = _MscVsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 13, 1, 9),
    _MscVsUnknownStatus_Type()
)
mscVsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsUnknownStatus.setStatus("mandatory")
_MscVsOperationalTable_Object = MibTable
mscVsOperationalTable = _MscVsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 15)
)
if mibBuilder.loadTexts:
    mscVsOperationalTable.setStatus("mandatory")
_MscVsOperationalEntry_Object = MibTableRow
mscVsOperationalEntry = _MscVsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 15, 1)
)
mscVsOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceMIB", "mscVsIndex"),
)
if mibBuilder.loadTexts:
    mscVsOperationalEntry.setStatus("mandatory")


class _MscVsServiceFailureReason_Type(OctetString):
    """Custom type mscVsServiceFailureReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVsServiceFailureReason_Type.__name__ = "OctetString"
_MscVsServiceFailureReason_Object = MibTableColumn
mscVsServiceFailureReason = _MscVsServiceFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 80, 15, 1, 1),
    _MscVsServiceFailureReason_Type()
)
mscVsServiceFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsServiceFailureReason.setStatus("mandatory")
_VoiceMIB_ObjectIdentity = ObjectIdentity
voiceMIB = _VoiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49)
)
_VoiceGroup_ObjectIdentity = ObjectIdentity
voiceGroup = _VoiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 1)
)
_VoiceGroupCA_ObjectIdentity = ObjectIdentity
voiceGroupCA = _VoiceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 1, 1)
)
_VoiceGroupCA02_ObjectIdentity = ObjectIdentity
voiceGroupCA02 = _VoiceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 1, 1, 3)
)
_VoiceGroupCA02A_ObjectIdentity = ObjectIdentity
voiceGroupCA02A = _VoiceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 1, 1, 3, 2)
)
_VoiceCapabilities_ObjectIdentity = ObjectIdentity
voiceCapabilities = _VoiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 3)
)
_VoiceCapabilitiesCA_ObjectIdentity = ObjectIdentity
voiceCapabilitiesCA = _VoiceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 3, 1)
)
_VoiceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
voiceCapabilitiesCA02 = _VoiceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 3, 1, 3)
)
_VoiceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
voiceCapabilitiesCA02A = _VoiceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 49, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VoiceMIB",
    **{"mscVs": mscVs,
       "mscVsRowStatusTable": mscVsRowStatusTable,
       "mscVsRowStatusEntry": mscVsRowStatusEntry,
       "mscVsRowStatus": mscVsRowStatus,
       "mscVsComponentName": mscVsComponentName,
       "mscVsStorageType": mscVsStorageType,
       "mscVsIndex": mscVsIndex,
       "mscVsFramer": mscVsFramer,
       "mscVsFramerRowStatusTable": mscVsFramerRowStatusTable,
       "mscVsFramerRowStatusEntry": mscVsFramerRowStatusEntry,
       "mscVsFramerRowStatus": mscVsFramerRowStatus,
       "mscVsFramerComponentName": mscVsFramerComponentName,
       "mscVsFramerStorageType": mscVsFramerStorageType,
       "mscVsFramerIndex": mscVsFramerIndex,
       "mscVsFramerVfpDebug": mscVsFramerVfpDebug,
       "mscVsFramerVfpDebugRowStatusTable": mscVsFramerVfpDebugRowStatusTable,
       "mscVsFramerVfpDebugRowStatusEntry": mscVsFramerVfpDebugRowStatusEntry,
       "mscVsFramerVfpDebugRowStatus": mscVsFramerVfpDebugRowStatus,
       "mscVsFramerVfpDebugComponentName": mscVsFramerVfpDebugComponentName,
       "mscVsFramerVfpDebugStorageType": mscVsFramerVfpDebugStorageType,
       "mscVsFramerVfpDebugIndex": mscVsFramerVfpDebugIndex,
       "mscVsFramerMvpDebug": mscVsFramerMvpDebug,
       "mscVsFramerMvpDebugRowStatusTable": mscVsFramerMvpDebugRowStatusTable,
       "mscVsFramerMvpDebugRowStatusEntry": mscVsFramerMvpDebugRowStatusEntry,
       "mscVsFramerMvpDebugRowStatus": mscVsFramerMvpDebugRowStatus,
       "mscVsFramerMvpDebugComponentName": mscVsFramerMvpDebugComponentName,
       "mscVsFramerMvpDebugStorageType": mscVsFramerMvpDebugStorageType,
       "mscVsFramerMvpDebugIndex": mscVsFramerMvpDebugIndex,
       "mscVsFramerPcmCapture": mscVsFramerPcmCapture,
       "mscVsFramerPcmCaptureRowStatusTable": mscVsFramerPcmCaptureRowStatusTable,
       "mscVsFramerPcmCaptureRowStatusEntry": mscVsFramerPcmCaptureRowStatusEntry,
       "mscVsFramerPcmCaptureRowStatus": mscVsFramerPcmCaptureRowStatus,
       "mscVsFramerPcmCaptureComponentName": mscVsFramerPcmCaptureComponentName,
       "mscVsFramerPcmCaptureStorageType": mscVsFramerPcmCaptureStorageType,
       "mscVsFramerPcmCaptureIndex": mscVsFramerPcmCaptureIndex,
       "mscVsFramerProvTable": mscVsFramerProvTable,
       "mscVsFramerProvEntry": mscVsFramerProvEntry,
       "mscVsFramerInterfaceName": mscVsFramerInterfaceName,
       "mscVsFramerCoderTable": mscVsFramerCoderTable,
       "mscVsFramerCoderEntry": mscVsFramerCoderEntry,
       "mscVsFramerMaxVoiceBitRate": mscVsFramerMaxVoiceBitRate,
       "mscVsFramerMinVoiceBitRate": mscVsFramerMinVoiceBitRate,
       "mscVsFramerMaxModemBitRate": mscVsFramerMaxModemBitRate,
       "mscVsFramerMinModemBitRate": mscVsFramerMinModemBitRate,
       "mscVsFramerAudioGain": mscVsFramerAudioGain,
       "mscVsFramerSilenceSuppression": mscVsFramerSilenceSuppression,
       "mscVsFramerEchoCancellation": mscVsFramerEchoCancellation,
       "mscVsFramerALawConversion": mscVsFramerALawConversion,
       "mscVsFramerVoiceEncoding": mscVsFramerVoiceEncoding,
       "mscVsFramerFaxEncoding": mscVsFramerFaxEncoding,
       "mscVsFramerTandemPassThrough": mscVsFramerTandemPassThrough,
       "mscVsFramerInsertedOutputDelay": mscVsFramerInsertedOutputDelay,
       "mscVsFramerEgressAudioGain": mscVsFramerEgressAudioGain,
       "mscVsFramerFaxIdleSuppressionG711G726": mscVsFramerFaxIdleSuppressionG711G726,
       "mscVsFramerEndOfCallPattern": mscVsFramerEndOfCallPattern,
       "mscVsFramerIngressAudioGain": mscVsFramerIngressAudioGain,
       "mscVsFramerEgressGain": mscVsFramerEgressGain,
       "mscVsFramerComfortNoiseCap": mscVsFramerComfortNoiseCap,
       "mscVsFramerEchoTailDelay": mscVsFramerEchoTailDelay,
       "mscVsFramerEchoReturnLoss": mscVsFramerEchoReturnLoss,
       "mscVsFramerDtmfRegeneration": mscVsFramerDtmfRegeneration,
       "mscVsFramerSpeechHangoverTime": mscVsFramerSpeechHangoverTime,
       "mscVsFramerFaxHangoverTimeG711G726": mscVsFramerFaxHangoverTimeG711G726,
       "mscVsFramerModemFaxSpeechDiscrim": mscVsFramerModemFaxSpeechDiscrim,
       "mscVsFramerV17EncodedAsG711G726": mscVsFramerV17EncodedAsG711G726,
       "mscVsFramerEcanBypassMode": mscVsFramerEcanBypassMode,
       "mscVsFramerMaxFaxRelayRate": mscVsFramerMaxFaxRelayRate,
       "mscVsFramerSignalTable": mscVsFramerSignalTable,
       "mscVsFramerSignalEntry": mscVsFramerSignalEntry,
       "mscVsFramerTransmitBusyYellow": mscVsFramerTransmitBusyYellow,
       "mscVsFramerTransportSignalling": mscVsFramerTransportSignalling,
       "mscVsFramerInterpretSignalling": mscVsFramerInterpretSignalling,
       "mscVsFramerInvertBits": mscVsFramerInvertBits,
       "mscVsFramerSignalBits": mscVsFramerSignalBits,
       "mscVsFramerTransmitCasYellow": mscVsFramerTransmitCasYellow,
       "mscVsFramerCasSignalling": mscVsFramerCasSignalling,
       "mscVsFramerStateTable": mscVsFramerStateTable,
       "mscVsFramerStateEntry": mscVsFramerStateEntry,
       "mscVsFramerAdminState": mscVsFramerAdminState,
       "mscVsFramerOperationalState": mscVsFramerOperationalState,
       "mscVsFramerUsageState": mscVsFramerUsageState,
       "mscVsFramerStatsTable": mscVsFramerStatsTable,
       "mscVsFramerStatsEntry": mscVsFramerStatsEntry,
       "mscVsFramerTotalCells": mscVsFramerTotalCells,
       "mscVsFramerAudioCells": mscVsFramerAudioCells,
       "mscVsFramerSilenceCells": mscVsFramerSilenceCells,
       "mscVsFramerModemCells": mscVsFramerModemCells,
       "mscVsFramerCurrentEncodingRate": mscVsFramerCurrentEncodingRate,
       "mscVsFramerLrcErrors": mscVsFramerLrcErrors,
       "mscVsFramerFrmLostInNetwork": mscVsFramerFrmLostInNetwork,
       "mscVsFramerFrmUnderRuns": mscVsFramerFrmUnderRuns,
       "mscVsFramerFrmDumped": mscVsFramerFrmDumped,
       "mscVsFramerModemSilenceCells": mscVsFramerModemSilenceCells,
       "mscVsFramerTptStatus": mscVsFramerTptStatus,
       "mscVsFramerCurrentEncoding": mscVsFramerCurrentEncoding,
       "mscVsFramerRecentIngressLineSamples": mscVsFramerRecentIngressLineSamples,
       "mscVsFramerSentMinVoiceG711G726Rate": mscVsFramerSentMinVoiceG711G726Rate,
       "mscVsFramerSentMinModemFaxG711G726Rate": mscVsFramerSentMinModemFaxG711G726Rate,
       "mscVsFramerSentFaxIdleSuppressionG711G726": mscVsFramerSentFaxIdleSuppressionG711G726,
       "mscVsFramerSentSilenceSuppression": mscVsFramerSentSilenceSuppression,
       "mscVsFramerFaxRelayCells": mscVsFramerFaxRelayCells,
       "mscVsFramerModemFaxCells": mscVsFramerModemFaxCells,
       "mscVsFramerFaxIdleCells": mscVsFramerFaxIdleCells,
       "mscVsFramerNegTable": mscVsFramerNegTable,
       "mscVsFramerNegEntry": mscVsFramerNegEntry,
       "mscVsFramerNegotiatedIgSilenceSuppression": mscVsFramerNegotiatedIgSilenceSuppression,
       "mscVsFramerNegotiatedIgFisG711G726": mscVsFramerNegotiatedIgFisG711G726,
       "mscVsFramerNegotiatedDtmfRegeneration": mscVsFramerNegotiatedDtmfRegeneration,
       "mscVsFramerNegotiatedV17AsG711G726": mscVsFramerNegotiatedV17AsG711G726,
       "mscVsFramerNegotiatedTandemPassThrough": mscVsFramerNegotiatedTandemPassThrough,
       "mscVsFramerOperTable": mscVsFramerOperTable,
       "mscVsFramerOperEntry": mscVsFramerOperEntry,
       "mscVsFramerOpCurrentEncoding": mscVsFramerOpCurrentEncoding,
       "mscVsFramerCurrentRate": mscVsFramerCurrentRate,
       "mscVsFramerOpTptStatus": mscVsFramerOpTptStatus,
       "mscVsFramerOpRecentIngressLineSamples": mscVsFramerOpRecentIngressLineSamples,
       "mscVsFramerIdleCodeTable": mscVsFramerIdleCodeTable,
       "mscVsFramerIdleCodeEntry": mscVsFramerIdleCodeEntry,
       "mscVsFramerIdleCodeIndex": mscVsFramerIdleCodeIndex,
       "mscVsFramerIdleCodeValue": mscVsFramerIdleCodeValue,
       "mscVsFramerSeizeCodeTable": mscVsFramerSeizeCodeTable,
       "mscVsFramerSeizeCodeEntry": mscVsFramerSeizeCodeEntry,
       "mscVsFramerSeizeCodeIndex": mscVsFramerSeizeCodeIndex,
       "mscVsFramerSeizeCodeValue": mscVsFramerSeizeCodeValue,
       "mscVsFramerFrmToNetworkTable": mscVsFramerFrmToNetworkTable,
       "mscVsFramerFrmToNetworkEntry": mscVsFramerFrmToNetworkEntry,
       "mscVsFramerFrmToNetworkIndex": mscVsFramerFrmToNetworkIndex,
       "mscVsFramerFrmToNetworkValue": mscVsFramerFrmToNetworkValue,
       "mscVsFramerNEncodingTable": mscVsFramerNEncodingTable,
       "mscVsFramerNEncodingEntry": mscVsFramerNEncodingEntry,
       "mscVsFramerNEncodingIndex": mscVsFramerNEncodingIndex,
       "mscVsFramerNEncodingValue": mscVsFramerNEncodingValue,
       "mscVsFramerNRatesTable": mscVsFramerNRatesTable,
       "mscVsFramerNRatesEntry": mscVsFramerNRatesEntry,
       "mscVsFramerNRatesTrafficIndex": mscVsFramerNRatesTrafficIndex,
       "mscVsFramerNRatesRateIndex": mscVsFramerNRatesRateIndex,
       "mscVsFramerNRatesValue": mscVsFramerNRatesValue,
       "mscVsPlc": mscVsPlc,
       "mscVsPlcRowStatusTable": mscVsPlcRowStatusTable,
       "mscVsPlcRowStatusEntry": mscVsPlcRowStatusEntry,
       "mscVsPlcRowStatus": mscVsPlcRowStatus,
       "mscVsPlcComponentName": mscVsPlcComponentName,
       "mscVsPlcStorageType": mscVsPlcStorageType,
       "mscVsPlcIndex": mscVsPlcIndex,
       "mscVsPlcProvTable": mscVsPlcProvTable,
       "mscVsPlcProvEntry": mscVsPlcProvEntry,
       "mscVsPlcRemoteName": mscVsPlcRemoteName,
       "mscVsPlcSetupPriority": mscVsPlcSetupPriority,
       "mscVsPlcHoldingPriority": mscVsPlcHoldingPriority,
       "mscVsPlcRequiredTxBandwidth": mscVsPlcRequiredTxBandwidth,
       "mscVsPlcRequiredRxBandwidth": mscVsPlcRequiredRxBandwidth,
       "mscVsPlcRequiredTrafficType": mscVsPlcRequiredTrafficType,
       "mscVsPlcPermittedTrunkTypes": mscVsPlcPermittedTrunkTypes,
       "mscVsPlcRequiredSecurity": mscVsPlcRequiredSecurity,
       "mscVsPlcRequiredCustomerParm": mscVsPlcRequiredCustomerParm,
       "mscVsPlcPathAttributeToMinimize": mscVsPlcPathAttributeToMinimize,
       "mscVsPlcMaximumAcceptableCost": mscVsPlcMaximumAcceptableCost,
       "mscVsPlcMaximumAcceptableDelay": mscVsPlcMaximumAcceptableDelay,
       "mscVsPlcEmissionPriority": mscVsPlcEmissionPriority,
       "mscVsPlcDiscardPriority": mscVsPlcDiscardPriority,
       "mscVsPlcPathType": mscVsPlcPathType,
       "mscVsPlcPathFailureAction": mscVsPlcPathFailureAction,
       "mscVsPlcBumpPreference": mscVsPlcBumpPreference,
       "mscVsPlcOptimization": mscVsPlcOptimization,
       "mscVsPlcAddressToCall": mscVsPlcAddressToCall,
       "mscVsPlcLocalAddress": mscVsPlcLocalAddress,
       "mscVsPlcMaximumAcceptableGatewayCost": mscVsPlcMaximumAcceptableGatewayCost,
       "mscVsPlcMpathTable": mscVsPlcMpathTable,
       "mscVsPlcMpathEntry": mscVsPlcMpathEntry,
       "mscVsPlcMpathIndex": mscVsPlcMpathIndex,
       "mscVsPlcMpathValue": mscVsPlcMpathValue,
       "mscVsLCo": mscVsLCo,
       "mscVsLCoRowStatusTable": mscVsLCoRowStatusTable,
       "mscVsLCoRowStatusEntry": mscVsLCoRowStatusEntry,
       "mscVsLCoRowStatus": mscVsLCoRowStatus,
       "mscVsLCoComponentName": mscVsLCoComponentName,
       "mscVsLCoStorageType": mscVsLCoStorageType,
       "mscVsLCoIndex": mscVsLCoIndex,
       "mscVsLCoPathDataTable": mscVsLCoPathDataTable,
       "mscVsLCoPathDataEntry": mscVsLCoPathDataEntry,
       "mscVsLCoState": mscVsLCoState,
       "mscVsLCoOverrideRemoteName": mscVsLCoOverrideRemoteName,
       "mscVsLCoEnd": mscVsLCoEnd,
       "mscVsLCoCostMetric": mscVsLCoCostMetric,
       "mscVsLCoDelayMetric": mscVsLCoDelayMetric,
       "mscVsLCoRoundTripDelay": mscVsLCoRoundTripDelay,
       "mscVsLCoSetupPriority": mscVsLCoSetupPriority,
       "mscVsLCoHoldingPriority": mscVsLCoHoldingPriority,
       "mscVsLCoRequiredTxBandwidth": mscVsLCoRequiredTxBandwidth,
       "mscVsLCoRequiredRxBandwidth": mscVsLCoRequiredRxBandwidth,
       "mscVsLCoRequiredTrafficType": mscVsLCoRequiredTrafficType,
       "mscVsLCoPermittedTrunkTypes": mscVsLCoPermittedTrunkTypes,
       "mscVsLCoRequiredSecurity": mscVsLCoRequiredSecurity,
       "mscVsLCoRequiredCustomerParameter": mscVsLCoRequiredCustomerParameter,
       "mscVsLCoEmissionPriority": mscVsLCoEmissionPriority,
       "mscVsLCoDiscardPriority": mscVsLCoDiscardPriority,
       "mscVsLCoPathType": mscVsLCoPathType,
       "mscVsLCoRetryCount": mscVsLCoRetryCount,
       "mscVsLCoPathFailureCount": mscVsLCoPathFailureCount,
       "mscVsLCoReasonForNoRoute": mscVsLCoReasonForNoRoute,
       "mscVsLCoLastTearDownReason": mscVsLCoLastTearDownReason,
       "mscVsLCoPathFailureAction": mscVsLCoPathFailureAction,
       "mscVsLCoBumpPreference": mscVsLCoBumpPreference,
       "mscVsLCoOptimization": mscVsLCoOptimization,
       "mscVsLCoPathUpDateTime": mscVsLCoPathUpDateTime,
       "mscVsLCoStatsTable": mscVsLCoStatsTable,
       "mscVsLCoStatsEntry": mscVsLCoStatsEntry,
       "mscVsLCoPktsToNetwork": mscVsLCoPktsToNetwork,
       "mscVsLCoBytesToNetwork": mscVsLCoBytesToNetwork,
       "mscVsLCoPktsFromNetwork": mscVsLCoPktsFromNetwork,
       "mscVsLCoBytesFromNetwork": mscVsLCoBytesFromNetwork,
       "mscVsLCoPathTable": mscVsLCoPathTable,
       "mscVsLCoPathEntry": mscVsLCoPathEntry,
       "mscVsLCoPathValue": mscVsLCoPathValue,
       "mscVsCidDataTable": mscVsCidDataTable,
       "mscVsCidDataEntry": mscVsCidDataEntry,
       "mscVsCustomerIdentifier": mscVsCustomerIdentifier,
       "mscVsIfEntryTable": mscVsIfEntryTable,
       "mscVsIfEntryEntry": mscVsIfEntryEntry,
       "mscVsIfAdminStatus": mscVsIfAdminStatus,
       "mscVsIfIndex": mscVsIfIndex,
       "mscVsOperStatusTable": mscVsOperStatusTable,
       "mscVsOperStatusEntry": mscVsOperStatusEntry,
       "mscVsSnmpOperStatus": mscVsSnmpOperStatus,
       "mscVsStateTable": mscVsStateTable,
       "mscVsStateEntry": mscVsStateEntry,
       "mscVsAdminState": mscVsAdminState,
       "mscVsOperationalState": mscVsOperationalState,
       "mscVsUsageState": mscVsUsageState,
       "mscVsAvailabilityStatus": mscVsAvailabilityStatus,
       "mscVsProceduralStatus": mscVsProceduralStatus,
       "mscVsControlStatus": mscVsControlStatus,
       "mscVsAlarmStatus": mscVsAlarmStatus,
       "mscVsStandbyStatus": mscVsStandbyStatus,
       "mscVsUnknownStatus": mscVsUnknownStatus,
       "mscVsOperationalTable": mscVsOperationalTable,
       "mscVsOperationalEntry": mscVsOperationalEntry,
       "mscVsServiceFailureReason": mscVsServiceFailureReason,
       "voiceMIB": voiceMIB,
       "voiceGroup": voiceGroup,
       "voiceGroupCA": voiceGroupCA,
       "voiceGroupCA02": voiceGroupCA02,
       "voiceGroupCA02A": voiceGroupCA02A,
       "voiceCapabilities": voiceCapabilities,
       "voiceCapabilitiesCA": voiceCapabilitiesCA,
       "voiceCapabilitiesCA02": voiceCapabilitiesCA02,
       "voiceCapabilitiesCA02A": voiceCapabilitiesCA02A}
)
