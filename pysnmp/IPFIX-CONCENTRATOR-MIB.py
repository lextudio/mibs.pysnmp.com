# SNMP MIB module (IPFIX-CONCENTRATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFIX-CONCENTRATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:48 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipfixConcentratorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 5555)
)
ipfixConcentratorMIB.setRevisions(
        ("2006-02-16 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConcFieldModifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("keep", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ConcentratorObjects_ObjectIdentity = ObjectIdentity
concentratorObjects = _ConcentratorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1)
)
_ConcExtraction_ObjectIdentity = ObjectIdentity
concExtraction = _ConcExtraction_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1)
)


class _ConcExtractIsAvail_Type(TruthValue):
    """Custom type concExtractIsAvail based on TruthValue"""


_ConcExtractIsAvail_Object = MibScalar
concExtractIsAvail = _ConcExtractIsAvail_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 1),
    _ConcExtractIsAvail_Type()
)
concExtractIsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concExtractIsAvail.setStatus("current")
_ConcExtractTable_Object = MibTable
concExtractTable = _ConcExtractTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2)
)
if mibBuilder.loadTexts:
    concExtractTable.setStatus("current")
_ConcExtractEntry_Object = MibTableRow
concExtractEntry = _ConcExtractEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1)
)
concExtractEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concExtractIndex"),
)
if mibBuilder.loadTexts:
    concExtractEntry.setStatus("current")


class _ConcExtractIndex_Type(Integer32):
    """Custom type concExtractIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcExtractIndex_Type.__name__ = "Integer32"
_ConcExtractIndex_Object = MibTableColumn
concExtractIndex = _ConcExtractIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 1),
    _ConcExtractIndex_Type()
)
concExtractIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concExtractIndex.setStatus("current")
_ConcExtractEtrIpAddrType_Type = InetAddressType
_ConcExtractEtrIpAddrType_Object = MibTableColumn
concExtractEtrIpAddrType = _ConcExtractEtrIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 2),
    _ConcExtractEtrIpAddrType_Type()
)
concExtractEtrIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExtractEtrIpAddrType.setStatus("current")
_ConcExtractEtrIpAddr_Type = InetAddress
_ConcExtractEtrIpAddr_Object = MibTableColumn
concExtractEtrIpAddr = _ConcExtractEtrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 3),
    _ConcExtractEtrIpAddr_Type()
)
concExtractEtrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExtractEtrIpAddr.setStatus("current")
_ConcExtractStartTime_Type = DateAndTime
_ConcExtractStartTime_Object = MibTableColumn
concExtractStartTime = _ConcExtractStartTime_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 4),
    _ConcExtractStartTime_Type()
)
concExtractStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExtractStartTime.setStatus("current")
_ConcExtractEndTime_Type = DateAndTime
_ConcExtractEndTime_Object = MibTableColumn
concExtractEndTime = _ConcExtractEndTime_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 5),
    _ConcExtractEndTime_Type()
)
concExtractEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExtractEndTime.setStatus("current")


class _ConcExtractProcessId_Type(Integer32):
    """Custom type concExtractProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ConcExtractProcessId_Type.__name__ = "Integer32"
_ConcExtractProcessId_Object = MibTableColumn
concExtractProcessId = _ConcExtractProcessId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 6),
    _ConcExtractProcessId_Type()
)
concExtractProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concExtractProcessId.setStatus("current")
_ConcExtractRowStatus_Type = RowStatus
_ConcExtractRowStatus_Object = MibTableColumn
concExtractRowStatus = _ConcExtractRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 1, 2, 1, 7),
    _ConcExtractRowStatus_Type()
)
concExtractRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExtractRowStatus.setStatus("current")
_ConcSelection_ObjectIdentity = ObjectIdentity
concSelection = _ConcSelection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2)
)


class _ConcSelectIsAvail_Type(TruthValue):
    """Custom type concSelectIsAvail based on TruthValue"""


_ConcSelectIsAvail_Object = MibScalar
concSelectIsAvail = _ConcSelectIsAvail_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 1),
    _ConcSelectIsAvail_Type()
)
concSelectIsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concSelectIsAvail.setStatus("current")
_ConcSelectMatchParamSetTable_Object = MibTable
concSelectMatchParamSetTable = _ConcSelectMatchParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2)
)
if mibBuilder.loadTexts:
    concSelectMatchParamSetTable.setStatus("current")
_ConcSelectMatchParamSetEntry_Object = MibTableRow
concSelectMatchParamSetEntry = _ConcSelectMatchParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1)
)
concSelectMatchParamSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concSelectMatchIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concSelectMatchInfoEltId"),
)
if mibBuilder.loadTexts:
    concSelectMatchParamSetEntry.setStatus("current")


