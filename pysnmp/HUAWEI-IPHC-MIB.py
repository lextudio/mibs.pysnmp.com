# SNMP MIB module (HUAWEI-IPHC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPHC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:06 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwIphcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWCompressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enableEcRtpCompress", 4),
          ("enableRtpCompress", 3),
          ("enableTcpCompress", 2),
          ("enableUdpCompressOnly", 5),
          ("enableUdpandRtpCompressOnly", 6),
          ("withoutCompress", 1))
    )



class HWCompressFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("nonstandard", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwIphcInfoObjects_ObjectIdentity = ObjectIdentity
hwIphcInfoObjects = _HwIphcInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1)
)
_HwIphcTcpConfigTable_Object = MibTable
hwIphcTcpConfigTable = _HwIphcTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1)
)
if mibBuilder.loadTexts:
    hwIphcTcpConfigTable.setStatus("current")
_HwIphcTcpConfigEntry_Object = MibTableRow
hwIphcTcpConfigEntry = _HwIphcTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1)
)
hwIphcTcpConfigEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcTcpConfigEntry.setStatus("current")
_HwIphcTcpIfIndex_Type = Integer32
_HwIphcTcpIfIndex_Object = MibTableColumn
hwIphcTcpIfIndex = _HwIphcTcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 1),
    _HwIphcTcpIfIndex_Type()
)
hwIphcTcpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIphcTcpIfIndex.setStatus("current")
_HwIphcTcpEnable_Type = HWCompressType
_HwIphcTcpEnable_Object = MibTableColumn
hwIphcTcpEnable = _HwIphcTcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 2),
    _HwIphcTcpEnable_Type()
)
hwIphcTcpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcTcpEnable.setStatus("current")
_HwIphcTcpConnnectionNumber_Type = Integer32
_HwIphcTcpConnnectionNumber_Object = MibTableColumn
hwIphcTcpConnnectionNumber = _HwIphcTcpConnnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 3),
    _HwIphcTcpConnnectionNumber_Type()
)
hwIphcTcpConnnectionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcTcpConnnectionNumber.setStatus("current")
_HwIphcTcpRowStatus_Type = RowStatus
_HwIphcTcpRowStatus_Object = MibTableColumn
hwIphcTcpRowStatus = _HwIphcTcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 1, 1, 4),
    _HwIphcTcpRowStatus_Type()
)
hwIphcTcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcTcpRowStatus.setStatus("current")
_HwIphcTcpConfigEffectTable_Object = MibTable
hwIphcTcpConfigEffectTable = _HwIphcTcpConfigEffectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2)
)
if mibBuilder.loadTexts:
    hwIphcTcpConfigEffectTable.setStatus("current")
_HwIphcTcpConfigEffectEntry_Object = MibTableRow
hwIphcTcpConfigEffectEntry = _HwIphcTcpConfigEffectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1)
)
hwIphcTcpConfigEffectEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcTcpConfigEffectEntry.setStatus("current")
_HwIphcTcpEffectEnable_Type = HWCompressType
_HwIphcTcpEffectEnable_Object = MibTableColumn
hwIphcTcpEffectEnable = _HwIphcTcpEffectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1, 1),
    _HwIphcTcpEffectEnable_Type()
)
hwIphcTcpEffectEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpEffectEnable.setStatus("current")
_HwIphcTcpEffectConnnectionNumber_Type = Integer32
_HwIphcTcpEffectConnnectionNumber_Object = MibTableColumn
hwIphcTcpEffectConnnectionNumber = _HwIphcTcpEffectConnnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 2, 1, 2),
    _HwIphcTcpEffectConnnectionNumber_Type()
)
hwIphcTcpEffectConnnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpEffectConnnectionNumber.setStatus("current")
_HwIphcRtpConfigTable_Object = MibTable
hwIphcRtpConfigTable = _HwIphcRtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3)
)
if mibBuilder.loadTexts:
    hwIphcRtpConfigTable.setStatus("current")
