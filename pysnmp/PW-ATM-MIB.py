# SNMP MIB module (PW-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:04 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pwAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 183)
)
pwAtmMIB.setRevisions(
        ("2009-06-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PwAtmNotifications_ObjectIdentity = ObjectIdentity
pwAtmNotifications = _PwAtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 183, 0)
)
_PwAtmObjects_ObjectIdentity = ObjectIdentity
pwAtmObjects = _PwAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 183, 1)
)
_PwAtmOutboundTable_Object = MibTable
pwAtmOutboundTable = _PwAtmOutboundTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1)
)
if mibBuilder.loadTexts:
    pwAtmOutboundTable.setStatus("current")
_PwAtmOutboundEntry_Object = MibTableRow
pwAtmOutboundEntry = _PwAtmOutboundEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1)
)
pwAtmOutboundEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwAtmOutboundEntry.setStatus("current")
_PwAtmOutboundAtmIf_Type = InterfaceIndex
_PwAtmOutboundAtmIf_Object = MibTableColumn
pwAtmOutboundAtmIf = _PwAtmOutboundAtmIf_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 1),
    _PwAtmOutboundAtmIf_Type()
)
pwAtmOutboundAtmIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundAtmIf.setStatus("current")
_PwAtmOutboundVpi_Type = AtmVpIdentifier
_PwAtmOutboundVpi_Object = MibTableColumn
pwAtmOutboundVpi = _PwAtmOutboundVpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 2),
    _PwAtmOutboundVpi_Type()
)
pwAtmOutboundVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundVpi.setStatus("current")
_PwAtmOutboundVci_Type = AtmVcIdentifier
_PwAtmOutboundVci_Object = MibTableColumn
pwAtmOutboundVci = _PwAtmOutboundVci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 3),
    _PwAtmOutboundVci_Type()
)
pwAtmOutboundVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundVci.setStatus("current")
_PwAtmOutboundTrafficParamDescr_Type = RowPointer
_PwAtmOutboundTrafficParamDescr_Object = MibTableColumn
pwAtmOutboundTrafficParamDescr = _PwAtmOutboundTrafficParamDescr_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 4),
    _PwAtmOutboundTrafficParamDescr_Type()
)
pwAtmOutboundTrafficParamDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundTrafficParamDescr.setStatus("current")
_PwAtmOutboundRowStatus_Type = RowStatus
_PwAtmOutboundRowStatus_Object = MibTableColumn
pwAtmOutboundRowStatus = _PwAtmOutboundRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 1, 1, 5),
    _PwAtmOutboundRowStatus_Type()
)
pwAtmOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundRowStatus.setStatus("current")
_PwAtmInboundTable_Object = MibTable
pwAtmInboundTable = _PwAtmInboundTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3)
)
if mibBuilder.loadTexts:
    pwAtmInboundTable.setStatus("current")
_PwAtmInboundEntry_Object = MibTableRow
pwAtmInboundEntry = _PwAtmInboundEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1)
)
pwAtmInboundEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwAtmInboundEntry.setStatus("current")
_PwAtmInboundAtmIf_Type = InterfaceIndex
_PwAtmInboundAtmIf_Object = MibTableColumn
pwAtmInboundAtmIf = _PwAtmInboundAtmIf_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 1),
    _PwAtmInboundAtmIf_Type()
)
pwAtmInboundAtmIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundAtmIf.setStatus("current")
_PwAtmInboundVpi_Type = AtmVpIdentifier
_PwAtmInboundVpi_Object = MibTableColumn
pwAtmInboundVpi = _PwAtmInboundVpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 2),
    _PwAtmInboundVpi_Type()
)
pwAtmInboundVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundVpi.setStatus("current")
_PwAtmInboundVci_Type = AtmVcIdentifier
_PwAtmInboundVci_Object = MibTableColumn
pwAtmInboundVci = _PwAtmInboundVci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 3),
    _PwAtmInboundVci_Type()
)
pwAtmInboundVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundVci.setStatus("current")
_PwAtmInboundTrafficParamDescr_Type = RowPointer
_PwAtmInboundTrafficParamDescr_Object = MibTableColumn
pwAtmInboundTrafficParamDescr = _PwAtmInboundTrafficParamDescr_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 4),
    _PwAtmInboundTrafficParamDescr_Type()
)
pwAtmInboundTrafficParamDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundTrafficParamDescr.setStatus("current")
_PwAtmInboundRowStatus_Type = RowStatus
_PwAtmInboundRowStatus_Object = MibTableColumn
pwAtmInboundRowStatus = _PwAtmInboundRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 3, 1, 5),
    _PwAtmInboundRowStatus_Type()
)
pwAtmInboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundRowStatus.setStatus("current")
_PwAtmCfgTable_Object = MibTable
pwAtmCfgTable = _PwAtmCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5)
)
if mibBuilder.loadTexts:
    pwAtmCfgTable.setStatus("current")
_PwAtmCfgEntry_Object = MibTableRow
pwAtmCfgEntry = _PwAtmCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5, 1)
)
pwAtmCfgEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwAtmCfgEntry.setStatus("current")


