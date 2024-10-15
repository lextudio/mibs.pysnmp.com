# SNMP MIB module (Nortel-Magellan-Passport-VoiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VoiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:40 2024
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
 FixedPoint1,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "FixedPoint1",
    "HexString",
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

_Vs_ObjectIdentity = ObjectIdentity
vs = _Vs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80)
)
_VsRowStatusTable_Object = MibTable
vsRowStatusTable = _VsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1)
)
if mibBuilder.loadTexts:
    vsRowStatusTable.setStatus("mandatory")
_VsRowStatusEntry_Object = MibTableRow
vsRowStatusEntry = _VsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1, 1)
)
vsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsRowStatusEntry.setStatus("mandatory")
_VsRowStatus_Type = RowStatus
_VsRowStatus_Object = MibTableColumn
vsRowStatus = _VsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1, 1, 1),
    _VsRowStatus_Type()
)
vsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsRowStatus.setStatus("mandatory")
_VsComponentName_Type = DisplayString
_VsComponentName_Object = MibTableColumn
vsComponentName = _VsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1, 1, 2),
    _VsComponentName_Type()
)
vsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsComponentName.setStatus("mandatory")
_VsStorageType_Type = StorageType
_VsStorageType_Object = MibTableColumn
vsStorageType = _VsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1, 1, 4),
    _VsStorageType_Type()
)
vsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsStorageType.setStatus("mandatory")


class _VsIndex_Type(Integer32):
    """Custom type vsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsIndex_Type.__name__ = "Integer32"
_VsIndex_Object = MibTableColumn
vsIndex = _VsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 1, 1, 10),
    _VsIndex_Type()
)
vsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsIndex.setStatus("mandatory")
_VsFramer_ObjectIdentity = ObjectIdentity
vsFramer = _VsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2)
)
_VsFramerRowStatusTable_Object = MibTable
vsFramerRowStatusTable = _VsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1)
)
if mibBuilder.loadTexts:
    vsFramerRowStatusTable.setStatus("mandatory")
_VsFramerRowStatusEntry_Object = MibTableRow
vsFramerRowStatusEntry = _VsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1, 1)
)
vsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerRowStatusEntry.setStatus("mandatory")
_VsFramerRowStatus_Type = RowStatus
_VsFramerRowStatus_Object = MibTableColumn
vsFramerRowStatus = _VsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1, 1, 1),
    _VsFramerRowStatus_Type()
)
vsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerRowStatus.setStatus("mandatory")
_VsFramerComponentName_Type = DisplayString
_VsFramerComponentName_Object = MibTableColumn
vsFramerComponentName = _VsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1, 1, 2),
    _VsFramerComponentName_Type()
)
vsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerComponentName.setStatus("mandatory")
_VsFramerStorageType_Type = StorageType
_VsFramerStorageType_Object = MibTableColumn
vsFramerStorageType = _VsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1, 1, 4),
    _VsFramerStorageType_Type()
)
vsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerStorageType.setStatus("mandatory")
_VsFramerIndex_Type = NonReplicated
_VsFramerIndex_Object = MibTableColumn
vsFramerIndex = _VsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 1, 1, 10),
    _VsFramerIndex_Type()
)
vsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerIndex.setStatus("mandatory")
_VsFramerVfpDebug_ObjectIdentity = ObjectIdentity
vsFramerVfpDebug = _VsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5)
)
_VsFramerVfpDebugRowStatusTable_Object = MibTable
vsFramerVfpDebugRowStatusTable = _VsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_VsFramerVfpDebugRowStatusEntry_Object = MibTableRow
vsFramerVfpDebugRowStatusEntry = _VsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1, 1)
)
vsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    vsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_VsFramerVfpDebugRowStatus_Type = RowStatus
_VsFramerVfpDebugRowStatus_Object = MibTableColumn
vsFramerVfpDebugRowStatus = _VsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1, 1, 1),
    _VsFramerVfpDebugRowStatus_Type()
)
vsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerVfpDebugRowStatus.setStatus("mandatory")
_VsFramerVfpDebugComponentName_Type = DisplayString
_VsFramerVfpDebugComponentName_Object = MibTableColumn
vsFramerVfpDebugComponentName = _VsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1, 1, 2),
    _VsFramerVfpDebugComponentName_Type()
)
vsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerVfpDebugComponentName.setStatus("mandatory")
_VsFramerVfpDebugStorageType_Type = StorageType
_VsFramerVfpDebugStorageType_Object = MibTableColumn
vsFramerVfpDebugStorageType = _VsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1, 1, 4),
    _VsFramerVfpDebugStorageType_Type()
)
vsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerVfpDebugStorageType.setStatus("mandatory")
_VsFramerVfpDebugIndex_Type = NonReplicated
_VsFramerVfpDebugIndex_Object = MibTableColumn
vsFramerVfpDebugIndex = _VsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 5, 1, 1, 10),
    _VsFramerVfpDebugIndex_Type()
)
vsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerVfpDebugIndex.setStatus("mandatory")
_VsFramerMvpDebug_ObjectIdentity = ObjectIdentity
vsFramerMvpDebug = _VsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6)
)
_VsFramerMvpDebugRowStatusTable_Object = MibTable
vsFramerMvpDebugRowStatusTable = _VsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_VsFramerMvpDebugRowStatusEntry_Object = MibTableRow
vsFramerMvpDebugRowStatusEntry = _VsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1, 1)
)
vsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    vsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_VsFramerMvpDebugRowStatus_Type = RowStatus
_VsFramerMvpDebugRowStatus_Object = MibTableColumn
vsFramerMvpDebugRowStatus = _VsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1, 1, 1),
    _VsFramerMvpDebugRowStatus_Type()
)
vsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerMvpDebugRowStatus.setStatus("mandatory")
_VsFramerMvpDebugComponentName_Type = DisplayString
_VsFramerMvpDebugComponentName_Object = MibTableColumn
vsFramerMvpDebugComponentName = _VsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1, 1, 2),
    _VsFramerMvpDebugComponentName_Type()
)
vsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerMvpDebugComponentName.setStatus("mandatory")
_VsFramerMvpDebugStorageType_Type = StorageType
_VsFramerMvpDebugStorageType_Object = MibTableColumn
vsFramerMvpDebugStorageType = _VsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1, 1, 4),
    _VsFramerMvpDebugStorageType_Type()
)
vsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerMvpDebugStorageType.setStatus("mandatory")
_VsFramerMvpDebugIndex_Type = NonReplicated
_VsFramerMvpDebugIndex_Object = MibTableColumn
vsFramerMvpDebugIndex = _VsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 6, 1, 1, 10),
    _VsFramerMvpDebugIndex_Type()
)
vsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerMvpDebugIndex.setStatus("mandatory")
_VsFramerPcmCapture_ObjectIdentity = ObjectIdentity
vsFramerPcmCapture = _VsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7)
)
_VsFramerPcmCaptureRowStatusTable_Object = MibTable
vsFramerPcmCaptureRowStatusTable = _VsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_VsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
vsFramerPcmCaptureRowStatusEntry = _VsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1, 1)
)
vsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    vsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_VsFramerPcmCaptureRowStatus_Type = RowStatus
_VsFramerPcmCaptureRowStatus_Object = MibTableColumn
vsFramerPcmCaptureRowStatus = _VsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1, 1, 1),
    _VsFramerPcmCaptureRowStatus_Type()
)
vsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerPcmCaptureRowStatus.setStatus("mandatory")
_VsFramerPcmCaptureComponentName_Type = DisplayString
_VsFramerPcmCaptureComponentName_Object = MibTableColumn
vsFramerPcmCaptureComponentName = _VsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1, 1, 2),
    _VsFramerPcmCaptureComponentName_Type()
)
vsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerPcmCaptureComponentName.setStatus("mandatory")
_VsFramerPcmCaptureStorageType_Type = StorageType
_VsFramerPcmCaptureStorageType_Object = MibTableColumn
vsFramerPcmCaptureStorageType = _VsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1, 1, 4),
    _VsFramerPcmCaptureStorageType_Type()
)
vsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerPcmCaptureStorageType.setStatus("mandatory")
_VsFramerPcmCaptureIndex_Type = NonReplicated
_VsFramerPcmCaptureIndex_Object = MibTableColumn
vsFramerPcmCaptureIndex = _VsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 7, 1, 1, 10),
    _VsFramerPcmCaptureIndex_Type()
)
vsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerPcmCaptureIndex.setStatus("mandatory")
_VsFramerProvTable_Object = MibTable
vsFramerProvTable = _VsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 10)
)
if mibBuilder.loadTexts:
    vsFramerProvTable.setStatus("mandatory")
_VsFramerProvEntry_Object = MibTableRow
vsFramerProvEntry = _VsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 10, 1)
)
vsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerProvEntry.setStatus("mandatory")
_VsFramerInterfaceName_Type = Link
_VsFramerInterfaceName_Object = MibTableColumn
vsFramerInterfaceName = _VsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 10, 1, 1),
    _VsFramerInterfaceName_Type()
)
vsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerInterfaceName.setStatus("mandatory")
_VsFramerCoderTable_Object = MibTable
vsFramerCoderTable = _VsFramerCoderTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12)
)
if mibBuilder.loadTexts:
    vsFramerCoderTable.setStatus("mandatory")
_VsFramerCoderEntry_Object = MibTableRow
vsFramerCoderEntry = _VsFramerCoderEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1)
)
vsFramerCoderEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerCoderEntry.setStatus("mandatory")


class _VsFramerMaxVoiceBitRate_Type(Integer32):
    """Custom type vsFramerMaxVoiceBitRate based on Integer32"""
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


_VsFramerMaxVoiceBitRate_Type.__name__ = "Integer32"
_VsFramerMaxVoiceBitRate_Object = MibTableColumn
vsFramerMaxVoiceBitRate = _VsFramerMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 1),
    _VsFramerMaxVoiceBitRate_Type()
)
vsFramerMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerMaxVoiceBitRate.setStatus("mandatory")


class _VsFramerMinVoiceBitRate_Type(Integer32):
    """Custom type vsFramerMinVoiceBitRate based on Integer32"""
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


_VsFramerMinVoiceBitRate_Type.__name__ = "Integer32"
_VsFramerMinVoiceBitRate_Object = MibTableColumn
vsFramerMinVoiceBitRate = _VsFramerMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 2),
    _VsFramerMinVoiceBitRate_Type()
)
vsFramerMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerMinVoiceBitRate.setStatus("mandatory")


class _VsFramerMaxModemBitRate_Type(Integer32):
    """Custom type vsFramerMaxModemBitRate based on Integer32"""
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


_VsFramerMaxModemBitRate_Type.__name__ = "Integer32"
_VsFramerMaxModemBitRate_Object = MibTableColumn
vsFramerMaxModemBitRate = _VsFramerMaxModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 3),
    _VsFramerMaxModemBitRate_Type()
)
vsFramerMaxModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerMaxModemBitRate.setStatus("mandatory")


class _VsFramerMinModemBitRate_Type(Integer32):
    """Custom type vsFramerMinModemBitRate based on Integer32"""
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


_VsFramerMinModemBitRate_Type.__name__ = "Integer32"
_VsFramerMinModemBitRate_Object = MibTableColumn
vsFramerMinModemBitRate = _VsFramerMinModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 4),
    _VsFramerMinModemBitRate_Type()
)
vsFramerMinModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerMinModemBitRate.setStatus("mandatory")


class _VsFramerAudioGain_Type(Integer32):
    """Custom type vsFramerAudioGain based on Integer32"""
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


_VsFramerAudioGain_Type.__name__ = "Integer32"
_VsFramerAudioGain_Object = MibTableColumn
vsFramerAudioGain = _VsFramerAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 5),
    _VsFramerAudioGain_Type()
)
vsFramerAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerAudioGain.setStatus("obsolete")


class _VsFramerSilenceSuppression_Type(Integer32):
    """Custom type vsFramerSilenceSuppression based on Integer32"""
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


_VsFramerSilenceSuppression_Type.__name__ = "Integer32"
_VsFramerSilenceSuppression_Object = MibTableColumn
vsFramerSilenceSuppression = _VsFramerSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 6),
    _VsFramerSilenceSuppression_Type()
)
vsFramerSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerSilenceSuppression.setStatus("mandatory")


class _VsFramerEchoCancellation_Type(Integer32):
    """Custom type vsFramerEchoCancellation based on Integer32"""
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


_VsFramerEchoCancellation_Type.__name__ = "Integer32"
_VsFramerEchoCancellation_Object = MibTableColumn
vsFramerEchoCancellation = _VsFramerEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 7),
    _VsFramerEchoCancellation_Type()
)
vsFramerEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEchoCancellation.setStatus("mandatory")


class _VsFramerALawConversion_Type(Integer32):
    """Custom type vsFramerALawConversion based on Integer32"""
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


_VsFramerALawConversion_Type.__name__ = "Integer32"
_VsFramerALawConversion_Object = MibTableColumn
vsFramerALawConversion = _VsFramerALawConversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 9),
    _VsFramerALawConversion_Type()
)
vsFramerALawConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerALawConversion.setStatus("mandatory")


class _VsFramerVoiceEncoding_Type(Integer32):
    """Custom type vsFramerVoiceEncoding based on Integer32"""
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


_VsFramerVoiceEncoding_Type.__name__ = "Integer32"
_VsFramerVoiceEncoding_Object = MibTableColumn
vsFramerVoiceEncoding = _VsFramerVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 11),
    _VsFramerVoiceEncoding_Type()
)
vsFramerVoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerVoiceEncoding.setStatus("mandatory")


class _VsFramerFaxEncoding_Type(Integer32):
    """Custom type vsFramerFaxEncoding based on Integer32"""
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


_VsFramerFaxEncoding_Type.__name__ = "Integer32"
_VsFramerFaxEncoding_Object = MibTableColumn
vsFramerFaxEncoding = _VsFramerFaxEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 12),
    _VsFramerFaxEncoding_Type()
)
vsFramerFaxEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerFaxEncoding.setStatus("mandatory")


class _VsFramerTandemPassThrough_Type(Integer32):
    """Custom type vsFramerTandemPassThrough based on Integer32"""
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


_VsFramerTandemPassThrough_Type.__name__ = "Integer32"
_VsFramerTandemPassThrough_Object = MibTableColumn
vsFramerTandemPassThrough = _VsFramerTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 13),
    _VsFramerTandemPassThrough_Type()
)
vsFramerTandemPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerTandemPassThrough.setStatus("mandatory")


class _VsFramerInsertedOutputDelay_Type(Integer32):
    """Custom type vsFramerInsertedOutputDelay based on Integer32"""
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


_VsFramerInsertedOutputDelay_Type.__name__ = "Integer32"
_VsFramerInsertedOutputDelay_Object = MibTableColumn
vsFramerInsertedOutputDelay = _VsFramerInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 14),
    _VsFramerInsertedOutputDelay_Type()
)
vsFramerInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerInsertedOutputDelay.setStatus("mandatory")


class _VsFramerEgressAudioGain_Type(Integer32):
    """Custom type vsFramerEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_VsFramerEgressAudioGain_Type.__name__ = "Integer32"
