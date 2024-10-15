# SNMP MIB module (Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:17 2024
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
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
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

_MscSigChan_ObjectIdentity = ObjectIdentity
mscSigChan = _MscSigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115)
)
_MscSigChanRowStatusTable_Object = MibTable
mscSigChanRowStatusTable = _MscSigChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1)
)
if mibBuilder.loadTexts:
    mscSigChanRowStatusTable.setStatus("mandatory")
_MscSigChanRowStatusEntry_Object = MibTableRow
mscSigChanRowStatusEntry = _MscSigChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1, 1)
)
mscSigChanRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanRowStatusEntry.setStatus("mandatory")
_MscSigChanRowStatus_Type = RowStatus
_MscSigChanRowStatus_Object = MibTableColumn
mscSigChanRowStatus = _MscSigChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1, 1, 1),
    _MscSigChanRowStatus_Type()
)
mscSigChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanRowStatus.setStatus("mandatory")
_MscSigChanComponentName_Type = DisplayString
_MscSigChanComponentName_Object = MibTableColumn
mscSigChanComponentName = _MscSigChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1, 1, 2),
    _MscSigChanComponentName_Type()
)
mscSigChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanComponentName.setStatus("mandatory")
_MscSigChanStorageType_Type = StorageType
_MscSigChanStorageType_Object = MibTableColumn
mscSigChanStorageType = _MscSigChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1, 1, 4),
    _MscSigChanStorageType_Type()
)
mscSigChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanStorageType.setStatus("mandatory")


class _MscSigChanIndex_Type(Integer32):
    """Custom type mscSigChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscSigChanIndex_Type.__name__ = "Integer32"
_MscSigChanIndex_Object = MibTableColumn
mscSigChanIndex = _MscSigChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 1, 1, 10),
    _MscSigChanIndex_Type()
)
mscSigChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanIndex.setStatus("mandatory")
_MscSigChanBch_ObjectIdentity = ObjectIdentity
mscSigChanBch = _MscSigChanBch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7)
)
_MscSigChanBchRowStatusTable_Object = MibTable
mscSigChanBchRowStatusTable = _MscSigChanBchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1)
)
if mibBuilder.loadTexts:
    mscSigChanBchRowStatusTable.setStatus("mandatory")
_MscSigChanBchRowStatusEntry_Object = MibTableRow
mscSigChanBchRowStatusEntry = _MscSigChanBchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1, 1)
)
mscSigChanBchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanBchIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanBchRowStatusEntry.setStatus("mandatory")
_MscSigChanBchRowStatus_Type = RowStatus
_MscSigChanBchRowStatus_Object = MibTableColumn
mscSigChanBchRowStatus = _MscSigChanBchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1, 1, 1),
    _MscSigChanBchRowStatus_Type()
)
mscSigChanBchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchRowStatus.setStatus("mandatory")
_MscSigChanBchComponentName_Type = DisplayString
_MscSigChanBchComponentName_Object = MibTableColumn
mscSigChanBchComponentName = _MscSigChanBchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1, 1, 2),
    _MscSigChanBchComponentName_Type()
)
mscSigChanBchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchComponentName.setStatus("mandatory")
_MscSigChanBchStorageType_Type = StorageType
_MscSigChanBchStorageType_Object = MibTableColumn
mscSigChanBchStorageType = _MscSigChanBchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1, 1, 4),
    _MscSigChanBchStorageType_Type()
)
mscSigChanBchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchStorageType.setStatus("mandatory")


class _MscSigChanBchIndex_Type(Integer32):
    """Custom type mscSigChanBchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 331),
    )


_MscSigChanBchIndex_Type.__name__ = "Integer32"
_MscSigChanBchIndex_Object = MibTableColumn
mscSigChanBchIndex = _MscSigChanBchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 1, 1, 10),
    _MscSigChanBchIndex_Type()
)
mscSigChanBchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanBchIndex.setStatus("mandatory")
_MscSigChanBchOperTable_Object = MibTable
mscSigChanBchOperTable = _MscSigChanBchOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4)
)
if mibBuilder.loadTexts:
    mscSigChanBchOperTable.setStatus("mandatory")
_MscSigChanBchOperEntry_Object = MibTableRow
mscSigChanBchOperEntry = _MscSigChanBchOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4, 1)
)
mscSigChanBchOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanBchIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanBchOperEntry.setStatus("mandatory")


class _MscSigChanBchStatus_Type(Integer32):
    """Custom type mscSigChanBchStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("egress", 5),
          ("egressMaintenance", 8),
          ("idle", 2),
          ("idleMaintenance", 6),
          ("ingress", 4),
          ("ingressMaintenance", 7),
          ("maintB", 1),
          ("outOfService", 9),
          ("unknown", 0))
    )


_MscSigChanBchStatus_Type.__name__ = "Integer32"
_MscSigChanBchStatus_Object = MibTableColumn
mscSigChanBchStatus = _MscSigChanBchStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4, 1, 1),
    _MscSigChanBchStatus_Type()
)
mscSigChanBchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchStatus.setStatus("mandatory")


class _MscSigChanBchTimeSlot_Type(Unsigned32):
    """Custom type mscSigChanBchTimeSlot based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscSigChanBchTimeSlot_Type.__name__ = "Unsigned32"
_MscSigChanBchTimeSlot_Object = MibTableColumn
mscSigChanBchTimeSlot = _MscSigChanBchTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4, 1, 2),
    _MscSigChanBchTimeSlot_Type()
)
mscSigChanBchTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchTimeSlot.setStatus("mandatory")


class _MscSigChanBchVsrInstance_Type(Unsigned32):
    """Custom type mscSigChanBchVsrInstance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscSigChanBchVsrInstance_Type.__name__ = "Unsigned32"
_MscSigChanBchVsrInstance_Object = MibTableColumn
mscSigChanBchVsrInstance = _MscSigChanBchVsrInstance_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4, 1, 3),
    _MscSigChanBchVsrInstance_Type()
)
mscSigChanBchVsrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchVsrInstance.setStatus("mandatory")


class _MscSigChanBchCalledDirectoryNumber_Type(DigitString):
    """Custom type mscSigChanBchCalledDirectoryNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscSigChanBchCalledDirectoryNumber_Type.__name__ = "DigitString"
_MscSigChanBchCalledDirectoryNumber_Object = MibTableColumn
mscSigChanBchCalledDirectoryNumber = _MscSigChanBchCalledDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 7, 4, 1, 4),
    _MscSigChanBchCalledDirectoryNumber_Type()
)
mscSigChanBchCalledDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanBchCalledDirectoryNumber.setStatus("mandatory")
_MscSigChanGw_ObjectIdentity = ObjectIdentity
mscSigChanGw = _MscSigChanGw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15)
)
_MscSigChanGwRowStatusTable_Object = MibTable
mscSigChanGwRowStatusTable = _MscSigChanGwRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1)
)
if mibBuilder.loadTexts:
    mscSigChanGwRowStatusTable.setStatus("mandatory")
_MscSigChanGwRowStatusEntry_Object = MibTableRow
mscSigChanGwRowStatusEntry = _MscSigChanGwRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1, 1)
)
mscSigChanGwRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanGwRowStatusEntry.setStatus("mandatory")
_MscSigChanGwRowStatus_Type = RowStatus
_MscSigChanGwRowStatus_Object = MibTableColumn
mscSigChanGwRowStatus = _MscSigChanGwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1, 1, 1),
    _MscSigChanGwRowStatus_Type()
)
mscSigChanGwRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwRowStatus.setStatus("mandatory")
_MscSigChanGwComponentName_Type = DisplayString
_MscSigChanGwComponentName_Object = MibTableColumn
mscSigChanGwComponentName = _MscSigChanGwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1, 1, 2),
    _MscSigChanGwComponentName_Type()
)
mscSigChanGwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwComponentName.setStatus("mandatory")
_MscSigChanGwStorageType_Type = StorageType
_MscSigChanGwStorageType_Object = MibTableColumn
mscSigChanGwStorageType = _MscSigChanGwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1, 1, 4),
    _MscSigChanGwStorageType_Type()
)
mscSigChanGwStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwStorageType.setStatus("mandatory")
_MscSigChanGwIndex_Type = NonReplicated
_MscSigChanGwIndex_Object = MibTableColumn
mscSigChanGwIndex = _MscSigChanGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 1, 1, 10),
    _MscSigChanGwIndex_Type()
)
mscSigChanGwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanGwIndex.setStatus("mandatory")
_MscSigChanGwStatsTable_Object = MibTable
mscSigChanGwStatsTable = _MscSigChanGwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 101)
)
if mibBuilder.loadTexts:
    mscSigChanGwStatsTable.setStatus("mandatory")
_MscSigChanGwStatsEntry_Object = MibTableRow
mscSigChanGwStatsEntry = _MscSigChanGwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 101, 1)
)
mscSigChanGwStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanGwStatsEntry.setStatus("mandatory")
_MscSigChanGwRequiredConversions_Type = Counter32
_MscSigChanGwRequiredConversions_Object = MibTableColumn
mscSigChanGwRequiredConversions = _MscSigChanGwRequiredConversions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 101, 1, 1),
    _MscSigChanGwRequiredConversions_Type()
)
mscSigChanGwRequiredConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwRequiredConversions.setStatus("mandatory")
_MscSigChanGwUnsupportedConversions_Type = Counter32
_MscSigChanGwUnsupportedConversions_Object = MibTableColumn
mscSigChanGwUnsupportedConversions = _MscSigChanGwUnsupportedConversions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 101, 1, 2),
    _MscSigChanGwUnsupportedConversions_Type()
)
mscSigChanGwUnsupportedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwUnsupportedConversions.setStatus("mandatory")
_MscSigChanGwGwcTable_Object = MibTable
mscSigChanGwGwcTable = _MscSigChanGwGwcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 301)
)
if mibBuilder.loadTexts:
    mscSigChanGwGwcTable.setStatus("obsolete")
_MscSigChanGwGwcEntry_Object = MibTableRow
mscSigChanGwGwcEntry = _MscSigChanGwGwcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 301, 1)
)
mscSigChanGwGwcEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwGwcIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanGwGwcEntry.setStatus("obsolete")


class _MscSigChanGwGwcIndex_Type(Integer32):
    """Custom type mscSigChanGwGwcIndex based on Integer32"""
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
        *(("analogAndCasPG", 2),
          ("etsiQsigPG", 0),
          ("euroIsdnPG", 3),
          ("mcdnPG", 4),
          ("mcdnUniPG", 5),
          ("nisPG", 1))
    )


_MscSigChanGwGwcIndex_Type.__name__ = "Integer32"
_MscSigChanGwGwcIndex_Object = MibTableColumn
mscSigChanGwGwcIndex = _MscSigChanGwGwcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 301, 1, 1),
    _MscSigChanGwGwcIndex_Type()
)
mscSigChanGwGwcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanGwGwcIndex.setStatus("obsolete")


class _MscSigChanGwGwcValue_Type(Integer32):
    """Custom type mscSigChanGwGwcValue based on Integer32"""
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
        *(("doubleEndedGw", 2),
          ("nativePG", 4),
          ("noGw", 0),
          ("singleEndedGw", 1),
          ("singleOrDoubleEndedGw", 3))
    )


_MscSigChanGwGwcValue_Type.__name__ = "Integer32"
_MscSigChanGwGwcValue_Object = MibTableColumn
mscSigChanGwGwcValue = _MscSigChanGwGwcValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 301, 1, 2),
    _MscSigChanGwGwcValue_Type()
)
mscSigChanGwGwcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwGwcValue.setStatus("obsolete")
_MscSigChanGwGatewayCapTable_Object = MibTable
mscSigChanGwGatewayCapTable = _MscSigChanGwGatewayCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 302)
)
if mibBuilder.loadTexts:
    mscSigChanGwGatewayCapTable.setStatus("mandatory")
_MscSigChanGwGatewayCapEntry_Object = MibTableRow
mscSigChanGwGatewayCapEntry = _MscSigChanGwGatewayCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 302, 1)
)
mscSigChanGwGatewayCapEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanGwGatewayCapIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanGwGatewayCapEntry.setStatus("mandatory")


class _MscSigChanGwGatewayCapIndex_Type(Integer32):
    """Custom type mscSigChanGwGatewayCapIndex based on Integer32"""
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
        *(("analogAndCasPG", 2),
          ("etsiQsigPG", 0),
          ("euroIsdnPG", 3),
          ("mcdnPG", 1))
    )


_MscSigChanGwGatewayCapIndex_Type.__name__ = "Integer32"
_MscSigChanGwGatewayCapIndex_Object = MibTableColumn
mscSigChanGwGatewayCapIndex = _MscSigChanGwGatewayCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 302, 1, 1),
    _MscSigChanGwGatewayCapIndex_Type()
)
mscSigChanGwGatewayCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanGwGatewayCapIndex.setStatus("mandatory")


class _MscSigChanGwGatewayCapValue_Type(Integer32):
    """Custom type mscSigChanGwGatewayCapValue based on Integer32"""
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
        *(("doubleEndedGw", 2),
          ("nativePG", 4),
          ("noGw", 0),
          ("singleEndedGw", 1),
          ("singleOrDoubleEndedGw", 3))
    )


_MscSigChanGwGatewayCapValue_Type.__name__ = "Integer32"
_MscSigChanGwGatewayCapValue_Object = MibTableColumn
mscSigChanGwGatewayCapValue = _MscSigChanGwGatewayCapValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 15, 302, 1, 2),
    _MscSigChanGwGatewayCapValue_Type()
)
mscSigChanGwGatewayCapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanGwGatewayCapValue.setStatus("mandatory")
_MscSigChanNcas_ObjectIdentity = ObjectIdentity
mscSigChanNcas = _MscSigChanNcas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16)
)
_MscSigChanNcasRowStatusTable_Object = MibTable
mscSigChanNcasRowStatusTable = _MscSigChanNcasRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1)
)
if mibBuilder.loadTexts:
    mscSigChanNcasRowStatusTable.setStatus("mandatory")
_MscSigChanNcasRowStatusEntry_Object = MibTableRow
mscSigChanNcasRowStatusEntry = _MscSigChanNcasRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1, 1)
)
mscSigChanNcasRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanNcasIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNcasRowStatusEntry.setStatus("mandatory")
_MscSigChanNcasRowStatus_Type = RowStatus
_MscSigChanNcasRowStatus_Object = MibTableColumn
mscSigChanNcasRowStatus = _MscSigChanNcasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1, 1, 1),
    _MscSigChanNcasRowStatus_Type()
)
mscSigChanNcasRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasRowStatus.setStatus("mandatory")
_MscSigChanNcasComponentName_Type = DisplayString
_MscSigChanNcasComponentName_Object = MibTableColumn
mscSigChanNcasComponentName = _MscSigChanNcasComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1, 1, 2),
    _MscSigChanNcasComponentName_Type()
)
mscSigChanNcasComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasComponentName.setStatus("mandatory")
_MscSigChanNcasStorageType_Type = StorageType
_MscSigChanNcasStorageType_Object = MibTableColumn
mscSigChanNcasStorageType = _MscSigChanNcasStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1, 1, 4),
    _MscSigChanNcasStorageType_Type()
)
mscSigChanNcasStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasStorageType.setStatus("mandatory")


class _MscSigChanNcasIndex_Type(Integer32):
    """Custom type mscSigChanNcasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscSigChanNcasIndex_Type.__name__ = "Integer32"
_MscSigChanNcasIndex_Object = MibTableColumn
mscSigChanNcasIndex = _MscSigChanNcasIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 1, 1, 10),
    _MscSigChanNcasIndex_Type()
)
mscSigChanNcasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanNcasIndex.setStatus("mandatory")
_MscSigChanNcasOperTable_Object = MibTable
mscSigChanNcasOperTable = _MscSigChanNcasOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100)
)
if mibBuilder.loadTexts:
    mscSigChanNcasOperTable.setStatus("mandatory")
_MscSigChanNcasOperEntry_Object = MibTableRow
mscSigChanNcasOperEntry = _MscSigChanNcasOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100, 1)
)
mscSigChanNcasOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanNcasIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNcasOperEntry.setStatus("mandatory")


class _MscSigChanNcasDirection_Type(Integer32):
    """Custom type mscSigChanNcasDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_MscSigChanNcasDirection_Type.__name__ = "Integer32"
_MscSigChanNcasDirection_Object = MibTableColumn
mscSigChanNcasDirection = _MscSigChanNcasDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100, 1, 1),
    _MscSigChanNcasDirection_Type()
)
mscSigChanNcasDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasDirection.setStatus("mandatory")


class _MscSigChanNcasCallReference_Type(Hex):
    """Custom type mscSigChanNcasCallReference based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscSigChanNcasCallReference_Type.__name__ = "Hex"
_MscSigChanNcasCallReference_Object = MibTableColumn
mscSigChanNcasCallReference = _MscSigChanNcasCallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100, 1, 2),
    _MscSigChanNcasCallReference_Type()
)
mscSigChanNcasCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasCallReference.setStatus("mandatory")


class _MscSigChanNcasCalledDirectoryNumber_Type(DigitString):
    """Custom type mscSigChanNcasCalledDirectoryNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscSigChanNcasCalledDirectoryNumber_Type.__name__ = "DigitString"
_MscSigChanNcasCalledDirectoryNumber_Object = MibTableColumn
mscSigChanNcasCalledDirectoryNumber = _MscSigChanNcasCalledDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100, 1, 3),
    _MscSigChanNcasCalledDirectoryNumber_Type()
)
mscSigChanNcasCalledDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasCalledDirectoryNumber.setStatus("mandatory")


class _MscSigChanNcasDuration_Type(Unsigned32):
    """Custom type mscSigChanNcasDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNcasDuration_Type.__name__ = "Unsigned32"
_MscSigChanNcasDuration_Object = MibTableColumn
mscSigChanNcasDuration = _MscSigChanNcasDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 16, 100, 1, 4),
    _MscSigChanNcasDuration_Type()
)
mscSigChanNcasDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNcasDuration.setStatus("mandatory")
_MscSigChanICmap_ObjectIdentity = ObjectIdentity
mscSigChanICmap = _MscSigChanICmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18)
)
_MscSigChanICmapRowStatusTable_Object = MibTable
mscSigChanICmapRowStatusTable = _MscSigChanICmapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1)
)
if mibBuilder.loadTexts:
    mscSigChanICmapRowStatusTable.setStatus("mandatory")
_MscSigChanICmapRowStatusEntry_Object = MibTableRow
mscSigChanICmapRowStatusEntry = _MscSigChanICmapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1, 1)
)
mscSigChanICmapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanICmapIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanICmapRowStatusEntry.setStatus("mandatory")
_MscSigChanICmapRowStatus_Type = RowStatus
_MscSigChanICmapRowStatus_Object = MibTableColumn
mscSigChanICmapRowStatus = _MscSigChanICmapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1, 1, 1),
    _MscSigChanICmapRowStatus_Type()
)
mscSigChanICmapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapRowStatus.setStatus("mandatory")
_MscSigChanICmapComponentName_Type = DisplayString
_MscSigChanICmapComponentName_Object = MibTableColumn
mscSigChanICmapComponentName = _MscSigChanICmapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1, 1, 2),
    _MscSigChanICmapComponentName_Type()
)
mscSigChanICmapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanICmapComponentName.setStatus("mandatory")
_MscSigChanICmapStorageType_Type = StorageType
_MscSigChanICmapStorageType_Object = MibTableColumn
mscSigChanICmapStorageType = _MscSigChanICmapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1, 1, 4),
    _MscSigChanICmapStorageType_Type()
)
mscSigChanICmapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanICmapStorageType.setStatus("mandatory")
_MscSigChanICmapIndex_Type = NonReplicated
_MscSigChanICmapIndex_Object = MibTableColumn
mscSigChanICmapIndex = _MscSigChanICmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 1, 1, 10),
    _MscSigChanICmapIndex_Type()
)
mscSigChanICmapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanICmapIndex.setStatus("mandatory")
_MscSigChanICmapIntCauseTable_Object = MibTable
mscSigChanICmapIntCauseTable = _MscSigChanICmapIntCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100)
)
if mibBuilder.loadTexts:
    mscSigChanICmapIntCauseTable.setStatus("mandatory")
_MscSigChanICmapIntCauseEntry_Object = MibTableRow
mscSigChanICmapIntCauseEntry = _MscSigChanICmapIntCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1)
)
mscSigChanICmapIntCauseEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanICmapIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanICmapIntCauseEntry.setStatus("mandatory")


class _MscSigChanICmapEgressLinkOutOfServCause_Type(Unsigned32):
    """Custom type mscSigChanICmapEgressLinkOutOfServCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapEgressLinkOutOfServCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapEgressLinkOutOfServCause_Object = MibTableColumn
mscSigChanICmapEgressLinkOutOfServCause = _MscSigChanICmapEgressLinkOutOfServCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 1),
    _MscSigChanICmapEgressLinkOutOfServCause_Type()
)
mscSigChanICmapEgressLinkOutOfServCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapEgressLinkOutOfServCause.setStatus("mandatory")


class _MscSigChanICmapChanOrCircNotAvailCause_Type(Unsigned32):
    """Custom type mscSigChanICmapChanOrCircNotAvailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapChanOrCircNotAvailCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapChanOrCircNotAvailCause_Object = MibTableColumn
mscSigChanICmapChanOrCircNotAvailCause = _MscSigChanICmapChanOrCircNotAvailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 2),
    _MscSigChanICmapChanOrCircNotAvailCause_Type()
)
mscSigChanICmapChanOrCircNotAvailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapChanOrCircNotAvailCause.setStatus("mandatory")


class _MscSigChanICmapTempFailureCause_Type(Unsigned32):
    """Custom type mscSigChanICmapTempFailureCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapTempFailureCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapTempFailureCause_Object = MibTableColumn
mscSigChanICmapTempFailureCause = _MscSigChanICmapTempFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 3),
    _MscSigChanICmapTempFailureCause_Type()
)
mscSigChanICmapTempFailureCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapTempFailureCause.setStatus("mandatory")


class _MscSigChanICmapSwitchCongestCause_Type(Unsigned32):
    """Custom type mscSigChanICmapSwitchCongestCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapSwitchCongestCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapSwitchCongestCause_Object = MibTableColumn
mscSigChanICmapSwitchCongestCause = _MscSigChanICmapSwitchCongestCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 4),
    _MscSigChanICmapSwitchCongestCause_Type()
)
mscSigChanICmapSwitchCongestCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapSwitchCongestCause.setStatus("mandatory")


class _MscSigChanICmapReqChanOrCircNotAvailCause_Type(Unsigned32):
    """Custom type mscSigChanICmapReqChanOrCircNotAvailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapReqChanOrCircNotAvailCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapReqChanOrCircNotAvailCause_Object = MibTableColumn
mscSigChanICmapReqChanOrCircNotAvailCause = _MscSigChanICmapReqChanOrCircNotAvailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 5),
    _MscSigChanICmapReqChanOrCircNotAvailCause_Type()
)
mscSigChanICmapReqChanOrCircNotAvailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapReqChanOrCircNotAvailCause.setStatus("mandatory")


class _MscSigChanICmapResourceUnavailCause_Type(Unsigned32):
    """Custom type mscSigChanICmapResourceUnavailCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapResourceUnavailCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapResourceUnavailCause_Object = MibTableColumn
mscSigChanICmapResourceUnavailCause = _MscSigChanICmapResourceUnavailCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 6),
    _MscSigChanICmapResourceUnavailCause_Type()
)
mscSigChanICmapResourceUnavailCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapResourceUnavailCause.setStatus("mandatory")


class _MscSigChanICmapServNotAllowedCause_Type(Unsigned32):
    """Custom type mscSigChanICmapServNotAllowedCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapServNotAllowedCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapServNotAllowedCause_Object = MibTableColumn