class _ConcSelectMatchIndex_Type(Integer32):
    """Custom type concSelectMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcSelectMatchIndex_Type.__name__ = "Integer32"
_ConcSelectMatchIndex_Object = MibTableColumn
concSelectMatchIndex = _ConcSelectMatchIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 1),
    _ConcSelectMatchIndex_Type()
)
concSelectMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concSelectMatchIndex.setStatus("current")


class _ConcSelectMatchInfoEltId_Type(Integer32):
    """Custom type concSelectMatchInfoEltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcSelectMatchInfoEltId_Type.__name__ = "Integer32"
_ConcSelectMatchInfoEltId_Object = MibTableColumn
concSelectMatchInfoEltId = _ConcSelectMatchInfoEltId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 2),
    _ConcSelectMatchInfoEltId_Type()
)
concSelectMatchInfoEltId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concSelectMatchInfoEltId.setStatus("current")
_ConcSelectMatchStartValue_Type = OctetString
_ConcSelectMatchStartValue_Object = MibTableColumn
concSelectMatchStartValue = _ConcSelectMatchStartValue_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 3),
    _ConcSelectMatchStartValue_Type()
)
concSelectMatchStartValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concSelectMatchStartValue.setStatus("current")


class _ConcSelectMatchEndValue_Type(OctetString):
    """Custom type concSelectMatchEndValue based on OctetString"""
    defaultHexValue = ""


_ConcSelectMatchEndValue_Object = MibTableColumn
concSelectMatchEndValue = _ConcSelectMatchEndValue_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 4),
    _ConcSelectMatchEndValue_Type()
)
concSelectMatchEndValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concSelectMatchEndValue.setStatus("current")


class _ConcSelectMatchMask_Type(OctetString):
    """Custom type concSelectMatchMask based on OctetString"""
    defaultHexValue = ""


_ConcSelectMatchMask_Object = MibTableColumn
concSelectMatchMask = _ConcSelectMatchMask_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 5),
    _ConcSelectMatchMask_Type()
)
concSelectMatchMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concSelectMatchMask.setStatus("current")
_ConcSelectMatchRowStatus_Type = RowStatus
_ConcSelectMatchRowStatus_Object = MibTableColumn
concSelectMatchRowStatus = _ConcSelectMatchRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 2, 2, 1, 6),
    _ConcSelectMatchRowStatus_Type()
)
concSelectMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concSelectMatchRowStatus.setStatus("current")
_ConcAggregation_ObjectIdentity = ObjectIdentity
concAggregation = _ConcAggregation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3)
)


class _ConcAggrIsAvail_Type(TruthValue):
    """Custom type concAggrIsAvail based on TruthValue"""


_ConcAggrIsAvail_Object = MibScalar
concAggrIsAvail = _ConcAggrIsAvail_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 1),
    _ConcAggrIsAvail_Type()
)
concAggrIsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concAggrIsAvail.setStatus("current")
_ConcAggrParamSetTable_Object = MibTable
concAggrParamSetTable = _ConcAggrParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 2)
)
if mibBuilder.loadTexts:
    concAggrParamSetTable.setStatus("current")
_ConcAggrParamSetEntry_Object = MibTableRow
concAggrParamSetEntry = _ConcAggrParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1)
)
concAggrParamSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"),
)
if mibBuilder.loadTexts:
    concAggrParamSetEntry.setStatus("current")


class _ConcAggrIndex_Type(Integer32):
    """Custom type concAggrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcAggrIndex_Type.__name__ = "Integer32"
_ConcAggrIndex_Object = MibTableColumn
concAggrIndex = _ConcAggrIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 1),
    _ConcAggrIndex_Type()
)
concAggrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concAggrIndex.setStatus("current")


class _ConcAggrTimeInterval_Type(Integer32):
    """Custom type concAggrTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcAggrTimeInterval_Type.__name__ = "Integer32"
_ConcAggrTimeInterval_Object = MibTableColumn
concAggrTimeInterval = _ConcAggrTimeInterval_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 2),
    _ConcAggrTimeInterval_Type()
)
concAggrTimeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    concAggrTimeInterval.setUnits("seconds")
_ConcAggrParamRowStatus_Type = RowStatus
_ConcAggrParamRowStatus_Object = MibTableColumn
concAggrParamRowStatus = _ConcAggrParamRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 2, 1, 3),
    _ConcAggrParamRowStatus_Type()
)
concAggrParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrParamRowStatus.setStatus("current")
_ConcAggrFieldSetTable_Object = MibTable
concAggrFieldSetTable = _ConcAggrFieldSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 3)
)
if mibBuilder.loadTexts:
    concAggrFieldSetTable.setStatus("current")
_ConcAggrFieldSetEntry_Object = MibTableRow
concAggrFieldSetEntry = _ConcAggrFieldSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1)
)
concAggrFieldSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concAggrFieldSetId"),
)
if mibBuilder.loadTexts:
    concAggrFieldSetEntry.setStatus("current")


