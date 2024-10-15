# SNMP MIB module (IPFIX-EXPORTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFIX-EXPORTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:49 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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

ipfixMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999)
)
ipfixMIB.setRevisions(
        ("2006-10-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PsampMethodAvailability(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_IpfixExporter_ObjectIdentity = ObjectIdentity
ipfixExporter = _IpfixExporter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1)
)
_IpfixExporterObjects_ObjectIdentity = ObjectIdentity
ipfixExporterObjects = _IpfixExporterObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1)
)
_IpfixReporting_ObjectIdentity = ObjectIdentity
ipfixReporting = _IpfixReporting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1)
)
_IpfixCollectorTable_Object = MibTable
ipfixCollectorTable = _IpfixCollectorTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixCollectorTable.setStatus("current")
_IpfixCollectorEntry_Object = MibTableRow
ipfixCollectorEntry = _IpfixCollectorEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1)
)
ipfixCollectorEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixCollectorIndex"),
)
if mibBuilder.loadTexts:
    ipfixCollectorEntry.setStatus("current")


class _IpfixCollectorIndex_Type(Integer32):
    """Custom type ipfixCollectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixCollectorIndex_Type.__name__ = "Integer32"
_IpfixCollectorIndex_Object = MibTableColumn
ipfixCollectorIndex = _IpfixCollectorIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 1),
    _IpfixCollectorIndex_Type()
)
ipfixCollectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixCollectorIndex.setStatus("current")
_IpfixCollectorDstIpAddressType_Type = InetAddressType
_IpfixCollectorDstIpAddressType_Object = MibTableColumn
ipfixCollectorDstIpAddressType = _IpfixCollectorDstIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 2),
    _IpfixCollectorDstIpAddressType_Type()
)
ipfixCollectorDstIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixCollectorDstIpAddressType.setStatus("current")
_IpfixCollectorDstIpAddress_Type = InetAddress
_IpfixCollectorDstIpAddress_Object = MibTableColumn
ipfixCollectorDstIpAddress = _IpfixCollectorDstIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 3),
    _IpfixCollectorDstIpAddress_Type()
)
ipfixCollectorDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixCollectorDstIpAddress.setStatus("current")


class _IpfixCollectorDstProtocol_Type(Integer32):
    """Custom type ipfixCollectorDstProtocol based on Integer32"""
    defaultValue = 132

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpfixCollectorDstProtocol_Type.__name__ = "Integer32"
_IpfixCollectorDstProtocol_Object = MibTableColumn
ipfixCollectorDstProtocol = _IpfixCollectorDstProtocol_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 4),
    _IpfixCollectorDstProtocol_Type()
)
ipfixCollectorDstProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixCollectorDstProtocol.setStatus("current")


class _IpfixCollectorDstPort_Type(Integer32):
    """Custom type ipfixCollectorDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpfixCollectorDstPort_Type.__name__ = "Integer32"
_IpfixCollectorDstPort_Object = MibTableColumn
ipfixCollectorDstPort = _IpfixCollectorDstPort_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 5),
    _IpfixCollectorDstPort_Type()
)
ipfixCollectorDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixCollectorDstPort.setStatus("current")
_IpfixCollectorReportsSent_Type = Integer32
_IpfixCollectorReportsSent_Object = MibTableColumn
ipfixCollectorReportsSent = _IpfixCollectorReportsSent_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 6),
    _IpfixCollectorReportsSent_Type()
)
ipfixCollectorReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixCollectorReportsSent.setStatus("current")
_IpfixCollectorGroupTable_Object = MibTable
ipfixCollectorGroupTable = _IpfixCollectorGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipfixCollectorGroupTable.setStatus("current")
_IpfixCollectorGroupEntry_Object = MibTableRow
ipfixCollectorGroupEntry = _IpfixCollectorGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2, 1)
)
ipfixCollectorGroupEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixCollectorGroupIndex"),
    (0, "IPFIX-EXPORTER-MIB", "ipfixCollectorIndex"),
)
if mibBuilder.loadTexts:
    ipfixCollectorGroupEntry.setStatus("current")


