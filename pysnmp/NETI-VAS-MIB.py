# SNMP MIB module (NETI-VAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-VAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:37 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netiVasMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5)
)
netiVasMIB.setRevisions(
        ("2015-04-20 07:00",
         "2015-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VasConnectionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("connecting", 1),
          ("offline", 0),
          ("reconnecting", 2),
          ("unknown", 9))
    )



class VasCipher(Integer32, TextualConvention):
    status = "current"
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
        *(("aes128", 1),
          ("aes192", 2),
          ("aes256", 3),
          ("none", 0))
    )



class VasResetStatistics(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )



class VasVideoFormat(Integer32, TextualConvention):
    status = "current"
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("fmt1080i50", 19),
          ("fmt1080i59", 20),
          ("fmt1080i60", 21),
          ("fmt1080p23", 11),
          ("fmt1080p24", 12),
          ("fmt1080p25", 13),
          ("fmt1080p29", 14),
          ("fmt1080p30", 15),
          ("fmt1080p50", 16),
          ("fmt1080p59", 17),
          ("fmt1080p60", 18),
          ("fmt525i59", 1),
          ("fmt625i50", 2),
          ("fmt720p23", 3),
          ("fmt720p24", 4),
          ("fmt720p25", 5),
          ("fmt720p29", 6),
          ("fmt720p30", 7),
          ("fmt720p50", 8),
          ("fmt720p59", 9),
          ("fmt720p60", 10),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Netinsight_ObjectIdentity = ObjectIdentity
netinsight = _Netinsight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928)
)
_NetiGeneric_ObjectIdentity = ObjectIdentity
netiGeneric = _NetiGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2)
)
_VasInterfaceGroup_ObjectIdentity = ObjectIdentity
vasInterfaceGroup = _VasInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1)
)
_VasIfTable_Object = MibTable
vasIfTable = _VasIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    vasIfTable.setStatus("current")
_VasIfEntry_Object = MibTableRow
vasIfEntry = _VasIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1)
)
vasIfEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasIfIndex"),
)
if mibBuilder.loadTexts:
    vasIfEntry.setStatus("current")
_VasIfIndex_Type = Unsigned32
_VasIfIndex_Object = MibTableColumn
vasIfIndex = _VasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 1),
    _VasIfIndex_Type()
)
vasIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasIfIndex.setStatus("current")
_VasIfName_Type = SnmpAdminString
_VasIfName_Object = MibTableColumn
vasIfName = _VasIfName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 2),
    _VasIfName_Type()
)
vasIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasIfName.setStatus("current")


class _VasIfPurpose_Type(SnmpAdminString):
    """Custom type vasIfPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasIfPurpose_Object = MibTableColumn
vasIfPurpose = _VasIfPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 3),
    _VasIfPurpose_Type()
)
vasIfPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasIfPurpose.setStatus("current")


class _VasIfAdminStatus_Type(Integer32):
    """Custom type vasIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasIfAdminStatus_Type.__name__ = "Integer32"
_VasIfAdminStatus_Object = MibTableColumn
vasIfAdminStatus = _VasIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 4),
    _VasIfAdminStatus_Type()
)
vasIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasIfAdminStatus.setStatus("current")


class _VasIfOperStatus_Type(Integer32):
    """Custom type vasIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasIfOperStatus_Type.__name__ = "Integer32"
_VasIfOperStatus_Object = MibTableColumn
vasIfOperStatus = _VasIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 5),
    _VasIfOperStatus_Type()
)
vasIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasIfOperStatus.setStatus("current")
_VasIfFailure_Type = SnmpAdminString
_VasIfFailure_Object = MibTableColumn
vasIfFailure = _VasIfFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 6),
    _VasIfFailure_Type()
)
vasIfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasIfFailure.setStatus("current")
_VasIfLastChanged_Type = TimeStamp
_VasIfLastChanged_Object = MibTableColumn
vasIfLastChanged = _VasIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 7),
    _VasIfLastChanged_Type()
)
vasIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasIfLastChanged.setStatus("current")
_VasIfResetStatistics_Type = VasResetStatistics
_VasIfResetStatistics_Object = MibTableColumn
vasIfResetStatistics = _VasIfResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 8),
    _VasIfResetStatistics_Type()
)
vasIfResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasIfResetStatistics.setStatus("current")
_VasIfInputFrom_Type = RowPointer
_VasIfInputFrom_Object = MibTableColumn
vasIfInputFrom = _VasIfInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 9),
    _VasIfInputFrom_Type()
)
vasIfInputFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasIfInputFrom.setStatus("current")


class _VasIfPortMode_Type(Integer32):
    """Custom type vasIfPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asiInput", 1),
          ("asiOutput", 2),
          ("sdiInput", 3),
          ("sdiOutput", 4))
    )


_VasIfPortMode_Type.__name__ = "Integer32"
_VasIfPortMode_Object = MibTableColumn
vasIfPortMode = _VasIfPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 10),
    _VasIfPortMode_Type()
)
vasIfPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasIfPortMode.setStatus("current")
_VasIfActiveFormat_Type = VasVideoFormat
_VasIfActiveFormat_Object = MibTableColumn
vasIfActiveFormat = _VasIfActiveFormat_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 1, 1, 1, 11),
    _VasIfActiveFormat_Type()
)
vasIfActiveFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasIfActiveFormat.setStatus("current")
_VasEncoderPipeGroup_ObjectIdentity = ObjectIdentity
vasEncoderPipeGroup = _VasEncoderPipeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2)
)
_VasEncPipeTable_Object = MibTable
vasEncPipeTable = _VasEncPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vasEncPipeTable.setStatus("current")
_VasEncPipeEntry_Object = MibTableRow
vasEncPipeEntry = _VasEncPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1)
)
vasEncPipeEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasEncPipeIndex"),
)
if mibBuilder.loadTexts:
    vasEncPipeEntry.setStatus("current")
_VasEncPipeIndex_Type = Unsigned32
_VasEncPipeIndex_Object = MibTableColumn
vasEncPipeIndex = _VasEncPipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 1),
    _VasEncPipeIndex_Type()
)
vasEncPipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasEncPipeIndex.setStatus("current")
_VasEncPipeRowStatus_Type = RowStatus
_VasEncPipeRowStatus_Object = MibTableColumn
vasEncPipeRowStatus = _VasEncPipeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 2),
    _VasEncPipeRowStatus_Type()
)
vasEncPipeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeRowStatus.setStatus("current")
_VasEncPipeName_Type = SnmpAdminString
_VasEncPipeName_Object = MibTableColumn
vasEncPipeName = _VasEncPipeName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 3),
    _VasEncPipeName_Type()
)
vasEncPipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeName.setStatus("current")


class _VasEncPipePurpose_Type(SnmpAdminString):
    """Custom type vasEncPipePurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasEncPipePurpose_Object = MibTableColumn
vasEncPipePurpose = _VasEncPipePurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 4),
    _VasEncPipePurpose_Type()
)
vasEncPipePurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipePurpose.setStatus("current")


class _VasEncPipeAdminStatus_Type(Integer32):
    """Custom type vasEncPipeAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasEncPipeAdminStatus_Type.__name__ = "Integer32"
_VasEncPipeAdminStatus_Object = MibTableColumn
vasEncPipeAdminStatus = _VasEncPipeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 5),
    _VasEncPipeAdminStatus_Type()
)
vasEncPipeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeAdminStatus.setStatus("current")


class _VasEncPipeOperStatus_Type(Integer32):
    """Custom type vasEncPipeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasEncPipeOperStatus_Type.__name__ = "Integer32"
_VasEncPipeOperStatus_Object = MibTableColumn
vasEncPipeOperStatus = _VasEncPipeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 6),
    _VasEncPipeOperStatus_Type()
)
vasEncPipeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeOperStatus.setStatus("current")
_VasEncPipeFailure_Type = SnmpAdminString
_VasEncPipeFailure_Object = MibTableColumn
vasEncPipeFailure = _VasEncPipeFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 7),
    _VasEncPipeFailure_Type()
)
vasEncPipeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeFailure.setStatus("current")
_VasEncPipeLastChanged_Type = TimeStamp
_VasEncPipeLastChanged_Object = MibTableColumn
vasEncPipeLastChanged = _VasEncPipeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 8),
    _VasEncPipeLastChanged_Type()
)
vasEncPipeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeLastChanged.setStatus("current")
_VasEncPipeResetStatistics_Type = VasResetStatistics
_VasEncPipeResetStatistics_Object = MibTableColumn
vasEncPipeResetStatistics = _VasEncPipeResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 9),
    _VasEncPipeResetStatistics_Type()
)
vasEncPipeResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasEncPipeResetStatistics.setStatus("current")
_VasEncPipeStatsTr101_Type = Unsigned32
_VasEncPipeStatsTr101_Object = MibTableColumn
vasEncPipeStatsTr101 = _VasEncPipeStatsTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 10),
    _VasEncPipeStatsTr101_Type()
)
vasEncPipeStatsTr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeStatsTr101.setStatus("current")


class _VasEncPipeEnableTr101_Type(TruthValue):
    """Custom type vasEncPipeEnableTr101 based on TruthValue"""


_VasEncPipeEnableTr101_Object = MibTableColumn
vasEncPipeEnableTr101 = _VasEncPipeEnableTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 11),
    _VasEncPipeEnableTr101_Type()
)
vasEncPipeEnableTr101.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeEnableTr101.setStatus("current")
_VasEncPipeInputFrom_Type = RowPointer
_VasEncPipeInputFrom_Object = MibTableColumn
vasEncPipeInputFrom = _VasEncPipeInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 12),
    _VasEncPipeInputFrom_Type()
)
vasEncPipeInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeInputFrom.setStatus("current")


class _VasEncPipeCipher_Type(VasCipher):
    """Custom type vasEncPipeCipher based on VasCipher"""


_VasEncPipeCipher_Object = MibTableColumn
vasEncPipeCipher = _VasEncPipeCipher_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 13),
    _VasEncPipeCipher_Type()
)
vasEncPipeCipher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeCipher.setStatus("current")


class _VasEncPipeEncryptKey_Type(SnmpAdminString):
    """Custom type vasEncPipeEncryptKey based on SnmpAdminString"""
    defaultHexValue = ""


_VasEncPipeEncryptKey_Object = MibTableColumn
vasEncPipeEncryptKey = _VasEncPipeEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 14),
    _VasEncPipeEncryptKey_Type()
)
vasEncPipeEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeEncryptKey.setStatus("current")
_VasEncPipeProcessedFrames_Type = Counter32
_VasEncPipeProcessedFrames_Object = MibTableColumn
vasEncPipeProcessedFrames = _VasEncPipeProcessedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 15),
    _VasEncPipeProcessedFrames_Type()
)
vasEncPipeProcessedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeProcessedFrames.setStatus("current")
_VasEncPipeCurrentTsBitrate_Type = Unsigned32
_VasEncPipeCurrentTsBitrate_Object = MibTableColumn
vasEncPipeCurrentTsBitrate = _VasEncPipeCurrentTsBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 16),
    _VasEncPipeCurrentTsBitrate_Type()
)
vasEncPipeCurrentTsBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasEncPipeCurrentTsBitrate.setStatus("current")
_VasEncPipeVideoBitrate_Type = Unsigned32
_VasEncPipeVideoBitrate_Object = MibTableColumn
vasEncPipeVideoBitrate = _VasEncPipeVideoBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 2, 1, 1, 17),
    _VasEncPipeVideoBitrate_Type()
)
vasEncPipeVideoBitrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasEncPipeVideoBitrate.setStatus("current")
_VasDecoderPipeGroup_ObjectIdentity = ObjectIdentity
vasDecoderPipeGroup = _VasDecoderPipeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3)
)
_VasDecPipeTable_Object = MibTable
vasDecPipeTable = _VasDecPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    vasDecPipeTable.setStatus("current")
_VasDecPipeEntry_Object = MibTableRow
vasDecPipeEntry = _VasDecPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1)
)
vasDecPipeEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasDecPipeIndex"),
)
if mibBuilder.loadTexts:
    vasDecPipeEntry.setStatus("current")
_VasDecPipeIndex_Type = Unsigned32
_VasDecPipeIndex_Object = MibTableColumn
vasDecPipeIndex = _VasDecPipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 1),
    _VasDecPipeIndex_Type()
)
vasDecPipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasDecPipeIndex.setStatus("current")
_VasDecPipeRowStatus_Type = RowStatus
_VasDecPipeRowStatus_Object = MibTableColumn
vasDecPipeRowStatus = _VasDecPipeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 2),
    _VasDecPipeRowStatus_Type()
)
vasDecPipeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipeRowStatus.setStatus("current")
_VasDecPipeName_Type = SnmpAdminString
_VasDecPipeName_Object = MibTableColumn
vasDecPipeName = _VasDecPipeName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 3),
    _VasDecPipeName_Type()
)
vasDecPipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeName.setStatus("current")


class _VasDecPipePurpose_Type(SnmpAdminString):
    """Custom type vasDecPipePurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasDecPipePurpose_Object = MibTableColumn
vasDecPipePurpose = _VasDecPipePurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 4),
    _VasDecPipePurpose_Type()
)
vasDecPipePurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipePurpose.setStatus("current")


class _VasDecPipeAdminStatus_Type(Integer32):
    """Custom type vasDecPipeAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasDecPipeAdminStatus_Type.__name__ = "Integer32"
_VasDecPipeAdminStatus_Object = MibTableColumn
vasDecPipeAdminStatus = _VasDecPipeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 5),
    _VasDecPipeAdminStatus_Type()
)
vasDecPipeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipeAdminStatus.setStatus("current")


class _VasDecPipeOperStatus_Type(Integer32):
    """Custom type vasDecPipeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasDecPipeOperStatus_Type.__name__ = "Integer32"