class _ConcAggrFieldSetId_Type(Integer32):
    """Custom type concAggrFieldSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcAggrFieldSetId_Type.__name__ = "Integer32"
_ConcAggrFieldSetId_Object = MibTableColumn
concAggrFieldSetId = _ConcAggrFieldSetId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 2),
    _ConcAggrFieldSetId_Type()
)
concAggrFieldSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrFieldSetId.setStatus("current")


class _ConcAggrFieldModifier_Type(ConcFieldModifier):
    """Custom type concAggrFieldModifier based on ConcFieldModifier"""


_ConcAggrFieldModifier_Object = MibTableColumn
concAggrFieldModifier = _ConcAggrFieldModifier_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 3),
    _ConcAggrFieldModifier_Type()
)
concAggrFieldModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrFieldModifier.setStatus("current")
_ConcAggrFieldRowStatus_Type = RowStatus
_ConcAggrFieldRowStatus_Object = MibTableColumn
concAggrFieldRowStatus = _ConcAggrFieldRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 3, 1, 4),
    _ConcAggrFieldRowStatus_Type()
)
concAggrFieldRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrFieldRowStatus.setStatus("current")
_ConcAggrAddFieldSetTable_Object = MibTable
concAggrAddFieldSetTable = _ConcAggrAddFieldSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 4)
)
if mibBuilder.loadTexts:
    concAggrAddFieldSetTable.setStatus("current")
_ConcAggrAddFieldSetEntry_Object = MibTableRow
concAggrAddFieldSetEntry = _ConcAggrAddFieldSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1)
)
concAggrAddFieldSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concAggrIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldSetId"),
)
if mibBuilder.loadTexts:
    concAggrAddFieldSetEntry.setStatus("current")


class _ConcAggrAddFieldSetId_Type(Integer32):
    """Custom type concAggrAddFieldSetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcAggrAddFieldSetId_Type.__name__ = "Integer32"
_ConcAggrAddFieldSetId_Object = MibTableColumn
concAggrAddFieldSetId = _ConcAggrAddFieldSetId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1, 2),
    _ConcAggrAddFieldSetId_Type()
)
concAggrAddFieldSetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrAddFieldSetId.setStatus("current")
_ConcAggrAddFieldRowStatus_Type = RowStatus
_ConcAggrAddFieldRowStatus_Object = MibTableColumn
concAggrAddFieldRowStatus = _ConcAggrAddFieldRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 3, 4, 1, 3),
    _ConcAggrAddFieldRowStatus_Type()
)
concAggrAddFieldRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concAggrAddFieldRowStatus.setStatus("current")
_ConcReport_ObjectIdentity = ObjectIdentity
concReport = _ConcReport_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4)
)
_ConcReportCtrTable_Object = MibTable
concReportCtrTable = _ConcReportCtrTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1)
)
if mibBuilder.loadTexts:
    concReportCtrTable.setStatus("current")
_ConcReportCtrEntry_Object = MibTableRow
concReportCtrEntry = _ConcReportCtrEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1)
)
concReportCtrEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrIndex"),
)
if mibBuilder.loadTexts:
    concReportCtrEntry.setStatus("current")


class _ConcReportCtrIndex_Type(Integer32):
    """Custom type concReportCtrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcReportCtrIndex_Type.__name__ = "Integer32"
_ConcReportCtrIndex_Object = MibTableColumn
concReportCtrIndex = _ConcReportCtrIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 1),
    _ConcReportCtrIndex_Type()
)
concReportCtrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concReportCtrIndex.setStatus("current")
_ConcReportCtrDstIpAddrType_Type = InetAddressType
_ConcReportCtrDstIpAddrType_Object = MibTableColumn
concReportCtrDstIpAddrType = _ConcReportCtrDstIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 2),
    _ConcReportCtrDstIpAddrType_Type()
)
concReportCtrDstIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrDstIpAddrType.setStatus("current")
_ConcReportCtrDstIpAddr_Type = InetAddress
_ConcReportCtrDstIpAddr_Object = MibTableColumn
concReportCtrDstIpAddr = _ConcReportCtrDstIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 3),
    _ConcReportCtrDstIpAddr_Type()
)
concReportCtrDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrDstIpAddr.setStatus("current")


class _ConcReportCtrDstProtocol_Type(Integer32):
    """Custom type concReportCtrDstProtocol based on Integer32"""
    defaultValue = 132

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ConcReportCtrDstProtocol_Type.__name__ = "Integer32"
_ConcReportCtrDstProtocol_Object = MibTableColumn
concReportCtrDstProtocol = _ConcReportCtrDstProtocol_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 4),
    _ConcReportCtrDstProtocol_Type()
)
concReportCtrDstProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrDstProtocol.setStatus("current")


class _ConcReportCtrDstPort_Type(Integer32):
    """Custom type concReportCtrDstPort based on Integer32"""
    defaultValue = 4739

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConcReportCtrDstPort_Type.__name__ = "Integer32"
_ConcReportCtrDstPort_Object = MibTableColumn
concReportCtrDstPort = _ConcReportCtrDstPort_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 5),
    _ConcReportCtrDstPort_Type()
)
concReportCtrDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrDstPort.setStatus("current")
_ConcReportCtrReportsSent_Type = Integer32
_ConcReportCtrReportsSent_Object = MibTableColumn
concReportCtrReportsSent = _ConcReportCtrReportsSent_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 6),
    _ConcReportCtrReportsSent_Type()
)
concReportCtrReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concReportCtrReportsSent.setStatus("current")
_ConcReportCtrRowStatus_Type = RowStatus
_ConcReportCtrRowStatus_Object = MibTableColumn
concReportCtrRowStatus = _ConcReportCtrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 1, 1, 7),
    _ConcReportCtrRowStatus_Type()
)
concReportCtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrRowStatus.setStatus("current")
_ConcReportCtrGrTable_Object = MibTable
concReportCtrGrTable = _ConcReportCtrGrTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 2)
)
if mibBuilder.loadTexts:
    concReportCtrGrTable.setStatus("current")
_ConcReportCtrGrEntry_Object = MibTableRow
concReportCtrGrEntry = _ConcReportCtrGrEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1)
)
concReportCtrGrEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrGrIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concReportCtrIndex"),
)
if mibBuilder.loadTexts:
    concReportCtrGrEntry.setStatus("current")


class _ConcReportCtrGrIndex_Type(Integer32):
    """Custom type concReportCtrGrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcReportCtrGrIndex_Type.__name__ = "Integer32"