_HwIphcRtpConfigEntry_Object = MibTableRow
hwIphcRtpConfigEntry = _HwIphcRtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1)
)
hwIphcRtpConfigEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcRtpConfigEntry.setStatus("current")
_HwIphcRtpIfIndex_Type = Integer32
_HwIphcRtpIfIndex_Object = MibTableColumn
hwIphcRtpIfIndex = _HwIphcRtpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 1),
    _HwIphcRtpIfIndex_Type()
)
hwIphcRtpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIphcRtpIfIndex.setStatus("current")
_HwIphcRtpEnable_Type = HWCompressType
_HwIphcRtpEnable_Object = MibTableColumn
hwIphcRtpEnable = _HwIphcRtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 2),
    _HwIphcRtpEnable_Type()
)
hwIphcRtpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcRtpEnable.setStatus("current")
_HwIphcRtpConnnectionNumber_Type = Integer32
_HwIphcRtpConnnectionNumber_Object = MibTableColumn
hwIphcRtpConnnectionNumber = _HwIphcRtpConnnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 3),
    _HwIphcRtpConnnectionNumber_Type()
)
hwIphcRtpConnnectionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcRtpConnnectionNumber.setStatus("current")
_HwIphcRtpNValue_Type = Integer32
_HwIphcRtpNValue_Object = MibTableColumn
hwIphcRtpNValue = _HwIphcRtpNValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 4),
    _HwIphcRtpNValue_Type()
)
hwIphcRtpNValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcRtpNValue.setStatus("current")
_HwIphcRtpFormatType_Type = HWCompressFormat
_HwIphcRtpFormatType_Object = MibTableColumn
hwIphcRtpFormatType = _HwIphcRtpFormatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 5),
    _HwIphcRtpFormatType_Type()
)
hwIphcRtpFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcRtpFormatType.setStatus("current")
_HwIphcRtpRowStatus_Type = RowStatus
_HwIphcRtpRowStatus_Object = MibTableColumn
hwIphcRtpRowStatus = _HwIphcRtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 3, 1, 6),
    _HwIphcRtpRowStatus_Type()
)
hwIphcRtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIphcRtpRowStatus.setStatus("current")
_HwIphcRtpConfigEffectTable_Object = MibTable
hwIphcRtpConfigEffectTable = _HwIphcRtpConfigEffectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4)
)
if mibBuilder.loadTexts:
    hwIphcRtpConfigEffectTable.setStatus("current")
_HwIphcRtpConfigEffectEntry_Object = MibTableRow
hwIphcRtpConfigEffectEntry = _HwIphcRtpConfigEffectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1)
)
hwIphcRtpConfigEffectEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcRtpConfigEffectEntry.setStatus("current")
_HwIphcRtpEffectEnable_Type = HWCompressType
_HwIphcRtpEffectEnable_Object = MibTableColumn
hwIphcRtpEffectEnable = _HwIphcRtpEffectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 1),
    _HwIphcRtpEffectEnable_Type()
)
hwIphcRtpEffectEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpEffectEnable.setStatus("current")
_HwIphcRtpEffectConnnectionNumber_Type = Integer32
_HwIphcRtpEffectConnnectionNumber_Object = MibTableColumn
hwIphcRtpEffectConnnectionNumber = _HwIphcRtpEffectConnnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 2),
    _HwIphcRtpEffectConnnectionNumber_Type()
)
hwIphcRtpEffectConnnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpEffectConnnectionNumber.setStatus("current")
_HwIphcRtpEffectNValue_Type = Integer32
_HwIphcRtpEffectNValue_Object = MibTableColumn
hwIphcRtpEffectNValue = _HwIphcRtpEffectNValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 1, 4, 1, 3),
    _HwIphcRtpEffectNValue_Type()
)
hwIphcRtpEffectNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpEffectNValue.setStatus("current")
_HwIphcStatisticsObjects_ObjectIdentity = ObjectIdentity
hwIphcStatisticsObjects = _HwIphcStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2)
)
_HwIphcTcpRunInfoTable_Object = MibTable
hwIphcTcpRunInfoTable = _HwIphcTcpRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1)
)
if mibBuilder.loadTexts:
    hwIphcTcpRunInfoTable.setStatus("current")