mscSigChanICmapServNotAllowedCause = _MscSigChanICmapServNotAllowedCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 7),
    _MscSigChanICmapServNotAllowedCause_Type()
)
mscSigChanICmapServNotAllowedCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapServNotAllowedCause.setStatus("mandatory")


class _MscSigChanICmapNoSuchChannelCause_Type(Unsigned32):
    """Custom type mscSigChanICmapNoSuchChannelCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapNoSuchChannelCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapNoSuchChannelCause_Object = MibTableColumn
mscSigChanICmapNoSuchChannelCause = _MscSigChanICmapNoSuchChannelCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 8),
    _MscSigChanICmapNoSuchChannelCause_Type()
)
mscSigChanICmapNoSuchChannelCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapNoSuchChannelCause.setStatus("mandatory")


class _MscSigChanICmapIncompatDestCause_Type(Unsigned32):
    """Custom type mscSigChanICmapIncompatDestCause based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
        ValueRangeConstraint(128, 128),
    )


_MscSigChanICmapIncompatDestCause_Type.__name__ = "Unsigned32"
_MscSigChanICmapIncompatDestCause_Object = MibTableColumn
mscSigChanICmapIncompatDestCause = _MscSigChanICmapIncompatDestCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 18, 100, 1, 9),
    _MscSigChanICmapIncompatDestCause_Type()
)
mscSigChanICmapIncompatDestCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanICmapIncompatDestCause.setStatus("mandatory")
_MscSigChanCidDataTable_Object = MibTable
mscSigChanCidDataTable = _MscSigChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 100)
)
if mibBuilder.loadTexts:
    mscSigChanCidDataTable.setStatus("mandatory")
_MscSigChanCidDataEntry_Object = MibTableRow
mscSigChanCidDataEntry = _MscSigChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 100, 1)
)
mscSigChanCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanCidDataEntry.setStatus("mandatory")


class _MscSigChanCustomerIdentifier_Type(Unsigned32):
    """Custom type mscSigChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscSigChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscSigChanCustomerIdentifier_Object = MibTableColumn
mscSigChanCustomerIdentifier = _MscSigChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 100, 1, 1),
    _MscSigChanCustomerIdentifier_Type()
)
mscSigChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanCustomerIdentifier.setStatus("mandatory")
_MscSigChanIfEntryTable_Object = MibTable
mscSigChanIfEntryTable = _MscSigChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 101)
)
if mibBuilder.loadTexts:
    mscSigChanIfEntryTable.setStatus("mandatory")
_MscSigChanIfEntryEntry_Object = MibTableRow
mscSigChanIfEntryEntry = _MscSigChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 101, 1)
)
mscSigChanIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanIfEntryEntry.setStatus("mandatory")


class _MscSigChanIfAdminStatus_Type(Integer32):
    """Custom type mscSigChanIfAdminStatus based on Integer32"""
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


_MscSigChanIfAdminStatus_Type.__name__ = "Integer32"
_MscSigChanIfAdminStatus_Object = MibTableColumn
mscSigChanIfAdminStatus = _MscSigChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 101, 1, 1),
    _MscSigChanIfAdminStatus_Type()
)
mscSigChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanIfAdminStatus.setStatus("mandatory")


class _MscSigChanIfIndex_Type(InterfaceIndex):
    """Custom type mscSigChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscSigChanIfIndex_Type.__name__ = "InterfaceIndex"
_MscSigChanIfIndex_Object = MibTableColumn
mscSigChanIfIndex = _MscSigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 101, 1, 2),
    _MscSigChanIfIndex_Type()
)
mscSigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanIfIndex.setStatus("mandatory")
_MscSigChanOperStatusTable_Object = MibTable
mscSigChanOperStatusTable = _MscSigChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 102)
)
if mibBuilder.loadTexts:
    mscSigChanOperStatusTable.setStatus("mandatory")
_MscSigChanOperStatusEntry_Object = MibTableRow
mscSigChanOperStatusEntry = _MscSigChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 102, 1)
)
mscSigChanOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanOperStatusEntry.setStatus("mandatory")


class _MscSigChanSnmpOperStatus_Type(Integer32):
    """Custom type mscSigChanSnmpOperStatus based on Integer32"""
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


_MscSigChanSnmpOperStatus_Type.__name__ = "Integer32"
_MscSigChanSnmpOperStatus_Object = MibTableColumn
mscSigChanSnmpOperStatus = _MscSigChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 102, 1, 1),
    _MscSigChanSnmpOperStatus_Type()
)
mscSigChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanSnmpOperStatus.setStatus("mandatory")
_MscSigChanStateTable_Object = MibTable
mscSigChanStateTable = _MscSigChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 103)
)
if mibBuilder.loadTexts:
    mscSigChanStateTable.setStatus("mandatory")
_MscSigChanStateEntry_Object = MibTableRow
mscSigChanStateEntry = _MscSigChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 103, 1)
)
mscSigChanStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanStateEntry.setStatus("mandatory")


class _MscSigChanAdminState_Type(Integer32):
    """Custom type mscSigChanAdminState based on Integer32"""
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


_MscSigChanAdminState_Type.__name__ = "Integer32"
_MscSigChanAdminState_Object = MibTableColumn
mscSigChanAdminState = _MscSigChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 103, 1, 1),
    _MscSigChanAdminState_Type()
)
mscSigChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanAdminState.setStatus("mandatory")


class _MscSigChanOperationalState_Type(Integer32):
    """Custom type mscSigChanOperationalState based on Integer32"""
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


_MscSigChanOperationalState_Type.__name__ = "Integer32"
_MscSigChanOperationalState_Object = MibTableColumn
mscSigChanOperationalState = _MscSigChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 103, 1, 2),
    _MscSigChanOperationalState_Type()
)
mscSigChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanOperationalState.setStatus("mandatory")


class _MscSigChanUsageState_Type(Integer32):
    """Custom type mscSigChanUsageState based on Integer32"""
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


_MscSigChanUsageState_Type.__name__ = "Integer32"
_MscSigChanUsageState_Object = MibTableColumn
mscSigChanUsageState = _MscSigChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 103, 1, 3),
    _MscSigChanUsageState_Type()
)
mscSigChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanUsageState.setStatus("mandatory")
_MscSigChanProvTable_Object = MibTable
mscSigChanProvTable = _MscSigChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104)
)
if mibBuilder.loadTexts:
    mscSigChanProvTable.setStatus("mandatory")
_MscSigChanProvEntry_Object = MibTableRow
mscSigChanProvEntry = _MscSigChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104, 1)
)
mscSigChanProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanProvEntry.setStatus("mandatory")


class _MscSigChanCommentText_Type(AsciiString):
    """Custom type mscSigChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscSigChanCommentText_Type.__name__ = "AsciiString"
_MscSigChanCommentText_Object = MibTableColumn
mscSigChanCommentText = _MscSigChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104, 1, 1),
    _MscSigChanCommentText_Type()
)
mscSigChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanCommentText.setStatus("mandatory")


class _MscSigChanOctothorpeEod_Type(Integer32):
    """Custom type mscSigChanOctothorpeEod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_MscSigChanOctothorpeEod_Type.__name__ = "Integer32"
_MscSigChanOctothorpeEod_Object = MibTableColumn
mscSigChanOctothorpeEod = _MscSigChanOctothorpeEod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104, 1, 2),
    _MscSigChanOctothorpeEod_Type()
)
mscSigChanOctothorpeEod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanOctothorpeEod.setStatus("mandatory")


class _MscSigChanForceNpiTon_Type(Integer32):
    """Custom type mscSigChanForceNpiTon based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_MscSigChanForceNpiTon_Type.__name__ = "Integer32"
_MscSigChanForceNpiTon_Object = MibTableColumn
mscSigChanForceNpiTon = _MscSigChanForceNpiTon_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104, 1, 3),
    _MscSigChanForceNpiTon_Type()
)
mscSigChanForceNpiTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanForceNpiTon.setStatus("mandatory")


class _MscSigChanDefaultNpiTon_Type(Integer32):
    """Custom type mscSigChanDefaultNpiTon based on Integer32"""
    defaultValue = 12

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("casUnknown", 12),
          ("international", 1),
          ("national", 2),
          ("p0", 4),
          ("p1", 5),
          ("p2", 6),
          ("p3", 7),
          ("p4", 8),
          ("p5", 9),
          ("p6", 10),
          ("p7", 11),
          ("subscriber", 3),
          ("unknown", 0))
    )


_MscSigChanDefaultNpiTon_Type.__name__ = "Integer32"
_MscSigChanDefaultNpiTon_Object = MibTableColumn
mscSigChanDefaultNpiTon = _MscSigChanDefaultNpiTon_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 104, 1, 4),
    _MscSigChanDefaultNpiTon_Type()
)
mscSigChanDefaultNpiTon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanDefaultNpiTon.setStatus("mandatory")
_MscSigChanSubroutesTable_Object = MibTable
mscSigChanSubroutesTable = _MscSigChanSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 307)
)
if mibBuilder.loadTexts:
    mscSigChanSubroutesTable.setStatus("mandatory")
_MscSigChanSubroutesEntry_Object = MibTableRow
mscSigChanSubroutesEntry = _MscSigChanSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 307, 1)
)
mscSigChanSubroutesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanSubroutesValue"),
)
if mibBuilder.loadTexts:
    mscSigChanSubroutesEntry.setStatus("mandatory")
_MscSigChanSubroutesValue_Type = Link
_MscSigChanSubroutesValue_Object = MibTableColumn
mscSigChanSubroutesValue = _MscSigChanSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 307, 1, 1),
    _MscSigChanSubroutesValue_Type()
)
mscSigChanSubroutesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanSubroutesValue.setStatus("mandatory")
_MscSigChanSubroutesRowStatus_Type = RowStatus
_MscSigChanSubroutesRowStatus_Object = MibTableColumn
mscSigChanSubroutesRowStatus = _MscSigChanSubroutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 307, 1, 2),
    _MscSigChanSubroutesRowStatus_Type()
)
mscSigChanSubroutesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscSigChanSubroutesRowStatus.setStatus("mandatory")
_MscSigChanDegradedSubroutesTable_Object = MibTable
mscSigChanDegradedSubroutesTable = _MscSigChanDegradedSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 308)
)
if mibBuilder.loadTexts:
    mscSigChanDegradedSubroutesTable.setStatus("mandatory")
_MscSigChanDegradedSubroutesEntry_Object = MibTableRow
mscSigChanDegradedSubroutesEntry = _MscSigChanDegradedSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 308, 1)
)
mscSigChanDegradedSubroutesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanDegradedSubroutesValue"),
)
if mibBuilder.loadTexts:
    mscSigChanDegradedSubroutesEntry.setStatus("mandatory")
_MscSigChanDegradedSubroutesValue_Type = RowPointer
_MscSigChanDegradedSubroutesValue_Object = MibTableColumn
mscSigChanDegradedSubroutesValue = _MscSigChanDegradedSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 308, 1, 1),
    _MscSigChanDegradedSubroutesValue_Type()
)
mscSigChanDegradedSubroutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanDegradedSubroutesValue.setStatus("mandatory")
_MscVRoute_ObjectIdentity = ObjectIdentity
mscVRoute = _MscVRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116)
)
_MscVRouteRowStatusTable_Object = MibTable
mscVRouteRowStatusTable = _MscVRouteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1)
)
if mibBuilder.loadTexts:
    mscVRouteRowStatusTable.setStatus("mandatory")
_MscVRouteRowStatusEntry_Object = MibTableRow
mscVRouteRowStatusEntry = _MscVRouteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1, 1)
)
mscVRouteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteRowStatusEntry.setStatus("mandatory")
_MscVRouteRowStatus_Type = RowStatus
_MscVRouteRowStatus_Object = MibTableColumn
mscVRouteRowStatus = _MscVRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1, 1, 1),
    _MscVRouteRowStatus_Type()
)
mscVRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteRowStatus.setStatus("mandatory")
_MscVRouteComponentName_Type = DisplayString
_MscVRouteComponentName_Object = MibTableColumn
mscVRouteComponentName = _MscVRouteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1, 1, 2),
    _MscVRouteComponentName_Type()
)
mscVRouteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteComponentName.setStatus("mandatory")
_MscVRouteStorageType_Type = StorageType
_MscVRouteStorageType_Object = MibTableColumn
mscVRouteStorageType = _MscVRouteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1, 1, 4),
    _MscVRouteStorageType_Type()
)
mscVRouteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteStorageType.setStatus("mandatory")


class _MscVRouteIndex_Type(Integer32):
    """Custom type mscVRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVRouteIndex_Type.__name__ = "Integer32"
_MscVRouteIndex_Object = MibTableColumn
mscVRouteIndex = _MscVRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 1, 1, 10),
    _MscVRouteIndex_Type()
)
mscVRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteIndex.setStatus("mandatory")
_MscVRouteDebug_ObjectIdentity = ObjectIdentity
mscVRouteDebug = _MscVRouteDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2)
)
_MscVRouteDebugRowStatusTable_Object = MibTable
mscVRouteDebugRowStatusTable = _MscVRouteDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1)
)
if mibBuilder.loadTexts:
    mscVRouteDebugRowStatusTable.setStatus("mandatory")
_MscVRouteDebugRowStatusEntry_Object = MibTableRow
mscVRouteDebugRowStatusEntry = _MscVRouteDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1, 1)
)
mscVRouteDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteDebugRowStatusEntry.setStatus("mandatory")
_MscVRouteDebugRowStatus_Type = RowStatus
_MscVRouteDebugRowStatus_Object = MibTableColumn
mscVRouteDebugRowStatus = _MscVRouteDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1, 1, 1),
    _MscVRouteDebugRowStatus_Type()
)
mscVRouteDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDebugRowStatus.setStatus("mandatory")
_MscVRouteDebugComponentName_Type = DisplayString
_MscVRouteDebugComponentName_Object = MibTableColumn
mscVRouteDebugComponentName = _MscVRouteDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1, 1, 2),
    _MscVRouteDebugComponentName_Type()
)
mscVRouteDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDebugComponentName.setStatus("mandatory")
_MscVRouteDebugStorageType_Type = StorageType
_MscVRouteDebugStorageType_Object = MibTableColumn
mscVRouteDebugStorageType = _MscVRouteDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1, 1, 4),
    _MscVRouteDebugStorageType_Type()
)
mscVRouteDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDebugStorageType.setStatus("mandatory")
_MscVRouteDebugIndex_Type = NonReplicated
_MscVRouteDebugIndex_Object = MibTableColumn
mscVRouteDebugIndex = _MscVRouteDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 2, 1, 1, 10),
    _MscVRouteDebugIndex_Type()
)
mscVRouteDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteDebugIndex.setStatus("mandatory")
_MscVRouteInterface_ObjectIdentity = ObjectIdentity
mscVRouteInterface = _MscVRouteInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3)
)
_MscVRouteInterfaceRowStatusTable_Object = MibTable
mscVRouteInterfaceRowStatusTable = _MscVRouteInterfaceRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1)
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceRowStatusTable.setStatus("mandatory")
_MscVRouteInterfaceRowStatusEntry_Object = MibTableRow
mscVRouteInterfaceRowStatusEntry = _MscVRouteInterfaceRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1, 1)
)
mscVRouteInterfaceRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceRowStatusEntry.setStatus("mandatory")
_MscVRouteInterfaceRowStatus_Type = RowStatus
_MscVRouteInterfaceRowStatus_Object = MibTableColumn
mscVRouteInterfaceRowStatus = _MscVRouteInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1, 1, 1),
    _MscVRouteInterfaceRowStatus_Type()
)
mscVRouteInterfaceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteInterfaceRowStatus.setStatus("mandatory")
_MscVRouteInterfaceComponentName_Type = DisplayString
_MscVRouteInterfaceComponentName_Object = MibTableColumn
mscVRouteInterfaceComponentName = _MscVRouteInterfaceComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1, 1, 2),
    _MscVRouteInterfaceComponentName_Type()
)
mscVRouteInterfaceComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteInterfaceComponentName.setStatus("mandatory")
_MscVRouteInterfaceStorageType_Type = StorageType
_MscVRouteInterfaceStorageType_Object = MibTableColumn
mscVRouteInterfaceStorageType = _MscVRouteInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1, 1, 4),
    _MscVRouteInterfaceStorageType_Type()
)
mscVRouteInterfaceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteInterfaceStorageType.setStatus("mandatory")
_MscVRouteInterfaceIndex_Type = NonReplicated
_MscVRouteInterfaceIndex_Object = MibTableColumn
mscVRouteInterfaceIndex = _MscVRouteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 1, 1, 10),
    _MscVRouteInterfaceIndex_Type()
)
mscVRouteInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteInterfaceIndex.setStatus("mandatory")
_MscVRouteInterfaceProvTable_Object = MibTable
mscVRouteInterfaceProvTable = _MscVRouteInterfaceProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10)
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceProvTable.setStatus("mandatory")
_MscVRouteInterfaceProvEntry_Object = MibTableRow
mscVRouteInterfaceProvEntry = _MscVRouteInterfaceProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1)
)
mscVRouteInterfaceProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceProvEntry.setStatus("mandatory")


class _MscVRouteInterfaceIngressAudioGain_Type(Integer32):
    """Custom type mscVRouteInterfaceIngressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscVRouteInterfaceIngressAudioGain_Type.__name__ = "Integer32"
_MscVRouteInterfaceIngressAudioGain_Object = MibTableColumn
mscVRouteInterfaceIngressAudioGain = _MscVRouteInterfaceIngressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 1),
    _MscVRouteInterfaceIngressAudioGain_Type()
)
mscVRouteInterfaceIngressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceIngressAudioGain.setStatus("mandatory")


class _MscVRouteInterfaceEgressAudioGain_Type(Integer32):
    """Custom type mscVRouteInterfaceEgressAudioGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_MscVRouteInterfaceEgressAudioGain_Type.__name__ = "Integer32"
_MscVRouteInterfaceEgressAudioGain_Object = MibTableColumn
mscVRouteInterfaceEgressAudioGain = _MscVRouteInterfaceEgressAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 2),
    _MscVRouteInterfaceEgressAudioGain_Type()
)
mscVRouteInterfaceEgressAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceEgressAudioGain.setStatus("mandatory")


class _MscVRouteInterfaceTandemPassThrough_Type(Integer32):
    """Custom type mscVRouteInterfaceTandemPassThrough based on Integer32"""
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


_MscVRouteInterfaceTandemPassThrough_Type.__name__ = "Integer32"
_MscVRouteInterfaceTandemPassThrough_Object = MibTableColumn
mscVRouteInterfaceTandemPassThrough = _MscVRouteInterfaceTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 3),
    _MscVRouteInterfaceTandemPassThrough_Type()
)
mscVRouteInterfaceTandemPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceTandemPassThrough.setStatus("mandatory")


class _MscVRouteInterfaceEchoCancellation_Type(Integer32):
    """Custom type mscVRouteInterfaceEchoCancellation based on Integer32"""
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


_MscVRouteInterfaceEchoCancellation_Type.__name__ = "Integer32"
_MscVRouteInterfaceEchoCancellation_Object = MibTableColumn
mscVRouteInterfaceEchoCancellation = _MscVRouteInterfaceEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 5),
    _MscVRouteInterfaceEchoCancellation_Type()
)
mscVRouteInterfaceEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceEchoCancellation.setStatus("obsolete")


class _MscVRouteInterfaceComfortNoiseCap_Type(Integer32):
    """Custom type mscVRouteInterfaceComfortNoiseCap based on Integer32"""
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


_MscVRouteInterfaceComfortNoiseCap_Type.__name__ = "Integer32"
_MscVRouteInterfaceComfortNoiseCap_Object = MibTableColumn
mscVRouteInterfaceComfortNoiseCap = _MscVRouteInterfaceComfortNoiseCap_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 6),
    _MscVRouteInterfaceComfortNoiseCap_Type()
)
mscVRouteInterfaceComfortNoiseCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceComfortNoiseCap.setStatus("mandatory")


class _MscVRouteInterfaceSpeechHangoverTime_Type(Unsigned32):
    """Custom type mscVRouteInterfaceSpeechHangoverTime based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_MscVRouteInterfaceSpeechHangoverTime_Type.__name__ = "Unsigned32"
_MscVRouteInterfaceSpeechHangoverTime_Object = MibTableColumn
mscVRouteInterfaceSpeechHangoverTime = _MscVRouteInterfaceSpeechHangoverTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 7),
    _MscVRouteInterfaceSpeechHangoverTime_Type()
)
mscVRouteInterfaceSpeechHangoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceSpeechHangoverTime.setStatus("mandatory")


class _MscVRouteInterfaceFaxHangoverTimeG711G726_Type(Unsigned32):
    """Custom type mscVRouteInterfaceFaxHangoverTimeG711G726 based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 20000),
    )


_MscVRouteInterfaceFaxHangoverTimeG711G726_Type.__name__ = "Unsigned32"
_MscVRouteInterfaceFaxHangoverTimeG711G726_Object = MibTableColumn
mscVRouteInterfaceFaxHangoverTimeG711G726 = _MscVRouteInterfaceFaxHangoverTimeG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 8),
    _MscVRouteInterfaceFaxHangoverTimeG711G726_Type()
)
mscVRouteInterfaceFaxHangoverTimeG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceFaxHangoverTimeG711G726.setStatus("mandatory")


class _MscVRouteInterfaceModemFaxSpeechDiscrim_Type(Integer32):
    """Custom type mscVRouteInterfaceModemFaxSpeechDiscrim based on Integer32"""
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


_MscVRouteInterfaceModemFaxSpeechDiscrim_Type.__name__ = "Integer32"
_MscVRouteInterfaceModemFaxSpeechDiscrim_Object = MibTableColumn
mscVRouteInterfaceModemFaxSpeechDiscrim = _MscVRouteInterfaceModemFaxSpeechDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 9),
    _MscVRouteInterfaceModemFaxSpeechDiscrim_Type()
)
mscVRouteInterfaceModemFaxSpeechDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceModemFaxSpeechDiscrim.setStatus("mandatory")


class _MscVRouteInterfaceEchoTailDelay_Type(Unsigned32):
    """Custom type mscVRouteInterfaceEchoTailDelay based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
    )


_MscVRouteInterfaceEchoTailDelay_Type.__name__ = "Unsigned32"
_MscVRouteInterfaceEchoTailDelay_Object = MibTableColumn
mscVRouteInterfaceEchoTailDelay = _MscVRouteInterfaceEchoTailDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 10),
    _MscVRouteInterfaceEchoTailDelay_Type()
)
mscVRouteInterfaceEchoTailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceEchoTailDelay.setStatus("mandatory")


class _MscVRouteInterfaceEchoReturnLoss_Type(Unsigned32):
    """Custom type mscVRouteInterfaceEchoReturnLoss based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(6, 6),
    )


_MscVRouteInterfaceEchoReturnLoss_Type.__name__ = "Unsigned32"
_MscVRouteInterfaceEchoReturnLoss_Object = MibTableColumn
mscVRouteInterfaceEchoReturnLoss = _MscVRouteInterfaceEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 11),
    _MscVRouteInterfaceEchoReturnLoss_Type()
)
mscVRouteInterfaceEchoReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceEchoReturnLoss.setStatus("mandatory")


class _MscVRouteInterfaceEcanBypassMode_Type(Integer32):
    """Custom type mscVRouteInterfaceEcanBypassMode based on Integer32"""
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