class _PwAtmCfgMaxCellConcatenation_Type(Unsigned32):
    """Custom type pwAtmCfgMaxCellConcatenation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_PwAtmCfgMaxCellConcatenation_Type.__name__ = "Unsigned32"
_PwAtmCfgMaxCellConcatenation_Object = MibTableColumn
pwAtmCfgMaxCellConcatenation = _PwAtmCfgMaxCellConcatenation_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 1),
    _PwAtmCfgMaxCellConcatenation_Type()
)
pwAtmCfgMaxCellConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAtmCfgMaxCellConcatenation.setStatus("current")


class _PwAtmCfgFarEndMaxCellConcatenation_Type(Unsigned32):
    """Custom type pwAtmCfgFarEndMaxCellConcatenation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_PwAtmCfgFarEndMaxCellConcatenation_Type.__name__ = "Unsigned32"
_PwAtmCfgFarEndMaxCellConcatenation_Object = MibTableColumn
pwAtmCfgFarEndMaxCellConcatenation = _PwAtmCfgFarEndMaxCellConcatenation_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 2),
    _PwAtmCfgFarEndMaxCellConcatenation_Type()
)
pwAtmCfgFarEndMaxCellConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAtmCfgFarEndMaxCellConcatenation.setStatus("current")


class _PwAtmCfgTimeoutMode_Type(Integer32):
    """Custom type pwAtmCfgTimeoutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notApplicable", 1))
    )


_PwAtmCfgTimeoutMode_Type.__name__ = "Integer32"
_PwAtmCfgTimeoutMode_Object = MibTableColumn
pwAtmCfgTimeoutMode = _PwAtmCfgTimeoutMode_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 3),
    _PwAtmCfgTimeoutMode_Type()
)
pwAtmCfgTimeoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAtmCfgTimeoutMode.setStatus("current")
_PwAtmClpQosMapping_Type = TruthValue
_PwAtmClpQosMapping_Object = MibTableColumn
pwAtmClpQosMapping = _PwAtmClpQosMapping_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 5, 1, 4),
    _PwAtmClpQosMapping_Type()
)
pwAtmClpQosMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAtmClpQosMapping.setStatus("current")
_PwAtmOutboundNto1Table_Object = MibTable
pwAtmOutboundNto1Table = _PwAtmOutboundNto1Table_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6)
)
if mibBuilder.loadTexts:
    pwAtmOutboundNto1Table.setStatus("current")
_PwAtmOutboundNto1Entry_Object = MibTableRow
pwAtmOutboundNto1Entry = _PwAtmOutboundNto1Entry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1)
)
pwAtmOutboundNto1Entry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ATM-MIB", "pwAtmOutboundNto1AtmIf"),
    (0, "PW-ATM-MIB", "pwAtmOutboundNto1Vpi"),
    (0, "PW-ATM-MIB", "pwAtmOutboundNto1Vci"),
)
if mibBuilder.loadTexts:
    pwAtmOutboundNto1Entry.setStatus("current")
_PwAtmOutboundNto1AtmIf_Type = InterfaceIndex
_PwAtmOutboundNto1AtmIf_Object = MibTableColumn
pwAtmOutboundNto1AtmIf = _PwAtmOutboundNto1AtmIf_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 1),
    _PwAtmOutboundNto1AtmIf_Type()
)
pwAtmOutboundNto1AtmIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1AtmIf.setStatus("current")
_PwAtmOutboundNto1Vpi_Type = AtmVpIdentifier
_PwAtmOutboundNto1Vpi_Object = MibTableColumn
pwAtmOutboundNto1Vpi = _PwAtmOutboundNto1Vpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 2),
    _PwAtmOutboundNto1Vpi_Type()
)
pwAtmOutboundNto1Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1Vpi.setStatus("current")
_PwAtmOutboundNto1Vci_Type = AtmVcIdentifier
_PwAtmOutboundNto1Vci_Object = MibTableColumn
pwAtmOutboundNto1Vci = _PwAtmOutboundNto1Vci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 3),
    _PwAtmOutboundNto1Vci_Type()
)
pwAtmOutboundNto1Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1Vci.setStatus("current")
_PwAtmOutboundNto1RowStatus_Type = RowStatus
_PwAtmOutboundNto1RowStatus_Object = MibTableColumn
pwAtmOutboundNto1RowStatus = _PwAtmOutboundNto1RowStatus_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 4),
    _PwAtmOutboundNto1RowStatus_Type()
)
pwAtmOutboundNto1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1RowStatus.setStatus("current")
_PwAtmOutboundNto1TrafficParamDescr_Type = RowPointer
_PwAtmOutboundNto1TrafficParamDescr_Object = MibTableColumn
pwAtmOutboundNto1TrafficParamDescr = _PwAtmOutboundNto1TrafficParamDescr_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 5),
    _PwAtmOutboundNto1TrafficParamDescr_Type()
)
pwAtmOutboundNto1TrafficParamDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1TrafficParamDescr.setStatus("current")
_PwAtmOutboundNto1MappedVpi_Type = AtmVpIdentifier
_PwAtmOutboundNto1MappedVpi_Object = MibTableColumn
pwAtmOutboundNto1MappedVpi = _PwAtmOutboundNto1MappedVpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 6),
    _PwAtmOutboundNto1MappedVpi_Type()
)
pwAtmOutboundNto1MappedVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1MappedVpi.setStatus("current")
_PwAtmOutboundNto1MappedVci_Type = AtmVcIdentifier
_PwAtmOutboundNto1MappedVci_Object = MibTableColumn
pwAtmOutboundNto1MappedVci = _PwAtmOutboundNto1MappedVci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 6, 1, 7),
    _PwAtmOutboundNto1MappedVci_Type()
)
pwAtmOutboundNto1MappedVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmOutboundNto1MappedVci.setStatus("current")
_PwAtmInboundNto1Table_Object = MibTable
pwAtmInboundNto1Table = _PwAtmInboundNto1Table_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7)
)
if mibBuilder.loadTexts:
    pwAtmInboundNto1Table.setStatus("current")
_PwAtmInboundNto1Entry_Object = MibTableRow
pwAtmInboundNto1Entry = _PwAtmInboundNto1Entry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1)
)
pwAtmInboundNto1Entry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ATM-MIB", "pwAtmInboundNto1AtmIf"),
    (0, "PW-ATM-MIB", "pwAtmInboundNto1Vpi"),
    (0, "PW-ATM-MIB", "pwAtmInboundNto1Vci"),
)
if mibBuilder.loadTexts:
    pwAtmInboundNto1Entry.setStatus("current")
_PwAtmInboundNto1AtmIf_Type = InterfaceIndex
_PwAtmInboundNto1AtmIf_Object = MibTableColumn
pwAtmInboundNto1AtmIf = _PwAtmInboundNto1AtmIf_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 1),
    _PwAtmInboundNto1AtmIf_Type()
)
pwAtmInboundNto1AtmIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmInboundNto1AtmIf.setStatus("current")
_PwAtmInboundNto1Vpi_Type = AtmVpIdentifier
_PwAtmInboundNto1Vpi_Object = MibTableColumn
pwAtmInboundNto1Vpi = _PwAtmInboundNto1Vpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 2),
    _PwAtmInboundNto1Vpi_Type()
)
pwAtmInboundNto1Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmInboundNto1Vpi.setStatus("current")
_PwAtmInboundNto1Vci_Type = AtmVcIdentifier
_PwAtmInboundNto1Vci_Object = MibTableColumn
pwAtmInboundNto1Vci = _PwAtmInboundNto1Vci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 3),
    _PwAtmInboundNto1Vci_Type()
)
pwAtmInboundNto1Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmInboundNto1Vci.setStatus("current")
_PwAtmInboundNto1RowStatus_Type = RowStatus
_PwAtmInboundNto1RowStatus_Object = MibTableColumn
pwAtmInboundNto1RowStatus = _PwAtmInboundNto1RowStatus_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 4),
    _PwAtmInboundNto1RowStatus_Type()
)
pwAtmInboundNto1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundNto1RowStatus.setStatus("current")
_PwAtmInboundNto1TrafficParamDescr_Type = RowPointer
_PwAtmInboundNto1TrafficParamDescr_Object = MibTableColumn
pwAtmInboundNto1TrafficParamDescr = _PwAtmInboundNto1TrafficParamDescr_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 5),
    _PwAtmInboundNto1TrafficParamDescr_Type()
)
pwAtmInboundNto1TrafficParamDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundNto1TrafficParamDescr.setStatus("current")
_PwAtmInboundNto1MappedVpi_Type = AtmVpIdentifier
_PwAtmInboundNto1MappedVpi_Object = MibTableColumn
pwAtmInboundNto1MappedVpi = _PwAtmInboundNto1MappedVpi_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 6),
    _PwAtmInboundNto1MappedVpi_Type()
)
pwAtmInboundNto1MappedVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundNto1MappedVpi.setStatus("current")
_PwAtmInboundNto1MappedVci_Type = AtmVcIdentifier
_PwAtmInboundNto1MappedVci_Object = MibTableColumn
pwAtmInboundNto1MappedVci = _PwAtmInboundNto1MappedVci_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 7, 1, 7),
    _PwAtmInboundNto1MappedVci_Type()
)
pwAtmInboundNto1MappedVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAtmInboundNto1MappedVci.setStatus("current")
_PwAtmPerfCurrentTable_Object = MibTable
pwAtmPerfCurrentTable = _PwAtmPerfCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8)
)
if mibBuilder.loadTexts:
    pwAtmPerfCurrentTable.setStatus("current")
_PwAtmPerfCurrentEntry_Object = MibTableRow
pwAtmPerfCurrentEntry = _PwAtmPerfCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1)
)
pwAtmPerfCurrentEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwAtmPerfCurrentEntry.setStatus("current")
_PwAtmPerfCurrentMissingPkts_Type = PerfCurrentCount
_PwAtmPerfCurrentMissingPkts_Object = MibTableColumn
pwAtmPerfCurrentMissingPkts = _PwAtmPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 1),
    _PwAtmPerfCurrentMissingPkts_Type()
)
pwAtmPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentMissingPkts.setStatus("current")
_PwAtmPerfCurrentPktsReOrder_Type = PerfCurrentCount
_PwAtmPerfCurrentPktsReOrder_Object = MibTableColumn
pwAtmPerfCurrentPktsReOrder = _PwAtmPerfCurrentPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 2),
    _PwAtmPerfCurrentPktsReOrder_Type()
)
pwAtmPerfCurrentPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentPktsReOrder.setStatus("current")
_PwAtmPerfCurrentPktsMisOrder_Type = PerfCurrentCount
_PwAtmPerfCurrentPktsMisOrder_Object = MibTableColumn
pwAtmPerfCurrentPktsMisOrder = _PwAtmPerfCurrentPktsMisOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 3),
    _PwAtmPerfCurrentPktsMisOrder_Type()
)
pwAtmPerfCurrentPktsMisOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentPktsMisOrder.setStatus("current")
_PwAtmPerfCurrentPktsTimeout_Type = PerfCurrentCount
_PwAtmPerfCurrentPktsTimeout_Object = MibTableColumn
pwAtmPerfCurrentPktsTimeout = _PwAtmPerfCurrentPktsTimeout_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 4),
    _PwAtmPerfCurrentPktsTimeout_Type()
)
pwAtmPerfCurrentPktsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentPktsTimeout.setStatus("current")
_PwAtmPerfCurrentCellsXmit_Type = PerfCurrentCount
_PwAtmPerfCurrentCellsXmit_Object = MibTableColumn
pwAtmPerfCurrentCellsXmit = _PwAtmPerfCurrentCellsXmit_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 5),
    _PwAtmPerfCurrentCellsXmit_Type()
)
pwAtmPerfCurrentCellsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentCellsXmit.setStatus("current")
_PwAtmPerfCurrentCellsDropped_Type = PerfCurrentCount
_PwAtmPerfCurrentCellsDropped_Object = MibTableColumn
pwAtmPerfCurrentCellsDropped = _PwAtmPerfCurrentCellsDropped_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 6),
    _PwAtmPerfCurrentCellsDropped_Type()
)
pwAtmPerfCurrentCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentCellsDropped.setStatus("current")
_PwAtmPerfCurrentCellsReceived_Type = PerfCurrentCount
_PwAtmPerfCurrentCellsReceived_Object = MibTableColumn
pwAtmPerfCurrentCellsReceived = _PwAtmPerfCurrentCellsReceived_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 7),
    _PwAtmPerfCurrentCellsReceived_Type()
)
pwAtmPerfCurrentCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentCellsReceived.setStatus("current")
_PwAtmPerfCurrentUnknownCells_Type = PerfCurrentCount
_PwAtmPerfCurrentUnknownCells_Object = MibTableColumn
pwAtmPerfCurrentUnknownCells = _PwAtmPerfCurrentUnknownCells_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 8, 1, 8),
    _PwAtmPerfCurrentUnknownCells_Type()
)
pwAtmPerfCurrentUnknownCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfCurrentUnknownCells.setStatus("current")
_PwAtmPerfIntervalTable_Object = MibTable
pwAtmPerfIntervalTable = _PwAtmPerfIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9)
)
if mibBuilder.loadTexts:
    pwAtmPerfIntervalTable.setStatus("current")
_PwAtmPerfIntervalEntry_Object = MibTableRow
pwAtmPerfIntervalEntry = _PwAtmPerfIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1)
)
pwAtmPerfIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ATM-MIB", "pwAtmPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwAtmPerfIntervalEntry.setStatus("current")


class _PwAtmPerfIntervalNumber_Type(Unsigned32):
    """Custom type pwAtmPerfIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PwAtmPerfIntervalNumber_Type.__name__ = "Unsigned32"