_HwIphcTcpRunInfoEntry_Object = MibTableRow
hwIphcTcpRunInfoEntry = _HwIphcTcpRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1)
)
hwIphcTcpRunInfoEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcTcpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcTcpRunInfoEntry.setStatus("current")
_HwIphcTcpSentTotalPackets_Type = Counter64
_HwIphcTcpSentTotalPackets_Object = MibTableColumn
hwIphcTcpSentTotalPackets = _HwIphcTcpSentTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 1),
    _HwIphcTcpSentTotalPackets_Type()
)
hwIphcTcpSentTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpSentTotalPackets.setStatus("current")
_HwIphcTcpSentTotalBytes_Type = Counter64
_HwIphcTcpSentTotalBytes_Object = MibTableColumn
hwIphcTcpSentTotalBytes = _HwIphcTcpSentTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 2),
    _HwIphcTcpSentTotalBytes_Type()
)
hwIphcTcpSentTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpSentTotalBytes.setStatus("current")
_HwIphcTcpSentCompressPackets_Type = Counter64
_HwIphcTcpSentCompressPackets_Object = MibTableColumn
hwIphcTcpSentCompressPackets = _HwIphcTcpSentCompressPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 3),
    _HwIphcTcpSentCompressPackets_Type()
)
hwIphcTcpSentCompressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpSentCompressPackets.setStatus("current")
_HwIphcTcpSentCompressBytes_Type = Counter64
_HwIphcTcpSentCompressBytes_Object = MibTableColumn
hwIphcTcpSentCompressBytes = _HwIphcTcpSentCompressBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 4),
    _HwIphcTcpSentCompressBytes_Type()
)
hwIphcTcpSentCompressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpSentCompressBytes.setStatus("current")
_HwIphcTcpSavedBytes_Type = Counter64
_HwIphcTcpSavedBytes_Object = MibTableColumn
hwIphcTcpSavedBytes = _HwIphcTcpSavedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 5),
    _HwIphcTcpSavedBytes_Type()
)
hwIphcTcpSavedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpSavedBytes.setStatus("current")
_HwIphcTcpCompressRatio_Type = Integer32
_HwIphcTcpCompressRatio_Object = MibTableColumn
hwIphcTcpCompressRatio = _HwIphcTcpCompressRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 6),
    _HwIphcTcpCompressRatio_Type()
)
hwIphcTcpCompressRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpCompressRatio.setStatus("current")
_HwIphcTcpReceivedTotalPackets_Type = Counter64
_HwIphcTcpReceivedTotalPackets_Object = MibTableColumn
hwIphcTcpReceivedTotalPackets = _HwIphcTcpReceivedTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 7),
    _HwIphcTcpReceivedTotalPackets_Type()
)
hwIphcTcpReceivedTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpReceivedTotalPackets.setStatus("current")
_HwIphcTcpReceivedCompressPackets_Type = Counter64
_HwIphcTcpReceivedCompressPackets_Object = MibTableColumn
hwIphcTcpReceivedCompressPackets = _HwIphcTcpReceivedCompressPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 8),
    _HwIphcTcpReceivedCompressPackets_Type()
)
hwIphcTcpReceivedCompressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpReceivedCompressPackets.setStatus("current")
_HwIphcTcpReceivedCompressErrorPackets_Type = Counter64
_HwIphcTcpReceivedCompressErrorPackets_Object = MibTableColumn
hwIphcTcpReceivedCompressErrorPackets = _HwIphcTcpReceivedCompressErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 9),
    _HwIphcTcpReceivedCompressErrorPackets_Type()
)
hwIphcTcpReceivedCompressErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpReceivedCompressErrorPackets.setStatus("current")
_HwIphcTcpReceivedCompressDiscardPackets_Type = Counter64
_HwIphcTcpReceivedCompressDiscardPackets_Object = MibTableColumn
hwIphcTcpReceivedCompressDiscardPackets = _HwIphcTcpReceivedCompressDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 1, 1, 10),
    _HwIphcTcpReceivedCompressDiscardPackets_Type()
)
hwIphcTcpReceivedCompressDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcTcpReceivedCompressDiscardPackets.setStatus("current")
_HwIphcRtpRunInfoTable_Object = MibTable
hwIphcRtpRunInfoTable = _HwIphcRtpRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2)
)
if mibBuilder.loadTexts:
    hwIphcRtpRunInfoTable.setStatus("current")