class _IpfixCollectorGroupIndex_Type(Integer32):
    """Custom type ipfixCollectorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixCollectorGroupIndex_Type.__name__ = "Integer32"
_IpfixCollectorGroupIndex_Object = MibTableColumn
ipfixCollectorGroupIndex = _IpfixCollectorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2, 1, 1),
    _IpfixCollectorGroupIndex_Type()
)
ipfixCollectorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixCollectorGroupIndex.setStatus("current")
_IpfixTemplateTable_Object = MibTable
ipfixTemplateTable = _IpfixTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipfixTemplateTable.setStatus("current")
_IpfixTemplateEntry_Object = MibTableRow
ipfixTemplateEntry = _IpfixTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1)
)
ipfixTemplateEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"),
    (0, "IPFIX-EXPORTER-MIB", "ipfixTemplateId"),
    (0, "IPFIX-EXPORTER-MIB", "ipfixTemplateIndex"),
)
if mibBuilder.loadTexts:
    ipfixTemplateEntry.setStatus("current")


class _IpfixTemplateId_Type(Integer32):
    """Custom type ipfixTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixTemplateId_Type.__name__ = "Integer32"
_IpfixTemplateId_Object = MibTableColumn
ipfixTemplateId = _IpfixTemplateId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 1),
    _IpfixTemplateId_Type()
)
ipfixTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateId.setStatus("current")


class _IpfixTemplateIndex_Type(Integer32):
    """Custom type ipfixTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixTemplateIndex_Type.__name__ = "Integer32"
_IpfixTemplateIndex_Object = MibTableColumn
ipfixTemplateIndex = _IpfixTemplateIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 2),
    _IpfixTemplateIndex_Type()
)
ipfixTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateIndex.setStatus("current")
_IpfixTemplateFieldId_Type = Integer32
_IpfixTemplateFieldId_Object = MibTableColumn
ipfixTemplateFieldId = _IpfixTemplateFieldId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 3),
    _IpfixTemplateFieldId_Type()
)
ipfixTemplateFieldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateFieldId.setStatus("current")
_IpfixTemplateFieldLength_Type = Integer32
_IpfixTemplateFieldLength_Object = MibTableColumn
ipfixTemplateFieldLength = _IpfixTemplateFieldLength_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 4),
    _IpfixTemplateFieldLength_Type()
)
ipfixTemplateFieldLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateFieldLength.setStatus("current")
_IpfixInstances_ObjectIdentity = ObjectIdentity
ipfixInstances = _IpfixInstances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2)
)
_IpfixObservationDomainTable_Object = MibTable
ipfixObservationDomainTable = _IpfixObservationDomainTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipfixObservationDomainTable.setStatus("current")
_IpfixObservationDomainEntry_Object = MibTableRow
ipfixObservationDomainEntry = _IpfixObservationDomainEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1)
)
ipfixObservationDomainEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"),
)
if mibBuilder.loadTexts:
    ipfixObservationDomainEntry.setStatus("current")


class _IpfixObservationDomainId_Type(Integer32):
    """Custom type ipfixObservationDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixObservationDomainId_Type.__name__ = "Integer32"
_IpfixObservationDomainId_Object = MibTableColumn
ipfixObservationDomainId = _IpfixObservationDomainId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 1),
    _IpfixObservationDomainId_Type()
)
ipfixObservationDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixObservationDomainId.setStatus("current")
_IpfixInstanceObservationPoint_Type = ObjectIdentifier
_IpfixInstanceObservationPoint_Object = MibTableColumn
ipfixInstanceObservationPoint = _IpfixInstanceObservationPoint_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 2),
    _IpfixInstanceObservationPoint_Type()
)
ipfixInstanceObservationPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixInstanceObservationPoint.setStatus("current")
_IpfixInstanceStartTime_Type = DateAndTime
_IpfixInstanceStartTime_Object = MibTableColumn
ipfixInstanceStartTime = _IpfixInstanceStartTime_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 3),
    _IpfixInstanceStartTime_Type()
)
ipfixInstanceStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixInstanceStartTime.setStatus("current")
_IpfixInstanceStopTime_Type = DateAndTime
_IpfixInstanceStopTime_Object = MibTableColumn
ipfixInstanceStopTime = _IpfixInstanceStopTime_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 4),
    _IpfixInstanceStopTime_Type()
)
ipfixInstanceStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixInstanceStopTime.setStatus("current")
_IpfixInstanceTable_Object = MibTable
ipfixInstanceTable = _IpfixInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipfixInstanceTable.setStatus("current")
_IpfixInstanceEntry_Object = MibTableRow
ipfixInstanceEntry = _IpfixInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1)
)
ipfixInstanceEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixInstanceIndex"),
    (0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"),
)
if mibBuilder.loadTexts:
    ipfixInstanceEntry.setStatus("current")