_VsFramerEgressAudioGain_Object = MibTableColumn
vsFramerEgressAudioGain = _VsFramerEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 15),
    _VsFramerEgressAudioGain_Type()
)
vsFramerEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEgressAudioGain.setStatus("obsolete")


class _VsFramerFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type vsFramerFaxIdleSuppressionG711G726 based on Integer32"""
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


_VsFramerFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_VsFramerFaxIdleSuppressionG711G726_Object = MibTableColumn
vsFramerFaxIdleSuppressionG711G726 = _VsFramerFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 16),
    _VsFramerFaxIdleSuppressionG711G726_Type()
)
vsFramerFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerFaxIdleSuppressionG711G726.setStatus("mandatory")


class _VsFramerEndOfCallPattern_Type(Integer32):
    """Custom type vsFramerEndOfCallPattern based on Integer32"""
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


_VsFramerEndOfCallPattern_Type.__name__ = "Integer32"
_VsFramerEndOfCallPattern_Object = MibTableColumn
vsFramerEndOfCallPattern = _VsFramerEndOfCallPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 17),
    _VsFramerEndOfCallPattern_Type()
)
vsFramerEndOfCallPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEndOfCallPattern.setStatus("mandatory")


class _VsFramerIngressAudioGain_Type(Integer32):
    """Custom type vsFramerIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_VsFramerIngressAudioGain_Type.__name__ = "Integer32"
_VsFramerIngressAudioGain_Object = MibTableColumn
vsFramerIngressAudioGain = _VsFramerIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 18),
    _VsFramerIngressAudioGain_Type()
)
vsFramerIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerIngressAudioGain.setStatus("mandatory")


class _VsFramerEgressGain_Type(Integer32):
    """Custom type vsFramerEgressGain based on Integer32"""
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


_VsFramerEgressGain_Type.__name__ = "Integer32"
_VsFramerEgressGain_Object = MibTableColumn
vsFramerEgressGain = _VsFramerEgressGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 19),
    _VsFramerEgressGain_Type()
)
vsFramerEgressGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEgressGain.setStatus("mandatory")


class _VsFramerComfortNoiseCap_Type(Integer32):
    """Custom type vsFramerComfortNoiseCap based on Integer32"""
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


_VsFramerComfortNoiseCap_Type.__name__ = "Integer32"
_VsFramerComfortNoiseCap_Object = MibTableColumn
vsFramerComfortNoiseCap = _VsFramerComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 20),
    _VsFramerComfortNoiseCap_Type()
)
vsFramerComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerComfortNoiseCap.setStatus("mandatory")


class _VsFramerEchoTailDelay_Type(Unsigned32):
    """Custom type vsFramerEchoTailDelay based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
    )


_VsFramerEchoTailDelay_Type.__name__ = "Unsigned32"
_VsFramerEchoTailDelay_Object = MibTableColumn
vsFramerEchoTailDelay = _VsFramerEchoTailDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 21),
    _VsFramerEchoTailDelay_Type()
)
vsFramerEchoTailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEchoTailDelay.setStatus("mandatory")


class _VsFramerEchoReturnLoss_Type(Unsigned32):
    """Custom type vsFramerEchoReturnLoss based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(6, 6),
    )


_VsFramerEchoReturnLoss_Type.__name__ = "Unsigned32"
_VsFramerEchoReturnLoss_Object = MibTableColumn
vsFramerEchoReturnLoss = _VsFramerEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 22),
    _VsFramerEchoReturnLoss_Type()
)
vsFramerEchoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEchoReturnLoss.setStatus("mandatory")


class _VsFramerDtmfRegeneration_Type(Integer32):
    """Custom type vsFramerDtmfRegeneration based on Integer32"""
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


_VsFramerDtmfRegeneration_Type.__name__ = "Integer32"
_VsFramerDtmfRegeneration_Object = MibTableColumn
vsFramerDtmfRegeneration = _VsFramerDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 34),
    _VsFramerDtmfRegeneration_Type()
)
vsFramerDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerDtmfRegeneration.setStatus("mandatory")


class _VsFramerSpeechHangoverTime_Type(Integer32):
    """Custom type vsFramerSpeechHangoverTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_VsFramerSpeechHangoverTime_Type.__name__ = "Integer32"
_VsFramerSpeechHangoverTime_Object = MibTableColumn
vsFramerSpeechHangoverTime = _VsFramerSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 35),
    _VsFramerSpeechHangoverTime_Type()
)
vsFramerSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerSpeechHangoverTime.setStatus("mandatory")


class _VsFramerFaxHangoverTimeG711G726_Type(Integer32):
    """Custom type vsFramerFaxHangoverTimeG711G726 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 20000),
    )


_VsFramerFaxHangoverTimeG711G726_Type.__name__ = "Integer32"
_VsFramerFaxHangoverTimeG711G726_Object = MibTableColumn
vsFramerFaxHangoverTimeG711G726 = _VsFramerFaxHangoverTimeG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 36),
    _VsFramerFaxHangoverTimeG711G726_Type()
)
vsFramerFaxHangoverTimeG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerFaxHangoverTimeG711G726.setStatus("mandatory")