_HwIphcRtpRunInfoEntry_Object = MibTableRow
hwIphcRtpRunInfoEntry = _HwIphcRtpRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1)
)
hwIphcRtpRunInfoEntry.setIndexNames(
    (0, "HUAWEI-IPHC-MIB", "hwIphcRtpIfIndex"),
)
if mibBuilder.loadTexts:
    hwIphcRtpRunInfoEntry.setStatus("current")
_HwIphcRtpSentTotalPackets_Type = Counter64
_HwIphcRtpSentTotalPackets_Object = MibTableColumn
hwIphcRtpSentTotalPackets = _HwIphcRtpSentTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 1),
    _HwIphcRtpSentTotalPackets_Type()
)
hwIphcRtpSentTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpSentTotalPackets.setStatus("current")
_HwIphcRtpSentTotalBytes_Type = Counter64
_HwIphcRtpSentTotalBytes_Object = MibTableColumn
hwIphcRtpSentTotalBytes = _HwIphcRtpSentTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 2),
    _HwIphcRtpSentTotalBytes_Type()
)
hwIphcRtpSentTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpSentTotalBytes.setStatus("current")
_HwIphcRtpSentCompressPackets_Type = Counter64
_HwIphcRtpSentCompressPackets_Object = MibTableColumn
hwIphcRtpSentCompressPackets = _HwIphcRtpSentCompressPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 3),
    _HwIphcRtpSentCompressPackets_Type()
)
hwIphcRtpSentCompressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpSentCompressPackets.setStatus("current")
_HwIphcRtpSentCompressBytes_Type = Counter64
_HwIphcRtpSentCompressBytes_Object = MibTableColumn
hwIphcRtpSentCompressBytes = _HwIphcRtpSentCompressBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 4),
    _HwIphcRtpSentCompressBytes_Type()
)
hwIphcRtpSentCompressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpSentCompressBytes.setStatus("current")
_HwIphcRtpSavedBytes_Type = Counter64
_HwIphcRtpSavedBytes_Object = MibTableColumn
hwIphcRtpSavedBytes = _HwIphcRtpSavedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 5),
    _HwIphcRtpSavedBytes_Type()
)
hwIphcRtpSavedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpSavedBytes.setStatus("current")
_HwIphcRtpCompressRatio_Type = Integer32
_HwIphcRtpCompressRatio_Object = MibTableColumn
hwIphcRtpCompressRatio = _HwIphcRtpCompressRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 6),
    _HwIphcRtpCompressRatio_Type()
)
hwIphcRtpCompressRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpCompressRatio.setStatus("current")
_HwIphcRtpReceivedTotalPackets_Type = Counter64
_HwIphcRtpReceivedTotalPackets_Object = MibTableColumn
hwIphcRtpReceivedTotalPackets = _HwIphcRtpReceivedTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 7),
    _HwIphcRtpReceivedTotalPackets_Type()
)
hwIphcRtpReceivedTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpReceivedTotalPackets.setStatus("current")
_HwIphcRtpReceivedCompressPackets_Type = Counter64
_HwIphcRtpReceivedCompressPackets_Object = MibTableColumn
hwIphcRtpReceivedCompressPackets = _HwIphcRtpReceivedCompressPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 8),
    _HwIphcRtpReceivedCompressPackets_Type()
)
hwIphcRtpReceivedCompressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpReceivedCompressPackets.setStatus("current")
_HwIphcRtpReceivedCompressErrorPackets_Type = Counter64
_HwIphcRtpReceivedCompressErrorPackets_Object = MibTableColumn
hwIphcRtpReceivedCompressErrorPackets = _HwIphcRtpReceivedCompressErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 9),
    _HwIphcRtpReceivedCompressErrorPackets_Type()
)
hwIphcRtpReceivedCompressErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpReceivedCompressErrorPackets.setStatus("current")
_HwIphcRtpReceivedCompressDiscardPackets_Type = Counter64
_HwIphcRtpReceivedCompressDiscardPackets_Object = MibTableColumn
hwIphcRtpReceivedCompressDiscardPackets = _HwIphcRtpReceivedCompressDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 2, 2, 1, 10),
    _HwIphcRtpReceivedCompressDiscardPackets_Type()
)
hwIphcRtpReceivedCompressDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIphcRtpReceivedCompressDiscardPackets.setStatus("current")
_HwIphcTraps_ObjectIdentity = ObjectIdentity
hwIphcTraps = _HwIphcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3)
)
_HwIphcConformance_ObjectIdentity = ObjectIdentity
hwIphcConformance = _HwIphcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4)
)
_HwIphcCompliances_ObjectIdentity = ObjectIdentity
hwIphcCompliances = _HwIphcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 1)
)
_HwIphcGroups_ObjectIdentity = ObjectIdentity
hwIphcGroups = _HwIphcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2)
)