_ConcReportCtrGrIndex_Object = MibTableColumn
concReportCtrGrIndex = _ConcReportCtrGrIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1, 1),
    _ConcReportCtrGrIndex_Type()
)
concReportCtrGrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concReportCtrGrIndex.setStatus("current")
_ConcReportCtrGrRowStatus_Type = RowStatus
_ConcReportCtrGrRowStatus_Object = MibTableColumn
concReportCtrGrRowStatus = _ConcReportCtrGrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 2, 1, 3),
    _ConcReportCtrGrRowStatus_Type()
)
concReportCtrGrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportCtrGrRowStatus.setStatus("current")
_ConcReportTemplateRcdTable_Object = MibTable
concReportTemplateRcdTable = _ConcReportTemplateRcdTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3)
)
if mibBuilder.loadTexts:
    concReportTemplateRcdTable.setStatus("current")
_ConcReportTemplateRcdEntry_Object = MibTableRow
concReportTemplateRcdEntry = _ConcReportTemplateRcdEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1)
)
concReportTemplateRcdEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdId"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdIndex"),
)
if mibBuilder.loadTexts:
    concReportTemplateRcdEntry.setStatus("current")


class _ConcReportTemplateRcdId_Type(Integer32):
    """Custom type concReportTemplateRcdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcReportTemplateRcdId_Type.__name__ = "Integer32"
_ConcReportTemplateRcdId_Object = MibTableColumn
concReportTemplateRcdId = _ConcReportTemplateRcdId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 1),
    _ConcReportTemplateRcdId_Type()
)
concReportTemplateRcdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concReportTemplateRcdId.setStatus("current")


class _ConcReportTemplateRcdIndex_Type(Integer32):
    """Custom type concReportTemplateRcdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcReportTemplateRcdIndex_Type.__name__ = "Integer32"
_ConcReportTemplateRcdIndex_Object = MibTableColumn
concReportTemplateRcdIndex = _ConcReportTemplateRcdIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 2),
    _ConcReportTemplateRcdIndex_Type()
)
concReportTemplateRcdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concReportTemplateRcdIndex.setStatus("current")
_ConcReportTemplateRcdInfoEltId_Type = Integer32
_ConcReportTemplateRcdInfoEltId_Object = MibTableColumn
concReportTemplateRcdInfoEltId = _ConcReportTemplateRcdInfoEltId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 3),
    _ConcReportTemplateRcdInfoEltId_Type()
)
concReportTemplateRcdInfoEltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concReportTemplateRcdInfoEltId.setStatus("current")
_ConcReportTemplateRcdRowStatus_Type = RowStatus
_ConcReportTemplateRcdRowStatus_Object = MibTableColumn
concReportTemplateRcdRowStatus = _ConcReportTemplateRcdRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 4, 3, 1, 4),
    _ConcReportTemplateRcdRowStatus_Type()
)
concReportTemplateRcdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concReportTemplateRcdRowStatus.setStatus("current")
_ConcStoring_ObjectIdentity = ObjectIdentity
concStoring = _ConcStoring_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5)
)


class _ConcStoringIsAvail_Type(TruthValue):
    """Custom type concStoringIsAvail based on TruthValue"""


