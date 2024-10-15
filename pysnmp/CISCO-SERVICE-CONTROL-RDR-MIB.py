# SNMP MIB module (CISCO-SERVICE-CONTROL-RDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROL-RDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:08 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoServiceControlRdrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637)
)
ciscoServiceControlRdrMIB.setRevisions(
        ("2007-08-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSCRdrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSCRdrMIBNotifs = _CiscoSCRdrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0)
)
_CiscoSCRdrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSCRdrMIBObjects = _CiscoSCRdrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1)
)
_CscRdrFormatterTable_Object = MibTable
cscRdrFormatterTable = _CscRdrFormatterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1)
)
if mibBuilder.loadTexts:
    cscRdrFormatterTable.setStatus("current")
_CscRdrFormatterEntry_Object = MibTableRow
cscRdrFormatterEntry = _CscRdrFormatterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1)
)
cscRdrFormatterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cscRdrFormatterEntry.setStatus("current")
_CscRdrFormatterEnable_Type = TruthValue
_CscRdrFormatterEnable_Object = MibTableColumn
cscRdrFormatterEnable = _CscRdrFormatterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 1),
    _CscRdrFormatterEnable_Type()
)
cscRdrFormatterEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterEnable.setStatus("current")
_CscRdrFormatterNumSentReports_Type = Counter32
_CscRdrFormatterNumSentReports_Object = MibTableColumn
cscRdrFormatterNumSentReports = _CscRdrFormatterNumSentReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 2),
    _CscRdrFormatterNumSentReports_Type()
)
cscRdrFormatterNumSentReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterNumSentReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrFormatterNumSentReports.setUnits("reports")
_CscRdrFormatterNumDiscardedReports_Type = Counter32
_CscRdrFormatterNumDiscardedReports_Object = MibTableColumn
cscRdrFormatterNumDiscardedReports = _CscRdrFormatterNumDiscardedReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 3),
    _CscRdrFormatterNumDiscardedReports_Type()
)
cscRdrFormatterNumDiscardedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterNumDiscardedReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrFormatterNumDiscardedReports.setUnits("reports")
_CscRdrFormatterReportRate_Type = Gauge32
_CscRdrFormatterReportRate_Object = MibTableColumn
cscRdrFormatterReportRate = _CscRdrFormatterReportRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 4),
    _CscRdrFormatterReportRate_Type()
)
cscRdrFormatterReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterReportRate.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrFormatterReportRate.setUnits("reports per second")
_CscRdrFormatterReportRatePeak_Type = Gauge32
_CscRdrFormatterReportRatePeak_Object = MibTableColumn
cscRdrFormatterReportRatePeak = _CscRdrFormatterReportRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 5),
    _CscRdrFormatterReportRatePeak_Type()
)
cscRdrFormatterReportRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterReportRatePeak.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrFormatterReportRatePeak.setUnits("reports per second")
_CscRdrFormatterReportRatePeakTime_Type = TimeTicks
_CscRdrFormatterReportRatePeakTime_Object = MibTableColumn
cscRdrFormatterReportRatePeakTime = _CscRdrFormatterReportRatePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 6),
    _CscRdrFormatterReportRatePeakTime_Type()
)
cscRdrFormatterReportRatePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrFormatterReportRatePeakTime.setStatus("current")


class _CscRdrFormatterProtocol_Type(Integer32):
    """Custom type cscRdrFormatterProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netflowV9", 3),
          ("other", 1),
          ("rdrv1", 2))
    )


_CscRdrFormatterProtocol_Type.__name__ = "Integer32"
_CscRdrFormatterProtocol_Object = MibTableColumn
cscRdrFormatterProtocol = _CscRdrFormatterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 7),
    _CscRdrFormatterProtocol_Type()
)
cscRdrFormatterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscRdrFormatterProtocol.setStatus("current")


class _CscRdrFormatterForwardingMode_Type(Integer32):
    """Custom type cscRdrFormatterForwardingMode based on Integer32"""
    defaultValue = 2

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
        *(("multicast", 4),
          ("other", 1),
          ("redundancy", 2),
          ("simpleLoadBalancing", 3))
    )


_CscRdrFormatterForwardingMode_Type.__name__ = "Integer32"
_CscRdrFormatterForwardingMode_Object = MibTableColumn
cscRdrFormatterForwardingMode = _CscRdrFormatterForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 1, 1, 8),
    _CscRdrFormatterForwardingMode_Type()
)
cscRdrFormatterForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscRdrFormatterForwardingMode.setStatus("current")
_CscRdrDestTable_Object = MibTable
cscRdrDestTable = _CscRdrDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2)
)
if mibBuilder.loadTexts:
    cscRdrDestTable.setStatus("current")
_CscRdrDestEntry_Object = MibTableRow
cscRdrDestEntry = _CscRdrDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1)
)
cscRdrDestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestIndex"),
)
if mibBuilder.loadTexts:
    cscRdrDestEntry.setStatus("current")


class _CscRdrDestIndex_Type(Unsigned32):
    """Custom type cscRdrDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CscRdrDestIndex_Type.__name__ = "Unsigned32"