_PwAtmPerfIntervalNumber_Object = MibTableColumn
pwAtmPerfIntervalNumber = _PwAtmPerfIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 1),
    _PwAtmPerfIntervalNumber_Type()
)
pwAtmPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalNumber.setStatus("current")
_PwAtmPerfIntervalValidData_Type = TruthValue
_PwAtmPerfIntervalValidData_Object = MibTableColumn
pwAtmPerfIntervalValidData = _PwAtmPerfIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 2),
    _PwAtmPerfIntervalValidData_Type()
)
pwAtmPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalValidData.setStatus("current")
_PwAtmPerfIntervalDuration_Type = Unsigned32
_PwAtmPerfIntervalDuration_Object = MibTableColumn
pwAtmPerfIntervalDuration = _PwAtmPerfIntervalDuration_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 3),
    _PwAtmPerfIntervalDuration_Type()
)
pwAtmPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalDuration.setStatus("current")
_PwAtmPerfIntervalMissingPkts_Type = PerfIntervalCount
_PwAtmPerfIntervalMissingPkts_Object = MibTableColumn
pwAtmPerfIntervalMissingPkts = _PwAtmPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 4),
    _PwAtmPerfIntervalMissingPkts_Type()
)
pwAtmPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalMissingPkts.setStatus("current")
_PwAtmPerfIntervalPktsReOrder_Type = PerfIntervalCount
_PwAtmPerfIntervalPktsReOrder_Object = MibTableColumn
pwAtmPerfIntervalPktsReOrder = _PwAtmPerfIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 5),
    _PwAtmPerfIntervalPktsReOrder_Type()
)
pwAtmPerfIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalPktsReOrder.setStatus("current")
_PwAtmPerfIntervalPktsMisOrder_Type = PerfIntervalCount
_PwAtmPerfIntervalPktsMisOrder_Object = MibTableColumn
pwAtmPerfIntervalPktsMisOrder = _PwAtmPerfIntervalPktsMisOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 6),
    _PwAtmPerfIntervalPktsMisOrder_Type()
)
pwAtmPerfIntervalPktsMisOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalPktsMisOrder.setStatus("current")
_PwAtmPerfIntervalPktsTimeout_Type = PerfIntervalCount
_PwAtmPerfIntervalPktsTimeout_Object = MibTableColumn
pwAtmPerfIntervalPktsTimeout = _PwAtmPerfIntervalPktsTimeout_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 7),
    _PwAtmPerfIntervalPktsTimeout_Type()
)
pwAtmPerfIntervalPktsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalPktsTimeout.setStatus("current")
_PwAtmPerfIntervalCellsXmit_Type = PerfIntervalCount
_PwAtmPerfIntervalCellsXmit_Object = MibTableColumn
pwAtmPerfIntervalCellsXmit = _PwAtmPerfIntervalCellsXmit_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 8),
    _PwAtmPerfIntervalCellsXmit_Type()
)
pwAtmPerfIntervalCellsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalCellsXmit.setStatus("current")
_PwAtmPerfIntervalCellsDropped_Type = PerfIntervalCount
_PwAtmPerfIntervalCellsDropped_Object = MibTableColumn
pwAtmPerfIntervalCellsDropped = _PwAtmPerfIntervalCellsDropped_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 9),
    _PwAtmPerfIntervalCellsDropped_Type()
)
pwAtmPerfIntervalCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalCellsDropped.setStatus("current")
_PwAtmPerfIntervalCellsReceived_Type = PerfIntervalCount
_PwAtmPerfIntervalCellsReceived_Object = MibTableColumn
pwAtmPerfIntervalCellsReceived = _PwAtmPerfIntervalCellsReceived_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 10),
    _PwAtmPerfIntervalCellsReceived_Type()
)
pwAtmPerfIntervalCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalCellsReceived.setStatus("current")
_PwAtmPerfIntervalUnknownCells_Type = PerfIntervalCount
_PwAtmPerfIntervalUnknownCells_Object = MibTableColumn
pwAtmPerfIntervalUnknownCells = _PwAtmPerfIntervalUnknownCells_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 9, 1, 11),
    _PwAtmPerfIntervalUnknownCells_Type()
)
pwAtmPerfIntervalUnknownCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerfIntervalUnknownCells.setStatus("current")
_PwAtmPerf1DayIntervalTable_Object = MibTable
pwAtmPerf1DayIntervalTable = _PwAtmPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10)
)
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalTable.setStatus("current")
_PwAtmPerf1DayIntervalEntry_Object = MibTableRow
pwAtmPerf1DayIntervalEntry = _PwAtmPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1)
)
pwAtmPerf1DayIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-ATM-MIB", "pwAtmPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalEntry.setStatus("current")