class _VsFramerModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type vsFramerModemFaxSpeechDiscrim based on Integer32"""
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


_VsFramerModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_VsFramerModemFaxSpeechDiscrim_Object = MibTableColumn
vsFramerModemFaxSpeechDiscrim = _VsFramerModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 37),
    _VsFramerModemFaxSpeechDiscrim_Type()
)
vsFramerModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerModemFaxSpeechDiscrim.setStatus("mandatory")


class _VsFramerV17EncodedAsG711G726_Type(Integer32):
    """Custom type vsFramerV17EncodedAsG711G726 based on Integer32"""
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


_VsFramerV17EncodedAsG711G726_Type.__name__ = "Integer32"
_VsFramerV17EncodedAsG711G726_Object = MibTableColumn
vsFramerV17EncodedAsG711G726 = _VsFramerV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 39),
    _VsFramerV17EncodedAsG711G726_Type()
)
vsFramerV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerV17EncodedAsG711G726.setStatus("mandatory")


class _VsFramerEcanBypassMode_Type(Integer32):
    """Custom type vsFramerEcanBypassMode based on Integer32"""
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


_VsFramerEcanBypassMode_Type.__name__ = "Integer32"
_VsFramerEcanBypassMode_Object = MibTableColumn
vsFramerEcanBypassMode = _VsFramerEcanBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 40),
    _VsFramerEcanBypassMode_Type()
)
vsFramerEcanBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerEcanBypassMode.setStatus("mandatory")


class _VsFramerMaxFaxRelayRate_Type(FixedPoint1):
    """Custom type vsFramerMaxFaxRelayRate based on FixedPoint1"""
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


_VsFramerMaxFaxRelayRate_Type.__name__ = "FixedPoint1"
_VsFramerMaxFaxRelayRate_Object = MibTableColumn
vsFramerMaxFaxRelayRate = _VsFramerMaxFaxRelayRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 12, 1, 41),
    _VsFramerMaxFaxRelayRate_Type()
)
vsFramerMaxFaxRelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerMaxFaxRelayRate.setStatus("mandatory")
_VsFramerSignalTable_Object = MibTable
vsFramerSignalTable = _VsFramerSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13)
)
if mibBuilder.loadTexts:
    vsFramerSignalTable.setStatus("mandatory")
_VsFramerSignalEntry_Object = MibTableRow
vsFramerSignalEntry = _VsFramerSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1)
)
vsFramerSignalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerSignalEntry.setStatus("mandatory")


class _VsFramerTransmitBusyYellow_Type(Integer32):
    """Custom type vsFramerTransmitBusyYellow based on Integer32"""
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


_VsFramerTransmitBusyYellow_Type.__name__ = "Integer32"
_VsFramerTransmitBusyYellow_Object = MibTableColumn
vsFramerTransmitBusyYellow = _VsFramerTransmitBusyYellow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 1),
    _VsFramerTransmitBusyYellow_Type()
)
vsFramerTransmitBusyYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerTransmitBusyYellow.setStatus("mandatory")


class _VsFramerTransportSignalling_Type(Integer32):
    """Custom type vsFramerTransportSignalling based on Integer32"""
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


_VsFramerTransportSignalling_Type.__name__ = "Integer32"
_VsFramerTransportSignalling_Object = MibTableColumn
vsFramerTransportSignalling = _VsFramerTransportSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 2),
    _VsFramerTransportSignalling_Type()
)
vsFramerTransportSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerTransportSignalling.setStatus("obsolete")


class _VsFramerInterpretSignalling_Type(Integer32):
    """Custom type vsFramerInterpretSignalling based on Integer32"""
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


_VsFramerInterpretSignalling_Type.__name__ = "Integer32"
_VsFramerInterpretSignalling_Object = MibTableColumn
vsFramerInterpretSignalling = _VsFramerInterpretSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 3),
    _VsFramerInterpretSignalling_Type()
)
vsFramerInterpretSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerInterpretSignalling.setStatus("obsolete")


class _VsFramerInvertBits_Type(Integer32):
    """Custom type vsFramerInvertBits based on Integer32"""
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


_VsFramerInvertBits_Type.__name__ = "Integer32"
_VsFramerInvertBits_Object = MibTableColumn
vsFramerInvertBits = _VsFramerInvertBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 4),
    _VsFramerInvertBits_Type()
)
vsFramerInvertBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerInvertBits.setStatus("mandatory")


class _VsFramerSignalBits_Type(Integer32):
    """Custom type vsFramerSignalBits based on Integer32"""
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


_VsFramerSignalBits_Type.__name__ = "Integer32"
_VsFramerSignalBits_Object = MibTableColumn
vsFramerSignalBits = _VsFramerSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 5),
    _VsFramerSignalBits_Type()
)
vsFramerSignalBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerSignalBits.setStatus("mandatory")


class _VsFramerTransmitCasYellow_Type(Integer32):
    """Custom type vsFramerTransmitCasYellow based on Integer32"""
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


_VsFramerTransmitCasYellow_Type.__name__ = "Integer32"
_VsFramerTransmitCasYellow_Object = MibTableColumn
vsFramerTransmitCasYellow = _VsFramerTransmitCasYellow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 7),
    _VsFramerTransmitCasYellow_Type()
)
vsFramerTransmitCasYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerTransmitCasYellow.setStatus("mandatory")


class _VsFramerCasSignalling_Type(Integer32):
    """Custom type vsFramerCasSignalling based on Integer32"""
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


_VsFramerCasSignalling_Type.__name__ = "Integer32"
_VsFramerCasSignalling_Object = MibTableColumn
vsFramerCasSignalling = _VsFramerCasSignalling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 13, 1, 8),
    _VsFramerCasSignalling_Type()
)
vsFramerCasSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerCasSignalling.setStatus("mandatory")
_VsFramerStateTable_Object = MibTable
vsFramerStateTable = _VsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 14)
)
if mibBuilder.loadTexts:
    vsFramerStateTable.setStatus("mandatory")
_VsFramerStateEntry_Object = MibTableRow
vsFramerStateEntry = _VsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 14, 1)
)
vsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerStateEntry.setStatus("mandatory")


class _VsFramerAdminState_Type(Integer32):
    """Custom type vsFramerAdminState based on Integer32"""
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


_VsFramerAdminState_Type.__name__ = "Integer32"
_VsFramerAdminState_Object = MibTableColumn
vsFramerAdminState = _VsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 14, 1, 1),
    _VsFramerAdminState_Type()
)
vsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerAdminState.setStatus("mandatory")


class _VsFramerOperationalState_Type(Integer32):
    """Custom type vsFramerOperationalState based on Integer32"""
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


_VsFramerOperationalState_Type.__name__ = "Integer32"
_VsFramerOperationalState_Object = MibTableColumn
vsFramerOperationalState = _VsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 14, 1, 2),
    _VsFramerOperationalState_Type()
)
vsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerOperationalState.setStatus("mandatory")


class _VsFramerUsageState_Type(Integer32):
    """Custom type vsFramerUsageState based on Integer32"""
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


_VsFramerUsageState_Type.__name__ = "Integer32"
_VsFramerUsageState_Object = MibTableColumn
vsFramerUsageState = _VsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 14, 1, 3),
    _VsFramerUsageState_Type()
)
vsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerUsageState.setStatus("mandatory")
_VsFramerStatsTable_Object = MibTable
vsFramerStatsTable = _VsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15)
)
if mibBuilder.loadTexts:
    vsFramerStatsTable.setStatus("mandatory")
_VsFramerStatsEntry_Object = MibTableRow
vsFramerStatsEntry = _VsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1)
)
vsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerStatsEntry.setStatus("mandatory")
_VsFramerTotalCells_Type = Counter32
_VsFramerTotalCells_Object = MibTableColumn
vsFramerTotalCells = _VsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 1),
    _VsFramerTotalCells_Type()
)
vsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerTotalCells.setStatus("mandatory")
_VsFramerAudioCells_Type = Counter32
_VsFramerAudioCells_Object = MibTableColumn
vsFramerAudioCells = _VsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 2),
    _VsFramerAudioCells_Type()
)
vsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerAudioCells.setStatus("mandatory")
_VsFramerSilenceCells_Type = Counter32
_VsFramerSilenceCells_Object = MibTableColumn
vsFramerSilenceCells = _VsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 4),
    _VsFramerSilenceCells_Type()
)
vsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerSilenceCells.setStatus("mandatory")
_VsFramerModemCells_Type = Counter32
_VsFramerModemCells_Object = MibTableColumn
vsFramerModemCells = _VsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 5),
    _VsFramerModemCells_Type()
)
vsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerModemCells.setStatus("obsolete")


class _VsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type vsFramerCurrentEncodingRate based on Integer32"""
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


_VsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_VsFramerCurrentEncodingRate_Object = MibTableColumn
vsFramerCurrentEncodingRate = _VsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 6),
    _VsFramerCurrentEncodingRate_Type()
)
vsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerCurrentEncodingRate.setStatus("obsolete")
_VsFramerLrcErrors_Type = Counter32
_VsFramerLrcErrors_Object = MibTableColumn
vsFramerLrcErrors = _VsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 7),
    _VsFramerLrcErrors_Type()
)
vsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerLrcErrors.setStatus("mandatory")
_VsFramerFrmLostInNetwork_Type = Counter32
_VsFramerFrmLostInNetwork_Object = MibTableColumn
vsFramerFrmLostInNetwork = _VsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 8),
    _VsFramerFrmLostInNetwork_Type()
)
vsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFrmLostInNetwork.setStatus("mandatory")
_VsFramerFrmUnderRuns_Type = Counter32
_VsFramerFrmUnderRuns_Object = MibTableColumn
vsFramerFrmUnderRuns = _VsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 9),
    _VsFramerFrmUnderRuns_Type()
)
vsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFrmUnderRuns.setStatus("mandatory")
_VsFramerFrmDumped_Type = Counter32
_VsFramerFrmDumped_Object = MibTableColumn
vsFramerFrmDumped = _VsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 10),
    _VsFramerFrmDumped_Type()
)
vsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFrmDumped.setStatus("mandatory")
_VsFramerModemSilenceCells_Type = Counter32
_VsFramerModemSilenceCells_Object = MibTableColumn
vsFramerModemSilenceCells = _VsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 26),
    _VsFramerModemSilenceCells_Type()
)
vsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerModemSilenceCells.setStatus("obsolete")


class _VsFramerTptStatus_Type(Integer32):
    """Custom type vsFramerTptStatus based on Integer32"""
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


_VsFramerTptStatus_Type.__name__ = "Integer32"
_VsFramerTptStatus_Object = MibTableColumn
vsFramerTptStatus = _VsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 27),
    _VsFramerTptStatus_Type()
)
vsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerTptStatus.setStatus("obsolete")


class _VsFramerCurrentEncoding_Type(Integer32):
    """Custom type vsFramerCurrentEncoding based on Integer32"""
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


_VsFramerCurrentEncoding_Type.__name__ = "Integer32"
_VsFramerCurrentEncoding_Object = MibTableColumn
vsFramerCurrentEncoding = _VsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 28),
    _VsFramerCurrentEncoding_Type()
)
vsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerCurrentEncoding.setStatus("obsolete")


class _VsFramerRecentIngressLineSamples_Type(HexString):
    """Custom type vsFramerRecentIngressLineSamples based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VsFramerRecentIngressLineSamples_Type.__name__ = "HexString"
_VsFramerRecentIngressLineSamples_Object = MibTableColumn
vsFramerRecentIngressLineSamples = _VsFramerRecentIngressLineSamples_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 29),
    _VsFramerRecentIngressLineSamples_Type()
)
vsFramerRecentIngressLineSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerRecentIngressLineSamples.setStatus("obsolete")


class _VsFramerSentMinVoiceG711G726Rate_Type(Integer32):
    """Custom type vsFramerSentMinVoiceG711G726Rate based on Integer32"""
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


_VsFramerSentMinVoiceG711G726Rate_Type.__name__ = "Integer32"
_VsFramerSentMinVoiceG711G726Rate_Object = MibTableColumn
vsFramerSentMinVoiceG711G726Rate = _VsFramerSentMinVoiceG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 30),
    _VsFramerSentMinVoiceG711G726Rate_Type()
)
vsFramerSentMinVoiceG711G726Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerSentMinVoiceG711G726Rate.setStatus("obsolete")


class _VsFramerSentMinModemFaxG711G726Rate_Type(Integer32):
    """Custom type vsFramerSentMinModemFaxG711G726Rate based on Integer32"""
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


_VsFramerSentMinModemFaxG711G726Rate_Type.__name__ = "Integer32"
_VsFramerSentMinModemFaxG711G726Rate_Object = MibTableColumn
vsFramerSentMinModemFaxG711G726Rate = _VsFramerSentMinModemFaxG711G726Rate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 31),
    _VsFramerSentMinModemFaxG711G726Rate_Type()
)
vsFramerSentMinModemFaxG711G726Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerSentMinModemFaxG711G726Rate.setStatus("obsolete")


class _VsFramerSentFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type vsFramerSentFaxIdleSuppressionG711G726 based on Integer32"""
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


_VsFramerSentFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_VsFramerSentFaxIdleSuppressionG711G726_Object = MibTableColumn
vsFramerSentFaxIdleSuppressionG711G726 = _VsFramerSentFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 32),
    _VsFramerSentFaxIdleSuppressionG711G726_Type()
)
vsFramerSentFaxIdleSuppressionG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerSentFaxIdleSuppressionG711G726.setStatus("obsolete")


class _VsFramerSentSilenceSuppression_Type(Integer32):
    """Custom type vsFramerSentSilenceSuppression based on Integer32"""
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


_VsFramerSentSilenceSuppression_Type.__name__ = "Integer32"
_VsFramerSentSilenceSuppression_Object = MibTableColumn
vsFramerSentSilenceSuppression = _VsFramerSentSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 33),
    _VsFramerSentSilenceSuppression_Type()
)
vsFramerSentSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerSentSilenceSuppression.setStatus("obsolete")
_VsFramerFaxRelayCells_Type = Counter32
_VsFramerFaxRelayCells_Object = MibTableColumn
vsFramerFaxRelayCells = _VsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 42),
    _VsFramerFaxRelayCells_Type()
)
vsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFaxRelayCells.setStatus("mandatory")
_VsFramerModemFaxCells_Type = Counter32
_VsFramerModemFaxCells_Object = MibTableColumn
vsFramerModemFaxCells = _VsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 43),
    _VsFramerModemFaxCells_Type()
)
vsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerModemFaxCells.setStatus("mandatory")
_VsFramerFaxIdleCells_Type = Counter32
_VsFramerFaxIdleCells_Object = MibTableColumn
vsFramerFaxIdleCells = _VsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 15, 1, 44),
    _VsFramerFaxIdleCells_Type()
)
vsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFaxIdleCells.setStatus("mandatory")
_VsFramerNegTable_Object = MibTable
vsFramerNegTable = _VsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16)
)
if mibBuilder.loadTexts:
    vsFramerNegTable.setStatus("mandatory")
_VsFramerNegEntry_Object = MibTableRow
vsFramerNegEntry = _VsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1)
)
vsFramerNegEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerNegEntry.setStatus("mandatory")