_ConcStoringIsAvail_Object = MibScalar
concStoringIsAvail = _ConcStoringIsAvail_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 1),
    _ConcStoringIsAvail_Type()
)
concStoringIsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concStoringIsAvail.setStatus("current")
_ConcStoringParamSetTable_Object = MibTable
concStoringParamSetTable = _ConcStoringParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2)
)
if mibBuilder.loadTexts:
    concStoringParamSetTable.setStatus("current")
_ConcStoringParamSetEntry_Object = MibTableRow
concStoringParamSetEntry = _ConcStoringParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1)
)
concStoringParamSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concStoringIndex"),
)
if mibBuilder.loadTexts:
    concStoringParamSetEntry.setStatus("current")


class _ConcStoringIndex_Type(Integer32):
    """Custom type concStoringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcStoringIndex_Type.__name__ = "Integer32"
_ConcStoringIndex_Object = MibTableColumn
concStoringIndex = _ConcStoringIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 1),
    _ConcStoringIndex_Type()
)
concStoringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concStoringIndex.setStatus("current")


class _ConcStoringSourceidModifier_Type(ConcFieldModifier):
    """Custom type concStoringSourceidModifier based on ConcFieldModifier"""


_ConcStoringSourceidModifier_Object = MibTableColumn
concStoringSourceidModifier = _ConcStoringSourceidModifier_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 2),
    _ConcStoringSourceidModifier_Type()
)
concStoringSourceidModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringSourceidModifier.setStatus("current")


class _ConcStoringExportTimeModifier_Type(ConcFieldModifier):
    """Custom type concStoringExportTimeModifier based on ConcFieldModifier"""


_ConcStoringExportTimeModifier_Object = MibTableColumn
concStoringExportTimeModifier = _ConcStoringExportTimeModifier_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 3),
    _ConcStoringExportTimeModifier_Type()
)
concStoringExportTimeModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringExportTimeModifier.setStatus("current")
_ConcStoringProcessId_Type = Integer32
_ConcStoringProcessId_Object = MibTableColumn
concStoringProcessId = _ConcStoringProcessId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 4),
    _ConcStoringProcessId_Type()
)
concStoringProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concStoringProcessId.setStatus("current")
_ConcStoringParamRowStatus_Type = RowStatus
_ConcStoringParamRowStatus_Object = MibTableColumn
concStoringParamRowStatus = _ConcStoringParamRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 2, 1, 5),
    _ConcStoringParamRowStatus_Type()
)
concStoringParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringParamRowStatus.setStatus("current")
_ConcStoringFieldSetTable_Object = MibTable
concStoringFieldSetTable = _ConcStoringFieldSetTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 3)
)
if mibBuilder.loadTexts:
    concStoringFieldSetTable.setStatus("current")
_ConcStoringFieldSetEntry_Object = MibTableRow
concStoringFieldSetEntry = _ConcStoringFieldSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1)
)
concStoringFieldSetEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concStoringIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concStoringInfoEltId"),
)
if mibBuilder.loadTexts:
    concStoringFieldSetEntry.setStatus("current")


class _ConcStoringInfoEltId_Type(Integer32):
    """Custom type concStoringInfoEltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcStoringInfoEltId_Type.__name__ = "Integer32"
_ConcStoringInfoEltId_Object = MibTableColumn
concStoringInfoEltId = _ConcStoringInfoEltId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 2),
    _ConcStoringInfoEltId_Type()
)
concStoringInfoEltId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringInfoEltId.setStatus("current")


class _ConcStoringFieldModifier_Type(ConcFieldModifier):
    """Custom type concStoringFieldModifier based on ConcFieldModifier"""


_ConcStoringFieldModifier_Object = MibTableColumn
concStoringFieldModifier = _ConcStoringFieldModifier_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 3),
    _ConcStoringFieldModifier_Type()
)
concStoringFieldModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringFieldModifier.setStatus("current")
_ConcStoringRowStatus_Type = RowStatus
_ConcStoringRowStatus_Object = MibTableColumn
concStoringRowStatus = _ConcStoringRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 5, 3, 1, 4),
    _ConcStoringRowStatus_Type()
)
concStoringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concStoringRowStatus.setStatus("current")
_ConcBaseAssociations_ObjectIdentity = ObjectIdentity
concBaseAssociations = _ConcBaseAssociations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6)
)
_ConcBaseAssocTable_Object = MibTable
concBaseAssocTable = _ConcBaseAssocTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1)
)
if mibBuilder.loadTexts:
    concBaseAssocTable.setStatus("current")
_ConcBaseAssocEntry_Object = MibTableRow
concBaseAssocEntry = _ConcBaseAssocEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1)
)
concBaseAssocEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concBaseAssocIndex"),
)
if mibBuilder.loadTexts:
    concBaseAssocEntry.setStatus("current")