_MscVRouteInterfaceEcanBypassMode_Type.__name__ = "Integer32"
_MscVRouteInterfaceEcanBypassMode_Object = MibTableColumn
mscVRouteInterfaceEcanBypassMode = _MscVRouteInterfaceEcanBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 10, 1, 15),
    _MscVRouteInterfaceEcanBypassMode_Type()
)
mscVRouteInterfaceEcanBypassMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceEcanBypassMode.setStatus("mandatory")
_MscVRouteInterfaceStructuredEchoCancellationTable_Object = MibTable
mscVRouteInterfaceStructuredEchoCancellationTable = _MscVRouteInterfaceStructuredEchoCancellationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 474)
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceStructuredEchoCancellationTable.setStatus("mandatory")
_MscVRouteInterfaceStructuredEchoCancellationEntry_Object = MibTableRow
mscVRouteInterfaceStructuredEchoCancellationEntry = _MscVRouteInterfaceStructuredEchoCancellationEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 474, 1)
)
mscVRouteInterfaceStructuredEchoCancellationEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteInterfaceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteInterfaceStructuredEchoCancellationIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteInterfaceStructuredEchoCancellationEntry.setStatus("mandatory")


class _MscVRouteInterfaceStructuredEchoCancellationIndex_Type(Integer32):
    """Custom type mscVRouteInterfaceStructuredEchoCancellationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2", 1))
    )


_MscVRouteInterfaceStructuredEchoCancellationIndex_Type.__name__ = "Integer32"
_MscVRouteInterfaceStructuredEchoCancellationIndex_Object = MibTableColumn
mscVRouteInterfaceStructuredEchoCancellationIndex = _MscVRouteInterfaceStructuredEchoCancellationIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 474, 1, 1),
    _MscVRouteInterfaceStructuredEchoCancellationIndex_Type()
)
mscVRouteInterfaceStructuredEchoCancellationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteInterfaceStructuredEchoCancellationIndex.setStatus("mandatory")


class _MscVRouteInterfaceStructuredEchoCancellationValue_Type(Integer32):
    """Custom type mscVRouteInterfaceStructuredEchoCancellationValue based on Integer32"""
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


_MscVRouteInterfaceStructuredEchoCancellationValue_Type.__name__ = "Integer32"
_MscVRouteInterfaceStructuredEchoCancellationValue_Object = MibTableColumn
mscVRouteInterfaceStructuredEchoCancellationValue = _MscVRouteInterfaceStructuredEchoCancellationValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 3, 474, 1, 2),
    _MscVRouteInterfaceStructuredEchoCancellationValue_Type()
)
mscVRouteInterfaceStructuredEchoCancellationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteInterfaceStructuredEchoCancellationValue.setStatus("mandatory")
_MscVRouteDna_ObjectIdentity = ObjectIdentity
mscVRouteDna = _MscVRouteDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4)
)
_MscVRouteDnaRowStatusTable_Object = MibTable
mscVRouteDnaRowStatusTable = _MscVRouteDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1)
)
if mibBuilder.loadTexts:
    mscVRouteDnaRowStatusTable.setStatus("mandatory")
_MscVRouteDnaRowStatusEntry_Object = MibTableRow
mscVRouteDnaRowStatusEntry = _MscVRouteDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1, 1)
)
mscVRouteDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteDnaRowStatusEntry.setStatus("mandatory")
_MscVRouteDnaRowStatus_Type = RowStatus
_MscVRouteDnaRowStatus_Object = MibTableColumn
mscVRouteDnaRowStatus = _MscVRouteDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1, 1, 1),
    _MscVRouteDnaRowStatus_Type()
)
mscVRouteDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDnaRowStatus.setStatus("mandatory")
_MscVRouteDnaComponentName_Type = DisplayString
_MscVRouteDnaComponentName_Object = MibTableColumn
mscVRouteDnaComponentName = _MscVRouteDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1, 1, 2),
    _MscVRouteDnaComponentName_Type()
)
mscVRouteDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDnaComponentName.setStatus("mandatory")
_MscVRouteDnaStorageType_Type = StorageType
_MscVRouteDnaStorageType_Object = MibTableColumn
mscVRouteDnaStorageType = _MscVRouteDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1, 1, 4),
    _MscVRouteDnaStorageType_Type()
)
mscVRouteDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDnaStorageType.setStatus("mandatory")
_MscVRouteDnaIndex_Type = NonReplicated
_MscVRouteDnaIndex_Object = MibTableColumn
mscVRouteDnaIndex = _MscVRouteDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 1, 1, 10),
    _MscVRouteDnaIndex_Type()
)
mscVRouteDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteDnaIndex.setStatus("mandatory")
_MscVRouteDnaAddressTable_Object = MibTable
mscVRouteDnaAddressTable = _MscVRouteDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 10)
)
if mibBuilder.loadTexts:
    mscVRouteDnaAddressTable.setStatus("mandatory")
_MscVRouteDnaAddressEntry_Object = MibTableRow
mscVRouteDnaAddressEntry = _MscVRouteDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 10, 1)
)
mscVRouteDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteDnaAddressEntry.setStatus("mandatory")


class _MscVRouteDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscVRouteDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_MscVRouteDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscVRouteDnaNumberingPlanIndicator_Object = MibTableColumn
mscVRouteDnaNumberingPlanIndicator = _MscVRouteDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 10, 1, 1),
    _MscVRouteDnaNumberingPlanIndicator_Type()
)
mscVRouteDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscVRouteDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscVRouteDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscVRouteDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscVRouteDnaDataNetworkAddress_Object = MibTableColumn
mscVRouteDnaDataNetworkAddress = _MscVRouteDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 4, 10, 1, 2),
    _MscVRouteDnaDataNetworkAddress_Type()
)
mscVRouteDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteDnaDataNetworkAddress.setStatus("mandatory")
_MscVRouteAcct_ObjectIdentity = ObjectIdentity
mscVRouteAcct = _MscVRouteAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5)
)
_MscVRouteAcctRowStatusTable_Object = MibTable
mscVRouteAcctRowStatusTable = _MscVRouteAcctRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1)
)
if mibBuilder.loadTexts:
    mscVRouteAcctRowStatusTable.setStatus("mandatory")
_MscVRouteAcctRowStatusEntry_Object = MibTableRow
mscVRouteAcctRowStatusEntry = _MscVRouteAcctRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1, 1)
)
mscVRouteAcctRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteAcctIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteAcctRowStatusEntry.setStatus("mandatory")
_MscVRouteAcctRowStatus_Type = RowStatus
_MscVRouteAcctRowStatus_Object = MibTableColumn
mscVRouteAcctRowStatus = _MscVRouteAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1, 1, 1),
    _MscVRouteAcctRowStatus_Type()
)
mscVRouteAcctRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteAcctRowStatus.setStatus("mandatory")
_MscVRouteAcctComponentName_Type = DisplayString
_MscVRouteAcctComponentName_Object = MibTableColumn
mscVRouteAcctComponentName = _MscVRouteAcctComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1, 1, 2),
    _MscVRouteAcctComponentName_Type()
)
mscVRouteAcctComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteAcctComponentName.setStatus("mandatory")
_MscVRouteAcctStorageType_Type = StorageType
_MscVRouteAcctStorageType_Object = MibTableColumn
mscVRouteAcctStorageType = _MscVRouteAcctStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1, 1, 4),
    _MscVRouteAcctStorageType_Type()
)
mscVRouteAcctStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteAcctStorageType.setStatus("mandatory")
_MscVRouteAcctIndex_Type = NonReplicated
_MscVRouteAcctIndex_Object = MibTableColumn
mscVRouteAcctIndex = _MscVRouteAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 1, 1, 10),
    _MscVRouteAcctIndex_Type()
)
mscVRouteAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVRouteAcctIndex.setStatus("mandatory")
_MscVRouteAcctProvTable_Object = MibTable
mscVRouteAcctProvTable = _MscVRouteAcctProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2)
)
if mibBuilder.loadTexts:
    mscVRouteAcctProvTable.setStatus("mandatory")
_MscVRouteAcctProvEntry_Object = MibTableRow
mscVRouteAcctProvEntry = _MscVRouteAcctProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1)
)
mscVRouteAcctProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteAcctIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteAcctProvEntry.setStatus("mandatory")


class _MscVRouteAcctAccountCollection_Type(OctetString):
    """Custom type mscVRouteAcctAccountCollection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVRouteAcctAccountCollection_Type.__name__ = "OctetString"
_MscVRouteAcctAccountCollection_Object = MibTableColumn
mscVRouteAcctAccountCollection = _MscVRouteAcctAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1, 2),
    _MscVRouteAcctAccountCollection_Type()
)
mscVRouteAcctAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteAcctAccountCollection.setStatus("mandatory")


class _MscVRouteAcctAccountClass_Type(Unsigned32):
    """Custom type mscVRouteAcctAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVRouteAcctAccountClass_Type.__name__ = "Unsigned32"
_MscVRouteAcctAccountClass_Object = MibTableColumn
mscVRouteAcctAccountClass = _MscVRouteAcctAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1, 3),
    _MscVRouteAcctAccountClass_Type()
)
mscVRouteAcctAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteAcctAccountClass.setStatus("mandatory")


class _MscVRouteAcctServiceExchange_Type(Unsigned32):
    """Custom type mscVRouteAcctServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVRouteAcctServiceExchange_Type.__name__ = "Unsigned32"
_MscVRouteAcctServiceExchange_Object = MibTableColumn
mscVRouteAcctServiceExchange = _MscVRouteAcctServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1, 4),
    _MscVRouteAcctServiceExchange_Type()
)
mscVRouteAcctServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteAcctServiceExchange.setStatus("mandatory")


class _MscVRouteAcctDigitsSuppressed_Type(Unsigned32):
    """Custom type mscVRouteAcctDigitsSuppressed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MscVRouteAcctDigitsSuppressed_Type.__name__ = "Unsigned32"
_MscVRouteAcctDigitsSuppressed_Object = MibTableColumn
mscVRouteAcctDigitsSuppressed = _MscVRouteAcctDigitsSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1, 5),
    _MscVRouteAcctDigitsSuppressed_Type()
)
mscVRouteAcctDigitsSuppressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteAcctDigitsSuppressed.setStatus("mandatory")


class _MscVRouteAcctAccountingOptions_Type(OctetString):
    """Custom type mscVRouteAcctAccountingOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVRouteAcctAccountingOptions_Type.__name__ = "OctetString"
_MscVRouteAcctAccountingOptions_Object = MibTableColumn
mscVRouteAcctAccountingOptions = _MscVRouteAcctAccountingOptions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 5, 2, 1, 6),
    _MscVRouteAcctAccountingOptions_Type()
)
mscVRouteAcctAccountingOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteAcctAccountingOptions.setStatus("mandatory")
_MscVRouteProvTable_Object = MibTable
mscVRouteProvTable = _MscVRouteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10)
)
if mibBuilder.loadTexts:
    mscVRouteProvTable.setStatus("mandatory")
_MscVRouteProvEntry_Object = MibTableRow
mscVRouteProvEntry = _MscVRouteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1)
)
mscVRouteProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteProvEntry.setStatus("mandatory")


class _MscVRouteCommentText_Type(AsciiString):
    """Custom type mscVRouteCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVRouteCommentText_Type.__name__ = "AsciiString"
_MscVRouteCommentText_Object = MibTableColumn
mscVRouteCommentText = _MscVRouteCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 1),
    _MscVRouteCommentText_Type()
)
mscVRouteCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteCommentText.setStatus("mandatory")


class _MscVRouteTypeOfRoute_Type(Integer32):
    """Custom type mscVRouteTypeOfRoute based on Integer32"""
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
        *(("data", 1),
          ("voice", 0),
          ("voiceData", 2))
    )


_MscVRouteTypeOfRoute_Type.__name__ = "Integer32"
_MscVRouteTypeOfRoute_Object = MibTableColumn
mscVRouteTypeOfRoute = _MscVRouteTypeOfRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 2),
    _MscVRouteTypeOfRoute_Type()
)
mscVRouteTypeOfRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteTypeOfRoute.setStatus("mandatory")


class _MscVRouteDiallingPlan0_Type(OctetString):
    """Custom type mscVRouteDiallingPlan0 based on OctetString"""
    defaultHexValue = "fff8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVRouteDiallingPlan0_Type.__name__ = "OctetString"
_MscVRouteDiallingPlan0_Object = MibTableColumn
mscVRouteDiallingPlan0 = _MscVRouteDiallingPlan0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 6),
    _MscVRouteDiallingPlan0_Type()
)
mscVRouteDiallingPlan0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteDiallingPlan0.setStatus("mandatory")


class _MscVRouteDiallingPlan1_Type(OctetString):
    """Custom type mscVRouteDiallingPlan1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVRouteDiallingPlan1_Type.__name__ = "OctetString"
_MscVRouteDiallingPlan1_Object = MibTableColumn
mscVRouteDiallingPlan1 = _MscVRouteDiallingPlan1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 7),
    _MscVRouteDiallingPlan1_Type()
)
mscVRouteDiallingPlan1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteDiallingPlan1.setStatus("mandatory")


class _MscVRouteDiallingPlan2_Type(OctetString):
    """Custom type mscVRouteDiallingPlan2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVRouteDiallingPlan2_Type.__name__ = "OctetString"
_MscVRouteDiallingPlan2_Object = MibTableColumn
mscVRouteDiallingPlan2 = _MscVRouteDiallingPlan2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 8),
    _MscVRouteDiallingPlan2_Type()
)
mscVRouteDiallingPlan2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteDiallingPlan2.setStatus("mandatory")


class _MscVRouteHuntingAlgorithm_Type(Integer32):
    """Custom type mscVRouteHuntingAlgorithm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bottomUpLinear", 0),
          ("topDownLinear", 1))
    )


_MscVRouteHuntingAlgorithm_Type.__name__ = "Integer32"
_MscVRouteHuntingAlgorithm_Object = MibTableColumn
mscVRouteHuntingAlgorithm = _MscVRouteHuntingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 9),
    _MscVRouteHuntingAlgorithm_Type()
)
mscVRouteHuntingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteHuntingAlgorithm.setStatus("mandatory")


class _MscVRouteMinimumDigitsToRoute_Type(Unsigned32):
    """Custom type mscVRouteMinimumDigitsToRoute based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVRouteMinimumDigitsToRoute_Type.__name__ = "Unsigned32"
_MscVRouteMinimumDigitsToRoute_Object = MibTableColumn
mscVRouteMinimumDigitsToRoute = _MscVRouteMinimumDigitsToRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 10),
    _MscVRouteMinimumDigitsToRoute_Type()
)
mscVRouteMinimumDigitsToRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteMinimumDigitsToRoute.setStatus("mandatory")
_MscVRouteVoiceNetworkingCallServer_Type = Link
_MscVRouteVoiceNetworkingCallServer_Object = MibTableColumn
mscVRouteVoiceNetworkingCallServer = _MscVRouteVoiceNetworkingCallServer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 11),
    _MscVRouteVoiceNetworkingCallServer_Type()
)
mscVRouteVoiceNetworkingCallServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteVoiceNetworkingCallServer.setStatus("mandatory")


class _MscVRouteOverrideDirectoryNumber_Type(DigitString):
    """Custom type mscVRouteOverrideDirectoryNumber based on DigitString"""
    defaultHexValue = ""

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_MscVRouteOverrideDirectoryNumber_Type.__name__ = "DigitString"
_MscVRouteOverrideDirectoryNumber_Object = MibTableColumn
mscVRouteOverrideDirectoryNumber = _MscVRouteOverrideDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 12),
    _MscVRouteOverrideDirectoryNumber_Type()
)
mscVRouteOverrideDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteOverrideDirectoryNumber.setStatus("mandatory")


class _MscVRoutePrivateNetworkIdentifer_Type(Unsigned32):
    """Custom type mscVRoutePrivateNetworkIdentifer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32700),
    )


_MscVRoutePrivateNetworkIdentifer_Type.__name__ = "Unsigned32"
_MscVRoutePrivateNetworkIdentifer_Object = MibTableColumn
mscVRoutePrivateNetworkIdentifer = _MscVRoutePrivateNetworkIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 10, 1, 13),
    _MscVRoutePrivateNetworkIdentifer_Type()
)
mscVRoutePrivateNetworkIdentifer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRoutePrivateNetworkIdentifer.setStatus("mandatory")
_MscVRouteCidDataTable_Object = MibTable
mscVRouteCidDataTable = _MscVRouteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 11)
)
if mibBuilder.loadTexts:
    mscVRouteCidDataTable.setStatus("mandatory")
_MscVRouteCidDataEntry_Object = MibTableRow
mscVRouteCidDataEntry = _MscVRouteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 11, 1)
)
mscVRouteCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteCidDataEntry.setStatus("mandatory")


class _MscVRouteCustomerIdentifier_Type(Unsigned32):
    """Custom type mscVRouteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscVRouteCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscVRouteCustomerIdentifier_Object = MibTableColumn
mscVRouteCustomerIdentifier = _MscVRouteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 11, 1, 1),
    _MscVRouteCustomerIdentifier_Type()
)
mscVRouteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteCustomerIdentifier.setStatus("mandatory")
_MscVRouteIfEntryTable_Object = MibTable
mscVRouteIfEntryTable = _MscVRouteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 12)
)
if mibBuilder.loadTexts:
    mscVRouteIfEntryTable.setStatus("mandatory")
_MscVRouteIfEntryEntry_Object = MibTableRow
mscVRouteIfEntryEntry = _MscVRouteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 12, 1)
)
mscVRouteIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteIfEntryEntry.setStatus("mandatory")


class _MscVRouteIfAdminStatus_Type(Integer32):
    """Custom type mscVRouteIfAdminStatus based on Integer32"""
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


_MscVRouteIfAdminStatus_Type.__name__ = "Integer32"
_MscVRouteIfAdminStatus_Object = MibTableColumn
mscVRouteIfAdminStatus = _MscVRouteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 12, 1, 1),
    _MscVRouteIfAdminStatus_Type()
)
mscVRouteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteIfAdminStatus.setStatus("mandatory")


class _MscVRouteIfIndex_Type(InterfaceIndex):
    """Custom type mscVRouteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVRouteIfIndex_Type.__name__ = "InterfaceIndex"
_MscVRouteIfIndex_Object = MibTableColumn
mscVRouteIfIndex = _MscVRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 12, 1, 2),
    _MscVRouteIfIndex_Type()
)
mscVRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteIfIndex.setStatus("mandatory")
_MscVRouteStateTable_Object = MibTable
mscVRouteStateTable = _MscVRouteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 13)
)
if mibBuilder.loadTexts:
    mscVRouteStateTable.setStatus("mandatory")
_MscVRouteStateEntry_Object = MibTableRow
mscVRouteStateEntry = _MscVRouteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 13, 1)
)
mscVRouteStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteStateEntry.setStatus("mandatory")


class _MscVRouteAdminState_Type(Integer32):
    """Custom type mscVRouteAdminState based on Integer32"""
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


_MscVRouteAdminState_Type.__name__ = "Integer32"
_MscVRouteAdminState_Object = MibTableColumn
mscVRouteAdminState = _MscVRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 13, 1, 1),
    _MscVRouteAdminState_Type()
)
mscVRouteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteAdminState.setStatus("mandatory")


class _MscVRouteOperationalState_Type(Integer32):
    """Custom type mscVRouteOperationalState based on Integer32"""
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


_MscVRouteOperationalState_Type.__name__ = "Integer32"
_MscVRouteOperationalState_Object = MibTableColumn
mscVRouteOperationalState = _MscVRouteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 13, 1, 2),
    _MscVRouteOperationalState_Type()
)
mscVRouteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteOperationalState.setStatus("mandatory")


class _MscVRouteUsageState_Type(Integer32):
    """Custom type mscVRouteUsageState based on Integer32"""
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


_MscVRouteUsageState_Type.__name__ = "Integer32"
_MscVRouteUsageState_Object = MibTableColumn
mscVRouteUsageState = _MscVRouteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 13, 1, 3),
    _MscVRouteUsageState_Type()
)
mscVRouteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteUsageState.setStatus("mandatory")
_MscVRouteOperStatusTable_Object = MibTable
mscVRouteOperStatusTable = _MscVRouteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 14)
)
if mibBuilder.loadTexts:
    mscVRouteOperStatusTable.setStatus("mandatory")
_MscVRouteOperStatusEntry_Object = MibTableRow
mscVRouteOperStatusEntry = _MscVRouteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 14, 1)
)
mscVRouteOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteOperStatusEntry.setStatus("mandatory")


class _MscVRouteSnmpOperStatus_Type(Integer32):
    """Custom type mscVRouteSnmpOperStatus based on Integer32"""
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


_MscVRouteSnmpOperStatus_Type.__name__ = "Integer32"
_MscVRouteSnmpOperStatus_Object = MibTableColumn
mscVRouteSnmpOperStatus = _MscVRouteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 14, 1, 1),
    _MscVRouteSnmpOperStatus_Type()
)
mscVRouteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteSnmpOperStatus.setStatus("mandatory")
_MscVRouteStatsTable_Object = MibTable
mscVRouteStatsTable = _MscVRouteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15)
)
if mibBuilder.loadTexts:
    mscVRouteStatsTable.setStatus("mandatory")
_MscVRouteStatsEntry_Object = MibTableRow
mscVRouteStatsEntry = _MscVRouteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15, 1)
)
mscVRouteStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
)
if mibBuilder.loadTexts:
    mscVRouteStatsEntry.setStatus("mandatory")
_MscVRouteTotalCallsFromSubnet_Type = Counter32
_MscVRouteTotalCallsFromSubnet_Object = MibTableColumn
mscVRouteTotalCallsFromSubnet = _MscVRouteTotalCallsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15, 1, 1),
    _MscVRouteTotalCallsFromSubnet_Type()
)
mscVRouteTotalCallsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteTotalCallsFromSubnet.setStatus("mandatory")
_MscVRouteCallsClearedNoChannel_Type = Counter32
_MscVRouteCallsClearedNoChannel_Object = MibTableColumn
mscVRouteCallsClearedNoChannel = _MscVRouteCallsClearedNoChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15, 1, 2),
    _MscVRouteCallsClearedNoChannel_Type()
)
mscVRouteCallsClearedNoChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteCallsClearedNoChannel.setStatus("mandatory")
_MscVRouteCallsClearedOutOfService_Type = Counter32
_MscVRouteCallsClearedOutOfService_Object = MibTableColumn
mscVRouteCallsClearedOutOfService = _MscVRouteCallsClearedOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15, 1, 3),
    _MscVRouteCallsClearedOutOfService_Type()
)
mscVRouteCallsClearedOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteCallsClearedOutOfService.setStatus("mandatory")
_MscVRouteCallsRejected_Type = Counter32
_MscVRouteCallsRejected_Object = MibTableColumn
mscVRouteCallsRejected = _MscVRouteCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 15, 1, 4),
    _MscVRouteCallsRejected_Type()
)
mscVRouteCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteCallsRejected.setStatus("mandatory")
_MscVRouteSubroutesTable_Object = MibTable
mscVRouteSubroutesTable = _MscVRouteSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 309)
)
if mibBuilder.loadTexts:
    mscVRouteSubroutesTable.setStatus("mandatory")
_MscVRouteSubroutesEntry_Object = MibTableRow
mscVRouteSubroutesEntry = _MscVRouteSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 309, 1)
)
mscVRouteSubroutesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteSubroutesValue"),
)
if mibBuilder.loadTexts:
    mscVRouteSubroutesEntry.setStatus("mandatory")
_MscVRouteSubroutesValue_Type = Link
_MscVRouteSubroutesValue_Object = MibTableColumn
mscVRouteSubroutesValue = _MscVRouteSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 309, 1, 1),
    _MscVRouteSubroutesValue_Type()
)
mscVRouteSubroutesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVRouteSubroutesValue.setStatus("mandatory")
_MscVRouteSubroutesRowStatus_Type = RowStatus
_MscVRouteSubroutesRowStatus_Object = MibTableColumn
mscVRouteSubroutesRowStatus = _MscVRouteSubroutesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 309, 1, 2),
    _MscVRouteSubroutesRowStatus_Type()
)
mscVRouteSubroutesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVRouteSubroutesRowStatus.setStatus("mandatory")
_MscVRouteDegradedSubroutesTable_Object = MibTable
mscVRouteDegradedSubroutesTable = _MscVRouteDegradedSubroutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 310)
)
if mibBuilder.loadTexts:
    mscVRouteDegradedSubroutesTable.setStatus("mandatory")