class _VsFramerNegotiatedIgSilenceSuppression_Type(Integer32):
    """Custom type vsFramerNegotiatedIgSilenceSuppression based on Integer32"""
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


_VsFramerNegotiatedIgSilenceSuppression_Type.__name__ = "Integer32"
_VsFramerNegotiatedIgSilenceSuppression_Object = MibTableColumn
vsFramerNegotiatedIgSilenceSuppression = _VsFramerNegotiatedIgSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1, 1),
    _VsFramerNegotiatedIgSilenceSuppression_Type()
)
vsFramerNegotiatedIgSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNegotiatedIgSilenceSuppression.setStatus("mandatory")


class _VsFramerNegotiatedIgFisG711G726_Type(Integer32):
    """Custom type vsFramerNegotiatedIgFisG711G726 based on Integer32"""
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


_VsFramerNegotiatedIgFisG711G726_Type.__name__ = "Integer32"
_VsFramerNegotiatedIgFisG711G726_Object = MibTableColumn
vsFramerNegotiatedIgFisG711G726 = _VsFramerNegotiatedIgFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1, 2),
    _VsFramerNegotiatedIgFisG711G726_Type()
)
vsFramerNegotiatedIgFisG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNegotiatedIgFisG711G726.setStatus("mandatory")


class _VsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type vsFramerNegotiatedDtmfRegeneration based on Integer32"""
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


_VsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_VsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
vsFramerNegotiatedDtmfRegeneration = _VsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1, 3),
    _VsFramerNegotiatedDtmfRegeneration_Type()
)
vsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _VsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type vsFramerNegotiatedV17AsG711G726 based on Integer32"""
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


_VsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_VsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
vsFramerNegotiatedV17AsG711G726 = _VsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1, 4),
    _VsFramerNegotiatedV17AsG711G726_Type()
)
vsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _VsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type vsFramerNegotiatedTandemPassThrough based on Integer32"""
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


_VsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_VsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
vsFramerNegotiatedTandemPassThrough = _VsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 16, 1, 5),
    _VsFramerNegotiatedTandemPassThrough_Type()
)
vsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_VsFramerOperTable_Object = MibTable
vsFramerOperTable = _VsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17)
)
if mibBuilder.loadTexts:
    vsFramerOperTable.setStatus("mandatory")
_VsFramerOperEntry_Object = MibTableRow
vsFramerOperEntry = _VsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17, 1)
)
vsFramerOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
)
if mibBuilder.loadTexts:
    vsFramerOperEntry.setStatus("mandatory")


class _VsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type vsFramerOpCurrentEncoding based on Integer32"""
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


_VsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_VsFramerOpCurrentEncoding_Object = MibTableColumn
vsFramerOpCurrentEncoding = _VsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17, 1, 1),
    _VsFramerOpCurrentEncoding_Type()
)
vsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerOpCurrentEncoding.setStatus("mandatory")


class _VsFramerCurrentRate_Type(Integer32):
    """Custom type vsFramerCurrentRate based on Integer32"""
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


_VsFramerCurrentRate_Type.__name__ = "Integer32"
_VsFramerCurrentRate_Object = MibTableColumn
vsFramerCurrentRate = _VsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17, 1, 2),
    _VsFramerCurrentRate_Type()
)
vsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerCurrentRate.setStatus("mandatory")


class _VsFramerOpTptStatus_Type(Integer32):
    """Custom type vsFramerOpTptStatus based on Integer32"""
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


_VsFramerOpTptStatus_Type.__name__ = "Integer32"
_VsFramerOpTptStatus_Object = MibTableColumn
vsFramerOpTptStatus = _VsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17, 1, 3),
    _VsFramerOpTptStatus_Type()
)
vsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerOpTptStatus.setStatus("mandatory")


class _VsFramerOpRecentIngressLineSamples_Type(HexString):
    """Custom type vsFramerOpRecentIngressLineSamples based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VsFramerOpRecentIngressLineSamples_Type.__name__ = "HexString"
_VsFramerOpRecentIngressLineSamples_Object = MibTableColumn
vsFramerOpRecentIngressLineSamples = _VsFramerOpRecentIngressLineSamples_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 17, 1, 4),
    _VsFramerOpRecentIngressLineSamples_Type()
)
vsFramerOpRecentIngressLineSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerOpRecentIngressLineSamples.setStatus("mandatory")
_VsFramerIdleCodeTable_Object = MibTable
vsFramerIdleCodeTable = _VsFramerIdleCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 204)
)
if mibBuilder.loadTexts:
    vsFramerIdleCodeTable.setStatus("mandatory")
_VsFramerIdleCodeEntry_Object = MibTableRow
vsFramerIdleCodeEntry = _VsFramerIdleCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 204, 1)
)
vsFramerIdleCodeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIdleCodeIndex"),
)
if mibBuilder.loadTexts:
    vsFramerIdleCodeEntry.setStatus("mandatory")


class _VsFramerIdleCodeIndex_Type(Integer32):
    """Custom type vsFramerIdleCodeIndex based on Integer32"""
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


_VsFramerIdleCodeIndex_Type.__name__ = "Integer32"
_VsFramerIdleCodeIndex_Object = MibTableColumn
vsFramerIdleCodeIndex = _VsFramerIdleCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 204, 1, 1),
    _VsFramerIdleCodeIndex_Type()
)
vsFramerIdleCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerIdleCodeIndex.setStatus("mandatory")


class _VsFramerIdleCodeValue_Type(Unsigned32):
    """Custom type vsFramerIdleCodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VsFramerIdleCodeValue_Type.__name__ = "Unsigned32"
_VsFramerIdleCodeValue_Object = MibTableColumn
vsFramerIdleCodeValue = _VsFramerIdleCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 204, 1, 2),
    _VsFramerIdleCodeValue_Type()
)
vsFramerIdleCodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerIdleCodeValue.setStatus("mandatory")
_VsFramerSeizeCodeTable_Object = MibTable
vsFramerSeizeCodeTable = _VsFramerSeizeCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 205)
)
if mibBuilder.loadTexts:
    vsFramerSeizeCodeTable.setStatus("mandatory")
_VsFramerSeizeCodeEntry_Object = MibTableRow
vsFramerSeizeCodeEntry = _VsFramerSeizeCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 205, 1)
)
vsFramerSeizeCodeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerSeizeCodeIndex"),
)
if mibBuilder.loadTexts:
    vsFramerSeizeCodeEntry.setStatus("mandatory")


class _VsFramerSeizeCodeIndex_Type(Integer32):
    """Custom type vsFramerSeizeCodeIndex based on Integer32"""
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


_VsFramerSeizeCodeIndex_Type.__name__ = "Integer32"
_VsFramerSeizeCodeIndex_Object = MibTableColumn
vsFramerSeizeCodeIndex = _VsFramerSeizeCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 205, 1, 1),
    _VsFramerSeizeCodeIndex_Type()
)
vsFramerSeizeCodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerSeizeCodeIndex.setStatus("mandatory")


class _VsFramerSeizeCodeValue_Type(Unsigned32):
    """Custom type vsFramerSeizeCodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VsFramerSeizeCodeValue_Type.__name__ = "Unsigned32"
_VsFramerSeizeCodeValue_Object = MibTableColumn
vsFramerSeizeCodeValue = _VsFramerSeizeCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 205, 1, 2),
    _VsFramerSeizeCodeValue_Type()
)
vsFramerSeizeCodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsFramerSeizeCodeValue.setStatus("mandatory")
_VsFramerFrmToNetworkTable_Object = MibTable
vsFramerFrmToNetworkTable = _VsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 206)
)
if mibBuilder.loadTexts:
    vsFramerFrmToNetworkTable.setStatus("mandatory")
_VsFramerFrmToNetworkEntry_Object = MibTableRow
vsFramerFrmToNetworkEntry = _VsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 206, 1)
)
vsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    vsFramerFrmToNetworkEntry.setStatus("mandatory")


class _VsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type vsFramerFrmToNetworkIndex based on Integer32"""
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


_VsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_VsFramerFrmToNetworkIndex_Object = MibTableColumn
vsFramerFrmToNetworkIndex = _VsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 206, 1, 1),
    _VsFramerFrmToNetworkIndex_Type()
)
vsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerFrmToNetworkIndex.setStatus("mandatory")
_VsFramerFrmToNetworkValue_Type = Counter32
_VsFramerFrmToNetworkValue_Object = MibTableColumn
vsFramerFrmToNetworkValue = _VsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 206, 1, 2),
    _VsFramerFrmToNetworkValue_Type()
)
vsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerFrmToNetworkValue.setStatus("mandatory")
_VsFramerNEncodingTable_Object = MibTable
vsFramerNEncodingTable = _VsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 438)
)
if mibBuilder.loadTexts:
    vsFramerNEncodingTable.setStatus("mandatory")
_VsFramerNEncodingEntry_Object = MibTableRow
vsFramerNEncodingEntry = _VsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 438, 1)
)
vsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    vsFramerNEncodingEntry.setStatus("mandatory")


class _VsFramerNEncodingIndex_Type(Integer32):
    """Custom type vsFramerNEncodingIndex based on Integer32"""
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


_VsFramerNEncodingIndex_Type.__name__ = "Integer32"
_VsFramerNEncodingIndex_Object = MibTableColumn
vsFramerNEncodingIndex = _VsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 438, 1, 1),
    _VsFramerNEncodingIndex_Type()
)
vsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerNEncodingIndex.setStatus("mandatory")


class _VsFramerNEncodingValue_Type(Integer32):
    """Custom type vsFramerNEncodingValue based on Integer32"""
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


_VsFramerNEncodingValue_Type.__name__ = "Integer32"
_VsFramerNEncodingValue_Object = MibTableColumn
vsFramerNEncodingValue = _VsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 438, 1, 2),
    _VsFramerNEncodingValue_Type()
)
vsFramerNEncodingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNEncodingValue.setStatus("mandatory")
_VsFramerNRatesTable_Object = MibTable
vsFramerNRatesTable = _VsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 439)
)
if mibBuilder.loadTexts:
    vsFramerNRatesTable.setStatus("mandatory")
_VsFramerNRatesEntry_Object = MibTableRow
vsFramerNRatesEntry = _VsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 439, 1)
)
vsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerNRatesTrafficIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vsFramerNRatesEntry.setStatus("mandatory")