class _PwAtmPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type pwAtmPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 365),
    )


_PwAtmPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PwAtmPerf1DayIntervalNumber_Object = MibTableColumn
pwAtmPerf1DayIntervalNumber = _PwAtmPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 1),
    _PwAtmPerf1DayIntervalNumber_Type()
)
pwAtmPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalNumber.setStatus("current")
_PwAtmPerf1DayIntervalValidData_Type = TruthValue
_PwAtmPerf1DayIntervalValidData_Object = MibTableColumn
pwAtmPerf1DayIntervalValidData = _PwAtmPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 2),
    _PwAtmPerf1DayIntervalValidData_Type()
)
pwAtmPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalValidData.setStatus("current")
_PwAtmPerf1DayIntervalDuration_Type = Unsigned32
_PwAtmPerf1DayIntervalDuration_Object = MibTableColumn
pwAtmPerf1DayIntervalDuration = _PwAtmPerf1DayIntervalDuration_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 3),
    _PwAtmPerf1DayIntervalDuration_Type()
)
pwAtmPerf1DayIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalDuration.setStatus("current")
_PwAtmPerf1DayIntervalMissingPkts_Type = Counter32
_PwAtmPerf1DayIntervalMissingPkts_Object = MibTableColumn
pwAtmPerf1DayIntervalMissingPkts = _PwAtmPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 4),
    _PwAtmPerf1DayIntervalMissingPkts_Type()
)
pwAtmPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalMissingPkts.setStatus("current")
_PwAtmPerf1DayIntervalPktsReOrder_Type = Counter32
_PwAtmPerf1DayIntervalPktsReOrder_Object = MibTableColumn
pwAtmPerf1DayIntervalPktsReOrder = _PwAtmPerf1DayIntervalPktsReOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 5),
    _PwAtmPerf1DayIntervalPktsReOrder_Type()
)
pwAtmPerf1DayIntervalPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalPktsReOrder.setStatus("current")
_PwAtmPerf1DayIntervalPktsMisOrder_Type = Counter32
_PwAtmPerf1DayIntervalPktsMisOrder_Object = MibTableColumn
pwAtmPerf1DayIntervalPktsMisOrder = _PwAtmPerf1DayIntervalPktsMisOrder_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 6),
    _PwAtmPerf1DayIntervalPktsMisOrder_Type()
)
pwAtmPerf1DayIntervalPktsMisOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalPktsMisOrder.setStatus("current")
_PwAtmPerf1DayIntervalPktsTimeout_Type = Counter32
_PwAtmPerf1DayIntervalPktsTimeout_Object = MibTableColumn
pwAtmPerf1DayIntervalPktsTimeout = _PwAtmPerf1DayIntervalPktsTimeout_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 7),
    _PwAtmPerf1DayIntervalPktsTimeout_Type()
)
pwAtmPerf1DayIntervalPktsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalPktsTimeout.setStatus("current")
_PwAtmPerf1DayIntervalCellsXmit_Type = Counter32
_PwAtmPerf1DayIntervalCellsXmit_Object = MibTableColumn
pwAtmPerf1DayIntervalCellsXmit = _PwAtmPerf1DayIntervalCellsXmit_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 8),
    _PwAtmPerf1DayIntervalCellsXmit_Type()
)
pwAtmPerf1DayIntervalCellsXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalCellsXmit.setStatus("current")
_PwAtmPerf1DayIntervalCellsDropped_Type = Counter32
_PwAtmPerf1DayIntervalCellsDropped_Object = MibTableColumn
pwAtmPerf1DayIntervalCellsDropped = _PwAtmPerf1DayIntervalCellsDropped_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 9),
    _PwAtmPerf1DayIntervalCellsDropped_Type()
)
pwAtmPerf1DayIntervalCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalCellsDropped.setStatus("current")
_PwAtmPerf1DayIntervalCellsReceived_Type = Counter32
_PwAtmPerf1DayIntervalCellsReceived_Object = MibTableColumn
pwAtmPerf1DayIntervalCellsReceived = _PwAtmPerf1DayIntervalCellsReceived_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 10),
    _PwAtmPerf1DayIntervalCellsReceived_Type()
)
pwAtmPerf1DayIntervalCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalCellsReceived.setStatus("current")
_PwAtmPerf1DayIntervalUnknownCells_Type = Counter32
_PwAtmPerf1DayIntervalUnknownCells_Object = MibTableColumn
pwAtmPerf1DayIntervalUnknownCells = _PwAtmPerf1DayIntervalUnknownCells_Object(
    (1, 3, 6, 1, 2, 1, 183, 1, 10, 1, 11),
    _PwAtmPerf1DayIntervalUnknownCells_Type()
)
pwAtmPerf1DayIntervalUnknownCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAtmPerf1DayIntervalUnknownCells.setStatus("current")
_PwAtmConformance_ObjectIdentity = ObjectIdentity
pwAtmConformance = _PwAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 183, 2)
)
_PwAtmCompliances_ObjectIdentity = ObjectIdentity
pwAtmCompliances = _PwAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 183, 2, 1)
)
_PwAtmGroups_ObjectIdentity = ObjectIdentity
pwAtmGroups = _PwAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 183, 2, 2)
)