_CscRdrDestIndex_Object = MibTableColumn
cscRdrDestIndex = _CscRdrDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 1),
    _CscRdrDestIndex_Type()
)
cscRdrDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscRdrDestIndex.setStatus("current")
_CscRdrDestInetAddressType_Type = InetAddressType
_CscRdrDestInetAddressType_Object = MibTableColumn
cscRdrDestInetAddressType = _CscRdrDestInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 2),
    _CscRdrDestInetAddressType_Type()
)
cscRdrDestInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestInetAddressType.setStatus("current")
_CscRdrDestInetAddress_Type = InetAddress
_CscRdrDestInetAddress_Object = MibTableColumn
cscRdrDestInetAddress = _CscRdrDestInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 3),
    _CscRdrDestInetAddress_Type()
)
cscRdrDestInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestInetAddress.setStatus("current")
_CscRdrDestPort_Type = InetPortNumber
_CscRdrDestPort_Object = MibTableColumn
cscRdrDestPort = _CscRdrDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 4),
    _CscRdrDestPort_Type()
)
cscRdrDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestPort.setStatus("current")


class _CscRdrDestPriority_Type(Integer32):
    """Custom type cscRdrDestPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CscRdrDestPriority_Type.__name__ = "Integer32"
_CscRdrDestPriority_Object = MibTableColumn
cscRdrDestPriority = _CscRdrDestPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 5),
    _CscRdrDestPriority_Type()
)
cscRdrDestPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestPriority.setStatus("current")


class _CscRdrDestStatus_Type(Integer32):
    """Custom type cscRdrDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_CscRdrDestStatus_Type.__name__ = "Integer32"
_CscRdrDestStatus_Object = MibTableColumn
cscRdrDestStatus = _CscRdrDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 6),
    _CscRdrDestStatus_Type()
)
cscRdrDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestStatus.setStatus("current")


class _CscRdrDestConnectionStatus_Type(Integer32):
    """Custom type cscRdrDestConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_CscRdrDestConnectionStatus_Type.__name__ = "Integer32"
_CscRdrDestConnectionStatus_Object = MibTableColumn
cscRdrDestConnectionStatus = _CscRdrDestConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 7),
    _CscRdrDestConnectionStatus_Type()
)
cscRdrDestConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestConnectionStatus.setStatus("current")
_CscRdrDestNumSentReports_Type = Counter32
_CscRdrDestNumSentReports_Object = MibTableColumn
cscRdrDestNumSentReports = _CscRdrDestNumSentReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 8),
    _CscRdrDestNumSentReports_Type()
)
cscRdrDestNumSentReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestNumSentReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrDestNumSentReports.setUnits("reports")
_CscRdrDestNumDiscardedReports_Type = Counter32
_CscRdrDestNumDiscardedReports_Object = MibTableColumn
cscRdrDestNumDiscardedReports = _CscRdrDestNumDiscardedReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 9),
    _CscRdrDestNumDiscardedReports_Type()
)
cscRdrDestNumDiscardedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestNumDiscardedReports.setStatus("current")
_CscRdrDestReportRate_Type = Gauge32
_CscRdrDestReportRate_Object = MibTableColumn
cscRdrDestReportRate = _CscRdrDestReportRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 2, 1, 10),
    _CscRdrDestReportRate_Type()
)
cscRdrDestReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrDestReportRate.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrDestReportRate.setUnits("reports per second")
_CscRdrCategoryTable_Object = MibTable
cscRdrCategoryTable = _CscRdrCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3)
)
if mibBuilder.loadTexts:
    cscRdrCategoryTable.setStatus("current")
_CscRdrCategoryEntry_Object = MibTableRow
cscRdrCategoryEntry = _CscRdrCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1)
)
cscRdrCategoryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryIndex"),
)
if mibBuilder.loadTexts:
    cscRdrCategoryEntry.setStatus("current")


class _CscRdrCategoryIndex_Type(Unsigned32):
    """Custom type cscRdrCategoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CscRdrCategoryIndex_Type.__name__ = "Unsigned32"