class _VsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type vsFramerNRatesTrafficIndex based on Integer32"""
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


_VsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_VsFramerNRatesTrafficIndex_Object = MibTableColumn
vsFramerNRatesTrafficIndex = _VsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 439, 1, 1),
    _VsFramerNRatesTrafficIndex_Type()
)
vsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerNRatesTrafficIndex.setStatus("mandatory")


class _VsFramerNRatesRateIndex_Type(Integer32):
    """Custom type vsFramerNRatesRateIndex based on Integer32"""
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


_VsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_VsFramerNRatesRateIndex_Object = MibTableColumn
vsFramerNRatesRateIndex = _VsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 439, 1, 2),
    _VsFramerNRatesRateIndex_Type()
)
vsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsFramerNRatesRateIndex.setStatus("mandatory")


class _VsFramerNRatesValue_Type(Integer32):
    """Custom type vsFramerNRatesValue based on Integer32"""
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


_VsFramerNRatesValue_Type.__name__ = "Integer32"
_VsFramerNRatesValue_Object = MibTableColumn
vsFramerNRatesValue = _VsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 2, 439, 1, 3),
    _VsFramerNRatesValue_Type()
)
vsFramerNRatesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsFramerNRatesValue.setStatus("mandatory")
_VsPlc_ObjectIdentity = ObjectIdentity
vsPlc = _VsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3)
)
_VsPlcRowStatusTable_Object = MibTable
vsPlcRowStatusTable = _VsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1)
)
if mibBuilder.loadTexts:
    vsPlcRowStatusTable.setStatus("mandatory")
_VsPlcRowStatusEntry_Object = MibTableRow
vsPlcRowStatusEntry = _VsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1, 1)
)
vsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsPlcIndex"),
)
if mibBuilder.loadTexts:
    vsPlcRowStatusEntry.setStatus("mandatory")
_VsPlcRowStatus_Type = RowStatus
_VsPlcRowStatus_Object = MibTableColumn
vsPlcRowStatus = _VsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1, 1, 1),
    _VsPlcRowStatus_Type()
)
vsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPlcRowStatus.setStatus("mandatory")
_VsPlcComponentName_Type = DisplayString
_VsPlcComponentName_Object = MibTableColumn
vsPlcComponentName = _VsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1, 1, 2),
    _VsPlcComponentName_Type()
)
vsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPlcComponentName.setStatus("mandatory")
_VsPlcStorageType_Type = StorageType
_VsPlcStorageType_Object = MibTableColumn
vsPlcStorageType = _VsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1, 1, 4),
    _VsPlcStorageType_Type()
)
vsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsPlcStorageType.setStatus("mandatory")
_VsPlcIndex_Type = NonReplicated
_VsPlcIndex_Object = MibTableColumn
vsPlcIndex = _VsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 1, 1, 10),
    _VsPlcIndex_Type()
)
vsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsPlcIndex.setStatus("mandatory")
_VsPlcProvTable_Object = MibTable
vsPlcProvTable = _VsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10)
)
if mibBuilder.loadTexts:
    vsPlcProvTable.setStatus("mandatory")
_VsPlcProvEntry_Object = MibTableRow
vsPlcProvEntry = _VsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1)
)
vsPlcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsPlcIndex"),
)
if mibBuilder.loadTexts:
    vsPlcProvEntry.setStatus("mandatory")


class _VsPlcRemoteName_Type(AsciiString):
    """Custom type vsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsPlcRemoteName_Type.__name__ = "AsciiString"
_VsPlcRemoteName_Object = MibTableColumn
vsPlcRemoteName = _VsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 2),
    _VsPlcRemoteName_Type()
)
vsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRemoteName.setStatus("mandatory")


class _VsPlcSetupPriority_Type(Unsigned32):
    """Custom type vsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsPlcSetupPriority_Type.__name__ = "Unsigned32"
_VsPlcSetupPriority_Object = MibTableColumn
vsPlcSetupPriority = _VsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 3),
    _VsPlcSetupPriority_Type()
)
vsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcSetupPriority.setStatus("mandatory")


class _VsPlcHoldingPriority_Type(Unsigned32):
    """Custom type vsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_VsPlcHoldingPriority_Object = MibTableColumn
vsPlcHoldingPriority = _VsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 4),
    _VsPlcHoldingPriority_Type()
)
vsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcHoldingPriority.setStatus("mandatory")


class _VsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type vsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_VsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_VsPlcRequiredTxBandwidth_Object = MibTableColumn
vsPlcRequiredTxBandwidth = _VsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 5),
    _VsPlcRequiredTxBandwidth_Type()
)
vsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRequiredTxBandwidth.setStatus("mandatory")


class _VsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type vsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_VsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_VsPlcRequiredRxBandwidth_Object = MibTableColumn
vsPlcRequiredRxBandwidth = _VsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 6),
    _VsPlcRequiredRxBandwidth_Type()
)
vsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRequiredRxBandwidth.setStatus("mandatory")


class _VsPlcRequiredTrafficType_Type(Integer32):
    """Custom type vsPlcRequiredTrafficType based on Integer32"""
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


_VsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_VsPlcRequiredTrafficType_Object = MibTableColumn
vsPlcRequiredTrafficType = _VsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 7),
    _VsPlcRequiredTrafficType_Type()
)
vsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRequiredTrafficType.setStatus("mandatory")


class _VsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type vsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_VsPlcPermittedTrunkTypes_Object = MibTableColumn
vsPlcPermittedTrunkTypes = _VsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 8),
    _VsPlcPermittedTrunkTypes_Type()
)
vsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcPermittedTrunkTypes.setStatus("mandatory")


class _VsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type vsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_VsPlcRequiredSecurity_Object = MibTableColumn
vsPlcRequiredSecurity = _VsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 9),
    _VsPlcRequiredSecurity_Type()
)
vsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRequiredSecurity.setStatus("mandatory")


class _VsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type vsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_VsPlcRequiredCustomerParm_Object = MibTableColumn
vsPlcRequiredCustomerParm = _VsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 10),
    _VsPlcRequiredCustomerParm_Type()
)
vsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcRequiredCustomerParm.setStatus("mandatory")


class _VsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type vsPlcPathAttributeToMinimize based on Integer32"""
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


_VsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_VsPlcPathAttributeToMinimize_Object = MibTableColumn
vsPlcPathAttributeToMinimize = _VsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 11),
    _VsPlcPathAttributeToMinimize_Type()
)
vsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcPathAttributeToMinimize.setStatus("mandatory")


class _VsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type vsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_VsPlcMaximumAcceptableCost_Object = MibTableColumn
vsPlcMaximumAcceptableCost = _VsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 12),
    _VsPlcMaximumAcceptableCost_Type()
)
vsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcMaximumAcceptableCost.setStatus("mandatory")


class _VsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type vsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_VsPlcMaximumAcceptableDelay_Object = MibTableColumn
vsPlcMaximumAcceptableDelay = _VsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 13),
    _VsPlcMaximumAcceptableDelay_Type()
)
vsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _VsPlcEmissionPriority_Type(Unsigned32):
    """Custom type vsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_VsPlcEmissionPriority_Object = MibTableColumn
vsPlcEmissionPriority = _VsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 14),
    _VsPlcEmissionPriority_Type()
)
vsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcEmissionPriority.setStatus("mandatory")


class _VsPlcDiscardPriority_Type(Unsigned32):
    """Custom type vsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_VsPlcDiscardPriority_Object = MibTableColumn
vsPlcDiscardPriority = _VsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 15),
    _VsPlcDiscardPriority_Type()
)
vsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcDiscardPriority.setStatus("mandatory")


class _VsPlcPathType_Type(Integer32):
    """Custom type vsPlcPathType based on Integer32"""
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


_VsPlcPathType_Type.__name__ = "Integer32"
_VsPlcPathType_Object = MibTableColumn
vsPlcPathType = _VsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 16),
    _VsPlcPathType_Type()
)
vsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcPathType.setStatus("mandatory")


class _VsPlcPathFailureAction_Type(Integer32):
    """Custom type vsPlcPathFailureAction based on Integer32"""
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


_VsPlcPathFailureAction_Type.__name__ = "Integer32"
_VsPlcPathFailureAction_Object = MibTableColumn
vsPlcPathFailureAction = _VsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 17),
    _VsPlcPathFailureAction_Type()
)
vsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcPathFailureAction.setStatus("mandatory")


class _VsPlcBumpPreference_Type(Integer32):
    """Custom type vsPlcBumpPreference based on Integer32"""
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


_VsPlcBumpPreference_Type.__name__ = "Integer32"
_VsPlcBumpPreference_Object = MibTableColumn
vsPlcBumpPreference = _VsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 18),
    _VsPlcBumpPreference_Type()
)
vsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcBumpPreference.setStatus("mandatory")


class _VsPlcOptimization_Type(Integer32):
    """Custom type vsPlcOptimization based on Integer32"""
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


_VsPlcOptimization_Type.__name__ = "Integer32"
_VsPlcOptimization_Object = MibTableColumn
vsPlcOptimization = _VsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 10, 1, 19),
    _VsPlcOptimization_Type()
)
vsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcOptimization.setStatus("mandatory")
_VsPlcMpathTable_Object = MibTable
vsPlcMpathTable = _VsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 207)
)
if mibBuilder.loadTexts:
    vsPlcMpathTable.setStatus("mandatory")
_VsPlcMpathEntry_Object = MibTableRow
vsPlcMpathEntry = _VsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 207, 1)
)
vsPlcMpathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsPlcIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    vsPlcMpathEntry.setStatus("mandatory")


class _VsPlcMpathIndex_Type(Integer32):
    """Custom type vsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_VsPlcMpathIndex_Type.__name__ = "Integer32"
_VsPlcMpathIndex_Object = MibTableColumn
vsPlcMpathIndex = _VsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 207, 1, 1),
    _VsPlcMpathIndex_Type()
)
vsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsPlcMpathIndex.setStatus("mandatory")


class _VsPlcMpathValue_Type(AsciiString):
    """Custom type vsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsPlcMpathValue_Type.__name__ = "AsciiString"
_VsPlcMpathValue_Object = MibTableColumn
vsPlcMpathValue = _VsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 3, 207, 1, 2),
    _VsPlcMpathValue_Type()
)
vsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsPlcMpathValue.setStatus("mandatory")
_VsLCo_ObjectIdentity = ObjectIdentity
vsLCo = _VsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4)
)
_VsLCoRowStatusTable_Object = MibTable
vsLCoRowStatusTable = _VsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1)
)
if mibBuilder.loadTexts:
    vsLCoRowStatusTable.setStatus("mandatory")
_VsLCoRowStatusEntry_Object = MibTableRow
vsLCoRowStatusEntry = _VsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1, 1)
)
vsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsLCoRowStatusEntry.setStatus("mandatory")
_VsLCoRowStatus_Type = RowStatus
_VsLCoRowStatus_Object = MibTableColumn
vsLCoRowStatus = _VsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1, 1, 1),
    _VsLCoRowStatus_Type()
)
vsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRowStatus.setStatus("mandatory")
_VsLCoComponentName_Type = DisplayString
_VsLCoComponentName_Object = MibTableColumn
vsLCoComponentName = _VsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1, 1, 2),
    _VsLCoComponentName_Type()
)
vsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoComponentName.setStatus("mandatory")
_VsLCoStorageType_Type = StorageType
_VsLCoStorageType_Object = MibTableColumn
vsLCoStorageType = _VsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1, 1, 4),
    _VsLCoStorageType_Type()
)
vsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoStorageType.setStatus("mandatory")
_VsLCoIndex_Type = NonReplicated
_VsLCoIndex_Object = MibTableColumn
vsLCoIndex = _VsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 1, 1, 10),
    _VsLCoIndex_Type()
)
vsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsLCoIndex.setStatus("mandatory")
_VsLCoPathDataTable_Object = MibTable
vsLCoPathDataTable = _VsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10)
)
if mibBuilder.loadTexts:
    vsLCoPathDataTable.setStatus("mandatory")
_VsLCoPathDataEntry_Object = MibTableRow
vsLCoPathDataEntry = _VsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1)
)
vsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsLCoPathDataEntry.setStatus("mandatory")


class _VsLCoState_Type(Integer32):
    """Custom type vsLCoState based on Integer32"""
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


_VsLCoState_Type.__name__ = "Integer32"
_VsLCoState_Object = MibTableColumn
vsLCoState = _VsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 1),
    _VsLCoState_Type()
)
vsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoState.setStatus("mandatory")


class _VsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type vsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_VsLCoOverrideRemoteName_Object = MibTableColumn
vsLCoOverrideRemoteName = _VsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 2),
    _VsLCoOverrideRemoteName_Type()
)
vsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsLCoOverrideRemoteName.setStatus("mandatory")


class _VsLCoEnd_Type(Integer32):
    """Custom type vsLCoEnd based on Integer32"""
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


_VsLCoEnd_Type.__name__ = "Integer32"
_VsLCoEnd_Object = MibTableColumn
vsLCoEnd = _VsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 3),
    _VsLCoEnd_Type()
)
vsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoEnd.setStatus("mandatory")


class _VsLCoCostMetric_Type(Unsigned32):
    """Custom type vsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsLCoCostMetric_Type.__name__ = "Unsigned32"