_VasDecPipeOperStatus_Object = MibTableColumn
vasDecPipeOperStatus = _VasDecPipeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 6),
    _VasDecPipeOperStatus_Type()
)
vasDecPipeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeOperStatus.setStatus("current")
_VasDecPipeFailure_Type = SnmpAdminString
_VasDecPipeFailure_Object = MibTableColumn
vasDecPipeFailure = _VasDecPipeFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 7),
    _VasDecPipeFailure_Type()
)
vasDecPipeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeFailure.setStatus("current")
_VasDecPipeLastChanged_Type = TimeStamp
_VasDecPipeLastChanged_Object = MibTableColumn
vasDecPipeLastChanged = _VasDecPipeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 8),
    _VasDecPipeLastChanged_Type()
)
vasDecPipeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeLastChanged.setStatus("current")
_VasDecPipeResetStatistics_Type = VasResetStatistics
_VasDecPipeResetStatistics_Object = MibTableColumn
vasDecPipeResetStatistics = _VasDecPipeResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 9),
    _VasDecPipeResetStatistics_Type()
)
vasDecPipeResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasDecPipeResetStatistics.setStatus("current")
_VasDecPipeInputFrom_Type = RowPointer
_VasDecPipeInputFrom_Object = MibTableColumn
vasDecPipeInputFrom = _VasDecPipeInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 10),
    _VasDecPipeInputFrom_Type()
)
vasDecPipeInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipeInputFrom.setStatus("current")


class _VasDecPipeCipher_Type(VasCipher):
    """Custom type vasDecPipeCipher based on VasCipher"""


_VasDecPipeCipher_Object = MibTableColumn
vasDecPipeCipher = _VasDecPipeCipher_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 11),
    _VasDecPipeCipher_Type()
)
vasDecPipeCipher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipeCipher.setStatus("current")


class _VasDecPipeDecryptKey_Type(SnmpAdminString):
    """Custom type vasDecPipeDecryptKey based on SnmpAdminString"""
    defaultHexValue = ""


_VasDecPipeDecryptKey_Object = MibTableColumn
vasDecPipeDecryptKey = _VasDecPipeDecryptKey_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 12),
    _VasDecPipeDecryptKey_Type()
)
vasDecPipeDecryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasDecPipeDecryptKey.setStatus("current")
_VasDecPipeProcessedFrames_Type = Counter32
_VasDecPipeProcessedFrames_Object = MibTableColumn
vasDecPipeProcessedFrames = _VasDecPipeProcessedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 13),
    _VasDecPipeProcessedFrames_Type()
)
vasDecPipeProcessedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeProcessedFrames.setStatus("current")
_VasDecPipeCurrentTsBitrate_Type = Unsigned32
_VasDecPipeCurrentTsBitrate_Object = MibTableColumn
vasDecPipeCurrentTsBitrate = _VasDecPipeCurrentTsBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 14),
    _VasDecPipeCurrentTsBitrate_Type()
)
vasDecPipeCurrentTsBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeCurrentTsBitrate.setStatus("current")
_VasDecPipeVideoBitrate_Type = Unsigned32
_VasDecPipeVideoBitrate_Object = MibTableColumn
vasDecPipeVideoBitrate = _VasDecPipeVideoBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 3, 1, 1, 15),
    _VasDecPipeVideoBitrate_Type()
)
vasDecPipeVideoBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasDecPipeVideoBitrate.setStatus("current")
_VasTransportsGroup_ObjectIdentity = ObjectIdentity
vasTransportsGroup = _VasTransportsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4)
)


class _VasStreamPort_Type(InetPortNumber):
    """Custom type vasStreamPort based on InetPortNumber"""
    defaultValue = 2088


_VasStreamPort_Object = MibScalar
vasStreamPort = _VasStreamPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 1),
    _VasStreamPort_Type()
)
vasStreamPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasStreamPort.setStatus("current")
_VasUdpSrcTable_Object = MibTable
vasUdpSrcTable = _VasUdpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2)
)
if mibBuilder.loadTexts:
    vasUdpSrcTable.setStatus("current")
_VasUdpSrcEntry_Object = MibTableRow
vasUdpSrcEntry = _VasUdpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1)
)
vasUdpSrcEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasUdpSrcIndex"),
)
if mibBuilder.loadTexts:
    vasUdpSrcEntry.setStatus("current")
_VasUdpSrcIndex_Type = Unsigned32
_VasUdpSrcIndex_Object = MibTableColumn
vasUdpSrcIndex = _VasUdpSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 1),
    _VasUdpSrcIndex_Type()
)
vasUdpSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasUdpSrcIndex.setStatus("current")
_VasUdpSrcRowStatus_Type = RowStatus
_VasUdpSrcRowStatus_Object = MibTableColumn
vasUdpSrcRowStatus = _VasUdpSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 2),
    _VasUdpSrcRowStatus_Type()
)
vasUdpSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcRowStatus.setStatus("current")
_VasUdpSrcName_Type = SnmpAdminString
_VasUdpSrcName_Object = MibTableColumn
vasUdpSrcName = _VasUdpSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 3),
    _VasUdpSrcName_Type()
)
vasUdpSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcName.setStatus("current")


class _VasUdpSrcPurpose_Type(SnmpAdminString):
    """Custom type vasUdpSrcPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasUdpSrcPurpose_Object = MibTableColumn
vasUdpSrcPurpose = _VasUdpSrcPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 4),
    _VasUdpSrcPurpose_Type()
)
vasUdpSrcPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcPurpose.setStatus("current")


class _VasUdpSrcAdminStatus_Type(Integer32):
    """Custom type vasUdpSrcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasUdpSrcAdminStatus_Type.__name__ = "Integer32"
_VasUdpSrcAdminStatus_Object = MibTableColumn
vasUdpSrcAdminStatus = _VasUdpSrcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 5),
    _VasUdpSrcAdminStatus_Type()
)
vasUdpSrcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcAdminStatus.setStatus("current")


class _VasUdpSrcOperStatus_Type(Integer32):
    """Custom type vasUdpSrcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasUdpSrcOperStatus_Type.__name__ = "Integer32"
_VasUdpSrcOperStatus_Object = MibTableColumn
vasUdpSrcOperStatus = _VasUdpSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 6),
    _VasUdpSrcOperStatus_Type()
)
vasUdpSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcOperStatus.setStatus("current")
_VasUdpSrcFailure_Type = SnmpAdminString
_VasUdpSrcFailure_Object = MibTableColumn
vasUdpSrcFailure = _VasUdpSrcFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 7),
    _VasUdpSrcFailure_Type()
)
vasUdpSrcFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcFailure.setStatus("current")
_VasUdpSrcLastChanged_Type = TimeStamp
_VasUdpSrcLastChanged_Object = MibTableColumn
vasUdpSrcLastChanged = _VasUdpSrcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 8),
    _VasUdpSrcLastChanged_Type()
)
vasUdpSrcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcLastChanged.setStatus("current")
_VasUdpSrcConnectionStatus_Type = VasConnectionStatus
_VasUdpSrcConnectionStatus_Object = MibTableColumn
vasUdpSrcConnectionStatus = _VasUdpSrcConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 9),
    _VasUdpSrcConnectionStatus_Type()
)
vasUdpSrcConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcConnectionStatus.setStatus("current")
_VasUdpSrcResetStatistics_Type = VasResetStatistics
_VasUdpSrcResetStatistics_Object = MibTableColumn
vasUdpSrcResetStatistics = _VasUdpSrcResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 10),
    _VasUdpSrcResetStatistics_Type()
)
vasUdpSrcResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasUdpSrcResetStatistics.setStatus("current")
_VasUdpSrcStatsUdp_Type = Unsigned32
_VasUdpSrcStatsUdp_Object = MibTableColumn
vasUdpSrcStatsUdp = _VasUdpSrcStatsUdp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 11),
    _VasUdpSrcStatsUdp_Type()
)
vasUdpSrcStatsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSrcStatsUdp.setStatus("current")
_VasUdpSrcInputFrom_Type = RowPointer
_VasUdpSrcInputFrom_Object = MibTableColumn
vasUdpSrcInputFrom = _VasUdpSrcInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 12),
    _VasUdpSrcInputFrom_Type()
)
vasUdpSrcInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcInputFrom.setStatus("current")


class _VasUdpSrcRemoteHostType_Type(InetAddressType):
    """Custom type vasUdpSrcRemoteHostType based on InetAddressType"""


_VasUdpSrcRemoteHostType_Object = MibTableColumn
vasUdpSrcRemoteHostType = _VasUdpSrcRemoteHostType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 13),
    _VasUdpSrcRemoteHostType_Type()
)
vasUdpSrcRemoteHostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcRemoteHostType.setStatus("current")


class _VasUdpSrcRemoteHostAddress_Type(InetAddress):
    """Custom type vasUdpSrcRemoteHostAddress based on InetAddress"""
    defaultHexValue = ""


_VasUdpSrcRemoteHostAddress_Object = MibTableColumn
vasUdpSrcRemoteHostAddress = _VasUdpSrcRemoteHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 14),
    _VasUdpSrcRemoteHostAddress_Type()
)
vasUdpSrcRemoteHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcRemoteHostAddress.setStatus("current")


class _VasUdpSrcRemotePort_Type(InetPortNumber):
    """Custom type vasUdpSrcRemotePort based on InetPortNumber"""
    defaultValue = 0


_VasUdpSrcRemotePort_Object = MibTableColumn
vasUdpSrcRemotePort = _VasUdpSrcRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 15),
    _VasUdpSrcRemotePort_Type()
)
vasUdpSrcRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcRemotePort.setStatus("current")


class _VasUdpSrcLocalIfType_Type(InetAddressType):
    """Custom type vasUdpSrcLocalIfType based on InetAddressType"""


_VasUdpSrcLocalIfType_Object = MibTableColumn
vasUdpSrcLocalIfType = _VasUdpSrcLocalIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 16),
    _VasUdpSrcLocalIfType_Type()
)
vasUdpSrcLocalIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcLocalIfType.setStatus("current")


class _VasUdpSrcLocalIfAddress_Type(InetAddress):
    """Custom type vasUdpSrcLocalIfAddress based on InetAddress"""
    defaultHexValue = "00000000"


_VasUdpSrcLocalIfAddress_Object = MibTableColumn
vasUdpSrcLocalIfAddress = _VasUdpSrcLocalIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 17),
    _VasUdpSrcLocalIfAddress_Type()
)
vasUdpSrcLocalIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcLocalIfAddress.setStatus("current")


class _VasUdpSrcLocalPort_Type(InetPortNumber):
    """Custom type vasUdpSrcLocalPort based on InetPortNumber"""
    defaultValue = 0


_VasUdpSrcLocalPort_Object = MibTableColumn
vasUdpSrcLocalPort = _VasUdpSrcLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 18),
    _VasUdpSrcLocalPort_Type()
)
vasUdpSrcLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcLocalPort.setStatus("current")


class _VasUdpSrcCipher_Type(VasCipher):
    """Custom type vasUdpSrcCipher based on VasCipher"""


_VasUdpSrcCipher_Object = MibTableColumn
vasUdpSrcCipher = _VasUdpSrcCipher_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 19),
    _VasUdpSrcCipher_Type()
)
vasUdpSrcCipher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcCipher.setStatus("current")


class _VasUdpSrcDecryptKey_Type(SnmpAdminString):
    """Custom type vasUdpSrcDecryptKey based on SnmpAdminString"""
    defaultHexValue = ""


_VasUdpSrcDecryptKey_Object = MibTableColumn
vasUdpSrcDecryptKey = _VasUdpSrcDecryptKey_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 20),
    _VasUdpSrcDecryptKey_Type()
)
vasUdpSrcDecryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcDecryptKey.setStatus("current")


class _VasUdpSrcTtl_Type(Unsigned32):
    """Custom type vasUdpSrcTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VasUdpSrcTtl_Type.__name__ = "Unsigned32"
_VasUdpSrcTtl_Object = MibTableColumn
vasUdpSrcTtl = _VasUdpSrcTtl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 21),
    _VasUdpSrcTtl_Type()
)
vasUdpSrcTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcTtl.setStatus("current")


class _VasUdpSrcDontFragment_Type(TruthValue):
    """Custom type vasUdpSrcDontFragment based on TruthValue"""


_VasUdpSrcDontFragment_Object = MibTableColumn
vasUdpSrcDontFragment = _VasUdpSrcDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 2, 1, 22),
    _VasUdpSrcDontFragment_Type()
)
vasUdpSrcDontFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSrcDontFragment.setStatus("current")
_VasUdpSnkTable_Object = MibTable
vasUdpSnkTable = _VasUdpSnkTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3)
)
if mibBuilder.loadTexts:
    vasUdpSnkTable.setStatus("current")
_VasUdpSnkEntry_Object = MibTableRow
vasUdpSnkEntry = _VasUdpSnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1)
)
vasUdpSnkEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasUdpSnkIndex"),
)
if mibBuilder.loadTexts:
    vasUdpSnkEntry.setStatus("current")