# Managed Objects groups

pwAtmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 5)
)
pwAtmCfgGroup.setObjects(
      *(("PW-ATM-MIB", "pwAtmCfgMaxCellConcatenation"),
        ("PW-ATM-MIB", "pwAtmCfgFarEndMaxCellConcatenation"),
        ("PW-ATM-MIB", "pwAtmCfgTimeoutMode"),
        ("PW-ATM-MIB", "pwAtmClpQosMapping"))
)
if mibBuilder.loadTexts:
    pwAtmCfgGroup.setStatus("current")

pwAtmPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 6)
)
pwAtmPerfGroup.setObjects(
      *(("PW-ATM-MIB", "pwAtmPerfCurrentMissingPkts"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentPktsReOrder"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentPktsMisOrder"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentPktsTimeout"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentCellsXmit"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentCellsDropped"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentCellsReceived"),
        ("PW-ATM-MIB", "pwAtmPerfCurrentUnknownCells"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalValidData"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalDuration"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalMissingPkts"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalPktsReOrder"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalPktsMisOrder"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalPktsTimeout"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalCellsXmit"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalCellsDropped"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalCellsReceived"),
        ("PW-ATM-MIB", "pwAtmPerfIntervalUnknownCells"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalValidData"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalDuration"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalMissingPkts"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsReOrder"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsMisOrder"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalPktsTimeout"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsXmit"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsDropped"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalCellsReceived"),
        ("PW-ATM-MIB", "pwAtmPerf1DayIntervalUnknownCells"))
)
if mibBuilder.loadTexts:
    pwAtmPerfGroup.setStatus("current")

pwAtmOutbound1to1Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 7)
)
pwAtmOutbound1to1Group.setObjects(
      *(("PW-ATM-MIB", "pwAtmOutboundAtmIf"),
        ("PW-ATM-MIB", "pwAtmOutboundVpi"),
        ("PW-ATM-MIB", "pwAtmOutboundVci"),
        ("PW-ATM-MIB", "pwAtmOutboundTrafficParamDescr"),
        ("PW-ATM-MIB", "pwAtmOutboundRowStatus"))
)
if mibBuilder.loadTexts:
    pwAtmOutbound1to1Group.setStatus("current")