_VsLCoCostMetric_Object = MibTableColumn
vsLCoCostMetric = _VsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 4),
    _VsLCoCostMetric_Type()
)
vsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoCostMetric.setStatus("mandatory")


class _VsLCoDelayMetric_Type(Unsigned32):
    """Custom type vsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VsLCoDelayMetric_Type.__name__ = "Unsigned32"
_VsLCoDelayMetric_Object = MibTableColumn
vsLCoDelayMetric = _VsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 5),
    _VsLCoDelayMetric_Type()
)
vsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoDelayMetric.setStatus("mandatory")


class _VsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type vsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_VsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_VsLCoRoundTripDelay_Object = MibTableColumn
vsLCoRoundTripDelay = _VsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 6),
    _VsLCoRoundTripDelay_Type()
)
vsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRoundTripDelay.setStatus("mandatory")


class _VsLCoSetupPriority_Type(Unsigned32):
    """Custom type vsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsLCoSetupPriority_Type.__name__ = "Unsigned32"
_VsLCoSetupPriority_Object = MibTableColumn
vsLCoSetupPriority = _VsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 7),
    _VsLCoSetupPriority_Type()
)
vsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoSetupPriority.setStatus("mandatory")


class _VsLCoHoldingPriority_Type(Unsigned32):
    """Custom type vsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_VsLCoHoldingPriority_Object = MibTableColumn
vsLCoHoldingPriority = _VsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 8),
    _VsLCoHoldingPriority_Type()
)
vsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoHoldingPriority.setStatus("mandatory")


class _VsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type vsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_VsLCoRequiredTxBandwidth_Object = MibTableColumn
vsLCoRequiredTxBandwidth = _VsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 9),
    _VsLCoRequiredTxBandwidth_Type()
)
vsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRequiredTxBandwidth.setStatus("mandatory")


class _VsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type vsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_VsLCoRequiredRxBandwidth_Object = MibTableColumn
vsLCoRequiredRxBandwidth = _VsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 10),
    _VsLCoRequiredRxBandwidth_Type()
)
vsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRequiredRxBandwidth.setStatus("mandatory")


class _VsLCoRequiredTrafficType_Type(Integer32):
    """Custom type vsLCoRequiredTrafficType based on Integer32"""
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


_VsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_VsLCoRequiredTrafficType_Object = MibTableColumn
vsLCoRequiredTrafficType = _VsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 11),
    _VsLCoRequiredTrafficType_Type()
)
vsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRequiredTrafficType.setStatus("mandatory")


class _VsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type vsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_VsLCoPermittedTrunkTypes_Object = MibTableColumn
vsLCoPermittedTrunkTypes = _VsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 12),
    _VsLCoPermittedTrunkTypes_Type()
)
vsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPermittedTrunkTypes.setStatus("mandatory")


class _VsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type vsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_VsLCoRequiredSecurity_Object = MibTableColumn
vsLCoRequiredSecurity = _VsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 13),
    _VsLCoRequiredSecurity_Type()
)
vsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRequiredSecurity.setStatus("mandatory")


class _VsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type vsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_VsLCoRequiredCustomerParameter_Object = MibTableColumn
vsLCoRequiredCustomerParameter = _VsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 14),
    _VsLCoRequiredCustomerParameter_Type()
)
vsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRequiredCustomerParameter.setStatus("mandatory")


class _VsLCoEmissionPriority_Type(Unsigned32):
    """Custom type vsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_VsLCoEmissionPriority_Object = MibTableColumn
vsLCoEmissionPriority = _VsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 15),
    _VsLCoEmissionPriority_Type()
)
vsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoEmissionPriority.setStatus("mandatory")


class _VsLCoDiscardPriority_Type(Unsigned32):
    """Custom type vsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_VsLCoDiscardPriority_Object = MibTableColumn
vsLCoDiscardPriority = _VsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 16),
    _VsLCoDiscardPriority_Type()
)
vsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoDiscardPriority.setStatus("mandatory")


class _VsLCoPathType_Type(Integer32):
    """Custom type vsLCoPathType based on Integer32"""
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


_VsLCoPathType_Type.__name__ = "Integer32"
_VsLCoPathType_Object = MibTableColumn
vsLCoPathType = _VsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 17),
    _VsLCoPathType_Type()
)
vsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPathType.setStatus("mandatory")


class _VsLCoRetryCount_Type(Unsigned32):
    """Custom type vsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VsLCoRetryCount_Type.__name__ = "Unsigned32"
_VsLCoRetryCount_Object = MibTableColumn
vsLCoRetryCount = _VsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 18),
    _VsLCoRetryCount_Type()
)
vsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoRetryCount.setStatus("mandatory")


class _VsLCoPathFailureCount_Type(Unsigned32):
    """Custom type vsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_VsLCoPathFailureCount_Object = MibTableColumn
vsLCoPathFailureCount = _VsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 19),
    _VsLCoPathFailureCount_Type()
)
vsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPathFailureCount.setStatus("mandatory")


class _VsLCoReasonForNoRoute_Type(Integer32):
    """Custom type vsLCoReasonForNoRoute based on Integer32"""
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


_VsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_VsLCoReasonForNoRoute_Object = MibTableColumn
vsLCoReasonForNoRoute = _VsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 20),
    _VsLCoReasonForNoRoute_Type()
)
vsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoReasonForNoRoute.setStatus("mandatory")


class _VsLCoLastTearDownReason_Type(Integer32):
    """Custom type vsLCoLastTearDownReason based on Integer32"""
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


_VsLCoLastTearDownReason_Type.__name__ = "Integer32"
_VsLCoLastTearDownReason_Object = MibTableColumn
vsLCoLastTearDownReason = _VsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 21),
    _VsLCoLastTearDownReason_Type()
)
vsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoLastTearDownReason.setStatus("mandatory")


class _VsLCoPathFailureAction_Type(Integer32):
    """Custom type vsLCoPathFailureAction based on Integer32"""
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


_VsLCoPathFailureAction_Type.__name__ = "Integer32"
_VsLCoPathFailureAction_Object = MibTableColumn
vsLCoPathFailureAction = _VsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 22),
    _VsLCoPathFailureAction_Type()
)
vsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPathFailureAction.setStatus("mandatory")


class _VsLCoBumpPreference_Type(Integer32):
    """Custom type vsLCoBumpPreference based on Integer32"""
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


_VsLCoBumpPreference_Type.__name__ = "Integer32"
_VsLCoBumpPreference_Object = MibTableColumn
vsLCoBumpPreference = _VsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 23),
    _VsLCoBumpPreference_Type()
)
vsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoBumpPreference.setStatus("mandatory")


class _VsLCoOptimization_Type(Integer32):
    """Custom type vsLCoOptimization based on Integer32"""
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


_VsLCoOptimization_Type.__name__ = "Integer32"
_VsLCoOptimization_Object = MibTableColumn
vsLCoOptimization = _VsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 24),
    _VsLCoOptimization_Type()
)
vsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoOptimization.setStatus("mandatory")


class _VsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type vsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_VsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_VsLCoPathUpDateTime_Object = MibTableColumn
vsLCoPathUpDateTime = _VsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 10, 1, 25),
    _VsLCoPathUpDateTime_Type()
)
vsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPathUpDateTime.setStatus("mandatory")
_VsLCoStatsTable_Object = MibTable
vsLCoStatsTable = _VsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11)
)
if mibBuilder.loadTexts:
    vsLCoStatsTable.setStatus("mandatory")
_VsLCoStatsEntry_Object = MibTableRow
vsLCoStatsEntry = _VsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11, 1)
)
vsLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsLCoIndex"),
)
if mibBuilder.loadTexts:
    vsLCoStatsEntry.setStatus("mandatory")
_VsLCoPktsToNetwork_Type = PassportCounter64
_VsLCoPktsToNetwork_Object = MibTableColumn
vsLCoPktsToNetwork = _VsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11, 1, 1),
    _VsLCoPktsToNetwork_Type()
)
vsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPktsToNetwork.setStatus("mandatory")
_VsLCoBytesToNetwork_Type = PassportCounter64
_VsLCoBytesToNetwork_Object = MibTableColumn
vsLCoBytesToNetwork = _VsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11, 1, 2),
    _VsLCoBytesToNetwork_Type()
)
vsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoBytesToNetwork.setStatus("mandatory")
_VsLCoPktsFromNetwork_Type = PassportCounter64
_VsLCoPktsFromNetwork_Object = MibTableColumn
vsLCoPktsFromNetwork = _VsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11, 1, 3),
    _VsLCoPktsFromNetwork_Type()
)
vsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPktsFromNetwork.setStatus("mandatory")
_VsLCoBytesFromNetwork_Type = PassportCounter64
_VsLCoBytesFromNetwork_Object = MibTableColumn
vsLCoBytesFromNetwork = _VsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 11, 1, 4),
    _VsLCoBytesFromNetwork_Type()
)
vsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoBytesFromNetwork.setStatus("mandatory")
_VsLCoPathTable_Object = MibTable
vsLCoPathTable = _VsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 264)
)
if mibBuilder.loadTexts:
    vsLCoPathTable.setStatus("mandatory")
_VsLCoPathEntry_Object = MibTableRow
vsLCoPathEntry = _VsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 264, 1)
)
vsLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsLCoIndex"),
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsLCoPathValue"),
)
if mibBuilder.loadTexts:
    vsLCoPathEntry.setStatus("mandatory")


class _VsLCoPathValue_Type(AsciiString):
    """Custom type vsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VsLCoPathValue_Type.__name__ = "AsciiString"
_VsLCoPathValue_Object = MibTableColumn
vsLCoPathValue = _VsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 4, 264, 1, 1),
    _VsLCoPathValue_Type()
)
vsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsLCoPathValue.setStatus("mandatory")
_VsCidDataTable_Object = MibTable
vsCidDataTable = _VsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 10)
)
if mibBuilder.loadTexts:
    vsCidDataTable.setStatus("mandatory")
_VsCidDataEntry_Object = MibTableRow
vsCidDataEntry = _VsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 10, 1)
)
vsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsCidDataEntry.setStatus("mandatory")


class _VsCustomerIdentifier_Type(Unsigned32):
    """Custom type vsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_VsCustomerIdentifier_Type.__name__ = "Unsigned32"
_VsCustomerIdentifier_Object = MibTableColumn
vsCustomerIdentifier = _VsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 10, 1, 1),
    _VsCustomerIdentifier_Type()
)
vsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsCustomerIdentifier.setStatus("mandatory")
_VsIfEntryTable_Object = MibTable
vsIfEntryTable = _VsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 11)
)
if mibBuilder.loadTexts:
    vsIfEntryTable.setStatus("mandatory")
_VsIfEntryEntry_Object = MibTableRow
vsIfEntryEntry = _VsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 11, 1)
)
vsIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsIfEntryEntry.setStatus("mandatory")


class _VsIfAdminStatus_Type(Integer32):
    """Custom type vsIfAdminStatus based on Integer32"""
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


_VsIfAdminStatus_Type.__name__ = "Integer32"
_VsIfAdminStatus_Object = MibTableColumn
vsIfAdminStatus = _VsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 11, 1, 1),
    _VsIfAdminStatus_Type()
)
vsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsIfAdminStatus.setStatus("mandatory")


class _VsIfIndex_Type(InterfaceIndex):
    """Custom type vsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsIfIndex_Type.__name__ = "InterfaceIndex"
_VsIfIndex_Object = MibTableColumn
vsIfIndex = _VsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 11, 1, 2),
    _VsIfIndex_Type()
)
vsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsIfIndex.setStatus("mandatory")
_VsOperStatusTable_Object = MibTable
vsOperStatusTable = _VsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 12)
)
if mibBuilder.loadTexts:
    vsOperStatusTable.setStatus("mandatory")