_VasUdpSnkIndex_Type = Unsigned32
_VasUdpSnkIndex_Object = MibTableColumn
vasUdpSnkIndex = _VasUdpSnkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 1),
    _VasUdpSnkIndex_Type()
)
vasUdpSnkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasUdpSnkIndex.setStatus("current")
_VasUdpSnkRowStatus_Type = RowStatus
_VasUdpSnkRowStatus_Object = MibTableColumn
vasUdpSnkRowStatus = _VasUdpSnkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 2),
    _VasUdpSnkRowStatus_Type()
)
vasUdpSnkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkRowStatus.setStatus("current")
_VasUdpSnkName_Type = SnmpAdminString
_VasUdpSnkName_Object = MibTableColumn
vasUdpSnkName = _VasUdpSnkName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 3),
    _VasUdpSnkName_Type()
)
vasUdpSnkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkName.setStatus("current")


class _VasUdpSnkPurpose_Type(SnmpAdminString):
    """Custom type vasUdpSnkPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasUdpSnkPurpose_Object = MibTableColumn
vasUdpSnkPurpose = _VasUdpSnkPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 4),
    _VasUdpSnkPurpose_Type()
)
vasUdpSnkPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkPurpose.setStatus("current")


class _VasUdpSnkAdminStatus_Type(Integer32):
    """Custom type vasUdpSnkAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasUdpSnkAdminStatus_Type.__name__ = "Integer32"
_VasUdpSnkAdminStatus_Object = MibTableColumn
vasUdpSnkAdminStatus = _VasUdpSnkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 5),
    _VasUdpSnkAdminStatus_Type()
)
vasUdpSnkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkAdminStatus.setStatus("current")


class _VasUdpSnkOperStatus_Type(Integer32):
    """Custom type vasUdpSnkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasUdpSnkOperStatus_Type.__name__ = "Integer32"
_VasUdpSnkOperStatus_Object = MibTableColumn
vasUdpSnkOperStatus = _VasUdpSnkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 6),
    _VasUdpSnkOperStatus_Type()
)
vasUdpSnkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkOperStatus.setStatus("current")
_VasUdpSnkFailure_Type = SnmpAdminString
_VasUdpSnkFailure_Object = MibTableColumn
vasUdpSnkFailure = _VasUdpSnkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 7),
    _VasUdpSnkFailure_Type()
)
vasUdpSnkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkFailure.setStatus("current")
_VasUdpSnkLastChanged_Type = TimeStamp
_VasUdpSnkLastChanged_Object = MibTableColumn
vasUdpSnkLastChanged = _VasUdpSnkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 8),
    _VasUdpSnkLastChanged_Type()
)
vasUdpSnkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkLastChanged.setStatus("current")
_VasUdpSnkConnectionStatus_Type = VasConnectionStatus
_VasUdpSnkConnectionStatus_Object = MibTableColumn
vasUdpSnkConnectionStatus = _VasUdpSnkConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 9),
    _VasUdpSnkConnectionStatus_Type()
)
vasUdpSnkConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkConnectionStatus.setStatus("current")


class _VasUdpSnkResetStatistics_Type(VasResetStatistics):
    """Custom type vasUdpSnkResetStatistics based on VasResetStatistics"""
    defaultValue = 0


_VasUdpSnkResetStatistics_Object = MibTableColumn
vasUdpSnkResetStatistics = _VasUdpSnkResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 10),
    _VasUdpSnkResetStatistics_Type()
)
vasUdpSnkResetStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkResetStatistics.setStatus("current")
_VasUdpSnkStatsUdp_Type = Unsigned32
_VasUdpSnkStatsUdp_Object = MibTableColumn
vasUdpSnkStatsUdp = _VasUdpSnkStatsUdp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 11),
    _VasUdpSnkStatsUdp_Type()
)
vasUdpSnkStatsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkStatsUdp.setStatus("current")
_VasUdpSnkStatsTr101_Type = Unsigned32
_VasUdpSnkStatsTr101_Object = MibTableColumn
vasUdpSnkStatsTr101 = _VasUdpSnkStatsTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 12),
    _VasUdpSnkStatsTr101_Type()
)
vasUdpSnkStatsTr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkStatsTr101.setStatus("current")


class _VasUdpSnkEnableTr101_Type(TruthValue):
    """Custom type vasUdpSnkEnableTr101 based on TruthValue"""


_VasUdpSnkEnableTr101_Object = MibTableColumn
vasUdpSnkEnableTr101 = _VasUdpSnkEnableTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 13),
    _VasUdpSnkEnableTr101_Type()
)
vasUdpSnkEnableTr101.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkEnableTr101.setStatus("current")
_VasUdpSnkRemoteInetType_Type = InetAddressType
_VasUdpSnkRemoteInetType_Object = MibTableColumn
vasUdpSnkRemoteInetType = _VasUdpSnkRemoteInetType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 14),
    _VasUdpSnkRemoteInetType_Type()
)
vasUdpSnkRemoteInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkRemoteInetType.setStatus("current")
_VasUdpSnkRemoteInetAddress_Type = InetAddress
_VasUdpSnkRemoteInetAddress_Object = MibTableColumn
vasUdpSnkRemoteInetAddress = _VasUdpSnkRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 15),
    _VasUdpSnkRemoteInetAddress_Type()
)
vasUdpSnkRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpSnkRemoteInetAddress.setStatus("current")


class _VasUdpSnkLocalIfType_Type(InetAddressType):
    """Custom type vasUdpSnkLocalIfType based on InetAddressType"""


_VasUdpSnkLocalIfType_Object = MibTableColumn
vasUdpSnkLocalIfType = _VasUdpSnkLocalIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 16),
    _VasUdpSnkLocalIfType_Type()
)
vasUdpSnkLocalIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkLocalIfType.setStatus("current")


class _VasUdpSnkLocalIfAddress_Type(InetAddress):
    """Custom type vasUdpSnkLocalIfAddress based on InetAddress"""
    defaultHexValue = "00000000"


_VasUdpSnkLocalIfAddress_Object = MibTableColumn
vasUdpSnkLocalIfAddress = _VasUdpSnkLocalIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 17),
    _VasUdpSnkLocalIfAddress_Type()
)
vasUdpSnkLocalIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkLocalIfAddress.setStatus("current")


class _VasUdpSnkLocalPort_Type(InetPortNumber):
    """Custom type vasUdpSnkLocalPort based on InetPortNumber"""
    defaultValue = 0


_VasUdpSnkLocalPort_Object = MibTableColumn
vasUdpSnkLocalPort = _VasUdpSnkLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 18),
    _VasUdpSnkLocalPort_Type()
)
vasUdpSnkLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkLocalPort.setStatus("current")


class _VasUdpSnkCipher_Type(VasCipher):
    """Custom type vasUdpSnkCipher based on VasCipher"""


_VasUdpSnkCipher_Object = MibTableColumn
vasUdpSnkCipher = _VasUdpSnkCipher_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 19),
    _VasUdpSnkCipher_Type()
)
vasUdpSnkCipher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkCipher.setStatus("current")


class _VasUdpSnkEncryptKey_Type(SnmpAdminString):
    """Custom type vasUdpSnkEncryptKey based on SnmpAdminString"""
    defaultHexValue = ""


_VasUdpSnkEncryptKey_Object = MibTableColumn
vasUdpSnkEncryptKey = _VasUdpSnkEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 20),
    _VasUdpSnkEncryptKey_Type()
)
vasUdpSnkEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkEncryptKey.setStatus("current")


class _VasUdpSnkMcastIpType_Type(InetAddressType):
    """Custom type vasUdpSnkMcastIpType based on InetAddressType"""


_VasUdpSnkMcastIpType_Object = MibTableColumn
vasUdpSnkMcastIpType = _VasUdpSnkMcastIpType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 21),
    _VasUdpSnkMcastIpType_Type()
)
vasUdpSnkMcastIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkMcastIpType.setStatus("current")


class _VasUdpSnkMcastIp_Type(InetAddress):
    """Custom type vasUdpSnkMcastIp based on InetAddress"""
    defaultHexValue = ""


_VasUdpSnkMcastIp_Object = MibTableColumn
vasUdpSnkMcastIp = _VasUdpSnkMcastIp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 22),
    _VasUdpSnkMcastIp_Type()
)
vasUdpSnkMcastIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkMcastIp.setStatus("current")


class _VasUdpSnkSsmSourceIp_Type(InetAddress):
    """Custom type vasUdpSnkSsmSourceIp based on InetAddress"""
    defaultHexValue = ""


_VasUdpSnkSsmSourceIp_Object = MibTableColumn
vasUdpSnkSsmSourceIp = _VasUdpSnkSsmSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 23),
    _VasUdpSnkSsmSourceIp_Type()
)
vasUdpSnkSsmSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkSsmSourceIp.setStatus("current")


class _VasUdpSnkCompress_Type(TruthValue):
    """Custom type vasUdpSnkCompress based on TruthValue"""


_VasUdpSnkCompress_Object = MibTableColumn
vasUdpSnkCompress = _VasUdpSnkCompress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 3, 1, 24),
    _VasUdpSnkCompress_Type()
)
vasUdpSnkCompress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasUdpSnkCompress.setStatus("current")
_VasPulSrcTable_Object = MibTable
vasPulSrcTable = _VasPulSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4)
)
if mibBuilder.loadTexts:
    vasPulSrcTable.setStatus("current")
_VasPulSrcEntry_Object = MibTableRow
vasPulSrcEntry = _VasPulSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1)
)
vasPulSrcEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasPulSrcIndex"),
)
if mibBuilder.loadTexts:
    vasPulSrcEntry.setStatus("current")
_VasPulSrcIndex_Type = Unsigned32
_VasPulSrcIndex_Object = MibTableColumn
vasPulSrcIndex = _VasPulSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 1),
    _VasPulSrcIndex_Type()
)
vasPulSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasPulSrcIndex.setStatus("current")
_VasPulSrcRowStatus_Type = RowStatus
_VasPulSrcRowStatus_Object = MibTableColumn
vasPulSrcRowStatus = _VasPulSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 2),
    _VasPulSrcRowStatus_Type()
)
vasPulSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcRowStatus.setStatus("current")
_VasPulSrcName_Type = SnmpAdminString
_VasPulSrcName_Object = MibTableColumn
vasPulSrcName = _VasPulSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 3),
    _VasPulSrcName_Type()
)
vasPulSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcName.setStatus("current")


class _VasPulSrcPurpose_Type(SnmpAdminString):
    """Custom type vasPulSrcPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasPulSrcPurpose_Object = MibTableColumn
vasPulSrcPurpose = _VasPulSrcPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 4),
    _VasPulSrcPurpose_Type()
)
vasPulSrcPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcPurpose.setStatus("current")


class _VasPulSrcAdminStatus_Type(Integer32):
    """Custom type vasPulSrcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPulSrcAdminStatus_Type.__name__ = "Integer32"
_VasPulSrcAdminStatus_Object = MibTableColumn
vasPulSrcAdminStatus = _VasPulSrcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 5),
    _VasPulSrcAdminStatus_Type()
)
vasPulSrcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcAdminStatus.setStatus("current")


class _VasPulSrcOperStatus_Type(Integer32):
    """Custom type vasPulSrcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 3),
          ("down", 2),
          ("partial", 4),
          ("up", 1))
    )


_VasPulSrcOperStatus_Type.__name__ = "Integer32"
_VasPulSrcOperStatus_Object = MibTableColumn
vasPulSrcOperStatus = _VasPulSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 6),
    _VasPulSrcOperStatus_Type()
)
vasPulSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcOperStatus.setStatus("current")
_VasPulSrcFailure_Type = SnmpAdminString
_VasPulSrcFailure_Object = MibTableColumn
vasPulSrcFailure = _VasPulSrcFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 7),
    _VasPulSrcFailure_Type()
)
vasPulSrcFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcFailure.setStatus("current")
_VasPulSrcLastChanged_Type = TimeStamp
_VasPulSrcLastChanged_Object = MibTableColumn
vasPulSrcLastChanged = _VasPulSrcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 8),
    _VasPulSrcLastChanged_Type()
)
vasPulSrcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcLastChanged.setStatus("current")
_VasPulSrcConnectionStatus_Type = VasConnectionStatus
_VasPulSrcConnectionStatus_Object = MibTableColumn
vasPulSrcConnectionStatus = _VasPulSrcConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 9),
    _VasPulSrcConnectionStatus_Type()
)
vasPulSrcConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcConnectionStatus.setStatus("current")
_VasPulSrcResetStatistics_Type = VasResetStatistics
_VasPulSrcResetStatistics_Object = MibTableColumn
vasPulSrcResetStatistics = _VasPulSrcResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 10),
    _VasPulSrcResetStatistics_Type()
)
vasPulSrcResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasPulSrcResetStatistics.setStatus("current")
_VasPulSrcStatsTrsp_Type = Unsigned32
_VasPulSrcStatsTrsp_Object = MibTableColumn
vasPulSrcStatsTrsp = _VasPulSrcStatsTrsp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 11),
    _VasPulSrcStatsTrsp_Type()
)
vasPulSrcStatsTrsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcStatsTrsp.setStatus("current")
_VasPulSrcRemoteInetType_Type = InetAddressType
_VasPulSrcRemoteInetType_Object = MibTableColumn
vasPulSrcRemoteInetType = _VasPulSrcRemoteInetType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 12),
    _VasPulSrcRemoteInetType_Type()
)
vasPulSrcRemoteInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcRemoteInetType.setStatus("current")
_VasPulSrcRemoteInetAddress_Type = InetAddress
_VasPulSrcRemoteInetAddress_Object = MibTableColumn
vasPulSrcRemoteInetAddress = _VasPulSrcRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 13),
    _VasPulSrcRemoteInetAddress_Type()
)
vasPulSrcRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSrcRemoteInetAddress.setStatus("current")
_VasPulSrcStreamId_Type = SnmpAdminString
_VasPulSrcStreamId_Object = MibTableColumn
vasPulSrcStreamId = _VasPulSrcStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 14),
    _VasPulSrcStreamId_Type()
)
vasPulSrcStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcStreamId.setStatus("current")
_VasPulSrcInputFrom_Type = RowPointer
_VasPulSrcInputFrom_Object = MibTableColumn
vasPulSrcInputFrom = _VasPulSrcInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 15),
    _VasPulSrcInputFrom_Type()
)
vasPulSrcInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcInputFrom.setStatus("current")
_VasPulSrcRemoteId_Type = SnmpAdminString
_VasPulSrcRemoteId_Object = MibTableColumn
vasPulSrcRemoteId = _VasPulSrcRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 16),
    _VasPulSrcRemoteId_Type()
)
vasPulSrcRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcRemoteId.setStatus("current")