class _IpfixInstanceIndex_Type(Integer32):
    """Custom type ipfixInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixInstanceIndex_Type.__name__ = "Integer32"
_IpfixInstanceIndex_Object = MibTableColumn
ipfixInstanceIndex = _IpfixInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 1),
    _IpfixInstanceIndex_Type()
)
ipfixInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixInstanceIndex.setStatus("current")


class _IpfixInstanceTemplateId_Type(Integer32):
    """Custom type ipfixInstanceTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixInstanceTemplateId_Type.__name__ = "Integer32"
_IpfixInstanceTemplateId_Object = MibTableColumn
ipfixInstanceTemplateId = _IpfixInstanceTemplateId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 2),
    _IpfixInstanceTemplateId_Type()
)
ipfixInstanceTemplateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixInstanceTemplateId.setStatus("current")
_IpfixInstanceCollectorGroupIndex_Type = Integer32
_IpfixInstanceCollectorGroupIndex_Object = MibTableColumn
ipfixInstanceCollectorGroupIndex = _IpfixInstanceCollectorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 3),
    _IpfixInstanceCollectorGroupIndex_Type()
)
ipfixInstanceCollectorGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixInstanceCollectorGroupIndex.setStatus("current")
_IpfixInstancePacketsObserved_Type = Integer32
_IpfixInstancePacketsObserved_Object = MibTableColumn
ipfixInstancePacketsObserved = _IpfixInstancePacketsObserved_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 4),
    _IpfixInstancePacketsObserved_Type()
)
ipfixInstancePacketsObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixInstancePacketsObserved.setStatus("current")
_IpfixInstancePacketsDropped_Type = Integer32
_IpfixInstancePacketsDropped_Object = MibTableColumn
ipfixInstancePacketsDropped = _IpfixInstancePacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 5),
    _IpfixInstancePacketsDropped_Type()
)
ipfixInstancePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixInstancePacketsDropped.setStatus("current")
_IpfixInstanceProcessId_Type = Integer32
_IpfixInstanceProcessId_Object = MibTableColumn
ipfixInstanceProcessId = _IpfixInstanceProcessId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 6),
    _IpfixInstanceProcessId_Type()
)
ipfixInstanceProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixInstanceProcessId.setStatus("current")
_IpfixInstanceReportingProcessId_Type = Integer32
_IpfixInstanceReportingProcessId_Object = MibTableColumn
ipfixInstanceReportingProcessId = _IpfixInstanceReportingProcessId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 7),
    _IpfixInstanceReportingProcessId_Type()
)
ipfixInstanceReportingProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixInstanceReportingProcessId.setStatus("current")
_IpfixInstanceReportsSent_Type = Integer32
_IpfixInstanceReportsSent_Object = MibTableColumn
ipfixInstanceReportsSent = _IpfixInstanceReportsSent_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 8),
    _IpfixInstanceReportsSent_Type()
)
ipfixInstanceReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixInstanceReportsSent.setStatus("current")
_IpfixMethodChainTable_Object = MibTable
ipfixMethodChainTable = _IpfixMethodChainTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ipfixMethodChainTable.setStatus("current")
_IpfixMethodChainEntry_Object = MibTableRow
ipfixMethodChainEntry = _IpfixMethodChainEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1)
)
ipfixMethodChainEntry.setIndexNames(
    (0, "IPFIX-EXPORTER-MIB", "ipfixInstanceIndex"),
    (0, "IPFIX-EXPORTER-MIB", "ipfixMethodChainIndex"),
)
if mibBuilder.loadTexts:
    ipfixMethodChainEntry.setStatus("current")