_VsOperStatusEntry_Object = MibTableRow
vsOperStatusEntry = _VsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 12, 1)
)
vsOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsOperStatusEntry.setStatus("mandatory")


class _VsSnmpOperStatus_Type(Integer32):
    """Custom type vsSnmpOperStatus based on Integer32"""
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


_VsSnmpOperStatus_Type.__name__ = "Integer32"
_VsSnmpOperStatus_Object = MibTableColumn
vsSnmpOperStatus = _VsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 12, 1, 1),
    _VsSnmpOperStatus_Type()
)
vsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsSnmpOperStatus.setStatus("mandatory")
_VsStateTable_Object = MibTable
vsStateTable = _VsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13)
)
if mibBuilder.loadTexts:
    vsStateTable.setStatus("mandatory")
_VsStateEntry_Object = MibTableRow
vsStateEntry = _VsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1)
)
vsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsStateEntry.setStatus("mandatory")


class _VsAdminState_Type(Integer32):
    """Custom type vsAdminState based on Integer32"""
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


_VsAdminState_Type.__name__ = "Integer32"
_VsAdminState_Object = MibTableColumn
vsAdminState = _VsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 1),
    _VsAdminState_Type()
)
vsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsAdminState.setStatus("mandatory")


class _VsOperationalState_Type(Integer32):
    """Custom type vsOperationalState based on Integer32"""
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


_VsOperationalState_Type.__name__ = "Integer32"
_VsOperationalState_Object = MibTableColumn
vsOperationalState = _VsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 2),
    _VsOperationalState_Type()
)
vsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsOperationalState.setStatus("mandatory")


class _VsUsageState_Type(Integer32):
    """Custom type vsUsageState based on Integer32"""
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


_VsUsageState_Type.__name__ = "Integer32"
_VsUsageState_Object = MibTableColumn
vsUsageState = _VsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 3),
    _VsUsageState_Type()
)
vsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsUsageState.setStatus("mandatory")


class _VsAvailabilityStatus_Type(OctetString):
    """Custom type vsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VsAvailabilityStatus_Type.__name__ = "OctetString"
_VsAvailabilityStatus_Object = MibTableColumn
vsAvailabilityStatus = _VsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 4),
    _VsAvailabilityStatus_Type()
)
vsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsAvailabilityStatus.setStatus("mandatory")


class _VsProceduralStatus_Type(OctetString):
    """Custom type vsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsProceduralStatus_Type.__name__ = "OctetString"
_VsProceduralStatus_Object = MibTableColumn
vsProceduralStatus = _VsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 5),
    _VsProceduralStatus_Type()
)
vsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsProceduralStatus.setStatus("mandatory")


class _VsControlStatus_Type(OctetString):
    """Custom type vsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsControlStatus_Type.__name__ = "OctetString"
_VsControlStatus_Object = MibTableColumn
vsControlStatus = _VsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 6),
    _VsControlStatus_Type()
)
vsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsControlStatus.setStatus("mandatory")


class _VsAlarmStatus_Type(OctetString):
    """Custom type vsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VsAlarmStatus_Type.__name__ = "OctetString"
_VsAlarmStatus_Object = MibTableColumn
vsAlarmStatus = _VsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 7),
    _VsAlarmStatus_Type()
)
vsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsAlarmStatus.setStatus("mandatory")


class _VsStandbyStatus_Type(Integer32):
    """Custom type vsStandbyStatus based on Integer32"""
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


_VsStandbyStatus_Type.__name__ = "Integer32"
_VsStandbyStatus_Object = MibTableColumn
vsStandbyStatus = _VsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 8),
    _VsStandbyStatus_Type()
)
vsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsStandbyStatus.setStatus("mandatory")


class _VsUnknownStatus_Type(Integer32):
    """Custom type vsUnknownStatus based on Integer32"""
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


_VsUnknownStatus_Type.__name__ = "Integer32"
_VsUnknownStatus_Object = MibTableColumn
vsUnknownStatus = _VsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 13, 1, 9),
    _VsUnknownStatus_Type()
)
vsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsUnknownStatus.setStatus("mandatory")
_VsOperationalTable_Object = MibTable
vsOperationalTable = _VsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 15)
)
if mibBuilder.loadTexts:
    vsOperationalTable.setStatus("mandatory")
_VsOperationalEntry_Object = MibTableRow
vsOperationalEntry = _VsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 15, 1)
)
vsOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceMIB", "vsIndex"),
)
if mibBuilder.loadTexts:
    vsOperationalEntry.setStatus("mandatory")