class _VasPulSrcPassword_Type(SnmpAdminString):
    """Custom type vasPulSrcPassword based on SnmpAdminString"""
    defaultHexValue = ""


_VasPulSrcPassword_Object = MibTableColumn
vasPulSrcPassword = _VasPulSrcPassword_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 4, 1, 17),
    _VasPulSrcPassword_Type()
)
vasPulSrcPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSrcPassword.setStatus("current")
_VasMpuSrcTable_Object = MibTable
vasMpuSrcTable = _VasMpuSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5)
)
if mibBuilder.loadTexts:
    vasMpuSrcTable.setStatus("current")
_VasMpuSrcEntry_Object = MibTableRow
vasMpuSrcEntry = _VasMpuSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1)
)
vasMpuSrcEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasMpuSrcIndex"),
)
if mibBuilder.loadTexts:
    vasMpuSrcEntry.setStatus("current")
_VasMpuSrcIndex_Type = Unsigned32
_VasMpuSrcIndex_Object = MibTableColumn
vasMpuSrcIndex = _VasMpuSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 1),
    _VasMpuSrcIndex_Type()
)
vasMpuSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasMpuSrcIndex.setStatus("current")
_VasMpuSrcRowStatus_Type = RowStatus
_VasMpuSrcRowStatus_Object = MibTableColumn
vasMpuSrcRowStatus = _VasMpuSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 2),
    _VasMpuSrcRowStatus_Type()
)
vasMpuSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasMpuSrcRowStatus.setStatus("current")
_VasMpuSrcName_Type = SnmpAdminString
_VasMpuSrcName_Object = MibTableColumn
vasMpuSrcName = _VasMpuSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 3),
    _VasMpuSrcName_Type()
)
vasMpuSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasMpuSrcName.setStatus("current")


class _VasMpuSrcPurpose_Type(SnmpAdminString):
    """Custom type vasMpuSrcPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasMpuSrcPurpose_Object = MibTableColumn
vasMpuSrcPurpose = _VasMpuSrcPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 4),
    _VasMpuSrcPurpose_Type()
)
vasMpuSrcPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasMpuSrcPurpose.setStatus("current")


class _VasMpuSrcAdminStatus_Type(Integer32):
    """Custom type vasMpuSrcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasMpuSrcAdminStatus_Type.__name__ = "Integer32"
_VasMpuSrcAdminStatus_Object = MibTableColumn
vasMpuSrcAdminStatus = _VasMpuSrcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 5),
    _VasMpuSrcAdminStatus_Type()
)
vasMpuSrcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasMpuSrcAdminStatus.setStatus("current")


class _VasMpuSrcOperStatus_Type(Integer32):
    """Custom type vasMpuSrcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 3),
          ("down", 2),
          ("partial", 4),
          ("up", 1))
    )


_VasMpuSrcOperStatus_Type.__name__ = "Integer32"
_VasMpuSrcOperStatus_Object = MibTableColumn
vasMpuSrcOperStatus = _VasMpuSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 6),
    _VasMpuSrcOperStatus_Type()
)
vasMpuSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasMpuSrcOperStatus.setStatus("current")
_VasMpuSrcFailure_Type = SnmpAdminString
_VasMpuSrcFailure_Object = MibTableColumn
vasMpuSrcFailure = _VasMpuSrcFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 7),
    _VasMpuSrcFailure_Type()
)
vasMpuSrcFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasMpuSrcFailure.setStatus("current")
_VasMpuSrcLastChanged_Type = TimeStamp
_VasMpuSrcLastChanged_Object = MibTableColumn
vasMpuSrcLastChanged = _VasMpuSrcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 8),
    _VasMpuSrcLastChanged_Type()
)
vasMpuSrcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasMpuSrcLastChanged.setStatus("current")
_VasMpuSrcStreamId_Type = SnmpAdminString
_VasMpuSrcStreamId_Object = MibTableColumn
vasMpuSrcStreamId = _VasMpuSrcStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 12),
    _VasMpuSrcStreamId_Type()
)
vasMpuSrcStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasMpuSrcStreamId.setStatus("current")
_VasMpuSrcInputFrom_Type = RowPointer
_VasMpuSrcInputFrom_Object = MibTableColumn
vasMpuSrcInputFrom = _VasMpuSrcInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 5, 1, 13),
    _VasMpuSrcInputFrom_Type()
)
vasMpuSrcInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasMpuSrcInputFrom.setStatus("current")
_VasPulSnkTable_Object = MibTable
vasPulSnkTable = _VasPulSnkTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6)
)
if mibBuilder.loadTexts:
    vasPulSnkTable.setStatus("current")
_VasPulSnkEntry_Object = MibTableRow
vasPulSnkEntry = _VasPulSnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1)
)
vasPulSnkEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasPulSnkIndex"),
)
if mibBuilder.loadTexts:
    vasPulSnkEntry.setStatus("current")
_VasPulSnkIndex_Type = Unsigned32
_VasPulSnkIndex_Object = MibTableColumn
vasPulSnkIndex = _VasPulSnkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 1),
    _VasPulSnkIndex_Type()
)
vasPulSnkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasPulSnkIndex.setStatus("current")
_VasPulSnkRowStatus_Type = RowStatus
_VasPulSnkRowStatus_Object = MibTableColumn
vasPulSnkRowStatus = _VasPulSnkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 2),
    _VasPulSnkRowStatus_Type()
)
vasPulSnkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRowStatus.setStatus("current")
_VasPulSnkName_Type = SnmpAdminString
_VasPulSnkName_Object = MibTableColumn
vasPulSnkName = _VasPulSnkName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 3),
    _VasPulSnkName_Type()
)
vasPulSnkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkName.setStatus("current")


class _VasPulSnkPurpose_Type(SnmpAdminString):
    """Custom type vasPulSnkPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasPulSnkPurpose_Object = MibTableColumn
vasPulSnkPurpose = _VasPulSnkPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 4),
    _VasPulSnkPurpose_Type()
)
vasPulSnkPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkPurpose.setStatus("current")


class _VasPulSnkAdminStatus_Type(Integer32):
    """Custom type vasPulSnkAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPulSnkAdminStatus_Type.__name__ = "Integer32"
_VasPulSnkAdminStatus_Object = MibTableColumn
vasPulSnkAdminStatus = _VasPulSnkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 5),
    _VasPulSnkAdminStatus_Type()
)
vasPulSnkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkAdminStatus.setStatus("current")


class _VasPulSnkOperStatus_Type(Integer32):
    """Custom type vasPulSnkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPulSnkOperStatus_Type.__name__ = "Integer32"
_VasPulSnkOperStatus_Object = MibTableColumn
vasPulSnkOperStatus = _VasPulSnkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 6),
    _VasPulSnkOperStatus_Type()
)
vasPulSnkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkOperStatus.setStatus("current")
_VasPulSnkFailure_Type = SnmpAdminString
_VasPulSnkFailure_Object = MibTableColumn
vasPulSnkFailure = _VasPulSnkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 7),
    _VasPulSnkFailure_Type()
)
vasPulSnkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkFailure.setStatus("current")
_VasPulSnkLastChanged_Type = TimeStamp
_VasPulSnkLastChanged_Object = MibTableColumn
vasPulSnkLastChanged = _VasPulSnkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 8),
    _VasPulSnkLastChanged_Type()
)
vasPulSnkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkLastChanged.setStatus("current")
_VasPulSnkConnectionStatus_Type = VasConnectionStatus
_VasPulSnkConnectionStatus_Object = MibTableColumn
vasPulSnkConnectionStatus = _VasPulSnkConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 9),
    _VasPulSnkConnectionStatus_Type()
)
vasPulSnkConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkConnectionStatus.setStatus("current")
_VasPulSnkResetStatistics_Type = VasResetStatistics
_VasPulSnkResetStatistics_Object = MibTableColumn
vasPulSnkResetStatistics = _VasPulSnkResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 10),
    _VasPulSnkResetStatistics_Type()
)
vasPulSnkResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasPulSnkResetStatistics.setStatus("current")
_VasPulSnkStatsTrsp_Type = Unsigned32
_VasPulSnkStatsTrsp_Object = MibTableColumn
vasPulSnkStatsTrsp = _VasPulSnkStatsTrsp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 11),
    _VasPulSnkStatsTrsp_Type()
)
vasPulSnkStatsTrsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkStatsTrsp.setStatus("current")
_VasPulSnkStatsTr101_Type = Unsigned32
_VasPulSnkStatsTr101_Object = MibTableColumn
vasPulSnkStatsTr101 = _VasPulSnkStatsTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 12),
    _VasPulSnkStatsTr101_Type()
)
vasPulSnkStatsTr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkStatsTr101.setStatus("current")


class _VasPulSnkEnableTr101_Type(TruthValue):
    """Custom type vasPulSnkEnableTr101 based on TruthValue"""


_VasPulSnkEnableTr101_Object = MibTableColumn
vasPulSnkEnableTr101 = _VasPulSnkEnableTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 13),
    _VasPulSnkEnableTr101_Type()
)
vasPulSnkEnableTr101.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkEnableTr101.setStatus("current")
_VasPulSnkRemoteInetType_Type = InetAddressType
_VasPulSnkRemoteInetType_Object = MibTableColumn
vasPulSnkRemoteInetType = _VasPulSnkRemoteInetType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 14),
    _VasPulSnkRemoteInetType_Type()
)
vasPulSnkRemoteInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkRemoteInetType.setStatus("current")
_VasPulSnkRemoteInetAddress_Type = InetAddress
_VasPulSnkRemoteInetAddress_Object = MibTableColumn
vasPulSnkRemoteInetAddress = _VasPulSnkRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 15),
    _VasPulSnkRemoteInetAddress_Type()
)
vasPulSnkRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPulSnkRemoteInetAddress.setStatus("current")
_VasPulSnkStreamId_Type = SnmpAdminString
_VasPulSnkStreamId_Object = MibTableColumn
vasPulSnkStreamId = _VasPulSnkStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 16),
    _VasPulSnkStreamId_Type()
)
vasPulSnkStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkStreamId.setStatus("current")


class _VasPulSnkPassword_Type(SnmpAdminString):
    """Custom type vasPulSnkPassword based on SnmpAdminString"""
    defaultHexValue = ""


_VasPulSnkPassword_Object = MibTableColumn
vasPulSnkPassword = _VasPulSnkPassword_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 17),
    _VasPulSnkPassword_Type()
)
vasPulSnkPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkPassword.setStatus("current")


class _VasPulSnkRemoteHostType_Type(InetAddressType):
    """Custom type vasPulSnkRemoteHostType based on InetAddressType"""


_VasPulSnkRemoteHostType_Object = MibTableColumn
vasPulSnkRemoteHostType = _VasPulSnkRemoteHostType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 18),
    _VasPulSnkRemoteHostType_Type()
)
vasPulSnkRemoteHostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRemoteHostType.setStatus("current")


class _VasPulSnkRemoteHostAddress_Type(InetAddress):
    """Custom type vasPulSnkRemoteHostAddress based on InetAddress"""
    defaultHexValue = ""


_VasPulSnkRemoteHostAddress_Object = MibTableColumn
vasPulSnkRemoteHostAddress = _VasPulSnkRemoteHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 19),
    _VasPulSnkRemoteHostAddress_Type()
)
vasPulSnkRemoteHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRemoteHostAddress.setStatus("current")


class _VasPulSnkRemoteHostType2_Type(InetAddressType):
    """Custom type vasPulSnkRemoteHostType2 based on InetAddressType"""


_VasPulSnkRemoteHostType2_Object = MibTableColumn
vasPulSnkRemoteHostType2 = _VasPulSnkRemoteHostType2_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 20),
    _VasPulSnkRemoteHostType2_Type()
)
vasPulSnkRemoteHostType2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRemoteHostType2.setStatus("current")


class _VasPulSnkRemoteHostAddress2_Type(InetAddress):
    """Custom type vasPulSnkRemoteHostAddress2 based on InetAddress"""
    defaultHexValue = ""


_VasPulSnkRemoteHostAddress2_Object = MibTableColumn
vasPulSnkRemoteHostAddress2 = _VasPulSnkRemoteHostAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 21),
    _VasPulSnkRemoteHostAddress2_Type()
)
vasPulSnkRemoteHostAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRemoteHostAddress2.setStatus("current")


class _VasPulSnkRemotePort_Type(InetPortNumber):
    """Custom type vasPulSnkRemotePort based on InetPortNumber"""
    defaultValue = 2088