pwAtmInbound1to1Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 8)
)
pwAtmInbound1to1Group.setObjects(
      *(("PW-ATM-MIB", "pwAtmInboundAtmIf"),
        ("PW-ATM-MIB", "pwAtmInboundVpi"),
        ("PW-ATM-MIB", "pwAtmInboundVci"),
        ("PW-ATM-MIB", "pwAtmInboundTrafficParamDescr"),
        ("PW-ATM-MIB", "pwAtmInboundRowStatus"))
)
if mibBuilder.loadTexts:
    pwAtmInbound1to1Group.setStatus("current")

pwAtmOutboundNto1Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 9)
)
pwAtmOutboundNto1Group.setObjects(
      *(("PW-ATM-MIB", "pwAtmOutboundNto1RowStatus"),
        ("PW-ATM-MIB", "pwAtmOutboundNto1TrafficParamDescr"),
        ("PW-ATM-MIB", "pwAtmOutboundNto1MappedVpi"),
        ("PW-ATM-MIB", "pwAtmOutboundNto1MappedVci"))
)
if mibBuilder.loadTexts:
    pwAtmOutboundNto1Group.setStatus("current")

pwAtmInboundNto1Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 183, 2, 2, 10)
)
pwAtmInboundNto1Group.setObjects(
      *(("PW-ATM-MIB", "pwAtmInboundNto1RowStatus"),
        ("PW-ATM-MIB", "pwAtmInboundNto1TrafficParamDescr"),
        ("PW-ATM-MIB", "pwAtmInboundNto1MappedVpi"),
        ("PW-ATM-MIB", "pwAtmInboundNto1MappedVci"))
)
if mibBuilder.loadTexts:
    pwAtmInboundNto1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pwAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 183, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pwAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-ATM-MIB",
    **{"pwAtmMIB": pwAtmMIB,
       "pwAtmNotifications": pwAtmNotifications,
       "pwAtmObjects": pwAtmObjects,
       "pwAtmOutboundTable": pwAtmOutboundTable,
       "pwAtmOutboundEntry": pwAtmOutboundEntry,
       "pwAtmOutboundAtmIf": pwAtmOutboundAtmIf,
       "pwAtmOutboundVpi": pwAtmOutboundVpi,
       "pwAtmOutboundVci": pwAtmOutboundVci,
       "pwAtmOutboundTrafficParamDescr": pwAtmOutboundTrafficParamDescr,
       "pwAtmOutboundRowStatus": pwAtmOutboundRowStatus,
       "pwAtmInboundTable": pwAtmInboundTable,
       "pwAtmInboundEntry": pwAtmInboundEntry,
       "pwAtmInboundAtmIf": pwAtmInboundAtmIf,
       "pwAtmInboundVpi": pwAtmInboundVpi,
       "pwAtmInboundVci": pwAtmInboundVci,
       "pwAtmInboundTrafficParamDescr": pwAtmInboundTrafficParamDescr,
       "pwAtmInboundRowStatus": pwAtmInboundRowStatus,
       "pwAtmCfgTable": pwAtmCfgTable,
       "pwAtmCfgEntry": pwAtmCfgEntry,
       "pwAtmCfgMaxCellConcatenation": pwAtmCfgMaxCellConcatenation,
       "pwAtmCfgFarEndMaxCellConcatenation": pwAtmCfgFarEndMaxCellConcatenation,
       "pwAtmCfgTimeoutMode": pwAtmCfgTimeoutMode,
       "pwAtmClpQosMapping": pwAtmClpQosMapping,
       "pwAtmOutboundNto1Table": pwAtmOutboundNto1Table,
       "pwAtmOutboundNto1Entry": pwAtmOutboundNto1Entry,
       "pwAtmOutboundNto1AtmIf": pwAtmOutboundNto1AtmIf,
       "pwAtmOutboundNto1Vpi": pwAtmOutboundNto1Vpi,
       "pwAtmOutboundNto1Vci": pwAtmOutboundNto1Vci,
       "pwAtmOutboundNto1RowStatus": pwAtmOutboundNto1RowStatus,
       "pwAtmOutboundNto1TrafficParamDescr": pwAtmOutboundNto1TrafficParamDescr,
       "pwAtmOutboundNto1MappedVpi": pwAtmOutboundNto1MappedVpi,
       "pwAtmOutboundNto1MappedVci": pwAtmOutboundNto1MappedVci,
       "pwAtmInboundNto1Table": pwAtmInboundNto1Table,
       "pwAtmInboundNto1Entry": pwAtmInboundNto1Entry,
       "pwAtmInboundNto1AtmIf": pwAtmInboundNto1AtmIf,
       "pwAtmInboundNto1Vpi": pwAtmInboundNto1Vpi,
       "pwAtmInboundNto1Vci": pwAtmInboundNto1Vci,
       "pwAtmInboundNto1RowStatus": pwAtmInboundNto1RowStatus,
       "pwAtmInboundNto1TrafficParamDescr": pwAtmInboundNto1TrafficParamDescr,
       "pwAtmInboundNto1MappedVpi": pwAtmInboundNto1MappedVpi,
       "pwAtmInboundNto1MappedVci": pwAtmInboundNto1MappedVci,
       "pwAtmPerfCurrentTable": pwAtmPerfCurrentTable,
       "pwAtmPerfCurrentEntry": pwAtmPerfCurrentEntry,
       "pwAtmPerfCurrentMissingPkts": pwAtmPerfCurrentMissingPkts,
       "pwAtmPerfCurrentPktsReOrder": pwAtmPerfCurrentPktsReOrder,
       "pwAtmPerfCurrentPktsMisOrder": pwAtmPerfCurrentPktsMisOrder,
       "pwAtmPerfCurrentPktsTimeout": pwAtmPerfCurrentPktsTimeout,
       "pwAtmPerfCurrentCellsXmit": pwAtmPerfCurrentCellsXmit,
       "pwAtmPerfCurrentCellsDropped": pwAtmPerfCurrentCellsDropped,
       "pwAtmPerfCurrentCellsReceived": pwAtmPerfCurrentCellsReceived,
       "pwAtmPerfCurrentUnknownCells": pwAtmPerfCurrentUnknownCells,
       "pwAtmPerfIntervalTable": pwAtmPerfIntervalTable,
       "pwAtmPerfIntervalEntry": pwAtmPerfIntervalEntry,
       "pwAtmPerfIntervalNumber": pwAtmPerfIntervalNumber,
       "pwAtmPerfIntervalValidData": pwAtmPerfIntervalValidData,
       "pwAtmPerfIntervalDuration": pwAtmPerfIntervalDuration,
       "pwAtmPerfIntervalMissingPkts": pwAtmPerfIntervalMissingPkts,
       "pwAtmPerfIntervalPktsReOrder": pwAtmPerfIntervalPktsReOrder,
       "pwAtmPerfIntervalPktsMisOrder": pwAtmPerfIntervalPktsMisOrder,
       "pwAtmPerfIntervalPktsTimeout": pwAtmPerfIntervalPktsTimeout,
       "pwAtmPerfIntervalCellsXmit": pwAtmPerfIntervalCellsXmit,
       "pwAtmPerfIntervalCellsDropped": pwAtmPerfIntervalCellsDropped,
       "pwAtmPerfIntervalCellsReceived": pwAtmPerfIntervalCellsReceived,
       "pwAtmPerfIntervalUnknownCells": pwAtmPerfIntervalUnknownCells,
       "pwAtmPerf1DayIntervalTable": pwAtmPerf1DayIntervalTable,
       "pwAtmPerf1DayIntervalEntry": pwAtmPerf1DayIntervalEntry,
       "pwAtmPerf1DayIntervalNumber": pwAtmPerf1DayIntervalNumber,
       "pwAtmPerf1DayIntervalValidData": pwAtmPerf1DayIntervalValidData,
       "pwAtmPerf1DayIntervalDuration": pwAtmPerf1DayIntervalDuration,
       "pwAtmPerf1DayIntervalMissingPkts": pwAtmPerf1DayIntervalMissingPkts,
       "pwAtmPerf1DayIntervalPktsReOrder": pwAtmPerf1DayIntervalPktsReOrder,
       "pwAtmPerf1DayIntervalPktsMisOrder": pwAtmPerf1DayIntervalPktsMisOrder,
       "pwAtmPerf1DayIntervalPktsTimeout": pwAtmPerf1DayIntervalPktsTimeout,
       "pwAtmPerf1DayIntervalCellsXmit": pwAtmPerf1DayIntervalCellsXmit,
       "pwAtmPerf1DayIntervalCellsDropped": pwAtmPerf1DayIntervalCellsDropped,
       "pwAtmPerf1DayIntervalCellsReceived": pwAtmPerf1DayIntervalCellsReceived,
       "pwAtmPerf1DayIntervalUnknownCells": pwAtmPerf1DayIntervalUnknownCells,
       "pwAtmConformance": pwAtmConformance,
       "pwAtmCompliances": pwAtmCompliances,
       "pwAtmCompliance": pwAtmCompliance,
       "pwAtmGroups": pwAtmGroups,
       "pwAtmCfgGroup": pwAtmCfgGroup,
       "pwAtmPerfGroup": pwAtmPerfGroup,
       "pwAtmOutbound1to1Group": pwAtmOutbound1to1Group,
       "pwAtmInbound1to1Group": pwAtmInbound1to1Group,
       "pwAtmOutboundNto1Group": pwAtmOutboundNto1Group,
       "pwAtmInboundNto1Group": pwAtmInboundNto1Group}
)