class _VsServiceFailureReason_Type(OctetString):
    """Custom type vsServiceFailureReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VsServiceFailureReason_Type.__name__ = "OctetString"
_VsServiceFailureReason_Object = MibTableColumn
vsServiceFailureReason = _VsServiceFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 80, 15, 1, 1),
    _VsServiceFailureReason_Type()
)
vsServiceFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsServiceFailureReason.setStatus("mandatory")
_VoiceMIB_ObjectIdentity = ObjectIdentity
voiceMIB = _VoiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49)
)
_VoiceGroup_ObjectIdentity = ObjectIdentity
voiceGroup = _VoiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 1)
)
_VoiceGroupBE_ObjectIdentity = ObjectIdentity
voiceGroupBE = _VoiceGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 1, 5)
)
_VoiceGroupBE01_ObjectIdentity = ObjectIdentity
voiceGroupBE01 = _VoiceGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 1, 5, 2)
)
_VoiceGroupBE01A_ObjectIdentity = ObjectIdentity
voiceGroupBE01A = _VoiceGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 1, 5, 2, 2)
)
_VoiceCapabilities_ObjectIdentity = ObjectIdentity
voiceCapabilities = _VoiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 3)
)
_VoiceCapabilitiesBE_ObjectIdentity = ObjectIdentity
voiceCapabilitiesBE = _VoiceCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 3, 5)
)
_VoiceCapabilitiesBE01_ObjectIdentity = ObjectIdentity
voiceCapabilitiesBE01 = _VoiceCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 3, 5, 2)
)
_VoiceCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
voiceCapabilitiesBE01A = _VoiceCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 49, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VoiceMIB",
    **{"vs": vs,
       "vsRowStatusTable": vsRowStatusTable,
       "vsRowStatusEntry": vsRowStatusEntry,
       "vsRowStatus": vsRowStatus,
       "vsComponentName": vsComponentName,
       "vsStorageType": vsStorageType,
       "vsIndex": vsIndex,
       "vsFramer": vsFramer,
       "vsFramerRowStatusTable": vsFramerRowStatusTable,
       "vsFramerRowStatusEntry": vsFramerRowStatusEntry,
       "vsFramerRowStatus": vsFramerRowStatus,
       "vsFramerComponentName": vsFramerComponentName,
       "vsFramerStorageType": vsFramerStorageType,
       "vsFramerIndex": vsFramerIndex,
       "vsFramerVfpDebug": vsFramerVfpDebug,
       "vsFramerVfpDebugRowStatusTable": vsFramerVfpDebugRowStatusTable,
       "vsFramerVfpDebugRowStatusEntry": vsFramerVfpDebugRowStatusEntry,
       "vsFramerVfpDebugRowStatus": vsFramerVfpDebugRowStatus,
       "vsFramerVfpDebugComponentName": vsFramerVfpDebugComponentName,
       "vsFramerVfpDebugStorageType": vsFramerVfpDebugStorageType,
       "vsFramerVfpDebugIndex": vsFramerVfpDebugIndex,
       "vsFramerMvpDebug": vsFramerMvpDebug,
       "vsFramerMvpDebugRowStatusTable": vsFramerMvpDebugRowStatusTable,
       "vsFramerMvpDebugRowStatusEntry": vsFramerMvpDebugRowStatusEntry,
       "vsFramerMvpDebugRowStatus": vsFramerMvpDebugRowStatus,
       "vsFramerMvpDebugComponentName": vsFramerMvpDebugComponentName,
       "vsFramerMvpDebugStorageType": vsFramerMvpDebugStorageType,
       "vsFramerMvpDebugIndex": vsFramerMvpDebugIndex,
       "vsFramerPcmCapture": vsFramerPcmCapture,
       "vsFramerPcmCaptureRowStatusTable": vsFramerPcmCaptureRowStatusTable,
       "vsFramerPcmCaptureRowStatusEntry": vsFramerPcmCaptureRowStatusEntry,
       "vsFramerPcmCaptureRowStatus": vsFramerPcmCaptureRowStatus,
       "vsFramerPcmCaptureComponentName": vsFramerPcmCaptureComponentName,
       "vsFramerPcmCaptureStorageType": vsFramerPcmCaptureStorageType,
       "vsFramerPcmCaptureIndex": vsFramerPcmCaptureIndex,
       "vsFramerProvTable": vsFramerProvTable,
       "vsFramerProvEntry": vsFramerProvEntry,
       "vsFramerInterfaceName": vsFramerInterfaceName,
       "vsFramerCoderTable": vsFramerCoderTable,
       "vsFramerCoderEntry": vsFramerCoderEntry,
       "vsFramerMaxVoiceBitRate": vsFramerMaxVoiceBitRate,
       "vsFramerMinVoiceBitRate": vsFramerMinVoiceBitRate,
       "vsFramerMaxModemBitRate": vsFramerMaxModemBitRate,
       "vsFramerMinModemBitRate": vsFramerMinModemBitRate,
       "vsFramerAudioGain": vsFramerAudioGain,
       "vsFramerSilenceSuppression": vsFramerSilenceSuppression,
       "vsFramerEchoCancellation": vsFramerEchoCancellation,
       "vsFramerALawConversion": vsFramerALawConversion,
       "vsFramerVoiceEncoding": vsFramerVoiceEncoding,
       "vsFramerFaxEncoding": vsFramerFaxEncoding,
       "vsFramerTandemPassThrough": vsFramerTandemPassThrough,
       "vsFramerInsertedOutputDelay": vsFramerInsertedOutputDelay,
       "vsFramerEgressAudioGain": vsFramerEgressAudioGain,
       "vsFramerFaxIdleSuppressionG711G726": vsFramerFaxIdleSuppressionG711G726,
       "vsFramerEndOfCallPattern": vsFramerEndOfCallPattern,
       "vsFramerIngressAudioGain": vsFramerIngressAudioGain,
       "vsFramerEgressGain": vsFramerEgressGain,
       "vsFramerComfortNoiseCap": vsFramerComfortNoiseCap,
       "vsFramerEchoTailDelay": vsFramerEchoTailDelay,
       "vsFramerEchoReturnLoss": vsFramerEchoReturnLoss,
       "vsFramerDtmfRegeneration": vsFramerDtmfRegeneration,
       "vsFramerSpeechHangoverTime": vsFramerSpeechHangoverTime,
       "vsFramerFaxHangoverTimeG711G726": vsFramerFaxHangoverTimeG711G726,
       "vsFramerModemFaxSpeechDiscrim": vsFramerModemFaxSpeechDiscrim,
       "vsFramerV17EncodedAsG711G726": vsFramerV17EncodedAsG711G726,
       "vsFramerEcanBypassMode": vsFramerEcanBypassMode,
       "vsFramerMaxFaxRelayRate": vsFramerMaxFaxRelayRate,
       "vsFramerSignalTable": vsFramerSignalTable,
       "vsFramerSignalEntry": vsFramerSignalEntry,
       "vsFramerTransmitBusyYellow": vsFramerTransmitBusyYellow,
       "vsFramerTransportSignalling": vsFramerTransportSignalling,
       "vsFramerInterpretSignalling": vsFramerInterpretSignalling,
       "vsFramerInvertBits": vsFramerInvertBits,
       "vsFramerSignalBits": vsFramerSignalBits,
       "vsFramerTransmitCasYellow": vsFramerTransmitCasYellow,
       "vsFramerCasSignalling": vsFramerCasSignalling,
       "vsFramerStateTable": vsFramerStateTable,
       "vsFramerStateEntry": vsFramerStateEntry,
       "vsFramerAdminState": vsFramerAdminState,
       "vsFramerOperationalState": vsFramerOperationalState,
       "vsFramerUsageState": vsFramerUsageState,
       "vsFramerStatsTable": vsFramerStatsTable,
       "vsFramerStatsEntry": vsFramerStatsEntry,
       "vsFramerTotalCells": vsFramerTotalCells,
       "vsFramerAudioCells": vsFramerAudioCells,
       "vsFramerSilenceCells": vsFramerSilenceCells,
       "vsFramerModemCells": vsFramerModemCells,
       "vsFramerCurrentEncodingRate": vsFramerCurrentEncodingRate,
       "vsFramerLrcErrors": vsFramerLrcErrors,
       "vsFramerFrmLostInNetwork": vsFramerFrmLostInNetwork,
       "vsFramerFrmUnderRuns": vsFramerFrmUnderRuns,
       "vsFramerFrmDumped": vsFramerFrmDumped,
       "vsFramerModemSilenceCells": vsFramerModemSilenceCells,
       "vsFramerTptStatus": vsFramerTptStatus,
       "vsFramerCurrentEncoding": vsFramerCurrentEncoding,
       "vsFramerRecentIngressLineSamples": vsFramerRecentIngressLineSamples,
       "vsFramerSentMinVoiceG711G726Rate": vsFramerSentMinVoiceG711G726Rate,
       "vsFramerSentMinModemFaxG711G726Rate": vsFramerSentMinModemFaxG711G726Rate,
       "vsFramerSentFaxIdleSuppressionG711G726": vsFramerSentFaxIdleSuppressionG711G726,
       "vsFramerSentSilenceSuppression": vsFramerSentSilenceSuppression,
       "vsFramerFaxRelayCells": vsFramerFaxRelayCells,
       "vsFramerModemFaxCells": vsFramerModemFaxCells,
       "vsFramerFaxIdleCells": vsFramerFaxIdleCells,
       "vsFramerNegTable": vsFramerNegTable,
       "vsFramerNegEntry": vsFramerNegEntry,
       "vsFramerNegotiatedIgSilenceSuppression": vsFramerNegotiatedIgSilenceSuppression,
       "vsFramerNegotiatedIgFisG711G726": vsFramerNegotiatedIgFisG711G726,
       "vsFramerNegotiatedDtmfRegeneration": vsFramerNegotiatedDtmfRegeneration,
       "vsFramerNegotiatedV17AsG711G726": vsFramerNegotiatedV17AsG711G726,
       "vsFramerNegotiatedTandemPassThrough": vsFramerNegotiatedTandemPassThrough,
       "vsFramerOperTable": vsFramerOperTable,
       "vsFramerOperEntry": vsFramerOperEntry,
       "vsFramerOpCurrentEncoding": vsFramerOpCurrentEncoding,
       "vsFramerCurrentRate": vsFramerCurrentRate,
       "vsFramerOpTptStatus": vsFramerOpTptStatus,
       "vsFramerOpRecentIngressLineSamples": vsFramerOpRecentIngressLineSamples,
       "vsFramerIdleCodeTable": vsFramerIdleCodeTable,
       "vsFramerIdleCodeEntry": vsFramerIdleCodeEntry,
       "vsFramerIdleCodeIndex": vsFramerIdleCodeIndex,
       "vsFramerIdleCodeValue": vsFramerIdleCodeValue,
       "vsFramerSeizeCodeTable": vsFramerSeizeCodeTable,
       "vsFramerSeizeCodeEntry": vsFramerSeizeCodeEntry,
       "vsFramerSeizeCodeIndex": vsFramerSeizeCodeIndex,
       "vsFramerSeizeCodeValue": vsFramerSeizeCodeValue,
       "vsFramerFrmToNetworkTable": vsFramerFrmToNetworkTable,
       "vsFramerFrmToNetworkEntry": vsFramerFrmToNetworkEntry,
       "vsFramerFrmToNetworkIndex": vsFramerFrmToNetworkIndex,
       "vsFramerFrmToNetworkValue": vsFramerFrmToNetworkValue,
       "vsFramerNEncodingTable": vsFramerNEncodingTable,
       "vsFramerNEncodingEntry": vsFramerNEncodingEntry,
       "vsFramerNEncodingIndex": vsFramerNEncodingIndex,
       "vsFramerNEncodingValue": vsFramerNEncodingValue,
       "vsFramerNRatesTable": vsFramerNRatesTable,
       "vsFramerNRatesEntry": vsFramerNRatesEntry,
       "vsFramerNRatesTrafficIndex": vsFramerNRatesTrafficIndex,
       "vsFramerNRatesRateIndex": vsFramerNRatesRateIndex,
       "vsFramerNRatesValue": vsFramerNRatesValue,
       "vsPlc": vsPlc,
       "vsPlcRowStatusTable": vsPlcRowStatusTable,
       "vsPlcRowStatusEntry": vsPlcRowStatusEntry,
       "vsPlcRowStatus": vsPlcRowStatus,
       "vsPlcComponentName": vsPlcComponentName,
       "vsPlcStorageType": vsPlcStorageType,
       "vsPlcIndex": vsPlcIndex,
       "vsPlcProvTable": vsPlcProvTable,
       "vsPlcProvEntry": vsPlcProvEntry,
       "vsPlcRemoteName": vsPlcRemoteName,
       "vsPlcSetupPriority": vsPlcSetupPriority,
       "vsPlcHoldingPriority": vsPlcHoldingPriority,
       "vsPlcRequiredTxBandwidth": vsPlcRequiredTxBandwidth,
       "vsPlcRequiredRxBandwidth": vsPlcRequiredRxBandwidth,
       "vsPlcRequiredTrafficType": vsPlcRequiredTrafficType,
       "vsPlcPermittedTrunkTypes": vsPlcPermittedTrunkTypes,
       "vsPlcRequiredSecurity": vsPlcRequiredSecurity,
       "vsPlcRequiredCustomerParm": vsPlcRequiredCustomerParm,
       "vsPlcPathAttributeToMinimize": vsPlcPathAttributeToMinimize,
       "vsPlcMaximumAcceptableCost": vsPlcMaximumAcceptableCost,
       "vsPlcMaximumAcceptableDelay": vsPlcMaximumAcceptableDelay,
       "vsPlcEmissionPriority": vsPlcEmissionPriority,
       "vsPlcDiscardPriority": vsPlcDiscardPriority,
       "vsPlcPathType": vsPlcPathType,
       "vsPlcPathFailureAction": vsPlcPathFailureAction,
       "vsPlcBumpPreference": vsPlcBumpPreference,
       "vsPlcOptimization": vsPlcOptimization,
       "vsPlcMpathTable": vsPlcMpathTable,
       "vsPlcMpathEntry": vsPlcMpathEntry,
       "vsPlcMpathIndex": vsPlcMpathIndex,
       "vsPlcMpathValue": vsPlcMpathValue,
       "vsLCo": vsLCo,
       "vsLCoRowStatusTable": vsLCoRowStatusTable,
       "vsLCoRowStatusEntry": vsLCoRowStatusEntry,
       "vsLCoRowStatus": vsLCoRowStatus,
       "vsLCoComponentName": vsLCoComponentName,
       "vsLCoStorageType": vsLCoStorageType,
       "vsLCoIndex": vsLCoIndex,
       "vsLCoPathDataTable": vsLCoPathDataTable,
       "vsLCoPathDataEntry": vsLCoPathDataEntry,
       "vsLCoState": vsLCoState,
       "vsLCoOverrideRemoteName": vsLCoOverrideRemoteName,
       "vsLCoEnd": vsLCoEnd,
       "vsLCoCostMetric": vsLCoCostMetric,
       "vsLCoDelayMetric": vsLCoDelayMetric,
       "vsLCoRoundTripDelay": vsLCoRoundTripDelay,
       "vsLCoSetupPriority": vsLCoSetupPriority,
       "vsLCoHoldingPriority": vsLCoHoldingPriority,
       "vsLCoRequiredTxBandwidth": vsLCoRequiredTxBandwidth,
       "vsLCoRequiredRxBandwidth": vsLCoRequiredRxBandwidth,
       "vsLCoRequiredTrafficType": vsLCoRequiredTrafficType,
       "vsLCoPermittedTrunkTypes": vsLCoPermittedTrunkTypes,
       "vsLCoRequiredSecurity": vsLCoRequiredSecurity,
       "vsLCoRequiredCustomerParameter": vsLCoRequiredCustomerParameter,
       "vsLCoEmissionPriority": vsLCoEmissionPriority,
       "vsLCoDiscardPriority": vsLCoDiscardPriority,
       "vsLCoPathType": vsLCoPathType,
       "vsLCoRetryCount": vsLCoRetryCount,
       "vsLCoPathFailureCount": vsLCoPathFailureCount,
       "vsLCoReasonForNoRoute": vsLCoReasonForNoRoute,
       "vsLCoLastTearDownReason": vsLCoLastTearDownReason,
       "vsLCoPathFailureAction": vsLCoPathFailureAction,
       "vsLCoBumpPreference": vsLCoBumpPreference,
       "vsLCoOptimization": vsLCoOptimization,
       "vsLCoPathUpDateTime": vsLCoPathUpDateTime,
       "vsLCoStatsTable": vsLCoStatsTable,
       "vsLCoStatsEntry": vsLCoStatsEntry,
       "vsLCoPktsToNetwork": vsLCoPktsToNetwork,
       "vsLCoBytesToNetwork": vsLCoBytesToNetwork,
       "vsLCoPktsFromNetwork": vsLCoPktsFromNetwork,
       "vsLCoBytesFromNetwork": vsLCoBytesFromNetwork,
       "vsLCoPathTable": vsLCoPathTable,
       "vsLCoPathEntry": vsLCoPathEntry,
       "vsLCoPathValue": vsLCoPathValue,
       "vsCidDataTable": vsCidDataTable,
       "vsCidDataEntry": vsCidDataEntry,
       "vsCustomerIdentifier": vsCustomerIdentifier,
       "vsIfEntryTable": vsIfEntryTable,
       "vsIfEntryEntry": vsIfEntryEntry,
       "vsIfAdminStatus": vsIfAdminStatus,
       "vsIfIndex": vsIfIndex,
       "vsOperStatusTable": vsOperStatusTable,
       "vsOperStatusEntry": vsOperStatusEntry,
       "vsSnmpOperStatus": vsSnmpOperStatus,
       "vsStateTable": vsStateTable,
       "vsStateEntry": vsStateEntry,
       "vsAdminState": vsAdminState,
       "vsOperationalState": vsOperationalState,
       "vsUsageState": vsUsageState,
       "vsAvailabilityStatus": vsAvailabilityStatus,
       "vsProceduralStatus": vsProceduralStatus,
       "vsControlStatus": vsControlStatus,
       "vsAlarmStatus": vsAlarmStatus,
       "vsStandbyStatus": vsStandbyStatus,
       "vsUnknownStatus": vsUnknownStatus,
       "vsOperationalTable": vsOperationalTable,
       "vsOperationalEntry": vsOperationalEntry,
       "vsServiceFailureReason": vsServiceFailureReason,
       "voiceMIB": voiceMIB,
       "voiceGroup": voiceGroup,
       "voiceGroupBE": voiceGroupBE,
       "voiceGroupBE01": voiceGroupBE01,
       "voiceGroupBE01A": voiceGroupBE01A,
       "voiceCapabilities": voiceCapabilities,
       "voiceCapabilitiesBE": voiceCapabilitiesBE,
       "voiceCapabilitiesBE01": voiceCapabilitiesBE01,
       "voiceCapabilitiesBE01A": voiceCapabilitiesBE01A}
)