_MscVRouteDegradedSubroutesEntry_Object = MibTableRow
mscVRouteDegradedSubroutesEntry = _MscVRouteDegradedSubroutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 310, 1)
)
mscVRouteDegradedSubroutesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVRouteDegradedSubroutesValue"),
)
if mibBuilder.loadTexts:
    mscVRouteDegradedSubroutesEntry.setStatus("mandatory")
_MscVRouteDegradedSubroutesValue_Type = RowPointer
_MscVRouteDegradedSubroutesValue_Object = MibTableColumn
mscVRouteDegradedSubroutesValue = _MscVRouteDegradedSubroutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 116, 310, 1, 1),
    _MscVRouteDegradedSubroutesValue_Type()
)
mscVRouteDegradedSubroutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVRouteDegradedSubroutesValue.setStatus("mandatory")
_MscVsr_ObjectIdentity = ObjectIdentity
mscVsr = _MscVsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117)
)
_MscVsrRowStatusTable_Object = MibTable
mscVsrRowStatusTable = _MscVsrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1)
)
if mibBuilder.loadTexts:
    mscVsrRowStatusTable.setStatus("mandatory")
_MscVsrRowStatusEntry_Object = MibTableRow
mscVsrRowStatusEntry = _MscVsrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1, 1)
)
mscVsrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrRowStatusEntry.setStatus("mandatory")
_MscVsrRowStatus_Type = RowStatus
_MscVsrRowStatus_Object = MibTableColumn
mscVsrRowStatus = _MscVsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1, 1, 1),
    _MscVsrRowStatus_Type()
)
mscVsrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrRowStatus.setStatus("mandatory")
_MscVsrComponentName_Type = DisplayString
_MscVsrComponentName_Object = MibTableColumn
mscVsrComponentName = _MscVsrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1, 1, 2),
    _MscVsrComponentName_Type()
)
mscVsrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrComponentName.setStatus("mandatory")
_MscVsrStorageType_Type = StorageType
_MscVsrStorageType_Object = MibTableColumn
mscVsrStorageType = _MscVsrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1, 1, 4),
    _MscVsrStorageType_Type()
)
mscVsrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrStorageType.setStatus("mandatory")


class _MscVsrIndex_Type(Integer32):
    """Custom type mscVsrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVsrIndex_Type.__name__ = "Integer32"
_MscVsrIndex_Object = MibTableColumn
mscVsrIndex = _MscVsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 1, 1, 10),
    _MscVsrIndex_Type()
)
mscVsrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrIndex.setStatus("mandatory")
_MscVsrSvs_ObjectIdentity = ObjectIdentity
mscVsrSvs = _MscVsrSvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2)
)
_MscVsrSvsRowStatusTable_Object = MibTable
mscVsrSvsRowStatusTable = _MscVsrSvsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsRowStatusTable.setStatus("mandatory")
_MscVsrSvsRowStatusEntry_Object = MibTableRow
mscVsrSvsRowStatusEntry = _MscVsrSvsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1, 1)
)
mscVsrSvsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsRowStatusEntry.setStatus("mandatory")
_MscVsrSvsRowStatus_Type = RowStatus
_MscVsrSvsRowStatus_Object = MibTableColumn
mscVsrSvsRowStatus = _MscVsrSvsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1, 1, 1),
    _MscVsrSvsRowStatus_Type()
)
mscVsrSvsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsRowStatus.setStatus("mandatory")
_MscVsrSvsComponentName_Type = DisplayString
_MscVsrSvsComponentName_Object = MibTableColumn
mscVsrSvsComponentName = _MscVsrSvsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1, 1, 2),
    _MscVsrSvsComponentName_Type()
)
mscVsrSvsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsComponentName.setStatus("mandatory")
_MscVsrSvsStorageType_Type = StorageType
_MscVsrSvsStorageType_Object = MibTableColumn
mscVsrSvsStorageType = _MscVsrSvsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1, 1, 4),
    _MscVsrSvsStorageType_Type()
)
mscVsrSvsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsStorageType.setStatus("mandatory")


class _MscVsrSvsIndex_Type(Integer32):
    """Custom type mscVsrSvsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MscVsrSvsIndex_Type.__name__ = "Integer32"
_MscVsrSvsIndex_Object = MibTableColumn
mscVsrSvsIndex = _MscVsrSvsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 1, 1, 10),
    _MscVsrSvsIndex_Type()
)
mscVsrSvsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsIndex.setStatus("mandatory")
_MscVsrSvsFramer_ObjectIdentity = ObjectIdentity
mscVsrSvsFramer = _MscVsrSvsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2)
)
_MscVsrSvsFramerRowStatusTable_Object = MibTable
mscVsrSvsFramerRowStatusTable = _MscVsrSvsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerRowStatusTable.setStatus("mandatory")
_MscVsrSvsFramerRowStatusEntry_Object = MibTableRow
mscVsrSvsFramerRowStatusEntry = _MscVsrSvsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1, 1)
)
mscVsrSvsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerRowStatusEntry.setStatus("mandatory")
_MscVsrSvsFramerRowStatus_Type = RowStatus
_MscVsrSvsFramerRowStatus_Object = MibTableColumn
mscVsrSvsFramerRowStatus = _MscVsrSvsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1, 1, 1),
    _MscVsrSvsFramerRowStatus_Type()
)
mscVsrSvsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerRowStatus.setStatus("mandatory")
_MscVsrSvsFramerComponentName_Type = DisplayString
_MscVsrSvsFramerComponentName_Object = MibTableColumn
mscVsrSvsFramerComponentName = _MscVsrSvsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1, 1, 2),
    _MscVsrSvsFramerComponentName_Type()
)
mscVsrSvsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerComponentName.setStatus("mandatory")
_MscVsrSvsFramerStorageType_Type = StorageType
_MscVsrSvsFramerStorageType_Object = MibTableColumn
mscVsrSvsFramerStorageType = _MscVsrSvsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1, 1, 4),
    _MscVsrSvsFramerStorageType_Type()
)
mscVsrSvsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerStorageType.setStatus("mandatory")
_MscVsrSvsFramerIndex_Type = NonReplicated
_MscVsrSvsFramerIndex_Object = MibTableColumn
mscVsrSvsFramerIndex = _MscVsrSvsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 1, 1, 10),
    _MscVsrSvsFramerIndex_Type()
)
mscVsrSvsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerIndex.setStatus("mandatory")
_MscVsrSvsFramerVfpDebug_ObjectIdentity = ObjectIdentity
mscVsrSvsFramerVfpDebug = _MscVsrSvsFramerVfpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5)
)
_MscVsrSvsFramerVfpDebugRowStatusTable_Object = MibTable
mscVsrSvsFramerVfpDebugRowStatusTable = _MscVsrSvsFramerVfpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugRowStatusTable.setStatus("mandatory")
_MscVsrSvsFramerVfpDebugRowStatusEntry_Object = MibTableRow
mscVsrSvsFramerVfpDebugRowStatusEntry = _MscVsrSvsFramerVfpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1, 1)
)
mscVsrSvsFramerVfpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerVfpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugRowStatusEntry.setStatus("mandatory")
_MscVsrSvsFramerVfpDebugRowStatus_Type = RowStatus
_MscVsrSvsFramerVfpDebugRowStatus_Object = MibTableColumn
mscVsrSvsFramerVfpDebugRowStatus = _MscVsrSvsFramerVfpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1, 1, 1),
    _MscVsrSvsFramerVfpDebugRowStatus_Type()
)
mscVsrSvsFramerVfpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugRowStatus.setStatus("mandatory")
_MscVsrSvsFramerVfpDebugComponentName_Type = DisplayString
_MscVsrSvsFramerVfpDebugComponentName_Object = MibTableColumn
mscVsrSvsFramerVfpDebugComponentName = _MscVsrSvsFramerVfpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1, 1, 2),
    _MscVsrSvsFramerVfpDebugComponentName_Type()
)
mscVsrSvsFramerVfpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugComponentName.setStatus("mandatory")
_MscVsrSvsFramerVfpDebugStorageType_Type = StorageType
_MscVsrSvsFramerVfpDebugStorageType_Object = MibTableColumn
mscVsrSvsFramerVfpDebugStorageType = _MscVsrSvsFramerVfpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1, 1, 4),
    _MscVsrSvsFramerVfpDebugStorageType_Type()
)
mscVsrSvsFramerVfpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugStorageType.setStatus("mandatory")
_MscVsrSvsFramerVfpDebugIndex_Type = NonReplicated
_MscVsrSvsFramerVfpDebugIndex_Object = MibTableColumn
mscVsrSvsFramerVfpDebugIndex = _MscVsrSvsFramerVfpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 5, 1, 1, 10),
    _MscVsrSvsFramerVfpDebugIndex_Type()
)
mscVsrSvsFramerVfpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerVfpDebugIndex.setStatus("mandatory")
_MscVsrSvsFramerMvpDebug_ObjectIdentity = ObjectIdentity
mscVsrSvsFramerMvpDebug = _MscVsrSvsFramerMvpDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6)
)
_MscVsrSvsFramerMvpDebugRowStatusTable_Object = MibTable
mscVsrSvsFramerMvpDebugRowStatusTable = _MscVsrSvsFramerMvpDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugRowStatusTable.setStatus("mandatory")
_MscVsrSvsFramerMvpDebugRowStatusEntry_Object = MibTableRow
mscVsrSvsFramerMvpDebugRowStatusEntry = _MscVsrSvsFramerMvpDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1, 1)
)
mscVsrSvsFramerMvpDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerMvpDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugRowStatusEntry.setStatus("mandatory")
_MscVsrSvsFramerMvpDebugRowStatus_Type = RowStatus
_MscVsrSvsFramerMvpDebugRowStatus_Object = MibTableColumn
mscVsrSvsFramerMvpDebugRowStatus = _MscVsrSvsFramerMvpDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1, 1, 1),
    _MscVsrSvsFramerMvpDebugRowStatus_Type()
)
mscVsrSvsFramerMvpDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugRowStatus.setStatus("mandatory")
_MscVsrSvsFramerMvpDebugComponentName_Type = DisplayString
_MscVsrSvsFramerMvpDebugComponentName_Object = MibTableColumn
mscVsrSvsFramerMvpDebugComponentName = _MscVsrSvsFramerMvpDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1, 1, 2),
    _MscVsrSvsFramerMvpDebugComponentName_Type()
)
mscVsrSvsFramerMvpDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugComponentName.setStatus("mandatory")
_MscVsrSvsFramerMvpDebugStorageType_Type = StorageType
_MscVsrSvsFramerMvpDebugStorageType_Object = MibTableColumn
mscVsrSvsFramerMvpDebugStorageType = _MscVsrSvsFramerMvpDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1, 1, 4),
    _MscVsrSvsFramerMvpDebugStorageType_Type()
)
mscVsrSvsFramerMvpDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugStorageType.setStatus("mandatory")
_MscVsrSvsFramerMvpDebugIndex_Type = NonReplicated
_MscVsrSvsFramerMvpDebugIndex_Object = MibTableColumn
mscVsrSvsFramerMvpDebugIndex = _MscVsrSvsFramerMvpDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 6, 1, 1, 10),
    _MscVsrSvsFramerMvpDebugIndex_Type()
)
mscVsrSvsFramerMvpDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerMvpDebugIndex.setStatus("mandatory")
_MscVsrSvsFramerPcmCapture_ObjectIdentity = ObjectIdentity
mscVsrSvsFramerPcmCapture = _MscVsrSvsFramerPcmCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7)
)
_MscVsrSvsFramerPcmCaptureRowStatusTable_Object = MibTable
mscVsrSvsFramerPcmCaptureRowStatusTable = _MscVsrSvsFramerPcmCaptureRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureRowStatusTable.setStatus("mandatory")
_MscVsrSvsFramerPcmCaptureRowStatusEntry_Object = MibTableRow
mscVsrSvsFramerPcmCaptureRowStatusEntry = _MscVsrSvsFramerPcmCaptureRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1, 1)
)
mscVsrSvsFramerPcmCaptureRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerPcmCaptureIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureRowStatusEntry.setStatus("mandatory")
_MscVsrSvsFramerPcmCaptureRowStatus_Type = RowStatus
_MscVsrSvsFramerPcmCaptureRowStatus_Object = MibTableColumn
mscVsrSvsFramerPcmCaptureRowStatus = _MscVsrSvsFramerPcmCaptureRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1, 1, 1),
    _MscVsrSvsFramerPcmCaptureRowStatus_Type()
)
mscVsrSvsFramerPcmCaptureRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureRowStatus.setStatus("mandatory")
_MscVsrSvsFramerPcmCaptureComponentName_Type = DisplayString
_MscVsrSvsFramerPcmCaptureComponentName_Object = MibTableColumn
mscVsrSvsFramerPcmCaptureComponentName = _MscVsrSvsFramerPcmCaptureComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1, 1, 2),
    _MscVsrSvsFramerPcmCaptureComponentName_Type()
)
mscVsrSvsFramerPcmCaptureComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureComponentName.setStatus("mandatory")
_MscVsrSvsFramerPcmCaptureStorageType_Type = StorageType
_MscVsrSvsFramerPcmCaptureStorageType_Object = MibTableColumn
mscVsrSvsFramerPcmCaptureStorageType = _MscVsrSvsFramerPcmCaptureStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1, 1, 4),
    _MscVsrSvsFramerPcmCaptureStorageType_Type()
)
mscVsrSvsFramerPcmCaptureStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureStorageType.setStatus("mandatory")
_MscVsrSvsFramerPcmCaptureIndex_Type = NonReplicated
_MscVsrSvsFramerPcmCaptureIndex_Object = MibTableColumn
mscVsrSvsFramerPcmCaptureIndex = _MscVsrSvsFramerPcmCaptureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 7, 1, 1, 10),
    _MscVsrSvsFramerPcmCaptureIndex_Type()
)
mscVsrSvsFramerPcmCaptureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerPcmCaptureIndex.setStatus("mandatory")
_MscVsrSvsFramerProvTable_Object = MibTable
mscVsrSvsFramerProvTable = _MscVsrSvsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerProvTable.setStatus("mandatory")
_MscVsrSvsFramerProvEntry_Object = MibTableRow
mscVsrSvsFramerProvEntry = _MscVsrSvsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 10, 1)
)
mscVsrSvsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerProvEntry.setStatus("mandatory")
_MscVsrSvsFramerInterfaceName_Type = Link
_MscVsrSvsFramerInterfaceName_Object = MibTableColumn
mscVsrSvsFramerInterfaceName = _MscVsrSvsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 10, 1, 1),
    _MscVsrSvsFramerInterfaceName_Type()
)
mscVsrSvsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerInterfaceName.setStatus("mandatory")
_MscVsrSvsFramerStateTable_Object = MibTable
mscVsrSvsFramerStateTable = _MscVsrSvsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 14)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerStateTable.setStatus("mandatory")
_MscVsrSvsFramerStateEntry_Object = MibTableRow
mscVsrSvsFramerStateEntry = _MscVsrSvsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 14, 1)
)
mscVsrSvsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerStateEntry.setStatus("mandatory")


class _MscVsrSvsFramerAdminState_Type(Integer32):
    """Custom type mscVsrSvsFramerAdminState based on Integer32"""
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


_MscVsrSvsFramerAdminState_Type.__name__ = "Integer32"
_MscVsrSvsFramerAdminState_Object = MibTableColumn
mscVsrSvsFramerAdminState = _MscVsrSvsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 14, 1, 1),
    _MscVsrSvsFramerAdminState_Type()
)
mscVsrSvsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerAdminState.setStatus("mandatory")


class _MscVsrSvsFramerOperationalState_Type(Integer32):
    """Custom type mscVsrSvsFramerOperationalState based on Integer32"""
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


_MscVsrSvsFramerOperationalState_Type.__name__ = "Integer32"
_MscVsrSvsFramerOperationalState_Object = MibTableColumn
mscVsrSvsFramerOperationalState = _MscVsrSvsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 14, 1, 2),
    _MscVsrSvsFramerOperationalState_Type()
)
mscVsrSvsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerOperationalState.setStatus("mandatory")


class _MscVsrSvsFramerUsageState_Type(Integer32):
    """Custom type mscVsrSvsFramerUsageState based on Integer32"""
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


_MscVsrSvsFramerUsageState_Type.__name__ = "Integer32"
_MscVsrSvsFramerUsageState_Object = MibTableColumn
mscVsrSvsFramerUsageState = _MscVsrSvsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 14, 1, 3),
    _MscVsrSvsFramerUsageState_Type()
)
mscVsrSvsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerUsageState.setStatus("mandatory")
_MscVsrSvsFramerStatsTable_Object = MibTable
mscVsrSvsFramerStatsTable = _MscVsrSvsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerStatsTable.setStatus("mandatory")
_MscVsrSvsFramerStatsEntry_Object = MibTableRow
mscVsrSvsFramerStatsEntry = _MscVsrSvsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1)
)
mscVsrSvsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerStatsEntry.setStatus("mandatory")


class _MscVsrSvsFramerTotalCells_Type(Unsigned32):
    """Custom type mscVsrSvsFramerTotalCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerTotalCells_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerTotalCells_Object = MibTableColumn
mscVsrSvsFramerTotalCells = _MscVsrSvsFramerTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 1),
    _MscVsrSvsFramerTotalCells_Type()
)
mscVsrSvsFramerTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerTotalCells.setStatus("mandatory")


class _MscVsrSvsFramerAudioCells_Type(Unsigned32):
    """Custom type mscVsrSvsFramerAudioCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerAudioCells_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerAudioCells_Object = MibTableColumn
mscVsrSvsFramerAudioCells = _MscVsrSvsFramerAudioCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 2),
    _MscVsrSvsFramerAudioCells_Type()
)
mscVsrSvsFramerAudioCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerAudioCells.setStatus("mandatory")


class _MscVsrSvsFramerSilenceCells_Type(Unsigned32):
    """Custom type mscVsrSvsFramerSilenceCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerSilenceCells_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerSilenceCells_Object = MibTableColumn
mscVsrSvsFramerSilenceCells = _MscVsrSvsFramerSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 4),
    _MscVsrSvsFramerSilenceCells_Type()
)
mscVsrSvsFramerSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerSilenceCells.setStatus("mandatory")


class _MscVsrSvsFramerModemCells_Type(Unsigned32):
    """Custom type mscVsrSvsFramerModemCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerModemCells_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerModemCells_Object = MibTableColumn
mscVsrSvsFramerModemCells = _MscVsrSvsFramerModemCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 5),
    _MscVsrSvsFramerModemCells_Type()
)
mscVsrSvsFramerModemCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerModemCells.setStatus("obsolete")


class _MscVsrSvsFramerCurrentEncodingRate_Type(Integer32):
    """Custom type mscVsrSvsFramerCurrentEncodingRate based on Integer32"""
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


_MscVsrSvsFramerCurrentEncodingRate_Type.__name__ = "Integer32"
_MscVsrSvsFramerCurrentEncodingRate_Object = MibTableColumn
mscVsrSvsFramerCurrentEncodingRate = _MscVsrSvsFramerCurrentEncodingRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 6),
    _MscVsrSvsFramerCurrentEncodingRate_Type()
)
mscVsrSvsFramerCurrentEncodingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerCurrentEncodingRate.setStatus("obsolete")


class _MscVsrSvsFramerLrcErrors_Type(Unsigned32):
    """Custom type mscVsrSvsFramerLrcErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerLrcErrors_Object = MibTableColumn
mscVsrSvsFramerLrcErrors = _MscVsrSvsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 7),
    _MscVsrSvsFramerLrcErrors_Type()
)
mscVsrSvsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerLrcErrors.setStatus("mandatory")


class _MscVsrSvsFramerFrmLostInNetwork_Type(Unsigned32):
    """Custom type mscVsrSvsFramerFrmLostInNetwork based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerFrmLostInNetwork_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerFrmLostInNetwork_Object = MibTableColumn
mscVsrSvsFramerFrmLostInNetwork = _MscVsrSvsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 8),
    _MscVsrSvsFramerFrmLostInNetwork_Type()
)
mscVsrSvsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmLostInNetwork.setStatus("mandatory")


class _MscVsrSvsFramerFrmUnderRuns_Type(Unsigned32):
    """Custom type mscVsrSvsFramerFrmUnderRuns based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerFrmUnderRuns_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerFrmUnderRuns_Object = MibTableColumn
mscVsrSvsFramerFrmUnderRuns = _MscVsrSvsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 9),
    _MscVsrSvsFramerFrmUnderRuns_Type()
)
mscVsrSvsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmUnderRuns.setStatus("mandatory")


class _MscVsrSvsFramerFrmDumped_Type(Unsigned32):
    """Custom type mscVsrSvsFramerFrmDumped based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerFrmDumped_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerFrmDumped_Object = MibTableColumn
mscVsrSvsFramerFrmDumped = _MscVsrSvsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 10),
    _MscVsrSvsFramerFrmDumped_Type()
)
mscVsrSvsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmDumped.setStatus("mandatory")
_MscVsrSvsFramerModemSilenceCells_Type = Counter32
_MscVsrSvsFramerModemSilenceCells_Object = MibTableColumn
mscVsrSvsFramerModemSilenceCells = _MscVsrSvsFramerModemSilenceCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 26),
    _MscVsrSvsFramerModemSilenceCells_Type()
)
mscVsrSvsFramerModemSilenceCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerModemSilenceCells.setStatus("obsolete")


class _MscVsrSvsFramerCurrentEncoding_Type(Integer32):
    """Custom type mscVsrSvsFramerCurrentEncoding based on Integer32"""
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


_MscVsrSvsFramerCurrentEncoding_Type.__name__ = "Integer32"
_MscVsrSvsFramerCurrentEncoding_Object = MibTableColumn
mscVsrSvsFramerCurrentEncoding = _MscVsrSvsFramerCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 27),
    _MscVsrSvsFramerCurrentEncoding_Type()
)
mscVsrSvsFramerCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerCurrentEncoding.setStatus("obsolete")


class _MscVsrSvsFramerTptStatus_Type(Integer32):
    """Custom type mscVsrSvsFramerTptStatus based on Integer32"""
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


_MscVsrSvsFramerTptStatus_Type.__name__ = "Integer32"
_MscVsrSvsFramerTptStatus_Object = MibTableColumn
mscVsrSvsFramerTptStatus = _MscVsrSvsFramerTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 28),
    _MscVsrSvsFramerTptStatus_Type()
)
mscVsrSvsFramerTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerTptStatus.setStatus("obsolete")
_MscVsrSvsFramerFaxRelayCells_Type = Counter32
_MscVsrSvsFramerFaxRelayCells_Object = MibTableColumn
mscVsrSvsFramerFaxRelayCells = _MscVsrSvsFramerFaxRelayCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 35),
    _MscVsrSvsFramerFaxRelayCells_Type()
)
mscVsrSvsFramerFaxRelayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFaxRelayCells.setStatus("mandatory")