class _ConcBaseAssocIndex_Type(Integer32):
    """Custom type concBaseAssocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocIndex_Type.__name__ = "Integer32"
_ConcBaseAssocIndex_Object = MibTableColumn
concBaseAssocIndex = _ConcBaseAssocIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 1),
    _ConcBaseAssocIndex_Type()
)
concBaseAssocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concBaseAssocIndex.setStatus("current")


class _ConcBaseAssocSelectMatchIndex_Type(Integer32):
    """Custom type concBaseAssocSelectMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocSelectMatchIndex_Type.__name__ = "Integer32"
_ConcBaseAssocSelectMatchIndex_Object = MibTableColumn
concBaseAssocSelectMatchIndex = _ConcBaseAssocSelectMatchIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 2),
    _ConcBaseAssocSelectMatchIndex_Type()
)
concBaseAssocSelectMatchIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocSelectMatchIndex.setStatus("current")


class _ConcBaseAssocAggrIndex_Type(Integer32):
    """Custom type concBaseAssocAggrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocAggrIndex_Type.__name__ = "Integer32"
_ConcBaseAssocAggrIndex_Object = MibTableColumn
concBaseAssocAggrIndex = _ConcBaseAssocAggrIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 3),
    _ConcBaseAssocAggrIndex_Type()
)
concBaseAssocAggrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocAggrIndex.setStatus("current")


class _ConcBaseAssocReportCtrGrIndex_Type(Integer32):
    """Custom type concBaseAssocReportCtrGrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocReportCtrGrIndex_Type.__name__ = "Integer32"
_ConcBaseAssocReportCtrGrIndex_Object = MibTableColumn
concBaseAssocReportCtrGrIndex = _ConcBaseAssocReportCtrGrIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 4),
    _ConcBaseAssocReportCtrGrIndex_Type()
)
concBaseAssocReportCtrGrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocReportCtrGrIndex.setStatus("current")


class _ConcBaseAssocReportTemplateRcdId_Type(Integer32):
    """Custom type concBaseAssocReportTemplateRcdId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocReportTemplateRcdId_Type.__name__ = "Integer32"
_ConcBaseAssocReportTemplateRcdId_Object = MibTableColumn
concBaseAssocReportTemplateRcdId = _ConcBaseAssocReportTemplateRcdId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 5),
    _ConcBaseAssocReportTemplateRcdId_Type()
)
concBaseAssocReportTemplateRcdId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocReportTemplateRcdId.setStatus("current")


class _ConcBaseAssocStoringIndex_Type(Integer32):
    """Custom type concBaseAssocStoringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcBaseAssocStoringIndex_Type.__name__ = "Integer32"
_ConcBaseAssocStoringIndex_Object = MibTableColumn
concBaseAssocStoringIndex = _ConcBaseAssocStoringIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 6),
    _ConcBaseAssocStoringIndex_Type()
)
concBaseAssocStoringIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocStoringIndex.setStatus("current")
_ConcBaseAssocMeteringProcessId_Type = Integer32
_ConcBaseAssocMeteringProcessId_Object = MibTableColumn
concBaseAssocMeteringProcessId = _ConcBaseAssocMeteringProcessId_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 7),
    _ConcBaseAssocMeteringProcessId_Type()
)
concBaseAssocMeteringProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concBaseAssocMeteringProcessId.setStatus("current")
_ConcBaseAssocExtractIndex_Type = Integer32
_ConcBaseAssocExtractIndex_Object = MibTableColumn
concBaseAssocExtractIndex = _ConcBaseAssocExtractIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 8),
    _ConcBaseAssocExtractIndex_Type()
)
concBaseAssocExtractIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concBaseAssocExtractIndex.setStatus("current")
_ConcBaseAssocRowStatus_Type = RowStatus
_ConcBaseAssocRowStatus_Object = MibTableColumn
concBaseAssocRowStatus = _ConcBaseAssocRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 1, 1, 9),
    _ConcBaseAssocRowStatus_Type()
)
concBaseAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concBaseAssocRowStatus.setStatus("current")
_ConcExporterListTable_Object = MibTable
concExporterListTable = _ConcExporterListTable_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 2)
)
if mibBuilder.loadTexts:
    concExporterListTable.setStatus("current")
_ConcExporterListEntry_Object = MibTableRow
concExporterListEntry = _ConcExporterListEntry_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1)
)
concExporterListEntry.setIndexNames(
    (0, "IPFIX-CONCENTRATOR-MIB", "concBaseAssocIndex"),
    (0, "IPFIX-CONCENTRATOR-MIB", "concExporterListIndex"),
)
if mibBuilder.loadTexts:
    concExporterListEntry.setStatus("current")