class _IpfixMethodChainIndex_Type(Integer32):
    """Custom type ipfixMethodChainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixMethodChainIndex_Type.__name__ = "Integer32"
_IpfixMethodChainIndex_Object = MibTableColumn
ipfixMethodChainIndex = _IpfixMethodChainIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 2),
    _IpfixMethodChainIndex_Type()
)
ipfixMethodChainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixMethodChainIndex.setStatus("current")
_IpfixMethodChainMethod_Type = ObjectIdentifier
_IpfixMethodChainMethod_Object = MibTableColumn
ipfixMethodChainMethod = _IpfixMethodChainMethod_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 3),
    _IpfixMethodChainMethod_Type()
)
ipfixMethodChainMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipfixMethodChainMethod.setStatus("current")
_IpfixMethodChainPacketsObserved_Type = Integer32
_IpfixMethodChainPacketsObserved_Object = MibTableColumn
ipfixMethodChainPacketsObserved = _IpfixMethodChainPacketsObserved_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 4),
    _IpfixMethodChainPacketsObserved_Type()
)
ipfixMethodChainPacketsObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMethodChainPacketsObserved.setStatus("current")
_IpfixMethodChainPacketsDropped_Type = Integer32
_IpfixMethodChainPacketsDropped_Object = MibTableColumn
ipfixMethodChainPacketsDropped = _IpfixMethodChainPacketsDropped_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 5),
    _IpfixMethodChainPacketsDropped_Type()
)
ipfixMethodChainPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixMethodChainPacketsDropped.setStatus("current")
_IpfixCollector_ObjectIdentity = ObjectIdentity
ipfixCollector = _IpfixCollector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2)
)
_IpfixPsampExtension_ObjectIdentity = ObjectIdentity
ipfixPsampExtension = _IpfixPsampExtension_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 3)
)
_IpfixConformance_ObjectIdentity = ObjectIdentity
ipfixConformance = _IpfixConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4)
)
_IpfixCompliances_ObjectIdentity = ObjectIdentity
ipfixCompliances = _IpfixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4, 1)
)
_IpfixGroups_ObjectIdentity = ObjectIdentity
ipfixGroups = _IpfixGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4, 2)
)

# Managed Objects groups

ipfixGroupMetering = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 1)
)
ipfixGroupMetering.setObjects(
      *(("IPFIX-EXPORTER-MIB", "ipfixTemplateFieldId"),
        ("IPFIX-EXPORTER-MIB", "ipfixTemplateFieldLength"),
        ("IPFIX-EXPORTER-MIB", "ipfixMethodChainMethod"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceObservationPoint"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceStartTime"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceStopTime"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceTemplateId"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceCollectorGroupIndex"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceProcessId"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceReportingProcessId"))
)
if mibBuilder.loadTexts:
    ipfixGroupMetering.setStatus("current")

ipfixGroupReporting = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 2)
)
ipfixGroupReporting.setObjects(
      *(("IPFIX-EXPORTER-MIB", "ipfixCollectorDstIpAddressType"),
        ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstIpAddress"),
        ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstProtocol"),
        ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstPort"))
)
if mibBuilder.loadTexts:
    ipfixGroupReporting.setStatus("current")

ipfixGroupStatistics = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 3)
)
ipfixGroupStatistics.setObjects(
      *(("IPFIX-EXPORTER-MIB", "ipfixCollectorReportsSent"),
        ("IPFIX-EXPORTER-MIB", "ipfixMethodChainPacketsObserved"),
        ("IPFIX-EXPORTER-MIB", "ipfixMethodChainPacketsDropped"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstancePacketsObserved"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstanceReportsSent"),
        ("IPFIX-EXPORTER-MIB", "ipfixInstancePacketsDropped"))
)
if mibBuilder.loadTexts:
    ipfixGroupStatistics.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipfixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-EXPORTER-MIB",
    **{"PsampMethodAvailability": PsampMethodAvailability,
       "ipfixMIB": ipfixMIB,
       "ipfixExporter": ipfixExporter,
       "ipfixExporterObjects": ipfixExporterObjects,
       "ipfixReporting": ipfixReporting,
       "ipfixCollectorTable": ipfixCollectorTable,
       "ipfixCollectorEntry": ipfixCollectorEntry,
       "ipfixCollectorIndex": ipfixCollectorIndex,
       "ipfixCollectorDstIpAddressType": ipfixCollectorDstIpAddressType,
       "ipfixCollectorDstIpAddress": ipfixCollectorDstIpAddress,
       "ipfixCollectorDstProtocol": ipfixCollectorDstProtocol,
       "ipfixCollectorDstPort": ipfixCollectorDstPort,
       "ipfixCollectorReportsSent": ipfixCollectorReportsSent,
       "ipfixCollectorGroupTable": ipfixCollectorGroupTable,
       "ipfixCollectorGroupEntry": ipfixCollectorGroupEntry,
       "ipfixCollectorGroupIndex": ipfixCollectorGroupIndex,
       "ipfixTemplateTable": ipfixTemplateTable,
       "ipfixTemplateEntry": ipfixTemplateEntry,
       "ipfixTemplateId": ipfixTemplateId,
       "ipfixTemplateIndex": ipfixTemplateIndex,
       "ipfixTemplateFieldId": ipfixTemplateFieldId,
       "ipfixTemplateFieldLength": ipfixTemplateFieldLength,
       "ipfixInstances": ipfixInstances,
       "ipfixObservationDomainTable": ipfixObservationDomainTable,
       "ipfixObservationDomainEntry": ipfixObservationDomainEntry,
       "ipfixObservationDomainId": ipfixObservationDomainId,
       "ipfixInstanceObservationPoint": ipfixInstanceObservationPoint,
       "ipfixInstanceStartTime": ipfixInstanceStartTime,
       "ipfixInstanceStopTime": ipfixInstanceStopTime,
       "ipfixInstanceTable": ipfixInstanceTable,
       "ipfixInstanceEntry": ipfixInstanceEntry,
       "ipfixInstanceIndex": ipfixInstanceIndex,
       "ipfixInstanceTemplateId": ipfixInstanceTemplateId,
       "ipfixInstanceCollectorGroupIndex": ipfixInstanceCollectorGroupIndex,
       "ipfixInstancePacketsObserved": ipfixInstancePacketsObserved,
       "ipfixInstancePacketsDropped": ipfixInstancePacketsDropped,
       "ipfixInstanceProcessId": ipfixInstanceProcessId,
       "ipfixInstanceReportingProcessId": ipfixInstanceReportingProcessId,
       "ipfixInstanceReportsSent": ipfixInstanceReportsSent,
       "ipfixMethodChainTable": ipfixMethodChainTable,
       "ipfixMethodChainEntry": ipfixMethodChainEntry,
       "ipfixMethodChainIndex": ipfixMethodChainIndex,
       "ipfixMethodChainMethod": ipfixMethodChainMethod,
       "ipfixMethodChainPacketsObserved": ipfixMethodChainPacketsObserved,
       "ipfixMethodChainPacketsDropped": ipfixMethodChainPacketsDropped,
       "ipfixCollector": ipfixCollector,
       "ipfixPsampExtension": ipfixPsampExtension,
       "ipfixConformance": ipfixConformance,
       "ipfixCompliances": ipfixCompliances,
       "ipfixCompliance": ipfixCompliance,
       "ipfixGroups": ipfixGroups,
       "ipfixGroupMetering": ipfixGroupMetering,
       "ipfixGroupReporting": ipfixGroupReporting,
       "ipfixGroupStatistics": ipfixGroupStatistics}
)