class _MscVsrSvsFramerModemFaxCells_Type(Unsigned32):
    """Custom type mscVsrSvsFramerModemFaxCells based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerModemFaxCells_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerModemFaxCells_Object = MibTableColumn
mscVsrSvsFramerModemFaxCells = _MscVsrSvsFramerModemFaxCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 36),
    _MscVsrSvsFramerModemFaxCells_Type()
)
mscVsrSvsFramerModemFaxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerModemFaxCells.setStatus("mandatory")
_MscVsrSvsFramerFaxIdleCells_Type = Counter32
_MscVsrSvsFramerFaxIdleCells_Object = MibTableColumn
mscVsrSvsFramerFaxIdleCells = _MscVsrSvsFramerFaxIdleCells_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 15, 1, 37),
    _MscVsrSvsFramerFaxIdleCells_Type()
)
mscVsrSvsFramerFaxIdleCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFaxIdleCells.setStatus("mandatory")
_MscVsrSvsFramerOperTable_Object = MibTable
mscVsrSvsFramerOperTable = _MscVsrSvsFramerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 16)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerOperTable.setStatus("mandatory")
_MscVsrSvsFramerOperEntry_Object = MibTableRow
mscVsrSvsFramerOperEntry = _MscVsrSvsFramerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 16, 1)
)
mscVsrSvsFramerOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerOperEntry.setStatus("mandatory")


class _MscVsrSvsFramerOpCurrentEncoding_Type(Integer32):
    """Custom type mscVsrSvsFramerOpCurrentEncoding based on Integer32"""
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


_MscVsrSvsFramerOpCurrentEncoding_Type.__name__ = "Integer32"
_MscVsrSvsFramerOpCurrentEncoding_Object = MibTableColumn
mscVsrSvsFramerOpCurrentEncoding = _MscVsrSvsFramerOpCurrentEncoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 16, 1, 1),
    _MscVsrSvsFramerOpCurrentEncoding_Type()
)
mscVsrSvsFramerOpCurrentEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerOpCurrentEncoding.setStatus("mandatory")


class _MscVsrSvsFramerCurrentRate_Type(Integer32):
    """Custom type mscVsrSvsFramerCurrentRate based on Integer32"""
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


_MscVsrSvsFramerCurrentRate_Type.__name__ = "Integer32"
_MscVsrSvsFramerCurrentRate_Object = MibTableColumn
mscVsrSvsFramerCurrentRate = _MscVsrSvsFramerCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 16, 1, 2),
    _MscVsrSvsFramerCurrentRate_Type()
)
mscVsrSvsFramerCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerCurrentRate.setStatus("mandatory")


class _MscVsrSvsFramerOpTptStatus_Type(Integer32):
    """Custom type mscVsrSvsFramerOpTptStatus based on Integer32"""
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


_MscVsrSvsFramerOpTptStatus_Type.__name__ = "Integer32"
_MscVsrSvsFramerOpTptStatus_Object = MibTableColumn
mscVsrSvsFramerOpTptStatus = _MscVsrSvsFramerOpTptStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 16, 1, 3),
    _MscVsrSvsFramerOpTptStatus_Type()
)
mscVsrSvsFramerOpTptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerOpTptStatus.setStatus("mandatory")
_MscVsrSvsFramerNegTable_Object = MibTable
mscVsrSvsFramerNegTable = _MscVsrSvsFramerNegTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegTable.setStatus("mandatory")
_MscVsrSvsFramerNegEntry_Object = MibTableRow
mscVsrSvsFramerNegEntry = _MscVsrSvsFramerNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1)
)
mscVsrSvsFramerNegEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegEntry.setStatus("mandatory")


class _MscVsrSvsFramerNegotiatedSilenceSuppression_Type(Integer32):
    """Custom type mscVsrSvsFramerNegotiatedSilenceSuppression based on Integer32"""
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
        *(("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_MscVsrSvsFramerNegotiatedSilenceSuppression_Type.__name__ = "Integer32"
_MscVsrSvsFramerNegotiatedSilenceSuppression_Object = MibTableColumn
mscVsrSvsFramerNegotiatedSilenceSuppression = _MscVsrSvsFramerNegotiatedSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1, 1),
    _MscVsrSvsFramerNegotiatedSilenceSuppression_Type()
)
mscVsrSvsFramerNegotiatedSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegotiatedSilenceSuppression.setStatus("mandatory")


class _MscVsrSvsFramerNegotiatedFisG711G726_Type(Integer32):
    """Custom type mscVsrSvsFramerNegotiatedFisG711G726 based on Integer32"""
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


_MscVsrSvsFramerNegotiatedFisG711G726_Type.__name__ = "Integer32"
_MscVsrSvsFramerNegotiatedFisG711G726_Object = MibTableColumn
mscVsrSvsFramerNegotiatedFisG711G726 = _MscVsrSvsFramerNegotiatedFisG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1, 2),
    _MscVsrSvsFramerNegotiatedFisG711G726_Type()
)
mscVsrSvsFramerNegotiatedFisG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegotiatedFisG711G726.setStatus("mandatory")


class _MscVsrSvsFramerNegotiatedDtmfRegeneration_Type(Integer32):
    """Custom type mscVsrSvsFramerNegotiatedDtmfRegeneration based on Integer32"""
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


_MscVsrSvsFramerNegotiatedDtmfRegeneration_Type.__name__ = "Integer32"
_MscVsrSvsFramerNegotiatedDtmfRegeneration_Object = MibTableColumn
mscVsrSvsFramerNegotiatedDtmfRegeneration = _MscVsrSvsFramerNegotiatedDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1, 3),
    _MscVsrSvsFramerNegotiatedDtmfRegeneration_Type()
)
mscVsrSvsFramerNegotiatedDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegotiatedDtmfRegeneration.setStatus("mandatory")


class _MscVsrSvsFramerNegotiatedV17AsG711G726_Type(Integer32):
    """Custom type mscVsrSvsFramerNegotiatedV17AsG711G726 based on Integer32"""
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


_MscVsrSvsFramerNegotiatedV17AsG711G726_Type.__name__ = "Integer32"
_MscVsrSvsFramerNegotiatedV17AsG711G726_Object = MibTableColumn
mscVsrSvsFramerNegotiatedV17AsG711G726 = _MscVsrSvsFramerNegotiatedV17AsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1, 4),
    _MscVsrSvsFramerNegotiatedV17AsG711G726_Type()
)
mscVsrSvsFramerNegotiatedV17AsG711G726.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegotiatedV17AsG711G726.setStatus("mandatory")


class _MscVsrSvsFramerNegotiatedTandemPassThrough_Type(Integer32):
    """Custom type mscVsrSvsFramerNegotiatedTandemPassThrough based on Integer32"""
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


_MscVsrSvsFramerNegotiatedTandemPassThrough_Type.__name__ = "Integer32"
_MscVsrSvsFramerNegotiatedTandemPassThrough_Object = MibTableColumn
mscVsrSvsFramerNegotiatedTandemPassThrough = _MscVsrSvsFramerNegotiatedTandemPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 17, 1, 5),
    _MscVsrSvsFramerNegotiatedTandemPassThrough_Type()
)
mscVsrSvsFramerNegotiatedTandemPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNegotiatedTandemPassThrough.setStatus("mandatory")
_MscVsrSvsFramerFrmToNetworkTable_Object = MibTable
mscVsrSvsFramerFrmToNetworkTable = _MscVsrSvsFramerFrmToNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 315)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmToNetworkTable.setStatus("mandatory")
_MscVsrSvsFramerFrmToNetworkEntry_Object = MibTableRow
mscVsrSvsFramerFrmToNetworkEntry = _MscVsrSvsFramerFrmToNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 315, 1)
)
mscVsrSvsFramerFrmToNetworkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerFrmToNetworkIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmToNetworkEntry.setStatus("mandatory")


class _MscVsrSvsFramerFrmToNetworkIndex_Type(Integer32):
    """Custom type mscVsrSvsFramerFrmToNetworkIndex based on Integer32"""
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


_MscVsrSvsFramerFrmToNetworkIndex_Type.__name__ = "Integer32"
_MscVsrSvsFramerFrmToNetworkIndex_Object = MibTableColumn
mscVsrSvsFramerFrmToNetworkIndex = _MscVsrSvsFramerFrmToNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 315, 1, 1),
    _MscVsrSvsFramerFrmToNetworkIndex_Type()
)
mscVsrSvsFramerFrmToNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmToNetworkIndex.setStatus("mandatory")


class _MscVsrSvsFramerFrmToNetworkValue_Type(Unsigned32):
    """Custom type mscVsrSvsFramerFrmToNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerFrmToNetworkValue_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerFrmToNetworkValue_Object = MibTableColumn
mscVsrSvsFramerFrmToNetworkValue = _MscVsrSvsFramerFrmToNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 315, 1, 2),
    _MscVsrSvsFramerFrmToNetworkValue_Type()
)
mscVsrSvsFramerFrmToNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmToNetworkValue.setStatus("mandatory")
_MscVsrSvsFramerFrmFromNetworkTable_Object = MibTable
mscVsrSvsFramerFrmFromNetworkTable = _MscVsrSvsFramerFrmFromNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 316)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmFromNetworkTable.setStatus("mandatory")
_MscVsrSvsFramerFrmFromNetworkEntry_Object = MibTableRow
mscVsrSvsFramerFrmFromNetworkEntry = _MscVsrSvsFramerFrmFromNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 316, 1)
)
mscVsrSvsFramerFrmFromNetworkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerFrmFromNetworkIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmFromNetworkEntry.setStatus("mandatory")


class _MscVsrSvsFramerFrmFromNetworkIndex_Type(Integer32):
    """Custom type mscVsrSvsFramerFrmFromNetworkIndex based on Integer32"""
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


_MscVsrSvsFramerFrmFromNetworkIndex_Type.__name__ = "Integer32"
_MscVsrSvsFramerFrmFromNetworkIndex_Object = MibTableColumn
mscVsrSvsFramerFrmFromNetworkIndex = _MscVsrSvsFramerFrmFromNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 316, 1, 1),
    _MscVsrSvsFramerFrmFromNetworkIndex_Type()
)
mscVsrSvsFramerFrmFromNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmFromNetworkIndex.setStatus("mandatory")


class _MscVsrSvsFramerFrmFromNetworkValue_Type(Unsigned32):
    """Custom type mscVsrSvsFramerFrmFromNetworkValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsFramerFrmFromNetworkValue_Type.__name__ = "Unsigned32"
_MscVsrSvsFramerFrmFromNetworkValue_Object = MibTableColumn
mscVsrSvsFramerFrmFromNetworkValue = _MscVsrSvsFramerFrmFromNetworkValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 316, 1, 2),
    _MscVsrSvsFramerFrmFromNetworkValue_Type()
)
mscVsrSvsFramerFrmFromNetworkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsFramerFrmFromNetworkValue.setStatus("mandatory")
_MscVsrSvsFramerNEncodingTable_Object = MibTable
mscVsrSvsFramerNEncodingTable = _MscVsrSvsFramerNEncodingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 467)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNEncodingTable.setStatus("mandatory")
_MscVsrSvsFramerNEncodingEntry_Object = MibTableRow
mscVsrSvsFramerNEncodingEntry = _MscVsrSvsFramerNEncodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 467, 1)
)
mscVsrSvsFramerNEncodingEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerNEncodingIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNEncodingEntry.setStatus("mandatory")


class _MscVsrSvsFramerNEncodingIndex_Type(Integer32):
    """Custom type mscVsrSvsFramerNEncodingIndex based on Integer32"""
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


_MscVsrSvsFramerNEncodingIndex_Type.__name__ = "Integer32"
_MscVsrSvsFramerNEncodingIndex_Object = MibTableColumn
mscVsrSvsFramerNEncodingIndex = _MscVsrSvsFramerNEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 467, 1, 1),
    _MscVsrSvsFramerNEncodingIndex_Type()
)
mscVsrSvsFramerNEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNEncodingIndex.setStatus("mandatory")


class _MscVsrSvsFramerNEncodingValue_Type(Integer32):
    """Custom type mscVsrSvsFramerNEncodingValue based on Integer32"""
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


_MscVsrSvsFramerNEncodingValue_Type.__name__ = "Integer32"
_MscVsrSvsFramerNEncodingValue_Object = MibTableColumn
mscVsrSvsFramerNEncodingValue = _MscVsrSvsFramerNEncodingValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 467, 1, 2),
    _MscVsrSvsFramerNEncodingValue_Type()
)
mscVsrSvsFramerNEncodingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNEncodingValue.setStatus("mandatory")
_MscVsrSvsFramerNRatesTable_Object = MibTable
mscVsrSvsFramerNRatesTable = _MscVsrSvsFramerNRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 479)
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNRatesTable.setStatus("mandatory")
_MscVsrSvsFramerNRatesEntry_Object = MibTableRow
mscVsrSvsFramerNRatesEntry = _MscVsrSvsFramerNRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 479, 1)
)
mscVsrSvsFramerNRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerNRatesTrafficIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsFramerNRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsFramerNRatesEntry.setStatus("mandatory")


class _MscVsrSvsFramerNRatesTrafficIndex_Type(Integer32):
    """Custom type mscVsrSvsFramerNRatesTrafficIndex based on Integer32"""
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


_MscVsrSvsFramerNRatesTrafficIndex_Type.__name__ = "Integer32"
_MscVsrSvsFramerNRatesTrafficIndex_Object = MibTableColumn
mscVsrSvsFramerNRatesTrafficIndex = _MscVsrSvsFramerNRatesTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 479, 1, 1),
    _MscVsrSvsFramerNRatesTrafficIndex_Type()
)
mscVsrSvsFramerNRatesTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNRatesTrafficIndex.setStatus("mandatory")


class _MscVsrSvsFramerNRatesRateIndex_Type(Integer32):
    """Custom type mscVsrSvsFramerNRatesRateIndex based on Integer32"""
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


_MscVsrSvsFramerNRatesRateIndex_Type.__name__ = "Integer32"
_MscVsrSvsFramerNRatesRateIndex_Object = MibTableColumn
mscVsrSvsFramerNRatesRateIndex = _MscVsrSvsFramerNRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 479, 1, 2),
    _MscVsrSvsFramerNRatesRateIndex_Type()
)
mscVsrSvsFramerNRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNRatesRateIndex.setStatus("mandatory")


class _MscVsrSvsFramerNRatesValue_Type(Integer32):
    """Custom type mscVsrSvsFramerNRatesValue based on Integer32"""
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


_MscVsrSvsFramerNRatesValue_Type.__name__ = "Integer32"
_MscVsrSvsFramerNRatesValue_Object = MibTableColumn
mscVsrSvsFramerNRatesValue = _MscVsrSvsFramerNRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 2, 479, 1, 3),
    _MscVsrSvsFramerNRatesValue_Type()
)
mscVsrSvsFramerNRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsFramerNRatesValue.setStatus("mandatory")
_MscVsrSvsLCo_ObjectIdentity = ObjectIdentity
mscVsrSvsLCo = _MscVsrSvsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3)
)
_MscVsrSvsLCoRowStatusTable_Object = MibTable
mscVsrSvsLCoRowStatusTable = _MscVsrSvsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoRowStatusTable.setStatus("mandatory")
_MscVsrSvsLCoRowStatusEntry_Object = MibTableRow
mscVsrSvsLCoRowStatusEntry = _MscVsrSvsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1, 1)
)
mscVsrSvsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoRowStatusEntry.setStatus("mandatory")
_MscVsrSvsLCoRowStatus_Type = RowStatus
_MscVsrSvsLCoRowStatus_Object = MibTableColumn
mscVsrSvsLCoRowStatus = _MscVsrSvsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1, 1, 1),
    _MscVsrSvsLCoRowStatus_Type()
)
mscVsrSvsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRowStatus.setStatus("mandatory")
_MscVsrSvsLCoComponentName_Type = DisplayString
_MscVsrSvsLCoComponentName_Object = MibTableColumn
mscVsrSvsLCoComponentName = _MscVsrSvsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1, 1, 2),
    _MscVsrSvsLCoComponentName_Type()
)
mscVsrSvsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoComponentName.setStatus("mandatory")
_MscVsrSvsLCoStorageType_Type = StorageType
_MscVsrSvsLCoStorageType_Object = MibTableColumn
mscVsrSvsLCoStorageType = _MscVsrSvsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1, 1, 4),
    _MscVsrSvsLCoStorageType_Type()
)
mscVsrSvsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoStorageType.setStatus("mandatory")
_MscVsrSvsLCoIndex_Type = NonReplicated
_MscVsrSvsLCoIndex_Object = MibTableColumn
mscVsrSvsLCoIndex = _MscVsrSvsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 1, 1, 10),
    _MscVsrSvsLCoIndex_Type()
)
mscVsrSvsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsLCoIndex.setStatus("mandatory")
_MscVsrSvsLCoPathDataTable_Object = MibTable
mscVsrSvsLCoPathDataTable = _MscVsrSvsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathDataTable.setStatus("mandatory")
_MscVsrSvsLCoPathDataEntry_Object = MibTableRow
mscVsrSvsLCoPathDataEntry = _MscVsrSvsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1)
)
mscVsrSvsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathDataEntry.setStatus("mandatory")


class _MscVsrSvsLCoState_Type(Integer32):
    """Custom type mscVsrSvsLCoState based on Integer32"""
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


_MscVsrSvsLCoState_Type.__name__ = "Integer32"
_MscVsrSvsLCoState_Object = MibTableColumn
mscVsrSvsLCoState = _MscVsrSvsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 1),
    _MscVsrSvsLCoState_Type()
)
mscVsrSvsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoState.setStatus("mandatory")


class _MscVsrSvsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscVsrSvsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsrSvsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscVsrSvsLCoOverrideRemoteName_Object = MibTableColumn
mscVsrSvsLCoOverrideRemoteName = _MscVsrSvsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 2),
    _MscVsrSvsLCoOverrideRemoteName_Type()
)
mscVsrSvsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsLCoOverrideRemoteName.setStatus("mandatory")


class _MscVsrSvsLCoEnd_Type(Integer32):
    """Custom type mscVsrSvsLCoEnd based on Integer32"""
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


_MscVsrSvsLCoEnd_Type.__name__ = "Integer32"
_MscVsrSvsLCoEnd_Object = MibTableColumn
mscVsrSvsLCoEnd = _MscVsrSvsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 3),
    _MscVsrSvsLCoEnd_Type()
)
mscVsrSvsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoEnd.setStatus("mandatory")


class _MscVsrSvsLCoCostMetric_Type(Unsigned32):
    """Custom type mscVsrSvsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsrSvsLCoCostMetric_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoCostMetric_Object = MibTableColumn
mscVsrSvsLCoCostMetric = _MscVsrSvsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 4),
    _MscVsrSvsLCoCostMetric_Type()
)
mscVsrSvsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoCostMetric.setStatus("mandatory")


class _MscVsrSvsLCoDelayMetric_Type(Unsigned32):
    """Custom type mscVsrSvsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscVsrSvsLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoDelayMetric_Object = MibTableColumn
mscVsrSvsLCoDelayMetric = _MscVsrSvsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 5),
    _MscVsrSvsLCoDelayMetric_Type()
)
mscVsrSvsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoDelayMetric.setStatus("mandatory")


class _MscVsrSvsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscVsrSvsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscVsrSvsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoRoundTripDelay_Object = MibTableColumn
mscVsrSvsLCoRoundTripDelay = _MscVsrSvsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 6),
    _MscVsrSvsLCoRoundTripDelay_Type()
)
mscVsrSvsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRoundTripDelay.setStatus("mandatory")


class _MscVsrSvsLCoSetupPriority_Type(Unsigned32):
    """Custom type mscVsrSvsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsrSvsLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoSetupPriority_Object = MibTableColumn
mscVsrSvsLCoSetupPriority = _MscVsrSvsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 7),
    _MscVsrSvsLCoSetupPriority_Type()
)
mscVsrSvsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoSetupPriority.setStatus("mandatory")


class _MscVsrSvsLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscVsrSvsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVsrSvsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoHoldingPriority_Object = MibTableColumn
mscVsrSvsLCoHoldingPriority = _MscVsrSvsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 8),
    _MscVsrSvsLCoHoldingPriority_Type()
)
mscVsrSvsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoHoldingPriority.setStatus("mandatory")


class _MscVsrSvsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscVsrSvsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscVsrSvsLCoRequiredTxBandwidth_Object = MibTableColumn
mscVsrSvsLCoRequiredTxBandwidth = _MscVsrSvsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 9),
    _MscVsrSvsLCoRequiredTxBandwidth_Type()
)
mscVsrSvsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscVsrSvsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscVsrSvsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVsrSvsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscVsrSvsLCoRequiredRxBandwidth_Object = MibTableColumn
mscVsrSvsLCoRequiredRxBandwidth = _MscVsrSvsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 10),
    _MscVsrSvsLCoRequiredRxBandwidth_Type()
)
mscVsrSvsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscVsrSvsLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscVsrSvsLCoRequiredTrafficType based on Integer32"""
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


_MscVsrSvsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscVsrSvsLCoRequiredTrafficType_Object = MibTableColumn
mscVsrSvsLCoRequiredTrafficType = _MscVsrSvsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 11),
    _MscVsrSvsLCoRequiredTrafficType_Type()
)
mscVsrSvsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRequiredTrafficType.setStatus("mandatory")


class _MscVsrSvsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscVsrSvsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVsrSvsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscVsrSvsLCoPermittedTrunkTypes_Object = MibTableColumn
mscVsrSvsLCoPermittedTrunkTypes = _MscVsrSvsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 12),
    _MscVsrSvsLCoPermittedTrunkTypes_Type()
)
mscVsrSvsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscVsrSvsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscVsrSvsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsrSvsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoRequiredSecurity_Object = MibTableColumn
mscVsrSvsLCoRequiredSecurity = _MscVsrSvsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 13),
    _MscVsrSvsLCoRequiredSecurity_Type()
)
mscVsrSvsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRequiredSecurity.setStatus("mandatory")


class _MscVsrSvsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscVsrSvsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVsrSvsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoRequiredCustomerParameter_Object = MibTableColumn
mscVsrSvsLCoRequiredCustomerParameter = _MscVsrSvsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 14),
    _MscVsrSvsLCoRequiredCustomerParameter_Type()
)
mscVsrSvsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscVsrSvsLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscVsrSvsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscVsrSvsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoEmissionPriority_Object = MibTableColumn
mscVsrSvsLCoEmissionPriority = _MscVsrSvsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 15),
    _MscVsrSvsLCoEmissionPriority_Type()
)
mscVsrSvsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoEmissionPriority.setStatus("mandatory")


class _MscVsrSvsLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscVsrSvsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscVsrSvsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoDiscardPriority_Object = MibTableColumn
mscVsrSvsLCoDiscardPriority = _MscVsrSvsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 16),
    _MscVsrSvsLCoDiscardPriority_Type()
)
mscVsrSvsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoDiscardPriority.setStatus("mandatory")


class _MscVsrSvsLCoPathType_Type(Integer32):
    """Custom type mscVsrSvsLCoPathType based on Integer32"""
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


_MscVsrSvsLCoPathType_Type.__name__ = "Integer32"
_MscVsrSvsLCoPathType_Object = MibTableColumn
mscVsrSvsLCoPathType = _MscVsrSvsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 17),
    _MscVsrSvsLCoPathType_Type()
)
mscVsrSvsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathType.setStatus("mandatory")


class _MscVsrSvsLCoRetryCount_Type(Unsigned32):
    """Custom type mscVsrSvsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVsrSvsLCoRetryCount_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoRetryCount_Object = MibTableColumn
mscVsrSvsLCoRetryCount = _MscVsrSvsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 18),
    _MscVsrSvsLCoRetryCount_Type()
)
mscVsrSvsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoRetryCount.setStatus("mandatory")


class _MscVsrSvsLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscVsrSvsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVsrSvsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscVsrSvsLCoPathFailureCount_Object = MibTableColumn
mscVsrSvsLCoPathFailureCount = _MscVsrSvsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 19),
    _MscVsrSvsLCoPathFailureCount_Type()
)
mscVsrSvsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathFailureCount.setStatus("mandatory")