_CscRdrCategoryIndex_Object = MibTableColumn
cscRdrCategoryIndex = _CscRdrCategoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 1),
    _CscRdrCategoryIndex_Type()
)
cscRdrCategoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscRdrCategoryIndex.setStatus("current")
_CscRdrCategoryID_Type = Unsigned32
_CscRdrCategoryID_Object = MibTableColumn
cscRdrCategoryID = _CscRdrCategoryID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 2),
    _CscRdrCategoryID_Type()
)
cscRdrCategoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryID.setStatus("current")
_CscRdrCategoryName_Type = SnmpAdminString
_CscRdrCategoryName_Object = MibTableColumn
cscRdrCategoryName = _CscRdrCategoryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 3),
    _CscRdrCategoryName_Type()
)
cscRdrCategoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryName.setStatus("current")
_CscRdrCategoryNumSentReports_Type = Counter32
_CscRdrCategoryNumSentReports_Object = MibTableColumn
cscRdrCategoryNumSentReports = _CscRdrCategoryNumSentReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 4),
    _CscRdrCategoryNumSentReports_Type()
)
cscRdrCategoryNumSentReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryNumSentReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrCategoryNumSentReports.setUnits("reports")
_CscRdrCategoryNumDiscardedReports_Type = Counter32
_CscRdrCategoryNumDiscardedReports_Object = MibTableColumn
cscRdrCategoryNumDiscardedReports = _CscRdrCategoryNumDiscardedReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 5),
    _CscRdrCategoryNumDiscardedReports_Type()
)
cscRdrCategoryNumDiscardedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryNumDiscardedReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrCategoryNumDiscardedReports.setUnits("reports")
_CscRdrCategoryReportRate_Type = Gauge32
_CscRdrCategoryReportRate_Object = MibTableColumn
cscRdrCategoryReportRate = _CscRdrCategoryReportRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 6),
    _CscRdrCategoryReportRate_Type()
)
cscRdrCategoryReportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryReportRate.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrCategoryReportRate.setUnits("reports per second")
_CscRdrCategoryNumQueuedReports_Type = Gauge32
_CscRdrCategoryNumQueuedReports_Object = MibTableColumn
cscRdrCategoryNumQueuedReports = _CscRdrCategoryNumQueuedReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 3, 1, 7),
    _CscRdrCategoryNumQueuedReports_Type()
)
cscRdrCategoryNumQueuedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryNumQueuedReports.setStatus("current")
if mibBuilder.loadTexts:
    cscRdrCategoryNumQueuedReports.setUnits("reports")
_CscRdrCategoryDestTable_Object = MibTable
cscRdrCategoryDestTable = _CscRdrCategoryDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4)
)
if mibBuilder.loadTexts:
    cscRdrCategoryDestTable.setStatus("current")
_CscRdrCategoryDestEntry_Object = MibTableRow
cscRdrCategoryDestEntry = _CscRdrCategoryDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1)
)
cscRdrCategoryDestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryIndex"),
    (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"),
    (0, "CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"),
)
if mibBuilder.loadTexts:
    cscRdrCategoryDestEntry.setStatus("current")


class _CscRdrCategoryDestPriority_Type(Integer32):
    """Custom type cscRdrCategoryDestPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CscRdrCategoryDestPriority_Type.__name__ = "Integer32"
_CscRdrCategoryDestPriority_Object = MibTableColumn
cscRdrCategoryDestPriority = _CscRdrCategoryDestPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1, 1),
    _CscRdrCategoryDestPriority_Type()
)
cscRdrCategoryDestPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryDestPriority.setStatus("current")


class _CscRdrCategoryDestStatus_Type(Integer32):
    """Custom type cscRdrCategoryDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_CscRdrCategoryDestStatus_Type.__name__ = "Integer32"