_VasPulSnkRemotePort_Object = MibTableColumn
vasPulSnkRemotePort = _VasPulSnkRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 22),
    _VasPulSnkRemotePort_Type()
)
vasPulSnkRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRemotePort.setStatus("current")


class _VasPulSnkRetransmitBuffer_Type(Unsigned32):
    """Custom type vasPulSnkRetransmitBuffer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_VasPulSnkRetransmitBuffer_Type.__name__ = "Unsigned32"
_VasPulSnkRetransmitBuffer_Object = MibTableColumn
vasPulSnkRetransmitBuffer = _VasPulSnkRetransmitBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 23),
    _VasPulSnkRetransmitBuffer_Type()
)
vasPulSnkRetransmitBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkRetransmitBuffer.setStatus("current")


class _VasPulSnkFecMaxOverhead_Type(Unsigned32):
    """Custom type vasPulSnkFecMaxOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VasPulSnkFecMaxOverhead_Type.__name__ = "Unsigned32"
_VasPulSnkFecMaxOverhead_Object = MibTableColumn
vasPulSnkFecMaxOverhead = _VasPulSnkFecMaxOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 24),
    _VasPulSnkFecMaxOverhead_Type()
)
vasPulSnkFecMaxOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkFecMaxOverhead.setStatus("current")


class _VasPulSnkFecOptimize_Type(TruthValue):
    """Custom type vasPulSnkFecOptimize based on TruthValue"""


_VasPulSnkFecOptimize_Object = MibTableColumn
vasPulSnkFecOptimize = _VasPulSnkFecOptimize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 25),
    _VasPulSnkFecOptimize_Type()
)
vasPulSnkFecOptimize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkFecOptimize.setStatus("current")


class _VasPulSnkFecLatency_Type(Unsigned32):
    """Custom type vasPulSnkFecLatency based on Unsigned32"""
    defaultValue = 100


_VasPulSnkFecLatency_Object = MibTableColumn
vasPulSnkFecLatency = _VasPulSnkFecLatency_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 6, 1, 26),
    _VasPulSnkFecLatency_Type()
)
vasPulSnkFecLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPulSnkFecLatency.setStatus("current")
_VasPusSrcTable_Object = MibTable
vasPusSrcTable = _VasPusSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7)
)
if mibBuilder.loadTexts:
    vasPusSrcTable.setStatus("current")
_VasPusSrcEntry_Object = MibTableRow
vasPusSrcEntry = _VasPusSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1)
)
vasPusSrcEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasPusSrcIndex"),
)
if mibBuilder.loadTexts:
    vasPusSrcEntry.setStatus("current")
_VasPusSrcIndex_Type = Unsigned32
_VasPusSrcIndex_Object = MibTableColumn
vasPusSrcIndex = _VasPusSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 1),
    _VasPusSrcIndex_Type()
)
vasPusSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasPusSrcIndex.setStatus("current")
_VasPusSrcRowStatus_Type = RowStatus
_VasPusSrcRowStatus_Object = MibTableColumn
vasPusSrcRowStatus = _VasPusSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 2),
    _VasPusSrcRowStatus_Type()
)
vasPusSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRowStatus.setStatus("current")
_VasPusSrcName_Type = SnmpAdminString
_VasPusSrcName_Object = MibTableColumn
vasPusSrcName = _VasPusSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 3),
    _VasPusSrcName_Type()
)
vasPusSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcName.setStatus("current")


class _VasPusSrcPurpose_Type(SnmpAdminString):
    """Custom type vasPusSrcPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasPusSrcPurpose_Object = MibTableColumn
vasPusSrcPurpose = _VasPusSrcPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 4),
    _VasPusSrcPurpose_Type()
)
vasPusSrcPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcPurpose.setStatus("current")


class _VasPusSrcAdminStatus_Type(Integer32):
    """Custom type vasPusSrcAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPusSrcAdminStatus_Type.__name__ = "Integer32"
_VasPusSrcAdminStatus_Object = MibTableColumn
vasPusSrcAdminStatus = _VasPusSrcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 5),
    _VasPusSrcAdminStatus_Type()
)
vasPusSrcAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcAdminStatus.setStatus("current")


class _VasPusSrcOperStatus_Type(Integer32):
    """Custom type vasPusSrcOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPusSrcOperStatus_Type.__name__ = "Integer32"
_VasPusSrcOperStatus_Object = MibTableColumn
vasPusSrcOperStatus = _VasPusSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 6),
    _VasPusSrcOperStatus_Type()
)
vasPusSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcOperStatus.setStatus("current")
_VasPusSrcFailure_Type = SnmpAdminString
_VasPusSrcFailure_Object = MibTableColumn
vasPusSrcFailure = _VasPusSrcFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 7),
    _VasPusSrcFailure_Type()
)
vasPusSrcFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcFailure.setStatus("current")
_VasPusSrcLastChanged_Type = TimeStamp
_VasPusSrcLastChanged_Object = MibTableColumn
vasPusSrcLastChanged = _VasPusSrcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 8),
    _VasPusSrcLastChanged_Type()
)
vasPusSrcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcLastChanged.setStatus("current")
_VasPusSrcConnectionStatus_Type = VasConnectionStatus
_VasPusSrcConnectionStatus_Object = MibTableColumn
vasPusSrcConnectionStatus = _VasPusSrcConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 9),
    _VasPusSrcConnectionStatus_Type()
)
vasPusSrcConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcConnectionStatus.setStatus("current")
_VasPusSrcResetStatistics_Type = VasResetStatistics
_VasPusSrcResetStatistics_Object = MibTableColumn
vasPusSrcResetStatistics = _VasPusSrcResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 10),
    _VasPusSrcResetStatistics_Type()
)
vasPusSrcResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasPusSrcResetStatistics.setStatus("current")
_VasPusSrcStatsTrsp_Type = Unsigned32
_VasPusSrcStatsTrsp_Object = MibTableColumn
vasPusSrcStatsTrsp = _VasPusSrcStatsTrsp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 11),
    _VasPusSrcStatsTrsp_Type()
)
vasPusSrcStatsTrsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcStatsTrsp.setStatus("current")
_VasPusSrcRemoteInetType_Type = InetAddressType
_VasPusSrcRemoteInetType_Object = MibTableColumn
vasPusSrcRemoteInetType = _VasPusSrcRemoteInetType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 12),
    _VasPusSrcRemoteInetType_Type()
)
vasPusSrcRemoteInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcRemoteInetType.setStatus("current")
_VasPusSrcRemoteInetAddress_Type = InetAddress
_VasPusSrcRemoteInetAddress_Object = MibTableColumn
vasPusSrcRemoteInetAddress = _VasPusSrcRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 13),
    _VasPusSrcRemoteInetAddress_Type()
)
vasPusSrcRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSrcRemoteInetAddress.setStatus("current")
_VasPusSrcStreamId_Type = SnmpAdminString
_VasPusSrcStreamId_Object = MibTableColumn
vasPusSrcStreamId = _VasPusSrcStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 14),
    _VasPusSrcStreamId_Type()
)
vasPusSrcStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcStreamId.setStatus("current")
_VasPusSrcInputFrom_Type = RowPointer
_VasPusSrcInputFrom_Object = MibTableColumn
vasPusSrcInputFrom = _VasPusSrcInputFrom_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 15),
    _VasPusSrcInputFrom_Type()
)
vasPusSrcInputFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcInputFrom.setStatus("current")


class _VasPusSrcPassword_Type(SnmpAdminString):
    """Custom type vasPusSrcPassword based on SnmpAdminString"""
    defaultHexValue = ""


_VasPusSrcPassword_Object = MibTableColumn
vasPusSrcPassword = _VasPusSrcPassword_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 16),
    _VasPusSrcPassword_Type()
)
vasPusSrcPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcPassword.setStatus("current")


class _VasPusSrcRemoteHostType_Type(InetAddressType):
    """Custom type vasPusSrcRemoteHostType based on InetAddressType"""


_VasPusSrcRemoteHostType_Object = MibTableColumn
vasPusSrcRemoteHostType = _VasPusSrcRemoteHostType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 17),
    _VasPusSrcRemoteHostType_Type()
)
vasPusSrcRemoteHostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRemoteHostType.setStatus("current")


class _VasPusSrcRemoteHostAddress_Type(InetAddress):
    """Custom type vasPusSrcRemoteHostAddress based on InetAddress"""
    defaultHexValue = ""


_VasPusSrcRemoteHostAddress_Object = MibTableColumn
vasPusSrcRemoteHostAddress = _VasPusSrcRemoteHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 18),
    _VasPusSrcRemoteHostAddress_Type()
)
vasPusSrcRemoteHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRemoteHostAddress.setStatus("current")


class _VasPusSrcRemoteHostType2_Type(InetAddressType):
    """Custom type vasPusSrcRemoteHostType2 based on InetAddressType"""


_VasPusSrcRemoteHostType2_Object = MibTableColumn
vasPusSrcRemoteHostType2 = _VasPusSrcRemoteHostType2_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 19),
    _VasPusSrcRemoteHostType2_Type()
)
vasPusSrcRemoteHostType2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRemoteHostType2.setStatus("current")


class _VasPusSrcRemoteHostAddress2_Type(InetAddress):
    """Custom type vasPusSrcRemoteHostAddress2 based on InetAddress"""
    defaultHexValue = ""


_VasPusSrcRemoteHostAddress2_Object = MibTableColumn
vasPusSrcRemoteHostAddress2 = _VasPusSrcRemoteHostAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 20),
    _VasPusSrcRemoteHostAddress2_Type()
)
vasPusSrcRemoteHostAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRemoteHostAddress2.setStatus("current")


class _VasPusSrcRemotePort_Type(InetPortNumber):
    """Custom type vasPusSrcRemotePort based on InetPortNumber"""
    defaultValue = 2088


_VasPusSrcRemotePort_Object = MibTableColumn
vasPusSrcRemotePort = _VasPusSrcRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 21),
    _VasPusSrcRemotePort_Type()
)
vasPusSrcRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRemotePort.setStatus("current")


class _VasPusSrcLocalIfType_Type(InetAddressType):
    """Custom type vasPusSrcLocalIfType based on InetAddressType"""


_VasPusSrcLocalIfType_Object = MibTableColumn
vasPusSrcLocalIfType = _VasPusSrcLocalIfType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 22),
    _VasPusSrcLocalIfType_Type()
)
vasPusSrcLocalIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcLocalIfType.setStatus("current")


class _VasPusSrcLocalIfAddress_Type(InetAddress):
    """Custom type vasPusSrcLocalIfAddress based on InetAddress"""
    defaultHexValue = "00000000"


_VasPusSrcLocalIfAddress_Object = MibTableColumn
vasPusSrcLocalIfAddress = _VasPusSrcLocalIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 23),
    _VasPusSrcLocalIfAddress_Type()
)
vasPusSrcLocalIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcLocalIfAddress.setStatus("current")


class _VasPusSrcRetransmitBuffer_Type(Unsigned32):
    """Custom type vasPusSrcRetransmitBuffer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_VasPusSrcRetransmitBuffer_Type.__name__ = "Unsigned32"
_VasPusSrcRetransmitBuffer_Object = MibTableColumn
vasPusSrcRetransmitBuffer = _VasPusSrcRetransmitBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 24),
    _VasPusSrcRetransmitBuffer_Type()
)
vasPusSrcRetransmitBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcRetransmitBuffer.setStatus("current")


class _VasPusSrcFecMaxOverhead_Type(Unsigned32):
    """Custom type vasPusSrcFecMaxOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VasPusSrcFecMaxOverhead_Type.__name__ = "Unsigned32"
_VasPusSrcFecMaxOverhead_Object = MibTableColumn
vasPusSrcFecMaxOverhead = _VasPusSrcFecMaxOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 25),
    _VasPusSrcFecMaxOverhead_Type()
)
vasPusSrcFecMaxOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcFecMaxOverhead.setStatus("current")


class _VasPusSrcFecOptimize_Type(TruthValue):
    """Custom type vasPusSrcFecOptimize based on TruthValue"""


_VasPusSrcFecOptimize_Object = MibTableColumn
vasPusSrcFecOptimize = _VasPusSrcFecOptimize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 26),
    _VasPusSrcFecOptimize_Type()
)
vasPusSrcFecOptimize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcFecOptimize.setStatus("current")


class _VasPusSrcFecLatency_Type(Unsigned32):
    """Custom type vasPusSrcFecLatency based on Unsigned32"""
    defaultValue = 100


_VasPusSrcFecLatency_Object = MibTableColumn
vasPusSrcFecLatency = _VasPusSrcFecLatency_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 7, 1, 27),
    _VasPusSrcFecLatency_Type()
)
vasPusSrcFecLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSrcFecLatency.setStatus("current")
_VasPusSnkTable_Object = MibTable
vasPusSnkTable = _VasPusSnkTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8)
)
if mibBuilder.loadTexts:
    vasPusSnkTable.setStatus("current")
_VasPusSnkEntry_Object = MibTableRow
vasPusSnkEntry = _VasPusSnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1)
)
vasPusSnkEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasPusSnkIndex"),
)
if mibBuilder.loadTexts:
    vasPusSnkEntry.setStatus("current")
_VasPusSnkIndex_Type = Unsigned32
_VasPusSnkIndex_Object = MibTableColumn
vasPusSnkIndex = _VasPusSnkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 1),
    _VasPusSnkIndex_Type()
)
vasPusSnkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasPusSnkIndex.setStatus("current")
_VasPusSnkRowStatus_Type = RowStatus
_VasPusSnkRowStatus_Object = MibTableColumn
vasPusSnkRowStatus = _VasPusSnkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 2),
    _VasPusSnkRowStatus_Type()
)
vasPusSnkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkRowStatus.setStatus("current")
_VasPusSnkName_Type = SnmpAdminString
_VasPusSnkName_Object = MibTableColumn
vasPusSnkName = _VasPusSnkName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 3),
    _VasPusSnkName_Type()
)
vasPusSnkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkName.setStatus("current")


class _VasPusSnkPurpose_Type(SnmpAdminString):
    """Custom type vasPusSnkPurpose based on SnmpAdminString"""
    defaultHexValue = ""


_VasPusSnkPurpose_Object = MibTableColumn
vasPusSnkPurpose = _VasPusSnkPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 4),
    _VasPusSnkPurpose_Type()
)
vasPusSnkPurpose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkPurpose.setStatus("current")


class _VasPusSnkAdminStatus_Type(Integer32):
    """Custom type vasPusSnkAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPusSnkAdminStatus_Type.__name__ = "Integer32"