class _ConcExporterListIndex_Type(Integer32):
    """Custom type concExporterListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConcExporterListIndex_Type.__name__ = "Integer32"
_ConcExporterListIndex_Object = MibTableColumn
concExporterListIndex = _ConcExporterListIndex_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 2),
    _ConcExporterListIndex_Type()
)
concExporterListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    concExporterListIndex.setStatus("current")
_ConcExporterListMethod_Type = ObjectIdentifier
_ConcExporterListMethod_Object = MibTableColumn
concExporterListMethod = _ConcExporterListMethod_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 3),
    _ConcExporterListMethod_Type()
)
concExporterListMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExporterListMethod.setStatus("current")
_ConcExporterListRowStatus_Type = RowStatus
_ConcExporterListRowStatus_Object = MibTableColumn
concExporterListRowStatus = _ConcExporterListRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 5555, 1, 6, 2, 1, 4),
    _ConcExporterListRowStatus_Type()
)
concExporterListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    concExporterListRowStatus.setStatus("current")
_ConcentratorConformance_ObjectIdentity = ObjectIdentity
concentratorConformance = _ConcentratorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 2)
)
_ConcCompliances_ObjectIdentity = ObjectIdentity
concCompliances = _ConcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 2, 1)
)
_ConcGroups_ObjectIdentity = ObjectIdentity
concGroups = _ConcGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5555, 2, 2)
)

# Managed Objects groups

concGroupMetering = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 5555, 2, 2, 1)
)
concGroupMetering.setObjects(
      *(("IPFIX-CONCENTRATOR-MIB", "concAggrTimeInterval"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrParamRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldModifier"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrFieldSetId"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrIsAvail"),
        ("IPFIX-CONCENTRATOR-MIB", "concAggrAddFieldSetId"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchInfoEltId"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchStartValue"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchEndValue"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchMask"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectMatchRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concSelectIsAvail"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstIpAddrType"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstIpAddr"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstProtocol"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrDstPort"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrReportsSent"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportCtrGrRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdInfoEltId"),
        ("IPFIX-CONCENTRATOR-MIB", "concReportTemplateRcdRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocReportCtrGrIndex"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocReportTemplateRcdId"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocSelectMatchIndex"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocAggrIndex"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocMeteringProcessId"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concExporterListMethod"),
        ("IPFIX-CONCENTRATOR-MIB", "concExporterListRowStatus"))
)
if mibBuilder.loadTexts:
    concGroupMetering.setStatus("current")

concGroupExtracting = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 5555, 2, 2, 2)
)
concGroupExtracting.setObjects(
      *(("IPFIX-CONCENTRATOR-MIB", "concExtractIsAvail"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractEtrIpAddrType"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractEtrIpAddr"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractStartTime"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractEndTime"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractProcessId"),
        ("IPFIX-CONCENTRATOR-MIB", "concExtractRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocExtractIndex"))
)
if mibBuilder.loadTexts:
    concGroupExtracting.setStatus("current")

concGroupStoring = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 5555, 2, 2, 3)
)
concGroupStoring.setObjects(
      *(("IPFIX-CONCENTRATOR-MIB", "concStoringSourceidModifier"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringExportTimeModifier"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringProcessId"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringParamRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concBaseAssocStoringIndex"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringRowStatus"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringFieldModifier"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringInfoEltId"),
        ("IPFIX-CONCENTRATOR-MIB", "concStoringIsAvail"))
)
if mibBuilder.loadTexts:
    concGroupStoring.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

concCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 5555, 2, 1, 1)
)
if mibBuilder.loadTexts:
    concCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-CONCENTRATOR-MIB",
    **{"ConcFieldModifier": ConcFieldModifier,
       "ipfixConcentratorMIB": ipfixConcentratorMIB,
       "concentratorObjects": concentratorObjects,
       "concExtraction": concExtraction,
       "concExtractIsAvail": concExtractIsAvail,
       "concExtractTable": concExtractTable,
       "concExtractEntry": concExtractEntry,
       "concExtractIndex": concExtractIndex,
       "concExtractEtrIpAddrType": concExtractEtrIpAddrType,
       "concExtractEtrIpAddr": concExtractEtrIpAddr,
       "concExtractStartTime": concExtractStartTime,
       "concExtractEndTime": concExtractEndTime,
       "concExtractProcessId": concExtractProcessId,
       "concExtractRowStatus": concExtractRowStatus,
       "concSelection": concSelection,
       "concSelectIsAvail": concSelectIsAvail,
       "concSelectMatchParamSetTable": concSelectMatchParamSetTable,
       "concSelectMatchParamSetEntry": concSelectMatchParamSetEntry,
       "concSelectMatchIndex": concSelectMatchIndex,
       "concSelectMatchInfoEltId": concSelectMatchInfoEltId,
       "concSelectMatchStartValue": concSelectMatchStartValue,
       "concSelectMatchEndValue": concSelectMatchEndValue,
       "concSelectMatchMask": concSelectMatchMask,
       "concSelectMatchRowStatus": concSelectMatchRowStatus,
       "concAggregation": concAggregation,
       "concAggrIsAvail": concAggrIsAvail,
       "concAggrParamSetTable": concAggrParamSetTable,
       "concAggrParamSetEntry": concAggrParamSetEntry,
       "concAggrIndex": concAggrIndex,
       "concAggrTimeInterval": concAggrTimeInterval,
       "concAggrParamRowStatus": concAggrParamRowStatus,
       "concAggrFieldSetTable": concAggrFieldSetTable,
       "concAggrFieldSetEntry": concAggrFieldSetEntry,
       "concAggrFieldSetId": concAggrFieldSetId,
       "concAggrFieldModifier": concAggrFieldModifier,
       "concAggrFieldRowStatus": concAggrFieldRowStatus,
       "concAggrAddFieldSetTable": concAggrAddFieldSetTable,
       "concAggrAddFieldSetEntry": concAggrAddFieldSetEntry,
       "concAggrAddFieldSetId": concAggrAddFieldSetId,
       "concAggrAddFieldRowStatus": concAggrAddFieldRowStatus,
       "concReport": concReport,
       "concReportCtrTable": concReportCtrTable,
       "concReportCtrEntry": concReportCtrEntry,
       "concReportCtrIndex": concReportCtrIndex,
       "concReportCtrDstIpAddrType": concReportCtrDstIpAddrType,
       "concReportCtrDstIpAddr": concReportCtrDstIpAddr,
       "concReportCtrDstProtocol": concReportCtrDstProtocol,
       "concReportCtrDstPort": concReportCtrDstPort,
       "concReportCtrReportsSent": concReportCtrReportsSent,
       "concReportCtrRowStatus": concReportCtrRowStatus,
       "concReportCtrGrTable": concReportCtrGrTable,
       "concReportCtrGrEntry": concReportCtrGrEntry,
       "concReportCtrGrIndex": concReportCtrGrIndex,
       "concReportCtrGrRowStatus": concReportCtrGrRowStatus,
       "concReportTemplateRcdTable": concReportTemplateRcdTable,
       "concReportTemplateRcdEntry": concReportTemplateRcdEntry,
       "concReportTemplateRcdId": concReportTemplateRcdId,
       "concReportTemplateRcdIndex": concReportTemplateRcdIndex,
       "concReportTemplateRcdInfoEltId": concReportTemplateRcdInfoEltId,
       "concReportTemplateRcdRowStatus": concReportTemplateRcdRowStatus,
       "concStoring": concStoring,
       "concStoringIsAvail": concStoringIsAvail,
       "concStoringParamSetTable": concStoringParamSetTable,
       "concStoringParamSetEntry": concStoringParamSetEntry,
       "concStoringIndex": concStoringIndex,
       "concStoringSourceidModifier": concStoringSourceidModifier,
       "concStoringExportTimeModifier": concStoringExportTimeModifier,
       "concStoringProcessId": concStoringProcessId,
       "concStoringParamRowStatus": concStoringParamRowStatus,
       "concStoringFieldSetTable": concStoringFieldSetTable,
       "concStoringFieldSetEntry": concStoringFieldSetEntry,
       "concStoringInfoEltId": concStoringInfoEltId,
       "concStoringFieldModifier": concStoringFieldModifier,
       "concStoringRowStatus": concStoringRowStatus,
       "concBaseAssociations": concBaseAssociations,
       "concBaseAssocTable": concBaseAssocTable,
       "concBaseAssocEntry": concBaseAssocEntry,
       "concBaseAssocIndex": concBaseAssocIndex,
       "concBaseAssocSelectMatchIndex": concBaseAssocSelectMatchIndex,
       "concBaseAssocAggrIndex": concBaseAssocAggrIndex,
       "concBaseAssocReportCtrGrIndex": concBaseAssocReportCtrGrIndex,
       "concBaseAssocReportTemplateRcdId": concBaseAssocReportTemplateRcdId,
       "concBaseAssocStoringIndex": concBaseAssocStoringIndex,
       "concBaseAssocMeteringProcessId": concBaseAssocMeteringProcessId,
       "concBaseAssocExtractIndex": concBaseAssocExtractIndex,
       "concBaseAssocRowStatus": concBaseAssocRowStatus,
       "concExporterListTable": concExporterListTable,
       "concExporterListEntry": concExporterListEntry,
       "concExporterListIndex": concExporterListIndex,
       "concExporterListMethod": concExporterListMethod,
       "concExporterListRowStatus": concExporterListRowStatus,
       "concentratorConformance": concentratorConformance,
       "concCompliances": concCompliances,
       "concCompliance": concCompliance,
       "concGroups": concGroups,
       "concGroupMetering": concGroupMetering,
       "concGroupExtracting": concGroupExtracting,
       "concGroupStoring": concGroupStoring}
)