# Managed Objects groups

hwIphcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 1)
)
hwIphcInfoGroup.setObjects(
      *(("HUAWEI-IPHC-MIB", "hwIphcTcpEnable"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpConnnectionNumber"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpRowStatus"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpEffectEnable"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpEffectConnnectionNumber"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpEnable"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpConnnectionNumber"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpNValue"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpFormatType"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpRowStatus"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectEnable"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectConnnectionNumber"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpEffectNValue"))
)
if mibBuilder.loadTexts:
    hwIphcInfoGroup.setStatus("current")

hwIphcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 2)
)
hwIphcStatisticsGroup.setObjects(
      *(("HUAWEI-IPHC-MIB", "hwIphcTcpSentTotalPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpSentTotalBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpSentCompressPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpSentCompressBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpSavedBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpCompressRatio"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedTotalPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressErrorPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcTcpReceivedCompressDiscardPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpSentTotalPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpSentTotalBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpSentCompressPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpSentCompressBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpSavedBytes"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpCompressRatio"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedTotalPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressErrorPackets"),
        ("HUAWEI-IPHC-MIB", "hwIphcRtpReceivedCompressDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwIphcStatisticsGroup.setStatus("current")


# Notification objects

hwIphcContextError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3, 1)
)
hwIphcContextError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwIphcContextError.setStatus(
        "current"
    )

hwIphcContextErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 3, 2)
)
hwIphcContextErrorResume.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwIphcContextErrorResume.setStatus(
        "current"
    )


# Notifications groups

hwIphcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 2, 3)
)
hwIphcNotificationGroup.setObjects(
      *(("HUAWEI-IPHC-MIB", "hwIphcContextError"),
        ("HUAWEI-IPHC-MIB", "hwIphcContextErrorResume"))
)
if mibBuilder.loadTexts:
    hwIphcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIphcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 154, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwIphcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPHC-MIB",
    **{"HWCompressType": HWCompressType,
       "HWCompressFormat": HWCompressFormat,
       "hwIphcMIB": hwIphcMIB,
       "hwIphcInfoObjects": hwIphcInfoObjects,
       "hwIphcTcpConfigTable": hwIphcTcpConfigTable,
       "hwIphcTcpConfigEntry": hwIphcTcpConfigEntry,
       "hwIphcTcpIfIndex": hwIphcTcpIfIndex,
       "hwIphcTcpEnable": hwIphcTcpEnable,
       "hwIphcTcpConnnectionNumber": hwIphcTcpConnnectionNumber,
       "hwIphcTcpRowStatus": hwIphcTcpRowStatus,
       "hwIphcTcpConfigEffectTable": hwIphcTcpConfigEffectTable,
       "hwIphcTcpConfigEffectEntry": hwIphcTcpConfigEffectEntry,
       "hwIphcTcpEffectEnable": hwIphcTcpEffectEnable,
       "hwIphcTcpEffectConnnectionNumber": hwIphcTcpEffectConnnectionNumber,
       "hwIphcRtpConfigTable": hwIphcRtpConfigTable,
       "hwIphcRtpConfigEntry": hwIphcRtpConfigEntry,
       "hwIphcRtpIfIndex": hwIphcRtpIfIndex,
       "hwIphcRtpEnable": hwIphcRtpEnable,
       "hwIphcRtpConnnectionNumber": hwIphcRtpConnnectionNumber,
       "hwIphcRtpNValue": hwIphcRtpNValue,
       "hwIphcRtpFormatType": hwIphcRtpFormatType,
       "hwIphcRtpRowStatus": hwIphcRtpRowStatus,
       "hwIphcRtpConfigEffectTable": hwIphcRtpConfigEffectTable,
       "hwIphcRtpConfigEffectEntry": hwIphcRtpConfigEffectEntry,
       "hwIphcRtpEffectEnable": hwIphcRtpEffectEnable,
       "hwIphcRtpEffectConnnectionNumber": hwIphcRtpEffectConnnectionNumber,
       "hwIphcRtpEffectNValue": hwIphcRtpEffectNValue,
       "hwIphcStatisticsObjects": hwIphcStatisticsObjects,
       "hwIphcTcpRunInfoTable": hwIphcTcpRunInfoTable,
       "hwIphcTcpRunInfoEntry": hwIphcTcpRunInfoEntry,
       "hwIphcTcpSentTotalPackets": hwIphcTcpSentTotalPackets,
       "hwIphcTcpSentTotalBytes": hwIphcTcpSentTotalBytes,
       "hwIphcTcpSentCompressPackets": hwIphcTcpSentCompressPackets,
       "hwIphcTcpSentCompressBytes": hwIphcTcpSentCompressBytes,
       "hwIphcTcpSavedBytes": hwIphcTcpSavedBytes,
       "hwIphcTcpCompressRatio": hwIphcTcpCompressRatio,
       "hwIphcTcpReceivedTotalPackets": hwIphcTcpReceivedTotalPackets,
       "hwIphcTcpReceivedCompressPackets": hwIphcTcpReceivedCompressPackets,
       "hwIphcTcpReceivedCompressErrorPackets": hwIphcTcpReceivedCompressErrorPackets,
       "hwIphcTcpReceivedCompressDiscardPackets": hwIphcTcpReceivedCompressDiscardPackets,
       "hwIphcRtpRunInfoTable": hwIphcRtpRunInfoTable,
       "hwIphcRtpRunInfoEntry": hwIphcRtpRunInfoEntry,
       "hwIphcRtpSentTotalPackets": hwIphcRtpSentTotalPackets,
       "hwIphcRtpSentTotalBytes": hwIphcRtpSentTotalBytes,
       "hwIphcRtpSentCompressPackets": hwIphcRtpSentCompressPackets,
       "hwIphcRtpSentCompressBytes": hwIphcRtpSentCompressBytes,
       "hwIphcRtpSavedBytes": hwIphcRtpSavedBytes,
       "hwIphcRtpCompressRatio": hwIphcRtpCompressRatio,
       "hwIphcRtpReceivedTotalPackets": hwIphcRtpReceivedTotalPackets,
       "hwIphcRtpReceivedCompressPackets": hwIphcRtpReceivedCompressPackets,
       "hwIphcRtpReceivedCompressErrorPackets": hwIphcRtpReceivedCompressErrorPackets,
       "hwIphcRtpReceivedCompressDiscardPackets": hwIphcRtpReceivedCompressDiscardPackets,
       "hwIphcTraps": hwIphcTraps,
       "hwIphcContextError": hwIphcContextError,
       "hwIphcContextErrorResume": hwIphcContextErrorResume,
       "hwIphcConformance": hwIphcConformance,
       "hwIphcCompliances": hwIphcCompliances,
       "hwIphcCompliance": hwIphcCompliance,
       "hwIphcGroups": hwIphcGroups,
       "hwIphcInfoGroup": hwIphcInfoGroup,
       "hwIphcStatisticsGroup": hwIphcStatisticsGroup,
       "hwIphcNotificationGroup": hwIphcNotificationGroup}
)