_VasPusSnkAdminStatus_Object = MibTableColumn
vasPusSnkAdminStatus = _VasPusSnkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 5),
    _VasPusSnkAdminStatus_Type()
)
vasPusSnkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkAdminStatus.setStatus("current")


class _VasPusSnkOperStatus_Type(Integer32):
    """Custom type vasPusSnkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VasPusSnkOperStatus_Type.__name__ = "Integer32"
_VasPusSnkOperStatus_Object = MibTableColumn
vasPusSnkOperStatus = _VasPusSnkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 6),
    _VasPusSnkOperStatus_Type()
)
vasPusSnkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkOperStatus.setStatus("current")
_VasPusSnkFailure_Type = SnmpAdminString
_VasPusSnkFailure_Object = MibTableColumn
vasPusSnkFailure = _VasPusSnkFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 7),
    _VasPusSnkFailure_Type()
)
vasPusSnkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkFailure.setStatus("current")
_VasPusSnkLastChanged_Type = TimeStamp
_VasPusSnkLastChanged_Object = MibTableColumn
vasPusSnkLastChanged = _VasPusSnkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 8),
    _VasPusSnkLastChanged_Type()
)
vasPusSnkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkLastChanged.setStatus("current")
_VasPusSnkConnectionStatus_Type = VasConnectionStatus
_VasPusSnkConnectionStatus_Object = MibTableColumn
vasPusSnkConnectionStatus = _VasPusSnkConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 9),
    _VasPusSnkConnectionStatus_Type()
)
vasPusSnkConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkConnectionStatus.setStatus("current")
_VasPusSnkResetStatistics_Type = VasResetStatistics
_VasPusSnkResetStatistics_Object = MibTableColumn
vasPusSnkResetStatistics = _VasPusSnkResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 10),
    _VasPusSnkResetStatistics_Type()
)
vasPusSnkResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vasPusSnkResetStatistics.setStatus("current")
_VasPusSnkStatsTrsp_Type = Unsigned32
_VasPusSnkStatsTrsp_Object = MibTableColumn
vasPusSnkStatsTrsp = _VasPusSnkStatsTrsp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 11),
    _VasPusSnkStatsTrsp_Type()
)
vasPusSnkStatsTrsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkStatsTrsp.setStatus("current")
_VasPusSnkStatsTr101_Type = Unsigned32
_VasPusSnkStatsTr101_Object = MibTableColumn
vasPusSnkStatsTr101 = _VasPusSnkStatsTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 12),
    _VasPusSnkStatsTr101_Type()
)
vasPusSnkStatsTr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkStatsTr101.setStatus("current")


class _VasPusSnkEnableTr101_Type(TruthValue):
    """Custom type vasPusSnkEnableTr101 based on TruthValue"""


_VasPusSnkEnableTr101_Object = MibTableColumn
vasPusSnkEnableTr101 = _VasPusSnkEnableTr101_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 13),
    _VasPusSnkEnableTr101_Type()
)
vasPusSnkEnableTr101.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkEnableTr101.setStatus("current")
_VasPusSnkRemoteInetType_Type = InetAddressType
_VasPusSnkRemoteInetType_Object = MibTableColumn
vasPusSnkRemoteInetType = _VasPusSnkRemoteInetType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 14),
    _VasPusSnkRemoteInetType_Type()
)
vasPusSnkRemoteInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkRemoteInetType.setStatus("current")
_VasPusSnkRemoteInetAddress_Type = InetAddress
_VasPusSnkRemoteInetAddress_Object = MibTableColumn
vasPusSnkRemoteInetAddress = _VasPusSnkRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 15),
    _VasPusSnkRemoteInetAddress_Type()
)
vasPusSnkRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasPusSnkRemoteInetAddress.setStatus("current")
_VasPusSnkStreamId_Type = SnmpAdminString
_VasPusSnkStreamId_Object = MibTableColumn
vasPusSnkStreamId = _VasPusSnkStreamId_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 16),
    _VasPusSnkStreamId_Type()
)
vasPusSnkStreamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkStreamId.setStatus("current")


class _VasPusSnkPassword_Type(SnmpAdminString):
    """Custom type vasPusSnkPassword based on SnmpAdminString"""
    defaultHexValue = ""


_VasPusSnkPassword_Object = MibTableColumn
vasPusSnkPassword = _VasPusSnkPassword_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 4, 8, 1, 17),
    _VasPusSnkPassword_Type()
)
vasPusSnkPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vasPusSnkPassword.setStatus("current")
_VasStatisticsGroup_ObjectIdentity = ObjectIdentity
vasStatisticsGroup = _VasStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5)
)
_VasUdpStatisticsTable_Object = MibTable
vasUdpStatisticsTable = _VasUdpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    vasUdpStatisticsTable.setStatus("current")
_VasUdpStatisticsEntry_Object = MibTableRow
vasUdpStatisticsEntry = _VasUdpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 1, 1)
)
vasUdpStatisticsEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasUdpStsIndex"),
)
if mibBuilder.loadTexts:
    vasUdpStatisticsEntry.setStatus("current")
_VasUdpStsIndex_Type = Unsigned32
_VasUdpStsIndex_Object = MibTableColumn
vasUdpStsIndex = _VasUdpStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 1, 1, 1),
    _VasUdpStsIndex_Type()
)
vasUdpStsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasUdpStsIndex.setStatus("current")
_VasUdpStsOwner_Type = RowPointer
_VasUdpStsOwner_Object = MibTableColumn
vasUdpStsOwner = _VasUdpStsOwner_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 1, 1, 2),
    _VasUdpStsOwner_Type()
)
vasUdpStsOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpStsOwner.setStatus("current")
_VasUdpStsBitrate_Type = Unsigned32
_VasUdpStsBitrate_Object = MibTableColumn
vasUdpStsBitrate = _VasUdpStsBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 1, 1, 3),
    _VasUdpStsBitrate_Type()
)
vasUdpStsBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasUdpStsBitrate.setStatus("current")
_VasTrspStatisticsTable_Object = MibTable
vasTrspStatisticsTable = _VasTrspStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    vasTrspStatisticsTable.setStatus("current")
_VasTrspStatisticsEntry_Object = MibTableRow
vasTrspStatisticsEntry = _VasTrspStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1)
)
vasTrspStatisticsEntry.setIndexNames(
    (0, "NETI-VAS-MIB", "vasTrspIndex"),
)
if mibBuilder.loadTexts:
    vasTrspStatisticsEntry.setStatus("current")
_VasTrspIndex_Type = Unsigned32
_VasTrspIndex_Object = MibTableColumn
vasTrspIndex = _VasTrspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 1),
    _VasTrspIndex_Type()
)
vasTrspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vasTrspIndex.setStatus("current")
_VasTrspOwner_Type = RowPointer
_VasTrspOwner_Object = MibTableColumn
vasTrspOwner = _VasTrspOwner_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 2),
    _VasTrspOwner_Type()
)
vasTrspOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspOwner.setStatus("current")
_VasTrspLastConnectionChange_Type = DateAndTime
_VasTrspLastConnectionChange_Object = MibTableColumn
vasTrspLastConnectionChange = _VasTrspLastConnectionChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 3),
    _VasTrspLastConnectionChange_Type()
)
vasTrspLastConnectionChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspLastConnectionChange.setStatus("current")
_VasTrspConnects_Type = Unsigned32
_VasTrspConnects_Object = MibTableColumn
vasTrspConnects = _VasTrspConnects_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 4),
    _VasTrspConnects_Type()
)
vasTrspConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspConnects.setStatus("current")
_VasTrspDisconnects_Type = Unsigned32
_VasTrspDisconnects_Object = MibTableColumn
vasTrspDisconnects = _VasTrspDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 5),
    _VasTrspDisconnects_Type()
)
vasTrspDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspDisconnects.setStatus("current")
_VasTrspNetRecvBitrate_Type = Unsigned32
_VasTrspNetRecvBitrate_Object = MibTableColumn
vasTrspNetRecvBitrate = _VasTrspNetRecvBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 6),
    _VasTrspNetRecvBitrate_Type()
)
vasTrspNetRecvBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvBitrate.setStatus("current")
_VasTrspNetRecvBurstLoss_Type = Counter32
_VasTrspNetRecvBurstLoss_Object = MibTableColumn
vasTrspNetRecvBurstLoss = _VasTrspNetRecvBurstLoss_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 7),
    _VasTrspNetRecvBurstLoss_Type()
)
vasTrspNetRecvBurstLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvBurstLoss.setStatus("current")
_VasTrspNetRecvOctets_Type = Counter64
_VasTrspNetRecvOctets_Object = MibTableColumn
vasTrspNetRecvOctets = _VasTrspNetRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 8),
    _VasTrspNetRecvOctets_Type()
)
vasTrspNetRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvOctets.setStatus("current")
_VasTrspNetRecvLatency_Type = Unsigned32
_VasTrspNetRecvLatency_Object = MibTableColumn
vasTrspNetRecvLatency = _VasTrspNetRecvLatency_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 9),
    _VasTrspNetRecvLatency_Type()
)
vasTrspNetRecvLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvLatency.setStatus("current")
_VasTrspNetRecvDropped_Type = Counter64
_VasTrspNetRecvDropped_Object = MibTableColumn
vasTrspNetRecvDropped = _VasTrspNetRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 10),
    _VasTrspNetRecvDropped_Type()
)
vasTrspNetRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvDropped.setStatus("current")
_VasTrspNetRecvJitter_Type = Unsigned32
_VasTrspNetRecvJitter_Object = MibTableColumn
vasTrspNetRecvJitter = _VasTrspNetRecvJitter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 11),
    _VasTrspNetRecvJitter_Type()
)
vasTrspNetRecvJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvJitter.setStatus("current")
_VasTrspNetRecvJitterRatio_Type = Integer32
_VasTrspNetRecvJitterRatio_Object = MibTableColumn
vasTrspNetRecvJitterRatio = _VasTrspNetRecvJitterRatio_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 12),
    _VasTrspNetRecvJitterRatio_Type()
)
vasTrspNetRecvJitterRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvJitterRatio.setStatus("current")
_VasTrspNetRecvOutOfOrder_Type = Counter64
_VasTrspNetRecvOutOfOrder_Object = MibTableColumn
vasTrspNetRecvOutOfOrder = _VasTrspNetRecvOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 13),
    _VasTrspNetRecvOutOfOrder_Type()
)
vasTrspNetRecvOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvOutOfOrder.setStatus("current")
_VasTrspNetRecvOverflows_Type = Counter64
_VasTrspNetRecvOverflows_Object = MibTableColumn
vasTrspNetRecvOverflows = _VasTrspNetRecvOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 14),
    _VasTrspNetRecvOverflows_Type()
)
vasTrspNetRecvOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvOverflows.setStatus("current")
_VasTrspNetRecvPackets_Type = Counter64
_VasTrspNetRecvPackets_Object = MibTableColumn
vasTrspNetRecvPackets = _VasTrspNetRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 15),
    _VasTrspNetRecvPackets_Type()
)
vasTrspNetRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvPackets.setStatus("current")
_VasTrspNetRecvPacketRate_Type = Unsigned32
_VasTrspNetRecvPacketRate_Object = MibTableColumn
vasTrspNetRecvPacketRate = _VasTrspNetRecvPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 16),
    _VasTrspNetRecvPacketRate_Type()
)
vasTrspNetRecvPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvPacketRate.setStatus("current")


class _VasTrspNetRecvPacketLoss_Type(Unsigned32):
    """Custom type vasTrspNetRecvPacketLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VasTrspNetRecvPacketLoss_Type.__name__ = "Unsigned32"