class _MscVsrSvsLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscVsrSvsLCoReasonForNoRoute based on Integer32"""
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


_MscVsrSvsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscVsrSvsLCoReasonForNoRoute_Object = MibTableColumn
mscVsrSvsLCoReasonForNoRoute = _MscVsrSvsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 20),
    _MscVsrSvsLCoReasonForNoRoute_Type()
)
mscVsrSvsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoReasonForNoRoute.setStatus("mandatory")


class _MscVsrSvsLCoLastTearDownReason_Type(Integer32):
    """Custom type mscVsrSvsLCoLastTearDownReason based on Integer32"""
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


_MscVsrSvsLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscVsrSvsLCoLastTearDownReason_Object = MibTableColumn
mscVsrSvsLCoLastTearDownReason = _MscVsrSvsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 21),
    _MscVsrSvsLCoLastTearDownReason_Type()
)
mscVsrSvsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoLastTearDownReason.setStatus("mandatory")


class _MscVsrSvsLCoPathFailureAction_Type(Integer32):
    """Custom type mscVsrSvsLCoPathFailureAction based on Integer32"""
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


_MscVsrSvsLCoPathFailureAction_Type.__name__ = "Integer32"
_MscVsrSvsLCoPathFailureAction_Object = MibTableColumn
mscVsrSvsLCoPathFailureAction = _MscVsrSvsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 22),
    _MscVsrSvsLCoPathFailureAction_Type()
)
mscVsrSvsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathFailureAction.setStatus("mandatory")


class _MscVsrSvsLCoBumpPreference_Type(Integer32):
    """Custom type mscVsrSvsLCoBumpPreference based on Integer32"""
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


_MscVsrSvsLCoBumpPreference_Type.__name__ = "Integer32"
_MscVsrSvsLCoBumpPreference_Object = MibTableColumn
mscVsrSvsLCoBumpPreference = _MscVsrSvsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 23),
    _MscVsrSvsLCoBumpPreference_Type()
)
mscVsrSvsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoBumpPreference.setStatus("mandatory")


class _MscVsrSvsLCoOptimization_Type(Integer32):
    """Custom type mscVsrSvsLCoOptimization based on Integer32"""
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


_MscVsrSvsLCoOptimization_Type.__name__ = "Integer32"
_MscVsrSvsLCoOptimization_Object = MibTableColumn
mscVsrSvsLCoOptimization = _MscVsrSvsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 24),
    _MscVsrSvsLCoOptimization_Type()
)
mscVsrSvsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoOptimization.setStatus("mandatory")


class _MscVsrSvsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscVsrSvsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscVsrSvsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscVsrSvsLCoPathUpDateTime_Object = MibTableColumn
mscVsrSvsLCoPathUpDateTime = _MscVsrSvsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 10, 1, 25),
    _MscVsrSvsLCoPathUpDateTime_Type()
)
mscVsrSvsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathUpDateTime.setStatus("mandatory")
_MscVsrSvsLCoStatsTable_Object = MibTable
mscVsrSvsLCoStatsTable = _MscVsrSvsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoStatsTable.setStatus("mandatory")
_MscVsrSvsLCoStatsEntry_Object = MibTableRow
mscVsrSvsLCoStatsEntry = _MscVsrSvsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11, 1)
)
mscVsrSvsLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoStatsEntry.setStatus("mandatory")
_MscVsrSvsLCoPktsToNetwork_Type = PassportCounter64
_MscVsrSvsLCoPktsToNetwork_Object = MibTableColumn
mscVsrSvsLCoPktsToNetwork = _MscVsrSvsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11, 1, 1),
    _MscVsrSvsLCoPktsToNetwork_Type()
)
mscVsrSvsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPktsToNetwork.setStatus("mandatory")
_MscVsrSvsLCoBytesToNetwork_Type = PassportCounter64
_MscVsrSvsLCoBytesToNetwork_Object = MibTableColumn
mscVsrSvsLCoBytesToNetwork = _MscVsrSvsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11, 1, 2),
    _MscVsrSvsLCoBytesToNetwork_Type()
)
mscVsrSvsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoBytesToNetwork.setStatus("mandatory")
_MscVsrSvsLCoPktsFromNetwork_Type = PassportCounter64
_MscVsrSvsLCoPktsFromNetwork_Object = MibTableColumn
mscVsrSvsLCoPktsFromNetwork = _MscVsrSvsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11, 1, 3),
    _MscVsrSvsLCoPktsFromNetwork_Type()
)
mscVsrSvsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPktsFromNetwork.setStatus("mandatory")
_MscVsrSvsLCoBytesFromNetwork_Type = PassportCounter64
_MscVsrSvsLCoBytesFromNetwork_Object = MibTableColumn
mscVsrSvsLCoBytesFromNetwork = _MscVsrSvsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 11, 1, 4),
    _MscVsrSvsLCoBytesFromNetwork_Type()
)
mscVsrSvsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoBytesFromNetwork.setStatus("mandatory")
_MscVsrSvsLCoPathTable_Object = MibTable
mscVsrSvsLCoPathTable = _MscVsrSvsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 264)
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathTable.setStatus("mandatory")
_MscVsrSvsLCoPathEntry_Object = MibTableRow
mscVsrSvsLCoPathEntry = _MscVsrSvsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 264, 1)
)
mscVsrSvsLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathEntry.setStatus("mandatory")


class _MscVsrSvsLCoPathValue_Type(AsciiString):
    """Custom type mscVsrSvsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsrSvsLCoPathValue_Type.__name__ = "AsciiString"
_MscVsrSvsLCoPathValue_Object = MibTableColumn
mscVsrSvsLCoPathValue = _MscVsrSvsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 3, 264, 1, 1),
    _MscVsrSvsLCoPathValue_Type()
)
mscVsrSvsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsLCoPathValue.setStatus("mandatory")
_MscVsrSvsDebug_ObjectIdentity = ObjectIdentity
mscVsrSvsDebug = _MscVsrSvsDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4)
)
_MscVsrSvsDebugRowStatusTable_Object = MibTable
mscVsrSvsDebugRowStatusTable = _MscVsrSvsDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscVsrSvsDebugRowStatusTable.setStatus("mandatory")
_MscVsrSvsDebugRowStatusEntry_Object = MibTableRow
mscVsrSvsDebugRowStatusEntry = _MscVsrSvsDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1, 1)
)
mscVsrSvsDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsDebugRowStatusEntry.setStatus("mandatory")
_MscVsrSvsDebugRowStatus_Type = RowStatus
_MscVsrSvsDebugRowStatus_Object = MibTableColumn
mscVsrSvsDebugRowStatus = _MscVsrSvsDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1, 1, 1),
    _MscVsrSvsDebugRowStatus_Type()
)
mscVsrSvsDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsDebugRowStatus.setStatus("mandatory")
_MscVsrSvsDebugComponentName_Type = DisplayString
_MscVsrSvsDebugComponentName_Object = MibTableColumn
mscVsrSvsDebugComponentName = _MscVsrSvsDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1, 1, 2),
    _MscVsrSvsDebugComponentName_Type()
)
mscVsrSvsDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsDebugComponentName.setStatus("mandatory")
_MscVsrSvsDebugStorageType_Type = StorageType
_MscVsrSvsDebugStorageType_Object = MibTableColumn
mscVsrSvsDebugStorageType = _MscVsrSvsDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1, 1, 4),
    _MscVsrSvsDebugStorageType_Type()
)
mscVsrSvsDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsDebugStorageType.setStatus("mandatory")
_MscVsrSvsDebugIndex_Type = NonReplicated
_MscVsrSvsDebugIndex_Object = MibTableColumn
mscVsrSvsDebugIndex = _MscVsrSvsDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 4, 1, 1, 10),
    _MscVsrSvsDebugIndex_Type()
)
mscVsrSvsDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrSvsDebugIndex.setStatus("mandatory")
_MscVsrSvsIfEntryTable_Object = MibTable
mscVsrSvsIfEntryTable = _MscVsrSvsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 11)
)
if mibBuilder.loadTexts:
    mscVsrSvsIfEntryTable.setStatus("mandatory")
_MscVsrSvsIfEntryEntry_Object = MibTableRow
mscVsrSvsIfEntryEntry = _MscVsrSvsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 11, 1)
)
mscVsrSvsIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsIfEntryEntry.setStatus("mandatory")


class _MscVsrSvsIfAdminStatus_Type(Integer32):
    """Custom type mscVsrSvsIfAdminStatus based on Integer32"""
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


_MscVsrSvsIfAdminStatus_Type.__name__ = "Integer32"
_MscVsrSvsIfAdminStatus_Object = MibTableColumn
mscVsrSvsIfAdminStatus = _MscVsrSvsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 11, 1, 1),
    _MscVsrSvsIfAdminStatus_Type()
)
mscVsrSvsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSvsIfAdminStatus.setStatus("mandatory")


class _MscVsrSvsIfIndex_Type(InterfaceIndex):
    """Custom type mscVsrSvsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVsrSvsIfIndex_Type.__name__ = "InterfaceIndex"
_MscVsrSvsIfIndex_Object = MibTableColumn
mscVsrSvsIfIndex = _MscVsrSvsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 11, 1, 2),
    _MscVsrSvsIfIndex_Type()
)
mscVsrSvsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsIfIndex.setStatus("mandatory")
_MscVsrSvsOperTable_Object = MibTable
mscVsrSvsOperTable = _MscVsrSvsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12)
)
if mibBuilder.loadTexts:
    mscVsrSvsOperTable.setStatus("mandatory")
_MscVsrSvsOperEntry_Object = MibTableRow
mscVsrSvsOperEntry = _MscVsrSvsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1)
)
mscVsrSvsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsOperEntry.setStatus("mandatory")


class _MscVsrSvsStatus_Type(Integer32):
    """Custom type mscVsrSvsStatus based on Integer32"""
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
        *(("answered", 2),
          ("clearing", 3),
          ("idle", 0),
          ("idleMaintenance", 5),
          ("lockout", 4),
          ("seized", 1))
    )


_MscVsrSvsStatus_Type.__name__ = "Integer32"
_MscVsrSvsStatus_Object = MibTableColumn
mscVsrSvsStatus = _MscVsrSvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 1),
    _MscVsrSvsStatus_Type()
)
mscVsrSvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsStatus.setStatus("mandatory")
_MscVsrSvsProfileNumber_Type = Counter32
_MscVsrSvsProfileNumber_Object = MibTableColumn
mscVsrSvsProfileNumber = _MscVsrSvsProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 2),
    _MscVsrSvsProfileNumber_Type()
)
mscVsrSvsProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsProfileNumber.setStatus("mandatory")


class _MscVsrSvsCallType_Type(Integer32):
    """Custom type mscVsrSvsCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("modem", 2),
          ("voice", 0))
    )


_MscVsrSvsCallType_Type.__name__ = "Integer32"
_MscVsrSvsCallType_Object = MibTableColumn
mscVsrSvsCallType = _MscVsrSvsCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 3),
    _MscVsrSvsCallType_Type()
)
mscVsrSvsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsCallType.setStatus("mandatory")


class _MscVsrSvsCalledNumber_Type(DigitString):
    """Custom type mscVsrSvsCalledNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVsrSvsCalledNumber_Type.__name__ = "DigitString"
_MscVsrSvsCalledNumber_Object = MibTableColumn
mscVsrSvsCalledNumber = _MscVsrSvsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 4),
    _MscVsrSvsCalledNumber_Type()
)
mscVsrSvsCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsCalledNumber.setStatus("mandatory")


class _MscVsrSvsCallingNumber_Type(DigitString):
    """Custom type mscVsrSvsCallingNumber based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MscVsrSvsCallingNumber_Type.__name__ = "DigitString"
_MscVsrSvsCallingNumber_Object = MibTableColumn
mscVsrSvsCallingNumber = _MscVsrSvsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 5),
    _MscVsrSvsCallingNumber_Type()
)
mscVsrSvsCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsCallingNumber.setStatus("mandatory")


class _MscVsrSvsClearCauseCode_Type(Hex):
    """Custom type mscVsrSvsClearCauseCode based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscVsrSvsClearCauseCode_Type.__name__ = "Hex"
_MscVsrSvsClearCauseCode_Object = MibTableColumn
mscVsrSvsClearCauseCode = _MscVsrSvsClearCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 12, 1, 6),
    _MscVsrSvsClearCauseCode_Type()
)
mscVsrSvsClearCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsClearCauseCode.setStatus("mandatory")
_MscVsrSvsStatsTable_Object = MibTable
mscVsrSvsStatsTable = _MscVsrSvsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 13)
)
if mibBuilder.loadTexts:
    mscVsrSvsStatsTable.setStatus("mandatory")
_MscVsrSvsStatsEntry_Object = MibTableRow
mscVsrSvsStatsEntry = _MscVsrSvsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 13, 1)
)
mscVsrSvsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsStatsEntry.setStatus("mandatory")
_MscVsrSvsTotalCalls_Type = Counter32
_MscVsrSvsTotalCalls_Object = MibTableColumn
mscVsrSvsTotalCalls = _MscVsrSvsTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 13, 1, 1),
    _MscVsrSvsTotalCalls_Type()
)
mscVsrSvsTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsTotalCalls.setStatus("mandatory")
_MscVsrSvsTotalCallSeconds_Type = Counter32
_MscVsrSvsTotalCallSeconds_Object = MibTableColumn
mscVsrSvsTotalCallSeconds = _MscVsrSvsTotalCallSeconds_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 13, 1, 2),
    _MscVsrSvsTotalCallSeconds_Type()
)
mscVsrSvsTotalCallSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsTotalCallSeconds.setStatus("mandatory")
_MscVsrSvsStateTable_Object = MibTable
mscVsrSvsStateTable = _MscVsrSvsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 14)
)
if mibBuilder.loadTexts:
    mscVsrSvsStateTable.setStatus("mandatory")
_MscVsrSvsStateEntry_Object = MibTableRow
mscVsrSvsStateEntry = _MscVsrSvsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 14, 1)
)
mscVsrSvsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsStateEntry.setStatus("mandatory")


class _MscVsrSvsAdminState_Type(Integer32):
    """Custom type mscVsrSvsAdminState based on Integer32"""
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


_MscVsrSvsAdminState_Type.__name__ = "Integer32"
_MscVsrSvsAdminState_Object = MibTableColumn
mscVsrSvsAdminState = _MscVsrSvsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 14, 1, 1),
    _MscVsrSvsAdminState_Type()
)
mscVsrSvsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsAdminState.setStatus("mandatory")


class _MscVsrSvsOperationalState_Type(Integer32):
    """Custom type mscVsrSvsOperationalState based on Integer32"""
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


_MscVsrSvsOperationalState_Type.__name__ = "Integer32"
_MscVsrSvsOperationalState_Object = MibTableColumn
mscVsrSvsOperationalState = _MscVsrSvsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 14, 1, 2),
    _MscVsrSvsOperationalState_Type()
)
mscVsrSvsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsOperationalState.setStatus("mandatory")


class _MscVsrSvsUsageState_Type(Integer32):
    """Custom type mscVsrSvsUsageState based on Integer32"""
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


_MscVsrSvsUsageState_Type.__name__ = "Integer32"
_MscVsrSvsUsageState_Object = MibTableColumn
mscVsrSvsUsageState = _MscVsrSvsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 14, 1, 3),
    _MscVsrSvsUsageState_Type()
)
mscVsrSvsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsUsageState.setStatus("mandatory")
_MscVsrSvsOperStatusTable_Object = MibTable
mscVsrSvsOperStatusTable = _MscVsrSvsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 15)
)
if mibBuilder.loadTexts:
    mscVsrSvsOperStatusTable.setStatus("mandatory")
_MscVsrSvsOperStatusEntry_Object = MibTableRow
mscVsrSvsOperStatusEntry = _MscVsrSvsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 15, 1)
)
mscVsrSvsOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrSvsIndex"),
)
if mibBuilder.loadTexts:
    mscVsrSvsOperStatusEntry.setStatus("mandatory")


class _MscVsrSvsSnmpOperStatus_Type(Integer32):
    """Custom type mscVsrSvsSnmpOperStatus based on Integer32"""
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


_MscVsrSvsSnmpOperStatus_Type.__name__ = "Integer32"
_MscVsrSvsSnmpOperStatus_Object = MibTableColumn
mscVsrSvsSnmpOperStatus = _MscVsrSvsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 2, 15, 1, 1),
    _MscVsrSvsSnmpOperStatus_Type()
)
mscVsrSvsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSvsSnmpOperStatus.setStatus("mandatory")
_MscVsrDebug_ObjectIdentity = ObjectIdentity
mscVsrDebug = _MscVsrDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3)
)
_MscVsrDebugRowStatusTable_Object = MibTable
mscVsrDebugRowStatusTable = _MscVsrDebugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1)
)
if mibBuilder.loadTexts:
    mscVsrDebugRowStatusTable.setStatus("mandatory")
_MscVsrDebugRowStatusEntry_Object = MibTableRow
mscVsrDebugRowStatusEntry = _MscVsrDebugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1, 1)
)
mscVsrDebugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrDebugIndex"),
)
if mibBuilder.loadTexts:
    mscVsrDebugRowStatusEntry.setStatus("mandatory")
_MscVsrDebugRowStatus_Type = RowStatus
_MscVsrDebugRowStatus_Object = MibTableColumn
mscVsrDebugRowStatus = _MscVsrDebugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1, 1, 1),
    _MscVsrDebugRowStatus_Type()
)
mscVsrDebugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrDebugRowStatus.setStatus("mandatory")
_MscVsrDebugComponentName_Type = DisplayString
_MscVsrDebugComponentName_Object = MibTableColumn
mscVsrDebugComponentName = _MscVsrDebugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1, 1, 2),
    _MscVsrDebugComponentName_Type()
)
mscVsrDebugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrDebugComponentName.setStatus("mandatory")
_MscVsrDebugStorageType_Type = StorageType
_MscVsrDebugStorageType_Object = MibTableColumn
mscVsrDebugStorageType = _MscVsrDebugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1, 1, 4),
    _MscVsrDebugStorageType_Type()
)
mscVsrDebugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrDebugStorageType.setStatus("mandatory")
_MscVsrDebugIndex_Type = NonReplicated
_MscVsrDebugIndex_Object = MibTableColumn
mscVsrDebugIndex = _MscVsrDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 3, 1, 1, 10),
    _MscVsrDebugIndex_Type()
)
mscVsrDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVsrDebugIndex.setStatus("mandatory")
_MscVsrCidDataTable_Object = MibTable
mscVsrCidDataTable = _MscVsrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 10)
)
if mibBuilder.loadTexts:
    mscVsrCidDataTable.setStatus("mandatory")
_MscVsrCidDataEntry_Object = MibTableRow
mscVsrCidDataEntry = _MscVsrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 10, 1)
)
mscVsrCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrCidDataEntry.setStatus("mandatory")


class _MscVsrCustomerIdentifier_Type(Unsigned32):
    """Custom type mscVsrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscVsrCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscVsrCustomerIdentifier_Object = MibTableColumn
mscVsrCustomerIdentifier = _MscVsrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 10, 1, 1),
    _MscVsrCustomerIdentifier_Type()
)
mscVsrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrCustomerIdentifier.setStatus("mandatory")
_MscVsrIfEntryTable_Object = MibTable
mscVsrIfEntryTable = _MscVsrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 11)
)
if mibBuilder.loadTexts:
    mscVsrIfEntryTable.setStatus("mandatory")
_MscVsrIfEntryEntry_Object = MibTableRow
mscVsrIfEntryEntry = _MscVsrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 11, 1)
)
mscVsrIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrIfEntryEntry.setStatus("mandatory")


class _MscVsrIfAdminStatus_Type(Integer32):
    """Custom type mscVsrIfAdminStatus based on Integer32"""
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


_MscVsrIfAdminStatus_Type.__name__ = "Integer32"
_MscVsrIfAdminStatus_Object = MibTableColumn
mscVsrIfAdminStatus = _MscVsrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 11, 1, 1),
    _MscVsrIfAdminStatus_Type()
)
mscVsrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrIfAdminStatus.setStatus("mandatory")


class _MscVsrIfIndex_Type(InterfaceIndex):
    """Custom type mscVsrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVsrIfIndex_Type.__name__ = "InterfaceIndex"
_MscVsrIfIndex_Object = MibTableColumn
mscVsrIfIndex = _MscVsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 11, 1, 2),
    _MscVsrIfIndex_Type()
)
mscVsrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrIfIndex.setStatus("mandatory")
_MscVsrProvTable_Object = MibTable
mscVsrProvTable = _MscVsrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 12)
)
if mibBuilder.loadTexts:
    mscVsrProvTable.setStatus("mandatory")
_MscVsrProvEntry_Object = MibTableRow
mscVsrProvEntry = _MscVsrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 12, 1)
)
mscVsrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrProvEntry.setStatus("mandatory")


class _MscVsrCommentText_Type(AsciiString):
    """Custom type mscVsrCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVsrCommentText_Type.__name__ = "AsciiString"
_MscVsrCommentText_Object = MibTableColumn
mscVsrCommentText = _MscVsrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 12, 1, 1),
    _MscVsrCommentText_Type()
)
mscVsrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrCommentText.setStatus("mandatory")
_MscVsrVoiceRoute_Type = Link
_MscVsrVoiceRoute_Object = MibTableColumn
mscVsrVoiceRoute = _MscVsrVoiceRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 12, 1, 3),
    _MscVsrVoiceRoute_Type()
)
mscVsrVoiceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrVoiceRoute.setStatus("mandatory")
_MscVsrSignallingChannel_Type = Link
_MscVsrSignallingChannel_Object = MibTableColumn
mscVsrSignallingChannel = _MscVsrSignallingChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 12, 1, 311),
    _MscVsrSignallingChannel_Type()
)
mscVsrSignallingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVsrSignallingChannel.setStatus("mandatory")
_MscVsrStateTable_Object = MibTable
mscVsrStateTable = _MscVsrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 13)
)
if mibBuilder.loadTexts:
    mscVsrStateTable.setStatus("mandatory")
_MscVsrStateEntry_Object = MibTableRow
mscVsrStateEntry = _MscVsrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 13, 1)
)
mscVsrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrStateEntry.setStatus("mandatory")


class _MscVsrAdminState_Type(Integer32):
    """Custom type mscVsrAdminState based on Integer32"""
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


_MscVsrAdminState_Type.__name__ = "Integer32"
_MscVsrAdminState_Object = MibTableColumn
mscVsrAdminState = _MscVsrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 13, 1, 1),
    _MscVsrAdminState_Type()
)
mscVsrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrAdminState.setStatus("mandatory")


class _MscVsrOperationalState_Type(Integer32):
    """Custom type mscVsrOperationalState based on Integer32"""
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


_MscVsrOperationalState_Type.__name__ = "Integer32"
_MscVsrOperationalState_Object = MibTableColumn
mscVsrOperationalState = _MscVsrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 13, 1, 2),
    _MscVsrOperationalState_Type()
)
mscVsrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrOperationalState.setStatus("mandatory")


class _MscVsrUsageState_Type(Integer32):
    """Custom type mscVsrUsageState based on Integer32"""
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


_MscVsrUsageState_Type.__name__ = "Integer32"
_MscVsrUsageState_Object = MibTableColumn
mscVsrUsageState = _MscVsrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 13, 1, 3),
    _MscVsrUsageState_Type()
)
mscVsrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrUsageState.setStatus("mandatory")
_MscVsrOperStatusTable_Object = MibTable
mscVsrOperStatusTable = _MscVsrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 14)
)
if mibBuilder.loadTexts:
    mscVsrOperStatusTable.setStatus("mandatory")
_MscVsrOperStatusEntry_Object = MibTableRow
mscVsrOperStatusEntry = _MscVsrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 14, 1)
)
mscVsrOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrOperStatusEntry.setStatus("mandatory")


class _MscVsrSnmpOperStatus_Type(Integer32):
    """Custom type mscVsrSnmpOperStatus based on Integer32"""
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


_MscVsrSnmpOperStatus_Type.__name__ = "Integer32"
_MscVsrSnmpOperStatus_Object = MibTableColumn
mscVsrSnmpOperStatus = _MscVsrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 14, 1, 1),
    _MscVsrSnmpOperStatus_Type()
)
mscVsrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrSnmpOperStatus.setStatus("mandatory")
_MscVsrStatsTable_Object = MibTable
mscVsrStatsTable = _MscVsrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15)
)
if mibBuilder.loadTexts:
    mscVsrStatsTable.setStatus("mandatory")