_CscRdrCategoryDestStatus_Object = MibTableColumn
cscRdrCategoryDestStatus = _CscRdrCategoryDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 4, 1, 2),
    _CscRdrCategoryDestStatus_Type()
)
cscRdrCategoryDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCategoryDestStatus.setStatus("current")
_CscRdrNotifsConfig_ObjectIdentity = ObjectIdentity
cscRdrNotifsConfig = _CscRdrNotifsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 5)
)
_CscRdrReportsEnableNotifs_Type = TruthValue
_CscRdrReportsEnableNotifs_Object = MibScalar
cscRdrReportsEnableNotifs = _CscRdrReportsEnableNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 5, 1),
    _CscRdrReportsEnableNotifs_Type()
)
cscRdrReportsEnableNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cscRdrReportsEnableNotifs.setStatus("current")
_CscRdrCounterDiscontinuityTime_Type = TimeStamp
_CscRdrCounterDiscontinuityTime_Object = MibScalar
cscRdrCounterDiscontinuityTime = _CscRdrCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 1, 6),
    _CscRdrCounterDiscontinuityTime_Type()
)
cscRdrCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscRdrCounterDiscontinuityTime.setStatus("current")
_CiscoSCRdrMIBConform_ObjectIdentity = ObjectIdentity
ciscoSCRdrMIBConform = _CiscoSCRdrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2)
)
_CscRdrMIBCompliances_ObjectIdentity = ObjectIdentity
cscRdrMIBCompliances = _CscRdrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 1)
)
_CscRdrMIBGroups_ObjectIdentity = ObjectIdentity
cscRdrMIBGroups = _CscRdrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2)
)

# Managed Objects groups

cscRdrObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 1)
)
cscRdrObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterEnable"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterNumSentReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterNumDiscardedReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRate"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterProtocol"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterForwardingMode"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddressType"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPriority"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestConnectionStatus"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestNumSentReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestNumDiscardedReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestReportRate"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumSentReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumDiscardedReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryReportRate"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryNumQueuedReports"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDestPriority"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDestStatus"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRatePeak"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrFormatterReportRatePeakTime"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
)
if mibBuilder.loadTexts:
    cscRdrObjectGroup.setStatus("current")

cscRdrNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 3)
)
cscRdrNotifsControlGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrReportsEnableNotifs")
)
if mibBuilder.loadTexts:
    cscRdrNotifsControlGroup.setStatus("current")

cscRdrCounterDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 4)
)
cscRdrCounterDiscontinuityGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCounterDiscontinuityTime")
)
if mibBuilder.loadTexts:
    cscRdrCounterDiscontinuityGroup.setStatus("current")


# Notification objects

cscRdrCategoryStoppedDiscardingReportsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 1)
)
cscRdrCategoryStoppedDiscardingReportsTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
)
if mibBuilder.loadTexts:
    cscRdrCategoryStoppedDiscardingReportsTrap.setStatus(
        "current"
    )

cscRdrCategoryDiscardingReportsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 2)
)
cscRdrCategoryDiscardingReportsTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryID"))
)
if mibBuilder.loadTexts:
    cscRdrCategoryDiscardingReportsTrap.setStatus(
        "current"
    )

cscRdrNoActiveConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 3)
)
cscRdrNoActiveConnectionTrap.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    cscRdrNoActiveConnectionTrap.setStatus(
        "current"
    )

cscRdrConnectionStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 4)
)
cscRdrConnectionStatusDownTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
)
if mibBuilder.loadTexts:
    cscRdrConnectionStatusDownTrap.setStatus(
        "current"
    )

cscRdrActiveConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 5)
)
cscRdrActiveConnectionTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
)
if mibBuilder.loadTexts:
    cscRdrActiveConnectionTrap.setStatus(
        "current"
    )

cscRdrConnectionStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 0, 6)
)
cscRdrConnectionStatusUpTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestStatus"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestInetAddress"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrDestPort"))
)
if mibBuilder.loadTexts:
    cscRdrConnectionStatusUpTrap.setStatus(
        "current"
    )


# Notifications groups

cscRdrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 2, 2)
)
cscRdrNotificationGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrActiveConnectionTrap"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryStoppedDiscardingReportsTrap"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrCategoryDiscardingReportsTrap"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrNoActiveConnectionTrap"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrConnectionStatusDownTrap"),
        ("CISCO-SERVICE-CONTROL-RDR-MIB", "cscRdrConnectionStatusUpTrap"))
)
if mibBuilder.loadTexts:
    cscRdrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cscRdrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 637, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cscRdrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROL-RDR-MIB",
    **{"ciscoServiceControlRdrMIB": ciscoServiceControlRdrMIB,
       "ciscoSCRdrMIBNotifs": ciscoSCRdrMIBNotifs,
       "cscRdrCategoryStoppedDiscardingReportsTrap": cscRdrCategoryStoppedDiscardingReportsTrap,
       "cscRdrCategoryDiscardingReportsTrap": cscRdrCategoryDiscardingReportsTrap,
       "cscRdrNoActiveConnectionTrap": cscRdrNoActiveConnectionTrap,
       "cscRdrConnectionStatusDownTrap": cscRdrConnectionStatusDownTrap,
       "cscRdrActiveConnectionTrap": cscRdrActiveConnectionTrap,
       "cscRdrConnectionStatusUpTrap": cscRdrConnectionStatusUpTrap,
       "ciscoSCRdrMIBObjects": ciscoSCRdrMIBObjects,
       "cscRdrFormatterTable": cscRdrFormatterTable,
       "cscRdrFormatterEntry": cscRdrFormatterEntry,
       "cscRdrFormatterEnable": cscRdrFormatterEnable,
       "cscRdrFormatterNumSentReports": cscRdrFormatterNumSentReports,
       "cscRdrFormatterNumDiscardedReports": cscRdrFormatterNumDiscardedReports,
       "cscRdrFormatterReportRate": cscRdrFormatterReportRate,
       "cscRdrFormatterReportRatePeak": cscRdrFormatterReportRatePeak,
       "cscRdrFormatterReportRatePeakTime": cscRdrFormatterReportRatePeakTime,
       "cscRdrFormatterProtocol": cscRdrFormatterProtocol,
       "cscRdrFormatterForwardingMode": cscRdrFormatterForwardingMode,
       "cscRdrDestTable": cscRdrDestTable,
       "cscRdrDestEntry": cscRdrDestEntry,
       "cscRdrDestIndex": cscRdrDestIndex,
       "cscRdrDestInetAddressType": cscRdrDestInetAddressType,
       "cscRdrDestInetAddress": cscRdrDestInetAddress,
       "cscRdrDestPort": cscRdrDestPort,
       "cscRdrDestPriority": cscRdrDestPriority,
       "cscRdrDestStatus": cscRdrDestStatus,
       "cscRdrDestConnectionStatus": cscRdrDestConnectionStatus,
       "cscRdrDestNumSentReports": cscRdrDestNumSentReports,
       "cscRdrDestNumDiscardedReports": cscRdrDestNumDiscardedReports,
       "cscRdrDestReportRate": cscRdrDestReportRate,
       "cscRdrCategoryTable": cscRdrCategoryTable,
       "cscRdrCategoryEntry": cscRdrCategoryEntry,
       "cscRdrCategoryIndex": cscRdrCategoryIndex,
       "cscRdrCategoryID": cscRdrCategoryID,
       "cscRdrCategoryName": cscRdrCategoryName,
       "cscRdrCategoryNumSentReports": cscRdrCategoryNumSentReports,
       "cscRdrCategoryNumDiscardedReports": cscRdrCategoryNumDiscardedReports,
       "cscRdrCategoryReportRate": cscRdrCategoryReportRate,
       "cscRdrCategoryNumQueuedReports": cscRdrCategoryNumQueuedReports,
       "cscRdrCategoryDestTable": cscRdrCategoryDestTable,
       "cscRdrCategoryDestEntry": cscRdrCategoryDestEntry,
       "cscRdrCategoryDestPriority": cscRdrCategoryDestPriority,
       "cscRdrCategoryDestStatus": cscRdrCategoryDestStatus,
       "cscRdrNotifsConfig": cscRdrNotifsConfig,
       "cscRdrReportsEnableNotifs": cscRdrReportsEnableNotifs,
       "cscRdrCounterDiscontinuityTime": cscRdrCounterDiscontinuityTime,
       "ciscoSCRdrMIBConform": ciscoSCRdrMIBConform,
       "cscRdrMIBCompliances": cscRdrMIBCompliances,
       "cscRdrCompliance": cscRdrCompliance,
       "cscRdrMIBGroups": cscRdrMIBGroups,
       "cscRdrObjectGroup": cscRdrObjectGroup,
       "cscRdrNotificationGroup": cscRdrNotificationGroup,
       "cscRdrNotifsControlGroup": cscRdrNotifsControlGroup,
       "cscRdrCounterDiscontinuityGroup": cscRdrCounterDiscontinuityGroup}
)