_VasTrspNetRecvPacketLoss_Object = MibTableColumn
vasTrspNetRecvPacketLoss = _VasTrspNetRecvPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 17),
    _VasTrspNetRecvPacketLoss_Type()
)
vasTrspNetRecvPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetRecvPacketLoss.setStatus("current")
_VasTrspArqRecvAlmostDropped_Type = Counter64
_VasTrspArqRecvAlmostDropped_Object = MibTableColumn
vasTrspArqRecvAlmostDropped = _VasTrspArqRecvAlmostDropped_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 18),
    _VasTrspArqRecvAlmostDropped_Type()
)
vasTrspArqRecvAlmostDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvAlmostDropped.setStatus("current")
_VasTrspArqRecvBitrate_Type = Unsigned32
_VasTrspArqRecvBitrate_Object = MibTableColumn
vasTrspArqRecvBitrate = _VasTrspArqRecvBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 19),
    _VasTrspArqRecvBitrate_Type()
)
vasTrspArqRecvBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvBitrate.setStatus("current")
_VasTrspArqRecvDropped_Type = Counter64
_VasTrspArqRecvDropped_Object = MibTableColumn
vasTrspArqRecvDropped = _VasTrspArqRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 20),
    _VasTrspArqRecvDropped_Type()
)
vasTrspArqRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvDropped.setStatus("current")
_VasTrspArqRecvDuplicates_Type = Counter64
_VasTrspArqRecvDuplicates_Object = MibTableColumn
vasTrspArqRecvDuplicates = _VasTrspArqRecvDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 21),
    _VasTrspArqRecvDuplicates_Type()
)
vasTrspArqRecvDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvDuplicates.setStatus("current")
_VasTrspArqRecvOverflows_Type = Counter64
_VasTrspArqRecvOverflows_Object = MibTableColumn
vasTrspArqRecvOverflows = _VasTrspArqRecvOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 22),
    _VasTrspArqRecvOverflows_Type()
)
vasTrspArqRecvOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvOverflows.setStatus("current")
_VasTrspArqRecvPackets_Type = Counter64
_VasTrspArqRecvPackets_Object = MibTableColumn
vasTrspArqRecvPackets = _VasTrspArqRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 23),
    _VasTrspArqRecvPackets_Type()
)
vasTrspArqRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvPackets.setStatus("current")
_VasTrspArqRecvRecovered_Type = Counter64
_VasTrspArqRecvRecovered_Object = MibTableColumn
vasTrspArqRecvRecovered = _VasTrspArqRecvRecovered_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 24),
    _VasTrspArqRecvRecovered_Type()
)
vasTrspArqRecvRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvRecovered.setStatus("current")
_VasTrspArqRecvRequests_Type = Counter64
_VasTrspArqRecvRequests_Object = MibTableColumn
vasTrspArqRecvRequests = _VasTrspArqRecvRequests_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 25),
    _VasTrspArqRecvRequests_Type()
)
vasTrspArqRecvRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqRecvRequests.setStatus("current")
_VasTrspNetSendBitrate_Type = Unsigned32
_VasTrspNetSendBitrate_Object = MibTableColumn
vasTrspNetSendBitrate = _VasTrspNetSendBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 26),
    _VasTrspNetSendBitrate_Type()
)
vasTrspNetSendBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendBitrate.setStatus("current")
_VasTrspNetSendOctets_Type = Counter64
_VasTrspNetSendOctets_Object = MibTableColumn
vasTrspNetSendOctets = _VasTrspNetSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 27),
    _VasTrspNetSendOctets_Type()
)
vasTrspNetSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendOctets.setStatus("current")
_VasTrspNetSendLimit_Type = Unsigned32
_VasTrspNetSendLimit_Object = MibTableColumn
vasTrspNetSendLimit = _VasTrspNetSendLimit_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 28),
    _VasTrspNetSendLimit_Type()
)
vasTrspNetSendLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendLimit.setStatus("current")
_VasTrspNetSendPackets_Type = Counter64
_VasTrspNetSendPackets_Object = MibTableColumn
vasTrspNetSendPackets = _VasTrspNetSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 29),
    _VasTrspNetSendPackets_Type()
)
vasTrspNetSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendPackets.setStatus("current")
_VasTrspNetSendRtt_Type = Unsigned32
_VasTrspNetSendRtt_Object = MibTableColumn
vasTrspNetSendRtt = _VasTrspNetSendRtt_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 30),
    _VasTrspNetSendRtt_Type()
)
vasTrspNetSendRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendRtt.setStatus("current")
_VasTrspNetSendErrors_Type = Counter64
_VasTrspNetSendErrors_Object = MibTableColumn
vasTrspNetSendErrors = _VasTrspNetSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 31),
    _VasTrspNetSendErrors_Type()
)
vasTrspNetSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspNetSendErrors.setStatus("current")
_VasTrspArqSendBitrate_Type = Unsigned32
_VasTrspArqSendBitrate_Object = MibTableColumn
vasTrspArqSendBitrate = _VasTrspArqSendBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 32),
    _VasTrspArqSendBitrate_Type()
)
vasTrspArqSendBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqSendBitrate.setStatus("current")
_VasTrspArqSendIgnored_Type = Counter64
_VasTrspArqSendIgnored_Object = MibTableColumn
vasTrspArqSendIgnored = _VasTrspArqSendIgnored_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 33),
    _VasTrspArqSendIgnored_Type()
)
vasTrspArqSendIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqSendIgnored.setStatus("current")
_VasTrspArqSendMissed_Type = Counter64
_VasTrspArqSendMissed_Object = MibTableColumn
vasTrspArqSendMissed = _VasTrspArqSendMissed_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 34),
    _VasTrspArqSendMissed_Type()
)
vasTrspArqSendMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqSendMissed.setStatus("current")
_VasTrspArqSendPacketRate_Type = Unsigned32
_VasTrspArqSendPacketRate_Object = MibTableColumn
vasTrspArqSendPacketRate = _VasTrspArqSendPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 35),
    _VasTrspArqSendPacketRate_Type()
)
vasTrspArqSendPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqSendPacketRate.setStatus("current")
_VasTrspArqSendPackets_Type = Counter64
_VasTrspArqSendPackets_Object = MibTableColumn
vasTrspArqSendPackets = _VasTrspArqSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 36),
    _VasTrspArqSendPackets_Type()
)
vasTrspArqSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspArqSendPackets.setStatus("current")
_VasTrspFecRecvBitrate_Type = Unsigned32
_VasTrspFecRecvBitrate_Object = MibTableColumn
vasTrspFecRecvBitrate = _VasTrspFecRecvBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 37),
    _VasTrspFecRecvBitrate_Type()
)
vasTrspFecRecvBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecRecvBitrate.setStatus("current")
_VasTrspFecRecvPacketRate_Type = Unsigned32
_VasTrspFecRecvPacketRate_Object = MibTableColumn
vasTrspFecRecvPacketRate = _VasTrspFecRecvPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 38),
    _VasTrspFecRecvPacketRate_Type()
)
vasTrspFecRecvPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecRecvPacketRate.setStatus("current")
_VasTrspFecRecvPackets_Type = Counter64
_VasTrspFecRecvPackets_Object = MibTableColumn
vasTrspFecRecvPackets = _VasTrspFecRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 39),
    _VasTrspFecRecvPackets_Type()
)
vasTrspFecRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecRecvPackets.setStatus("current")
_VasTrspFecRecvRecovered_Type = Counter64
_VasTrspFecRecvRecovered_Object = MibTableColumn
vasTrspFecRecvRecovered = _VasTrspFecRecvRecovered_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 40),
    _VasTrspFecRecvRecovered_Type()
)
vasTrspFecRecvRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecRecvRecovered.setStatus("current")
_VasTrspFecSendBitrate_Type = Unsigned32
_VasTrspFecSendBitrate_Object = MibTableColumn
vasTrspFecSendBitrate = _VasTrspFecSendBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 41),
    _VasTrspFecSendBitrate_Type()
)
vasTrspFecSendBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecSendBitrate.setStatus("current")
_VasTrspFecSendPacketRate_Type = Unsigned32
_VasTrspFecSendPacketRate_Object = MibTableColumn
vasTrspFecSendPacketRate = _VasTrspFecSendPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 42),
    _VasTrspFecSendPacketRate_Type()
)
vasTrspFecSendPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecSendPacketRate.setStatus("current")
_VasTrspFecSendPackets_Type = Counter64
_VasTrspFecSendPackets_Object = MibTableColumn
vasTrspFecSendPackets = _VasTrspFecSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 5, 5, 2, 1, 43),
    _VasTrspFecSendPackets_Type()
)
vasTrspFecSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vasTrspFecSendPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-VAS-MIB",
    **{"VasConnectionStatus": VasConnectionStatus,
       "VasCipher": VasCipher,
       "VasResetStatistics": VasResetStatistics,
       "VasVideoFormat": VasVideoFormat,
       "netinsight": netinsight,
       "netiGeneric": netiGeneric,
       "netiVasMIB": netiVasMIB,
       "vasInterfaceGroup": vasInterfaceGroup,
       "vasIfTable": vasIfTable,
       "vasIfEntry": vasIfEntry,
       "vasIfIndex": vasIfIndex,
       "vasIfName": vasIfName,
       "vasIfPurpose": vasIfPurpose,
       "vasIfAdminStatus": vasIfAdminStatus,
       "vasIfOperStatus": vasIfOperStatus,
       "vasIfFailure": vasIfFailure,
       "vasIfLastChanged": vasIfLastChanged,
       "vasIfResetStatistics": vasIfResetStatistics,
       "vasIfInputFrom": vasIfInputFrom,
       "vasIfPortMode": vasIfPortMode,
       "vasIfActiveFormat": vasIfActiveFormat,
       "vasEncoderPipeGroup": vasEncoderPipeGroup,
       "vasEncPipeTable": vasEncPipeTable,
       "vasEncPipeEntry": vasEncPipeEntry,
       "vasEncPipeIndex": vasEncPipeIndex,
       "vasEncPipeRowStatus": vasEncPipeRowStatus,
       "vasEncPipeName": vasEncPipeName,
       "vasEncPipePurpose": vasEncPipePurpose,
       "vasEncPipeAdminStatus": vasEncPipeAdminStatus,
       "vasEncPipeOperStatus": vasEncPipeOperStatus,
       "vasEncPipeFailure": vasEncPipeFailure,
       "vasEncPipeLastChanged": vasEncPipeLastChanged,
       "vasEncPipeResetStatistics": vasEncPipeResetStatistics,
       "vasEncPipeStatsTr101": vasEncPipeStatsTr101,
       "vasEncPipeEnableTr101": vasEncPipeEnableTr101,
       "vasEncPipeInputFrom": vasEncPipeInputFrom,
       "vasEncPipeCipher": vasEncPipeCipher,
       "vasEncPipeEncryptKey": vasEncPipeEncryptKey,
       "vasEncPipeProcessedFrames": vasEncPipeProcessedFrames,
       "vasEncPipeCurrentTsBitrate": vasEncPipeCurrentTsBitrate,
       "vasEncPipeVideoBitrate": vasEncPipeVideoBitrate,
       "vasDecoderPipeGroup": vasDecoderPipeGroup,
       "vasDecPipeTable": vasDecPipeTable,
       "vasDecPipeEntry": vasDecPipeEntry,
       "vasDecPipeIndex": vasDecPipeIndex,
       "vasDecPipeRowStatus": vasDecPipeRowStatus,
       "vasDecPipeName": vasDecPipeName,
       "vasDecPipePurpose": vasDecPipePurpose,
       "vasDecPipeAdminStatus": vasDecPipeAdminStatus,
       "vasDecPipeOperStatus": vasDecPipeOperStatus,
       "vasDecPipeFailure": vasDecPipeFailure,
       "vasDecPipeLastChanged": vasDecPipeLastChanged,
       "vasDecPipeResetStatistics": vasDecPipeResetStatistics,
       "vasDecPipeInputFrom": vasDecPipeInputFrom,
       "vasDecPipeCipher": vasDecPipeCipher,
       "vasDecPipeDecryptKey": vasDecPipeDecryptKey,
       "vasDecPipeProcessedFrames": vasDecPipeProcessedFrames,
       "vasDecPipeCurrentTsBitrate": vasDecPipeCurrentTsBitrate,
       "vasDecPipeVideoBitrate": vasDecPipeVideoBitrate,
       "vasTransportsGroup": vasTransportsGroup,
       "vasStreamPort": vasStreamPort,
       "vasUdpSrcTable": vasUdpSrcTable,
       "vasUdpSrcEntry": vasUdpSrcEntry,
       "vasUdpSrcIndex": vasUdpSrcIndex,
       "vasUdpSrcRowStatus": vasUdpSrcRowStatus,
       "vasUdpSrcName": vasUdpSrcName,
       "vasUdpSrcPurpose": vasUdpSrcPurpose,
       "vasUdpSrcAdminStatus": vasUdpSrcAdminStatus,
       "vasUdpSrcOperStatus": vasUdpSrcOperStatus,
       "vasUdpSrcFailure": vasUdpSrcFailure,
       "vasUdpSrcLastChanged": vasUdpSrcLastChanged,
       "vasUdpSrcConnectionStatus": vasUdpSrcConnectionStatus,
       "vasUdpSrcResetStatistics": vasUdpSrcResetStatistics,
       "vasUdpSrcStatsUdp": vasUdpSrcStatsUdp,
       "vasUdpSrcInputFrom": vasUdpSrcInputFrom,
       "vasUdpSrcRemoteHostType": vasUdpSrcRemoteHostType,
       "vasUdpSrcRemoteHostAddress": vasUdpSrcRemoteHostAddress,
       "vasUdpSrcRemotePort": vasUdpSrcRemotePort,
       "vasUdpSrcLocalIfType": vasUdpSrcLocalIfType,
       "vasUdpSrcLocalIfAddress": vasUdpSrcLocalIfAddress,
       "vasUdpSrcLocalPort": vasUdpSrcLocalPort,
       "vasUdpSrcCipher": vasUdpSrcCipher,
       "vasUdpSrcDecryptKey": vasUdpSrcDecryptKey,
       "vasUdpSrcTtl": vasUdpSrcTtl,
       "vasUdpSrcDontFragment": vasUdpSrcDontFragment,
       "vasUdpSnkTable": vasUdpSnkTable,
       "vasUdpSnkEntry": vasUdpSnkEntry,
       "vasUdpSnkIndex": vasUdpSnkIndex,
       "vasUdpSnkRowStatus": vasUdpSnkRowStatus,
       "vasUdpSnkName": vasUdpSnkName,
       "vasUdpSnkPurpose": vasUdpSnkPurpose,
       "vasUdpSnkAdminStatus": vasUdpSnkAdminStatus,
       "vasUdpSnkOperStatus": vasUdpSnkOperStatus,
       "vasUdpSnkFailure": vasUdpSnkFailure,
       "vasUdpSnkLastChanged": vasUdpSnkLastChanged,
       "vasUdpSnkConnectionStatus": vasUdpSnkConnectionStatus,
       "vasUdpSnkResetStatistics": vasUdpSnkResetStatistics,
       "vasUdpSnkStatsUdp": vasUdpSnkStatsUdp,
       "vasUdpSnkStatsTr101": vasUdpSnkStatsTr101,
       "vasUdpSnkEnableTr101": vasUdpSnkEnableTr101,
       "vasUdpSnkRemoteInetType": vasUdpSnkRemoteInetType,
       "vasUdpSnkRemoteInetAddress": vasUdpSnkRemoteInetAddress,
       "vasUdpSnkLocalIfType": vasUdpSnkLocalIfType,
       "vasUdpSnkLocalIfAddress": vasUdpSnkLocalIfAddress,
       "vasUdpSnkLocalPort": vasUdpSnkLocalPort,
       "vasUdpSnkCipher": vasUdpSnkCipher,
       "vasUdpSnkEncryptKey": vasUdpSnkEncryptKey,
       "vasUdpSnkMcastIpType": vasUdpSnkMcastIpType,
       "vasUdpSnkMcastIp": vasUdpSnkMcastIp,
       "vasUdpSnkSsmSourceIp": vasUdpSnkSsmSourceIp,
       "vasUdpSnkCompress": vasUdpSnkCompress,
       "vasPulSrcTable": vasPulSrcTable,
       "vasPulSrcEntry": vasPulSrcEntry,
       "vasPulSrcIndex": vasPulSrcIndex,
       "vasPulSrcRowStatus": vasPulSrcRowStatus,
       "vasPulSrcName": vasPulSrcName,
       "vasPulSrcPurpose": vasPulSrcPurpose,
       "vasPulSrcAdminStatus": vasPulSrcAdminStatus,
       "vasPulSrcOperStatus": vasPulSrcOperStatus,
       "vasPulSrcFailure": vasPulSrcFailure,
       "vasPulSrcLastChanged": vasPulSrcLastChanged,
       "vasPulSrcConnectionStatus": vasPulSrcConnectionStatus,
       "vasPulSrcResetStatistics": vasPulSrcResetStatistics,
       "vasPulSrcStatsTrsp": vasPulSrcStatsTrsp,
       "vasPulSrcRemoteInetType": vasPulSrcRemoteInetType,
       "vasPulSrcRemoteInetAddress": vasPulSrcRemoteInetAddress,
       "vasPulSrcStreamId": vasPulSrcStreamId,
       "vasPulSrcInputFrom": vasPulSrcInputFrom,
       "vasPulSrcRemoteId": vasPulSrcRemoteId,
       "vasPulSrcPassword": vasPulSrcPassword,
       "vasMpuSrcTable": vasMpuSrcTable,
       "vasMpuSrcEntry": vasMpuSrcEntry,
       "vasMpuSrcIndex": vasMpuSrcIndex,
       "vasMpuSrcRowStatus": vasMpuSrcRowStatus,
       "vasMpuSrcName": vasMpuSrcName,
       "vasMpuSrcPurpose": vasMpuSrcPurpose,
       "vasMpuSrcAdminStatus": vasMpuSrcAdminStatus,
       "vasMpuSrcOperStatus": vasMpuSrcOperStatus,
       "vasMpuSrcFailure": vasMpuSrcFailure,
       "vasMpuSrcLastChanged": vasMpuSrcLastChanged,
       "vasMpuSrcStreamId": vasMpuSrcStreamId,
       "vasMpuSrcInputFrom": vasMpuSrcInputFrom,
       "vasPulSnkTable": vasPulSnkTable,
       "vasPulSnkEntry": vasPulSnkEntry,
       "vasPulSnkIndex": vasPulSnkIndex,
       "vasPulSnkRowStatus": vasPulSnkRowStatus,
       "vasPulSnkName": vasPulSnkName,
       "vasPulSnkPurpose": vasPulSnkPurpose,
       "vasPulSnkAdminStatus": vasPulSnkAdminStatus,
       "vasPulSnkOperStatus": vasPulSnkOperStatus,
       "vasPulSnkFailure": vasPulSnkFailure,
       "vasPulSnkLastChanged": vasPulSnkLastChanged,
       "vasPulSnkConnectionStatus": vasPulSnkConnectionStatus,
       "vasPulSnkResetStatistics": vasPulSnkResetStatistics,
       "vasPulSnkStatsTrsp": vasPulSnkStatsTrsp,
       "vasPulSnkStatsTr101": vasPulSnkStatsTr101,
       "vasPulSnkEnableTr101": vasPulSnkEnableTr101,
       "vasPulSnkRemoteInetType": vasPulSnkRemoteInetType,
       "vasPulSnkRemoteInetAddress": vasPulSnkRemoteInetAddress,
       "vasPulSnkStreamId": vasPulSnkStreamId,
       "vasPulSnkPassword": vasPulSnkPassword,
       "vasPulSnkRemoteHostType": vasPulSnkRemoteHostType,
       "vasPulSnkRemoteHostAddress": vasPulSnkRemoteHostAddress,
       "vasPulSnkRemoteHostType2": vasPulSnkRemoteHostType2,
       "vasPulSnkRemoteHostAddress2": vasPulSnkRemoteHostAddress2,
       "vasPulSnkRemotePort": vasPulSnkRemotePort,
       "vasPulSnkRetransmitBuffer": vasPulSnkRetransmitBuffer,
       "vasPulSnkFecMaxOverhead": vasPulSnkFecMaxOverhead,
       "vasPulSnkFecOptimize": vasPulSnkFecOptimize,
       "vasPulSnkFecLatency": vasPulSnkFecLatency,
       "vasPusSrcTable": vasPusSrcTable,
       "vasPusSrcEntry": vasPusSrcEntry,
       "vasPusSrcIndex": vasPusSrcIndex,
       "vasPusSrcRowStatus": vasPusSrcRowStatus,
       "vasPusSrcName": vasPusSrcName,
       "vasPusSrcPurpose": vasPusSrcPurpose,
       "vasPusSrcAdminStatus": vasPusSrcAdminStatus,
       "vasPusSrcOperStatus": vasPusSrcOperStatus,
       "vasPusSrcFailure": vasPusSrcFailure,
       "vasPusSrcLastChanged": vasPusSrcLastChanged,
       "vasPusSrcConnectionStatus": vasPusSrcConnectionStatus,
       "vasPusSrcResetStatistics": vasPusSrcResetStatistics,
       "vasPusSrcStatsTrsp": vasPusSrcStatsTrsp,
       "vasPusSrcRemoteInetType": vasPusSrcRemoteInetType,
       "vasPusSrcRemoteInetAddress": vasPusSrcRemoteInetAddress,
       "vasPusSrcStreamId": vasPusSrcStreamId,
       "vasPusSrcInputFrom": vasPusSrcInputFrom,
       "vasPusSrcPassword": vasPusSrcPassword,
       "vasPusSrcRemoteHostType": vasPusSrcRemoteHostType,
       "vasPusSrcRemoteHostAddress": vasPusSrcRemoteHostAddress,
       "vasPusSrcRemoteHostType2": vasPusSrcRemoteHostType2,
       "vasPusSrcRemoteHostAddress2": vasPusSrcRemoteHostAddress2,
       "vasPusSrcRemotePort": vasPusSrcRemotePort,
       "vasPusSrcLocalIfType": vasPusSrcLocalIfType,
       "vasPusSrcLocalIfAddress": vasPusSrcLocalIfAddress,
       "vasPusSrcRetransmitBuffer": vasPusSrcRetransmitBuffer,
       "vasPusSrcFecMaxOverhead": vasPusSrcFecMaxOverhead,
       "vasPusSrcFecOptimize": vasPusSrcFecOptimize,
       "vasPusSrcFecLatency": vasPusSrcFecLatency,
       "vasPusSnkTable": vasPusSnkTable,
       "vasPusSnkEntry": vasPusSnkEntry,
       "vasPusSnkIndex": vasPusSnkIndex,
       "vasPusSnkRowStatus": vasPusSnkRowStatus,
       "vasPusSnkName": vasPusSnkName,
       "vasPusSnkPurpose": vasPusSnkPurpose,
       "vasPusSnkAdminStatus": vasPusSnkAdminStatus,
       "vasPusSnkOperStatus": vasPusSnkOperStatus,
       "vasPusSnkFailure": vasPusSnkFailure,
       "vasPusSnkLastChanged": vasPusSnkLastChanged,
       "vasPusSnkConnectionStatus": vasPusSnkConnectionStatus,
       "vasPusSnkResetStatistics": vasPusSnkResetStatistics,
       "vasPusSnkStatsTrsp": vasPusSnkStatsTrsp,
       "vasPusSnkStatsTr101": vasPusSnkStatsTr101,
       "vasPusSnkEnableTr101": vasPusSnkEnableTr101,
       "vasPusSnkRemoteInetType": vasPusSnkRemoteInetType,
       "vasPusSnkRemoteInetAddress": vasPusSnkRemoteInetAddress,
       "vasPusSnkStreamId": vasPusSnkStreamId,
       "vasPusSnkPassword": vasPusSnkPassword,
       "vasStatisticsGroup": vasStatisticsGroup,
       "vasUdpStatisticsTable": vasUdpStatisticsTable,
       "vasUdpStatisticsEntry": vasUdpStatisticsEntry,
       "vasUdpStsIndex": vasUdpStsIndex,
       "vasUdpStsOwner": vasUdpStsOwner,
       "vasUdpStsBitrate": vasUdpStsBitrate,
       "vasTrspStatisticsTable": vasTrspStatisticsTable,
       "vasTrspStatisticsEntry": vasTrspStatisticsEntry,
       "vasTrspIndex": vasTrspIndex,
       "vasTrspOwner": vasTrspOwner,
       "vasTrspLastConnectionChange": vasTrspLastConnectionChange,
       "vasTrspConnects": vasTrspConnects,
       "vasTrspDisconnects": vasTrspDisconnects,
       "vasTrspNetRecvBitrate": vasTrspNetRecvBitrate,
       "vasTrspNetRecvBurstLoss": vasTrspNetRecvBurstLoss,
       "vasTrspNetRecvOctets": vasTrspNetRecvOctets,
       "vasTrspNetRecvLatency": vasTrspNetRecvLatency,
       "vasTrspNetRecvDropped": vasTrspNetRecvDropped,
       "vasTrspNetRecvJitter": vasTrspNetRecvJitter,
       "vasTrspNetRecvJitterRatio": vasTrspNetRecvJitterRatio,
       "vasTrspNetRecvOutOfOrder": vasTrspNetRecvOutOfOrder,
       "vasTrspNetRecvOverflows": vasTrspNetRecvOverflows,
       "vasTrspNetRecvPackets": vasTrspNetRecvPackets,
       "vasTrspNetRecvPacketRate": vasTrspNetRecvPacketRate,
       "vasTrspNetRecvPacketLoss": vasTrspNetRecvPacketLoss,
       "vasTrspArqRecvAlmostDropped": vasTrspArqRecvAlmostDropped,
       "vasTrspArqRecvBitrate": vasTrspArqRecvBitrate,
       "vasTrspArqRecvDropped": vasTrspArqRecvDropped,
       "vasTrspArqRecvDuplicates": vasTrspArqRecvDuplicates,
       "vasTrspArqRecvOverflows": vasTrspArqRecvOverflows,
       "vasTrspArqRecvPackets": vasTrspArqRecvPackets,
       "vasTrspArqRecvRecovered": vasTrspArqRecvRecovered,
       "vasTrspArqRecvRequests": vasTrspArqRecvRequests,
       "vasTrspNetSendBitrate": vasTrspNetSendBitrate,
       "vasTrspNetSendOctets": vasTrspNetSendOctets,
       "vasTrspNetSendLimit": vasTrspNetSendLimit,
       "vasTrspNetSendPackets": vasTrspNetSendPackets,
       "vasTrspNetSendRtt": vasTrspNetSendRtt,
       "vasTrspNetSendErrors": vasTrspNetSendErrors,
       "vasTrspArqSendBitrate": vasTrspArqSendBitrate,
       "vasTrspArqSendIgnored": vasTrspArqSendIgnored,
       "vasTrspArqSendMissed": vasTrspArqSendMissed,
       "vasTrspArqSendPacketRate": vasTrspArqSendPacketRate,
       "vasTrspArqSendPackets": vasTrspArqSendPackets,
       "vasTrspFecRecvBitrate": vasTrspFecRecvBitrate,
       "vasTrspFecRecvPacketRate": vasTrspFecRecvPacketRate,
       "vasTrspFecRecvPackets": vasTrspFecRecvPackets,
       "vasTrspFecRecvRecovered": vasTrspFecRecvRecovered,
       "vasTrspFecSendBitrate": vasTrspFecSendBitrate,
       "vasTrspFecSendPacketRate": vasTrspFecSendPacketRate,
       "vasTrspFecSendPackets": vasTrspFecSendPackets}
)