_MscVsrStatsEntry_Object = MibTableRow
mscVsrStatsEntry = _MscVsrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1)
)
mscVsrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrStatsEntry.setStatus("mandatory")
_MscVsrTotalCallsFromIf_Type = Counter32
_MscVsrTotalCallsFromIf_Object = MibTableColumn
mscVsrTotalCallsFromIf = _MscVsrTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 1),
    _MscVsrTotalCallsFromIf_Type()
)
mscVsrTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrTotalCallsFromIf.setStatus("mandatory")
_MscVsrTotalFailedCallsFromIf_Type = Counter32
_MscVsrTotalFailedCallsFromIf_Object = MibTableColumn
mscVsrTotalFailedCallsFromIf = _MscVsrTotalFailedCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 2),
    _MscVsrTotalFailedCallsFromIf_Type()
)
mscVsrTotalFailedCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrTotalFailedCallsFromIf.setStatus("mandatory")
_MscVsrInvalidNumberingPlanCalls_Type = Counter32
_MscVsrInvalidNumberingPlanCalls_Object = MibTableColumn
mscVsrInvalidNumberingPlanCalls = _MscVsrInvalidNumberingPlanCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 3),
    _MscVsrInvalidNumberingPlanCalls_Type()
)
mscVsrInvalidNumberingPlanCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrInvalidNumberingPlanCalls.setStatus("mandatory")
_MscVsrAddressResolutionFailedCalls_Type = Counter32
_MscVsrAddressResolutionFailedCalls_Object = MibTableColumn
mscVsrAddressResolutionFailedCalls = _MscVsrAddressResolutionFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 4),
    _MscVsrAddressResolutionFailedCalls_Type()
)
mscVsrAddressResolutionFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrAddressResolutionFailedCalls.setStatus("mandatory")
_MscVsrAddressIncompleteCalls_Type = Counter32
_MscVsrAddressIncompleteCalls_Object = MibTableColumn
mscVsrAddressIncompleteCalls = _MscVsrAddressIncompleteCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 5),
    _MscVsrAddressIncompleteCalls_Type()
)
mscVsrAddressIncompleteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrAddressIncompleteCalls.setStatus("mandatory")
_MscVsrPathAttributesNotMetCalls_Type = Counter32
_MscVsrPathAttributesNotMetCalls_Object = MibTableColumn
mscVsrPathAttributesNotMetCalls = _MscVsrPathAttributesNotMetCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 6),
    _MscVsrPathAttributesNotMetCalls_Type()
)
mscVsrPathAttributesNotMetCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPathAttributesNotMetCalls.setStatus("mandatory")
_MscVsrPathSetupTimeOutCalls_Type = Counter32
_MscVsrPathSetupTimeOutCalls_Object = MibTableColumn
mscVsrPathSetupTimeOutCalls = _MscVsrPathSetupTimeOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 7),
    _MscVsrPathSetupTimeOutCalls_Type()
)
mscVsrPathSetupTimeOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPathSetupTimeOutCalls.setStatus("mandatory")
_MscVsrCallsRejectedLocally_Type = Counter32
_MscVsrCallsRejectedLocally_Object = MibTableColumn
mscVsrCallsRejectedLocally = _MscVsrCallsRejectedLocally_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 8),
    _MscVsrCallsRejectedLocally_Type()
)
mscVsrCallsRejectedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrCallsRejectedLocally.setStatus("mandatory")
_MscVsrCallsRejectedByFarEnd_Type = Counter32
_MscVsrCallsRejectedByFarEnd_Object = MibTableColumn
mscVsrCallsRejectedByFarEnd = _MscVsrCallsRejectedByFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 15, 1, 9),
    _MscVsrCallsRejectedByFarEnd_Type()
)
mscVsrCallsRejectedByFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrCallsRejectedByFarEnd.setStatus("mandatory")
_MscVsrOperTable_Object = MibTable
mscVsrOperTable = _MscVsrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16)
)
if mibBuilder.loadTexts:
    mscVsrOperTable.setStatus("mandatory")
_MscVsrOperEntry_Object = MibTableRow
mscVsrOperEntry = _MscVsrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1)
)
mscVsrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscVsrIndex"),
)
if mibBuilder.loadTexts:
    mscVsrOperEntry.setStatus("mandatory")
_MscVsrActiveChannels_Type = Counter32
_MscVsrActiveChannels_Object = MibTableColumn
mscVsrActiveChannels = _MscVsrActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 2),
    _MscVsrActiveChannels_Type()
)
mscVsrActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveChannels.setStatus("mandatory")
_MscVsrPeakActiveChannels_Type = Counter32
_MscVsrPeakActiveChannels_Object = MibTableColumn
mscVsrPeakActiveChannels = _MscVsrPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 3),
    _MscVsrPeakActiveChannels_Type()
)
mscVsrPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveChannels.setStatus("mandatory")
_MscVsrActiveVoiceChannels_Type = Counter32
_MscVsrActiveVoiceChannels_Object = MibTableColumn
mscVsrActiveVoiceChannels = _MscVsrActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 4),
    _MscVsrActiveVoiceChannels_Type()
)
mscVsrActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveVoiceChannels.setStatus("mandatory")
_MscVsrActiveModemChannels_Type = Counter32
_MscVsrActiveModemChannels_Object = MibTableColumn
mscVsrActiveModemChannels = _MscVsrActiveModemChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 5),
    _MscVsrActiveModemChannels_Type()
)
mscVsrActiveModemChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveModemChannels.setStatus("mandatory")
_MscVsrActiveDataChannels_Type = Counter32
_MscVsrActiveDataChannels_Object = MibTableColumn
mscVsrActiveDataChannels = _MscVsrActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 6),
    _MscVsrActiveDataChannels_Type()
)
mscVsrActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveDataChannels.setStatus("mandatory")
_MscVsrPeakActiveVoiceChannels_Type = Counter32
_MscVsrPeakActiveVoiceChannels_Object = MibTableColumn
mscVsrPeakActiveVoiceChannels = _MscVsrPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 7),
    _MscVsrPeakActiveVoiceChannels_Type()
)
mscVsrPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveVoiceChannels.setStatus("mandatory")
_MscVsrPeakActiveModemChannels_Type = Counter32
_MscVsrPeakActiveModemChannels_Object = MibTableColumn
mscVsrPeakActiveModemChannels = _MscVsrPeakActiveModemChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 8),
    _MscVsrPeakActiveModemChannels_Type()
)
mscVsrPeakActiveModemChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveModemChannels.setStatus("mandatory")
_MscVsrPeakActiveDataChannels_Type = Counter32
_MscVsrPeakActiveDataChannels_Object = MibTableColumn
mscVsrPeakActiveDataChannels = _MscVsrPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 9),
    _MscVsrPeakActiveDataChannels_Type()
)
mscVsrPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveDataChannels.setStatus("mandatory")


class _MscVsrActiveFaxRelayChannels_Type(Gauge32):
    """Custom type mscVsrActiveFaxRelayChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscVsrActiveFaxRelayChannels_Type.__name__ = "Gauge32"
_MscVsrActiveFaxRelayChannels_Object = MibTableColumn
mscVsrActiveFaxRelayChannels = _MscVsrActiveFaxRelayChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 10),
    _MscVsrActiveFaxRelayChannels_Type()
)
mscVsrActiveFaxRelayChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveFaxRelayChannels.setStatus("mandatory")


class _MscVsrActiveTptChannels_Type(Gauge32):
    """Custom type mscVsrActiveTptChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVsrActiveTptChannels_Type.__name__ = "Gauge32"
_MscVsrActiveTptChannels_Object = MibTableColumn
mscVsrActiveTptChannels = _MscVsrActiveTptChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 11),
    _MscVsrActiveTptChannels_Type()
)
mscVsrActiveTptChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrActiveTptChannels.setStatus("mandatory")


class _MscVsrPeakActiveFaxRelayChannels_Type(Gauge32):
    """Custom type mscVsrPeakActiveFaxRelayChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscVsrPeakActiveFaxRelayChannels_Type.__name__ = "Gauge32"
_MscVsrPeakActiveFaxRelayChannels_Object = MibTableColumn
mscVsrPeakActiveFaxRelayChannels = _MscVsrPeakActiveFaxRelayChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 12),
    _MscVsrPeakActiveFaxRelayChannels_Type()
)
mscVsrPeakActiveFaxRelayChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveFaxRelayChannels.setStatus("mandatory")


class _MscVsrPeakActiveTptChannels_Type(Gauge32):
    """Custom type mscVsrPeakActiveTptChannels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscVsrPeakActiveTptChannels_Type.__name__ = "Gauge32"
_MscVsrPeakActiveTptChannels_Object = MibTableColumn
mscVsrPeakActiveTptChannels = _MscVsrPeakActiveTptChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 117, 16, 1, 13),
    _MscVsrPeakActiveTptChannels_Type()
)
mscVsrPeakActiveTptChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVsrPeakActiveTptChannels.setStatus("mandatory")
_VoiceNetworkingMIB_ObjectIdentity = ObjectIdentity
voiceNetworkingMIB = _VoiceNetworkingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109)
)
_VoiceNetworkingGroup_ObjectIdentity = ObjectIdentity
voiceNetworkingGroup = _VoiceNetworkingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 1)
)
_VoiceNetworkingGroupCA_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupCA = _VoiceNetworkingGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 1, 1)
)
_VoiceNetworkingGroupCA02_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupCA02 = _VoiceNetworkingGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 1, 1, 3)
)
_VoiceNetworkingGroupCA02A_ObjectIdentity = ObjectIdentity
voiceNetworkingGroupCA02A = _VoiceNetworkingGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 1, 1, 3, 2)
)
_VoiceNetworkingCapabilities_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilities = _VoiceNetworkingCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 3)
)
_VoiceNetworkingCapabilitiesCA_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesCA = _VoiceNetworkingCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 3, 1)
)
_VoiceNetworkingCapabilitiesCA02_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesCA02 = _VoiceNetworkingCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 3, 1, 3)
)
_VoiceNetworkingCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
voiceNetworkingCapabilitiesCA02A = _VoiceNetworkingCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 109, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB",
    **{"mscSigChan": mscSigChan,
       "mscSigChanRowStatusTable": mscSigChanRowStatusTable,
       "mscSigChanRowStatusEntry": mscSigChanRowStatusEntry,
       "mscSigChanRowStatus": mscSigChanRowStatus,
       "mscSigChanComponentName": mscSigChanComponentName,
       "mscSigChanStorageType": mscSigChanStorageType,
       "mscSigChanIndex": mscSigChanIndex,
       "mscSigChanBch": mscSigChanBch,
       "mscSigChanBchRowStatusTable": mscSigChanBchRowStatusTable,
       "mscSigChanBchRowStatusEntry": mscSigChanBchRowStatusEntry,
       "mscSigChanBchRowStatus": mscSigChanBchRowStatus,
       "mscSigChanBchComponentName": mscSigChanBchComponentName,
       "mscSigChanBchStorageType": mscSigChanBchStorageType,
       "mscSigChanBchIndex": mscSigChanBchIndex,
       "mscSigChanBchOperTable": mscSigChanBchOperTable,
       "mscSigChanBchOperEntry": mscSigChanBchOperEntry,
       "mscSigChanBchStatus": mscSigChanBchStatus,
       "mscSigChanBchTimeSlot": mscSigChanBchTimeSlot,
       "mscSigChanBchVsrInstance": mscSigChanBchVsrInstance,
       "mscSigChanBchCalledDirectoryNumber": mscSigChanBchCalledDirectoryNumber,
       "mscSigChanGw": mscSigChanGw,
       "mscSigChanGwRowStatusTable": mscSigChanGwRowStatusTable,
       "mscSigChanGwRowStatusEntry": mscSigChanGwRowStatusEntry,
       "mscSigChanGwRowStatus": mscSigChanGwRowStatus,
       "mscSigChanGwComponentName": mscSigChanGwComponentName,
       "mscSigChanGwStorageType": mscSigChanGwStorageType,
       "mscSigChanGwIndex": mscSigChanGwIndex,
       "mscSigChanGwStatsTable": mscSigChanGwStatsTable,
       "mscSigChanGwStatsEntry": mscSigChanGwStatsEntry,
       "mscSigChanGwRequiredConversions": mscSigChanGwRequiredConversions,
       "mscSigChanGwUnsupportedConversions": mscSigChanGwUnsupportedConversions,
       "mscSigChanGwGwcTable": mscSigChanGwGwcTable,
       "mscSigChanGwGwcEntry": mscSigChanGwGwcEntry,
       "mscSigChanGwGwcIndex": mscSigChanGwGwcIndex,
       "mscSigChanGwGwcValue": mscSigChanGwGwcValue,
       "mscSigChanGwGatewayCapTable": mscSigChanGwGatewayCapTable,
       "mscSigChanGwGatewayCapEntry": mscSigChanGwGatewayCapEntry,
       "mscSigChanGwGatewayCapIndex": mscSigChanGwGatewayCapIndex,
       "mscSigChanGwGatewayCapValue": mscSigChanGwGatewayCapValue,
       "mscSigChanNcas": mscSigChanNcas,
       "mscSigChanNcasRowStatusTable": mscSigChanNcasRowStatusTable,
       "mscSigChanNcasRowStatusEntry": mscSigChanNcasRowStatusEntry,
       "mscSigChanNcasRowStatus": mscSigChanNcasRowStatus,
       "mscSigChanNcasComponentName": mscSigChanNcasComponentName,
       "mscSigChanNcasStorageType": mscSigChanNcasStorageType,
       "mscSigChanNcasIndex": mscSigChanNcasIndex,
       "mscSigChanNcasOperTable": mscSigChanNcasOperTable,
       "mscSigChanNcasOperEntry": mscSigChanNcasOperEntry,
       "mscSigChanNcasDirection": mscSigChanNcasDirection,
       "mscSigChanNcasCallReference": mscSigChanNcasCallReference,
       "mscSigChanNcasCalledDirectoryNumber": mscSigChanNcasCalledDirectoryNumber,
       "mscSigChanNcasDuration": mscSigChanNcasDuration,
       "mscSigChanICmap": mscSigChanICmap,
       "mscSigChanICmapRowStatusTable": mscSigChanICmapRowStatusTable,
       "mscSigChanICmapRowStatusEntry": mscSigChanICmapRowStatusEntry,
       "mscSigChanICmapRowStatus": mscSigChanICmapRowStatus,
       "mscSigChanICmapComponentName": mscSigChanICmapComponentName,
       "mscSigChanICmapStorageType": mscSigChanICmapStorageType,
       "mscSigChanICmapIndex": mscSigChanICmapIndex,
       "mscSigChanICmapIntCauseTable": mscSigChanICmapIntCauseTable,
       "mscSigChanICmapIntCauseEntry": mscSigChanICmapIntCauseEntry,
       "mscSigChanICmapEgressLinkOutOfServCause": mscSigChanICmapEgressLinkOutOfServCause,
       "mscSigChanICmapChanOrCircNotAvailCause": mscSigChanICmapChanOrCircNotAvailCause,
       "mscSigChanICmapTempFailureCause": mscSigChanICmapTempFailureCause,
       "mscSigChanICmapSwitchCongestCause": mscSigChanICmapSwitchCongestCause,
       "mscSigChanICmapReqChanOrCircNotAvailCause": mscSigChanICmapReqChanOrCircNotAvailCause,
       "mscSigChanICmapResourceUnavailCause": mscSigChanICmapResourceUnavailCause,
       "mscSigChanICmapServNotAllowedCause": mscSigChanICmapServNotAllowedCause,
       "mscSigChanICmapNoSuchChannelCause": mscSigChanICmapNoSuchChannelCause,
       "mscSigChanICmapIncompatDestCause": mscSigChanICmapIncompatDestCause,
       "mscSigChanCidDataTable": mscSigChanCidDataTable,
       "mscSigChanCidDataEntry": mscSigChanCidDataEntry,
       "mscSigChanCustomerIdentifier": mscSigChanCustomerIdentifier,
       "mscSigChanIfEntryTable": mscSigChanIfEntryTable,
       "mscSigChanIfEntryEntry": mscSigChanIfEntryEntry,
       "mscSigChanIfAdminStatus": mscSigChanIfAdminStatus,
       "mscSigChanIfIndex": mscSigChanIfIndex,
       "mscSigChanOperStatusTable": mscSigChanOperStatusTable,
       "mscSigChanOperStatusEntry": mscSigChanOperStatusEntry,
       "mscSigChanSnmpOperStatus": mscSigChanSnmpOperStatus,
       "mscSigChanStateTable": mscSigChanStateTable,
       "mscSigChanStateEntry": mscSigChanStateEntry,
       "mscSigChanAdminState": mscSigChanAdminState,
       "mscSigChanOperationalState": mscSigChanOperationalState,
       "mscSigChanUsageState": mscSigChanUsageState,
       "mscSigChanProvTable": mscSigChanProvTable,
       "mscSigChanProvEntry": mscSigChanProvEntry,
       "mscSigChanCommentText": mscSigChanCommentText,
       "mscSigChanOctothorpeEod": mscSigChanOctothorpeEod,
       "mscSigChanForceNpiTon": mscSigChanForceNpiTon,
       "mscSigChanDefaultNpiTon": mscSigChanDefaultNpiTon,
       "mscSigChanSubroutesTable": mscSigChanSubroutesTable,
       "mscSigChanSubroutesEntry": mscSigChanSubroutesEntry,
       "mscSigChanSubroutesValue": mscSigChanSubroutesValue,
       "mscSigChanSubroutesRowStatus": mscSigChanSubroutesRowStatus,
       "mscSigChanDegradedSubroutesTable": mscSigChanDegradedSubroutesTable,
       "mscSigChanDegradedSubroutesEntry": mscSigChanDegradedSubroutesEntry,
       "mscSigChanDegradedSubroutesValue": mscSigChanDegradedSubroutesValue,
       "mscVRoute": mscVRoute,
       "mscVRouteRowStatusTable": mscVRouteRowStatusTable,
       "mscVRouteRowStatusEntry": mscVRouteRowStatusEntry,
       "mscVRouteRowStatus": mscVRouteRowStatus,
       "mscVRouteComponentName": mscVRouteComponentName,
       "mscVRouteStorageType": mscVRouteStorageType,
       "mscVRouteIndex": mscVRouteIndex,
       "mscVRouteDebug": mscVRouteDebug,
       "mscVRouteDebugRowStatusTable": mscVRouteDebugRowStatusTable,
       "mscVRouteDebugRowStatusEntry": mscVRouteDebugRowStatusEntry,
       "mscVRouteDebugRowStatus": mscVRouteDebugRowStatus,
       "mscVRouteDebugComponentName": mscVRouteDebugComponentName,
       "mscVRouteDebugStorageType": mscVRouteDebugStorageType,
       "mscVRouteDebugIndex": mscVRouteDebugIndex,
       "mscVRouteInterface": mscVRouteInterface,
       "mscVRouteInterfaceRowStatusTable": mscVRouteInterfaceRowStatusTable,
       "mscVRouteInterfaceRowStatusEntry": mscVRouteInterfaceRowStatusEntry,
       "mscVRouteInterfaceRowStatus": mscVRouteInterfaceRowStatus,
       "mscVRouteInterfaceComponentName": mscVRouteInterfaceComponentName,
       "mscVRouteInterfaceStorageType": mscVRouteInterfaceStorageType,
       "mscVRouteInterfaceIndex": mscVRouteInterfaceIndex,
       "mscVRouteInterfaceProvTable": mscVRouteInterfaceProvTable,
       "mscVRouteInterfaceProvEntry": mscVRouteInterfaceProvEntry,
       "mscVRouteInterfaceIngressAudioGain": mscVRouteInterfaceIngressAudioGain,
       "mscVRouteInterfaceEgressAudioGain": mscVRouteInterfaceEgressAudioGain,
       "mscVRouteInterfaceTandemPassThrough": mscVRouteInterfaceTandemPassThrough,
       "mscVRouteInterfaceEchoCancellation": mscVRouteInterfaceEchoCancellation,
       "mscVRouteInterfaceComfortNoiseCap": mscVRouteInterfaceComfortNoiseCap,
       "mscVRouteInterfaceSpeechHangoverTime": mscVRouteInterfaceSpeechHangoverTime,
       "mscVRouteInterfaceFaxHangoverTimeG711G726": mscVRouteInterfaceFaxHangoverTimeG711G726,
       "mscVRouteInterfaceModemFaxSpeechDiscrim": mscVRouteInterfaceModemFaxSpeechDiscrim,
       "mscVRouteInterfaceEchoTailDelay": mscVRouteInterfaceEchoTailDelay,
       "mscVRouteInterfaceEchoReturnLoss": mscVRouteInterfaceEchoReturnLoss,
       "mscVRouteInterfaceEcanBypassMode": mscVRouteInterfaceEcanBypassMode,
       "mscVRouteInterfaceStructuredEchoCancellationTable": mscVRouteInterfaceStructuredEchoCancellationTable,
       "mscVRouteInterfaceStructuredEchoCancellationEntry": mscVRouteInterfaceStructuredEchoCancellationEntry,
       "mscVRouteInterfaceStructuredEchoCancellationIndex": mscVRouteInterfaceStructuredEchoCancellationIndex,
       "mscVRouteInterfaceStructuredEchoCancellationValue": mscVRouteInterfaceStructuredEchoCancellationValue,
       "mscVRouteDna": mscVRouteDna,
       "mscVRouteDnaRowStatusTable": mscVRouteDnaRowStatusTable,
       "mscVRouteDnaRowStatusEntry": mscVRouteDnaRowStatusEntry,
       "mscVRouteDnaRowStatus": mscVRouteDnaRowStatus,
       "mscVRouteDnaComponentName": mscVRouteDnaComponentName,
       "mscVRouteDnaStorageType": mscVRouteDnaStorageType,
       "mscVRouteDnaIndex": mscVRouteDnaIndex,
       "mscVRouteDnaAddressTable": mscVRouteDnaAddressTable,
       "mscVRouteDnaAddressEntry": mscVRouteDnaAddressEntry,
       "mscVRouteDnaNumberingPlanIndicator": mscVRouteDnaNumberingPlanIndicator,
       "mscVRouteDnaDataNetworkAddress": mscVRouteDnaDataNetworkAddress,
       "mscVRouteAcct": mscVRouteAcct,
       "mscVRouteAcctRowStatusTable": mscVRouteAcctRowStatusTable,
       "mscVRouteAcctRowStatusEntry": mscVRouteAcctRowStatusEntry,
       "mscVRouteAcctRowStatus": mscVRouteAcctRowStatus,
       "mscVRouteAcctComponentName": mscVRouteAcctComponentName,
       "mscVRouteAcctStorageType": mscVRouteAcctStorageType,
       "mscVRouteAcctIndex": mscVRouteAcctIndex,
       "mscVRouteAcctProvTable": mscVRouteAcctProvTable,
       "mscVRouteAcctProvEntry": mscVRouteAcctProvEntry,
       "mscVRouteAcctAccountCollection": mscVRouteAcctAccountCollection,
       "mscVRouteAcctAccountClass": mscVRouteAcctAccountClass,
       "mscVRouteAcctServiceExchange": mscVRouteAcctServiceExchange,
       "mscVRouteAcctDigitsSuppressed": mscVRouteAcctDigitsSuppressed,
       "mscVRouteAcctAccountingOptions": mscVRouteAcctAccountingOptions,
       "mscVRouteProvTable": mscVRouteProvTable,
       "mscVRouteProvEntry": mscVRouteProvEntry,
       "mscVRouteCommentText": mscVRouteCommentText,
       "mscVRouteTypeOfRoute": mscVRouteTypeOfRoute,
       "mscVRouteDiallingPlan0": mscVRouteDiallingPlan0,
       "mscVRouteDiallingPlan1": mscVRouteDiallingPlan1,
       "mscVRouteDiallingPlan2": mscVRouteDiallingPlan2,
       "mscVRouteHuntingAlgorithm": mscVRouteHuntingAlgorithm,
       "mscVRouteMinimumDigitsToRoute": mscVRouteMinimumDigitsToRoute,
       "mscVRouteVoiceNetworkingCallServer": mscVRouteVoiceNetworkingCallServer,
       "mscVRouteOverrideDirectoryNumber": mscVRouteOverrideDirectoryNumber,
       "mscVRoutePrivateNetworkIdentifer": mscVRoutePrivateNetworkIdentifer,
       "mscVRouteCidDataTable": mscVRouteCidDataTable,
       "mscVRouteCidDataEntry": mscVRouteCidDataEntry,
       "mscVRouteCustomerIdentifier": mscVRouteCustomerIdentifier,
       "mscVRouteIfEntryTable": mscVRouteIfEntryTable,
       "mscVRouteIfEntryEntry": mscVRouteIfEntryEntry,
       "mscVRouteIfAdminStatus": mscVRouteIfAdminStatus,
       "mscVRouteIfIndex": mscVRouteIfIndex,
       "mscVRouteStateTable": mscVRouteStateTable,
       "mscVRouteStateEntry": mscVRouteStateEntry,
       "mscVRouteAdminState": mscVRouteAdminState,
       "mscVRouteOperationalState": mscVRouteOperationalState,
       "mscVRouteUsageState": mscVRouteUsageState,
       "mscVRouteOperStatusTable": mscVRouteOperStatusTable,
       "mscVRouteOperStatusEntry": mscVRouteOperStatusEntry,
       "mscVRouteSnmpOperStatus": mscVRouteSnmpOperStatus,
       "mscVRouteStatsTable": mscVRouteStatsTable,
       "mscVRouteStatsEntry": mscVRouteStatsEntry,
       "mscVRouteTotalCallsFromSubnet": mscVRouteTotalCallsFromSubnet,
       "mscVRouteCallsClearedNoChannel": mscVRouteCallsClearedNoChannel,
       "mscVRouteCallsClearedOutOfService": mscVRouteCallsClearedOutOfService,
       "mscVRouteCallsRejected": mscVRouteCallsRejected,
       "mscVRouteSubroutesTable": mscVRouteSubroutesTable,
       "mscVRouteSubroutesEntry": mscVRouteSubroutesEntry,
       "mscVRouteSubroutesValue": mscVRouteSubroutesValue,
       "mscVRouteSubroutesRowStatus": mscVRouteSubroutesRowStatus,
       "mscVRouteDegradedSubroutesTable": mscVRouteDegradedSubroutesTable,
       "mscVRouteDegradedSubroutesEntry": mscVRouteDegradedSubroutesEntry,
       "mscVRouteDegradedSubroutesValue": mscVRouteDegradedSubroutesValue,
       "mscVsr": mscVsr,
       "mscVsrRowStatusTable": mscVsrRowStatusTable,
       "mscVsrRowStatusEntry": mscVsrRowStatusEntry,
       "mscVsrRowStatus": mscVsrRowStatus,
       "mscVsrComponentName": mscVsrComponentName,
       "mscVsrStorageType": mscVsrStorageType,
       "mscVsrIndex": mscVsrIndex,
       "mscVsrSvs": mscVsrSvs,
       "mscVsrSvsRowStatusTable": mscVsrSvsRowStatusTable,
       "mscVsrSvsRowStatusEntry": mscVsrSvsRowStatusEntry,
       "mscVsrSvsRowStatus": mscVsrSvsRowStatus,
       "mscVsrSvsComponentName": mscVsrSvsComponentName,
       "mscVsrSvsStorageType": mscVsrSvsStorageType,
       "mscVsrSvsIndex": mscVsrSvsIndex,
       "mscVsrSvsFramer": mscVsrSvsFramer,
       "mscVsrSvsFramerRowStatusTable": mscVsrSvsFramerRowStatusTable,
       "mscVsrSvsFramerRowStatusEntry": mscVsrSvsFramerRowStatusEntry,
       "mscVsrSvsFramerRowStatus": mscVsrSvsFramerRowStatus,
       "mscVsrSvsFramerComponentName": mscVsrSvsFramerComponentName,
       "mscVsrSvsFramerStorageType": mscVsrSvsFramerStorageType,
       "mscVsrSvsFramerIndex": mscVsrSvsFramerIndex,
       "mscVsrSvsFramerVfpDebug": mscVsrSvsFramerVfpDebug,
       "mscVsrSvsFramerVfpDebugRowStatusTable": mscVsrSvsFramerVfpDebugRowStatusTable,
       "mscVsrSvsFramerVfpDebugRowStatusEntry": mscVsrSvsFramerVfpDebugRowStatusEntry,
       "mscVsrSvsFramerVfpDebugRowStatus": mscVsrSvsFramerVfpDebugRowStatus,
       "mscVsrSvsFramerVfpDebugComponentName": mscVsrSvsFramerVfpDebugComponentName,
       "mscVsrSvsFramerVfpDebugStorageType": mscVsrSvsFramerVfpDebugStorageType,
       "mscVsrSvsFramerVfpDebugIndex": mscVsrSvsFramerVfpDebugIndex,
       "mscVsrSvsFramerMvpDebug": mscVsrSvsFramerMvpDebug,
       "mscVsrSvsFramerMvpDebugRowStatusTable": mscVsrSvsFramerMvpDebugRowStatusTable,
       "mscVsrSvsFramerMvpDebugRowStatusEntry": mscVsrSvsFramerMvpDebugRowStatusEntry,
       "mscVsrSvsFramerMvpDebugRowStatus": mscVsrSvsFramerMvpDebugRowStatus,
       "mscVsrSvsFramerMvpDebugComponentName": mscVsrSvsFramerMvpDebugComponentName,
       "mscVsrSvsFramerMvpDebugStorageType": mscVsrSvsFramerMvpDebugStorageType,
       "mscVsrSvsFramerMvpDebugIndex": mscVsrSvsFramerMvpDebugIndex,
       "mscVsrSvsFramerPcmCapture": mscVsrSvsFramerPcmCapture,
       "mscVsrSvsFramerPcmCaptureRowStatusTable": mscVsrSvsFramerPcmCaptureRowStatusTable,
       "mscVsrSvsFramerPcmCaptureRowStatusEntry": mscVsrSvsFramerPcmCaptureRowStatusEntry,
       "mscVsrSvsFramerPcmCaptureRowStatus": mscVsrSvsFramerPcmCaptureRowStatus,
       "mscVsrSvsFramerPcmCaptureComponentName": mscVsrSvsFramerPcmCaptureComponentName,
       "mscVsrSvsFramerPcmCaptureStorageType": mscVsrSvsFramerPcmCaptureStorageType,
       "mscVsrSvsFramerPcmCaptureIndex": mscVsrSvsFramerPcmCaptureIndex,
       "mscVsrSvsFramerProvTable": mscVsrSvsFramerProvTable,
       "mscVsrSvsFramerProvEntry": mscVsrSvsFramerProvEntry,
       "mscVsrSvsFramerInterfaceName": mscVsrSvsFramerInterfaceName,
       "mscVsrSvsFramerStateTable": mscVsrSvsFramerStateTable,
       "mscVsrSvsFramerStateEntry": mscVsrSvsFramerStateEntry,
       "mscVsrSvsFramerAdminState": mscVsrSvsFramerAdminState,
       "mscVsrSvsFramerOperationalState": mscVsrSvsFramerOperationalState,
       "mscVsrSvsFramerUsageState": mscVsrSvsFramerUsageState,
       "mscVsrSvsFramerStatsTable": mscVsrSvsFramerStatsTable,
       "mscVsrSvsFramerStatsEntry": mscVsrSvsFramerStatsEntry,
       "mscVsrSvsFramerTotalCells": mscVsrSvsFramerTotalCells,
       "mscVsrSvsFramerAudioCells": mscVsrSvsFramerAudioCells,
       "mscVsrSvsFramerSilenceCells": mscVsrSvsFramerSilenceCells,
       "mscVsrSvsFramerModemCells": mscVsrSvsFramerModemCells,
       "mscVsrSvsFramerCurrentEncodingRate": mscVsrSvsFramerCurrentEncodingRate,
       "mscVsrSvsFramerLrcErrors": mscVsrSvsFramerLrcErrors,
       "mscVsrSvsFramerFrmLostInNetwork": mscVsrSvsFramerFrmLostInNetwork,
       "mscVsrSvsFramerFrmUnderRuns": mscVsrSvsFramerFrmUnderRuns,
       "mscVsrSvsFramerFrmDumped": mscVsrSvsFramerFrmDumped,
       "mscVsrSvsFramerModemSilenceCells": mscVsrSvsFramerModemSilenceCells,
       "mscVsrSvsFramerCurrentEncoding": mscVsrSvsFramerCurrentEncoding,
       "mscVsrSvsFramerTptStatus": mscVsrSvsFramerTptStatus,
       "mscVsrSvsFramerFaxRelayCells": mscVsrSvsFramerFaxRelayCells,
       "mscVsrSvsFramerModemFaxCells": mscVsrSvsFramerModemFaxCells,
       "mscVsrSvsFramerFaxIdleCells": mscVsrSvsFramerFaxIdleCells,
       "mscVsrSvsFramerOperTable": mscVsrSvsFramerOperTable,
       "mscVsrSvsFramerOperEntry": mscVsrSvsFramerOperEntry,
       "mscVsrSvsFramerOpCurrentEncoding": mscVsrSvsFramerOpCurrentEncoding,
       "mscVsrSvsFramerCurrentRate": mscVsrSvsFramerCurrentRate,
       "mscVsrSvsFramerOpTptStatus": mscVsrSvsFramerOpTptStatus,
       "mscVsrSvsFramerNegTable": mscVsrSvsFramerNegTable,
       "mscVsrSvsFramerNegEntry": mscVsrSvsFramerNegEntry,
       "mscVsrSvsFramerNegotiatedSilenceSuppression": mscVsrSvsFramerNegotiatedSilenceSuppression,
       "mscVsrSvsFramerNegotiatedFisG711G726": mscVsrSvsFramerNegotiatedFisG711G726,
       "mscVsrSvsFramerNegotiatedDtmfRegeneration": mscVsrSvsFramerNegotiatedDtmfRegeneration,
       "mscVsrSvsFramerNegotiatedV17AsG711G726": mscVsrSvsFramerNegotiatedV17AsG711G726,
       "mscVsrSvsFramerNegotiatedTandemPassThrough": mscVsrSvsFramerNegotiatedTandemPassThrough,
       "mscVsrSvsFramerFrmToNetworkTable": mscVsrSvsFramerFrmToNetworkTable,
       "mscVsrSvsFramerFrmToNetworkEntry": mscVsrSvsFramerFrmToNetworkEntry,
       "mscVsrSvsFramerFrmToNetworkIndex": mscVsrSvsFramerFrmToNetworkIndex,
       "mscVsrSvsFramerFrmToNetworkValue": mscVsrSvsFramerFrmToNetworkValue,
       "mscVsrSvsFramerFrmFromNetworkTable": mscVsrSvsFramerFrmFromNetworkTable,
       "mscVsrSvsFramerFrmFromNetworkEntry": mscVsrSvsFramerFrmFromNetworkEntry,
       "mscVsrSvsFramerFrmFromNetworkIndex": mscVsrSvsFramerFrmFromNetworkIndex,
       "mscVsrSvsFramerFrmFromNetworkValue": mscVsrSvsFramerFrmFromNetworkValue,
       "mscVsrSvsFramerNEncodingTable": mscVsrSvsFramerNEncodingTable,
       "mscVsrSvsFramerNEncodingEntry": mscVsrSvsFramerNEncodingEntry,
       "mscVsrSvsFramerNEncodingIndex": mscVsrSvsFramerNEncodingIndex,
       "mscVsrSvsFramerNEncodingValue": mscVsrSvsFramerNEncodingValue,
       "mscVsrSvsFramerNRatesTable": mscVsrSvsFramerNRatesTable,
       "mscVsrSvsFramerNRatesEntry": mscVsrSvsFramerNRatesEntry,
       "mscVsrSvsFramerNRatesTrafficIndex": mscVsrSvsFramerNRatesTrafficIndex,
       "mscVsrSvsFramerNRatesRateIndex": mscVsrSvsFramerNRatesRateIndex,
       "mscVsrSvsFramerNRatesValue": mscVsrSvsFramerNRatesValue,
       "mscVsrSvsLCo": mscVsrSvsLCo,
       "mscVsrSvsLCoRowStatusTable": mscVsrSvsLCoRowStatusTable,
       "mscVsrSvsLCoRowStatusEntry": mscVsrSvsLCoRowStatusEntry,
       "mscVsrSvsLCoRowStatus": mscVsrSvsLCoRowStatus,
       "mscVsrSvsLCoComponentName": mscVsrSvsLCoComponentName,
       "mscVsrSvsLCoStorageType": mscVsrSvsLCoStorageType,
       "mscVsrSvsLCoIndex": mscVsrSvsLCoIndex,
       "mscVsrSvsLCoPathDataTable": mscVsrSvsLCoPathDataTable,
       "mscVsrSvsLCoPathDataEntry": mscVsrSvsLCoPathDataEntry,
       "mscVsrSvsLCoState": mscVsrSvsLCoState,
       "mscVsrSvsLCoOverrideRemoteName": mscVsrSvsLCoOverrideRemoteName,
       "mscVsrSvsLCoEnd": mscVsrSvsLCoEnd,
       "mscVsrSvsLCoCostMetric": mscVsrSvsLCoCostMetric,
       "mscVsrSvsLCoDelayMetric": mscVsrSvsLCoDelayMetric,
       "mscVsrSvsLCoRoundTripDelay": mscVsrSvsLCoRoundTripDelay,
       "mscVsrSvsLCoSetupPriority": mscVsrSvsLCoSetupPriority,
       "mscVsrSvsLCoHoldingPriority": mscVsrSvsLCoHoldingPriority,
       "mscVsrSvsLCoRequiredTxBandwidth": mscVsrSvsLCoRequiredTxBandwidth,
       "mscVsrSvsLCoRequiredRxBandwidth": mscVsrSvsLCoRequiredRxBandwidth,
       "mscVsrSvsLCoRequiredTrafficType": mscVsrSvsLCoRequiredTrafficType,
       "mscVsrSvsLCoPermittedTrunkTypes": mscVsrSvsLCoPermittedTrunkTypes,
       "mscVsrSvsLCoRequiredSecurity": mscVsrSvsLCoRequiredSecurity,
       "mscVsrSvsLCoRequiredCustomerParameter": mscVsrSvsLCoRequiredCustomerParameter,
       "mscVsrSvsLCoEmissionPriority": mscVsrSvsLCoEmissionPriority,
       "mscVsrSvsLCoDiscardPriority": mscVsrSvsLCoDiscardPriority,
       "mscVsrSvsLCoPathType": mscVsrSvsLCoPathType,
       "mscVsrSvsLCoRetryCount": mscVsrSvsLCoRetryCount,
       "mscVsrSvsLCoPathFailureCount": mscVsrSvsLCoPathFailureCount,
       "mscVsrSvsLCoReasonForNoRoute": mscVsrSvsLCoReasonForNoRoute,
       "mscVsrSvsLCoLastTearDownReason": mscVsrSvsLCoLastTearDownReason,
       "mscVsrSvsLCoPathFailureAction": mscVsrSvsLCoPathFailureAction,
       "mscVsrSvsLCoBumpPreference": mscVsrSvsLCoBumpPreference,
       "mscVsrSvsLCoOptimization": mscVsrSvsLCoOptimization,
       "mscVsrSvsLCoPathUpDateTime": mscVsrSvsLCoPathUpDateTime,
       "mscVsrSvsLCoStatsTable": mscVsrSvsLCoStatsTable,
       "mscVsrSvsLCoStatsEntry": mscVsrSvsLCoStatsEntry,
       "mscVsrSvsLCoPktsToNetwork": mscVsrSvsLCoPktsToNetwork,
       "mscVsrSvsLCoBytesToNetwork": mscVsrSvsLCoBytesToNetwork,
       "mscVsrSvsLCoPktsFromNetwork": mscVsrSvsLCoPktsFromNetwork,
       "mscVsrSvsLCoBytesFromNetwork": mscVsrSvsLCoBytesFromNetwork,
       "mscVsrSvsLCoPathTable": mscVsrSvsLCoPathTable,
       "mscVsrSvsLCoPathEntry": mscVsrSvsLCoPathEntry,
       "mscVsrSvsLCoPathValue": mscVsrSvsLCoPathValue,
       "mscVsrSvsDebug": mscVsrSvsDebug,
       "mscVsrSvsDebugRowStatusTable": mscVsrSvsDebugRowStatusTable,
       "mscVsrSvsDebugRowStatusEntry": mscVsrSvsDebugRowStatusEntry,
       "mscVsrSvsDebugRowStatus": mscVsrSvsDebugRowStatus,
       "mscVsrSvsDebugComponentName": mscVsrSvsDebugComponentName,
       "mscVsrSvsDebugStorageType": mscVsrSvsDebugStorageType,
       "mscVsrSvsDebugIndex": mscVsrSvsDebugIndex,
       "mscVsrSvsIfEntryTable": mscVsrSvsIfEntryTable,
       "mscVsrSvsIfEntryEntry": mscVsrSvsIfEntryEntry,
       "mscVsrSvsIfAdminStatus": mscVsrSvsIfAdminStatus,
       "mscVsrSvsIfIndex": mscVsrSvsIfIndex,
       "mscVsrSvsOperTable": mscVsrSvsOperTable,
       "mscVsrSvsOperEntry": mscVsrSvsOperEntry,
       "mscVsrSvsStatus": mscVsrSvsStatus,
       "mscVsrSvsProfileNumber": mscVsrSvsProfileNumber,
       "mscVsrSvsCallType": mscVsrSvsCallType,
       "mscVsrSvsCalledNumber": mscVsrSvsCalledNumber,
       "mscVsrSvsCallingNumber": mscVsrSvsCallingNumber,
       "mscVsrSvsClearCauseCode": mscVsrSvsClearCauseCode,
       "mscVsrSvsStatsTable": mscVsrSvsStatsTable,
       "mscVsrSvsStatsEntry": mscVsrSvsStatsEntry,
       "mscVsrSvsTotalCalls": mscVsrSvsTotalCalls,
       "mscVsrSvsTotalCallSeconds": mscVsrSvsTotalCallSeconds,
       "mscVsrSvsStateTable": mscVsrSvsStateTable,
       "mscVsrSvsStateEntry": mscVsrSvsStateEntry,
       "mscVsrSvsAdminState": mscVsrSvsAdminState,
       "mscVsrSvsOperationalState": mscVsrSvsOperationalState,
       "mscVsrSvsUsageState": mscVsrSvsUsageState,
       "mscVsrSvsOperStatusTable": mscVsrSvsOperStatusTable,
       "mscVsrSvsOperStatusEntry": mscVsrSvsOperStatusEntry,
       "mscVsrSvsSnmpOperStatus": mscVsrSvsSnmpOperStatus,
       "mscVsrDebug": mscVsrDebug,
       "mscVsrDebugRowStatusTable": mscVsrDebugRowStatusTable,
       "mscVsrDebugRowStatusEntry": mscVsrDebugRowStatusEntry,
       "mscVsrDebugRowStatus": mscVsrDebugRowStatus,
       "mscVsrDebugComponentName": mscVsrDebugComponentName,
       "mscVsrDebugStorageType": mscVsrDebugStorageType,
       "mscVsrDebugIndex": mscVsrDebugIndex,
       "mscVsrCidDataTable": mscVsrCidDataTable,
       "mscVsrCidDataEntry": mscVsrCidDataEntry,
       "mscVsrCustomerIdentifier": mscVsrCustomerIdentifier,
       "mscVsrIfEntryTable": mscVsrIfEntryTable,
       "mscVsrIfEntryEntry": mscVsrIfEntryEntry,
       "mscVsrIfAdminStatus": mscVsrIfAdminStatus,
       "mscVsrIfIndex": mscVsrIfIndex,
       "mscVsrProvTable": mscVsrProvTable,
       "mscVsrProvEntry": mscVsrProvEntry,
       "mscVsrCommentText": mscVsrCommentText,
       "mscVsrVoiceRoute": mscVsrVoiceRoute,
       "mscVsrSignallingChannel": mscVsrSignallingChannel,
       "mscVsrStateTable": mscVsrStateTable,
       "mscVsrStateEntry": mscVsrStateEntry,
       "mscVsrAdminState": mscVsrAdminState,
       "mscVsrOperationalState": mscVsrOperationalState,
       "mscVsrUsageState": mscVsrUsageState,
       "mscVsrOperStatusTable": mscVsrOperStatusTable,
       "mscVsrOperStatusEntry": mscVsrOperStatusEntry,
       "mscVsrSnmpOperStatus": mscVsrSnmpOperStatus,
       "mscVsrStatsTable": mscVsrStatsTable,
       "mscVsrStatsEntry": mscVsrStatsEntry,
       "mscVsrTotalCallsFromIf": mscVsrTotalCallsFromIf,
       "mscVsrTotalFailedCallsFromIf": mscVsrTotalFailedCallsFromIf,
       "mscVsrInvalidNumberingPlanCalls": mscVsrInvalidNumberingPlanCalls,
       "mscVsrAddressResolutionFailedCalls": mscVsrAddressResolutionFailedCalls,
       "mscVsrAddressIncompleteCalls": mscVsrAddressIncompleteCalls,
       "mscVsrPathAttributesNotMetCalls": mscVsrPathAttributesNotMetCalls,
       "mscVsrPathSetupTimeOutCalls": mscVsrPathSetupTimeOutCalls,
       "mscVsrCallsRejectedLocally": mscVsrCallsRejectedLocally,
       "mscVsrCallsRejectedByFarEnd": mscVsrCallsRejectedByFarEnd,
       "mscVsrOperTable": mscVsrOperTable,
       "mscVsrOperEntry": mscVsrOperEntry,
       "mscVsrActiveChannels": mscVsrActiveChannels,
       "mscVsrPeakActiveChannels": mscVsrPeakActiveChannels,
       "mscVsrActiveVoiceChannels": mscVsrActiveVoiceChannels,
       "mscVsrActiveModemChannels": mscVsrActiveModemChannels,
       "mscVsrActiveDataChannels": mscVsrActiveDataChannels,
       "mscVsrPeakActiveVoiceChannels": mscVsrPeakActiveVoiceChannels,
       "mscVsrPeakActiveModemChannels": mscVsrPeakActiveModemChannels,
       "mscVsrPeakActiveDataChannels": mscVsrPeakActiveDataChannels,
       "mscVsrActiveFaxRelayChannels": mscVsrActiveFaxRelayChannels,
       "mscVsrActiveTptChannels": mscVsrActiveTptChannels,
       "mscVsrPeakActiveFaxRelayChannels": mscVsrPeakActiveFaxRelayChannels,
       "mscVsrPeakActiveTptChannels": mscVsrPeakActiveTptChannels,
       "voiceNetworkingMIB": voiceNetworkingMIB,
       "voiceNetworkingGroup": voiceNetworkingGroup,
       "voiceNetworkingGroupCA": voiceNetworkingGroupCA,
       "voiceNetworkingGroupCA02": voiceNetworkingGroupCA02,
       "voiceNetworkingGroupCA02A": voiceNetworkingGroupCA02A,
       "voiceNetworkingCapabilities": voiceNetworkingCapabilities,
       "voiceNetworkingCapabilitiesCA": voiceNetworkingCapabilitiesCA,
       "voiceNetworkingCapabilitiesCA02": voiceNetworkingCapabilitiesCA02,
       "voiceNetworkingCapabilitiesCA02A": voiceNetworkingCapabilitiesCA02A}
)
