# SNMP MIB module (FR-ATM-PVC-SERVICE-IWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FR-ATM-PVC-SERVICE-IWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:15 2024
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

(atmVclEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclEntry")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

frAtmIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 86)
)
frAtmIwfMIB.setRevisions(
        ("2000-09-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrAtmIwfMIBObjects_ObjectIdentity = ObjectIdentity
frAtmIwfMIBObjects = _FrAtmIwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 1)
)


class _FrAtmIwfConnIndexNext_Type(Integer32):
    """Custom type frAtmIwfConnIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrAtmIwfConnIndexNext_Type.__name__ = "Integer32"
_FrAtmIwfConnIndexNext_Object = MibScalar
frAtmIwfConnIndexNext = _FrAtmIwfConnIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 1),
    _FrAtmIwfConnIndexNext_Type()
)
frAtmIwfConnIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnIndexNext.setStatus("current")
_FrAtmIwfConnectionTable_Object = MibTable
frAtmIwfConnectionTable = _FrAtmIwfConnectionTable_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2)
)
if mibBuilder.loadTexts:
    frAtmIwfConnectionTable.setStatus("current")
_FrAtmIwfConnectionEntry_Object = MibTableRow
frAtmIwfConnectionEntry = _FrAtmIwfConnectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1)
)
frAtmIwfConnectionEntry.setIndexNames(
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndex"),
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtmPort"),
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVpi"),
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVci"),
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFrPort"),
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDlci"),
)
if mibBuilder.loadTexts:
    frAtmIwfConnectionEntry.setStatus("current")


class _FrAtmIwfConnIndex_Type(Integer32):
    """Custom type frAtmIwfConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrAtmIwfConnIndex_Type.__name__ = "Integer32"
_FrAtmIwfConnIndex_Object = MibTableColumn
frAtmIwfConnIndex = _FrAtmIwfConnIndex_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 1),
    _FrAtmIwfConnIndex_Type()
)
frAtmIwfConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnIndex.setStatus("current")
_FrAtmIwfConnAtmPort_Type = InterfaceIndex
_FrAtmIwfConnAtmPort_Object = MibTableColumn
frAtmIwfConnAtmPort = _FrAtmIwfConnAtmPort_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 2),
    _FrAtmIwfConnAtmPort_Type()
)
frAtmIwfConnAtmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnAtmPort.setStatus("current")
_FrAtmIwfConnVpi_Type = AtmVpIdentifier
_FrAtmIwfConnVpi_Object = MibTableColumn
frAtmIwfConnVpi = _FrAtmIwfConnVpi_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 3),
    _FrAtmIwfConnVpi_Type()
)
frAtmIwfConnVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnVpi.setStatus("current")
_FrAtmIwfConnVci_Type = AtmVcIdentifier
_FrAtmIwfConnVci_Object = MibTableColumn
frAtmIwfConnVci = _FrAtmIwfConnVci_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 4),
    _FrAtmIwfConnVci_Type()
)
frAtmIwfConnVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnVci.setStatus("current")
_FrAtmIwfConnFrPort_Type = InterfaceIndex
_FrAtmIwfConnFrPort_Object = MibTableColumn
frAtmIwfConnFrPort = _FrAtmIwfConnFrPort_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 5),
    _FrAtmIwfConnFrPort_Type()
)
frAtmIwfConnFrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnFrPort.setStatus("current")


class _FrAtmIwfConnDlci_Type(Integer32):
    """Custom type frAtmIwfConnDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4194303),
    )


_FrAtmIwfConnDlci_Type.__name__ = "Integer32"
_FrAtmIwfConnDlci_Object = MibTableColumn
frAtmIwfConnDlci = _FrAtmIwfConnDlci_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 6),
    _FrAtmIwfConnDlci_Type()
)
frAtmIwfConnDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnDlci.setStatus("current")
_FrAtmIwfConnRowStatus_Type = RowStatus
_FrAtmIwfConnRowStatus_Object = MibTableColumn
frAtmIwfConnRowStatus = _FrAtmIwfConnRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 7),
    _FrAtmIwfConnRowStatus_Type()
)
frAtmIwfConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnRowStatus.setStatus("current")


class _FrAtmIwfConnAdminStatus_Type(Integer32):
    """Custom type frAtmIwfConnAdminStatus based on Integer32"""
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


_FrAtmIwfConnAdminStatus_Type.__name__ = "Integer32"
_FrAtmIwfConnAdminStatus_Object = MibTableColumn
frAtmIwfConnAdminStatus = _FrAtmIwfConnAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 8),
    _FrAtmIwfConnAdminStatus_Type()
)
frAtmIwfConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnAdminStatus.setStatus("current")


class _FrAtmIwfConnAtm2FrOperStatus_Type(Integer32):
    """Custom type frAtmIwfConnAtm2FrOperStatus based on Integer32"""
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


_FrAtmIwfConnAtm2FrOperStatus_Type.__name__ = "Integer32"
_FrAtmIwfConnAtm2FrOperStatus_Object = MibTableColumn
frAtmIwfConnAtm2FrOperStatus = _FrAtmIwfConnAtm2FrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 9),
    _FrAtmIwfConnAtm2FrOperStatus_Type()
)
frAtmIwfConnAtm2FrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnAtm2FrOperStatus.setStatus("current")
_FrAtmIwfConnAtm2FrLastChange_Type = TimeStamp
_FrAtmIwfConnAtm2FrLastChange_Object = MibTableColumn
frAtmIwfConnAtm2FrLastChange = _FrAtmIwfConnAtm2FrLastChange_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 10),
    _FrAtmIwfConnAtm2FrLastChange_Type()
)
frAtmIwfConnAtm2FrLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnAtm2FrLastChange.setStatus("current")


class _FrAtmIwfConnFr2AtmOperStatus_Type(Integer32):
    """Custom type frAtmIwfConnFr2AtmOperStatus based on Integer32"""
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


_FrAtmIwfConnFr2AtmOperStatus_Type.__name__ = "Integer32"
_FrAtmIwfConnFr2AtmOperStatus_Object = MibTableColumn
frAtmIwfConnFr2AtmOperStatus = _FrAtmIwfConnFr2AtmOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 11),
    _FrAtmIwfConnFr2AtmOperStatus_Type()
)
frAtmIwfConnFr2AtmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnFr2AtmOperStatus.setStatus("current")
_FrAtmIwfConnFr2AtmLastChange_Type = TimeStamp
_FrAtmIwfConnFr2AtmLastChange_Object = MibTableColumn
frAtmIwfConnFr2AtmLastChange = _FrAtmIwfConnFr2AtmLastChange_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 12),
    _FrAtmIwfConnFr2AtmLastChange_Type()
)
frAtmIwfConnFr2AtmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnFr2AtmLastChange.setStatus("current")
_FrAtmIwfConnectionDescriptor_Type = Integer32
_FrAtmIwfConnectionDescriptor_Object = MibTableColumn
frAtmIwfConnectionDescriptor = _FrAtmIwfConnectionDescriptor_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 13),
    _FrAtmIwfConnectionDescriptor_Type()
)
frAtmIwfConnectionDescriptor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptor.setStatus("current")
_FrAtmIwfConnFailedFrameTranslate_Type = Counter32
_FrAtmIwfConnFailedFrameTranslate_Object = MibTableColumn
frAtmIwfConnFailedFrameTranslate = _FrAtmIwfConnFailedFrameTranslate_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 14),
    _FrAtmIwfConnFailedFrameTranslate_Type()
)
frAtmIwfConnFailedFrameTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnFailedFrameTranslate.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnFailedFrameTranslate.setUnits("Frames")
_FrAtmIwfConnOverSizedFrames_Type = Counter32
_FrAtmIwfConnOverSizedFrames_Object = MibTableColumn
frAtmIwfConnOverSizedFrames = _FrAtmIwfConnOverSizedFrames_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 15),
    _FrAtmIwfConnOverSizedFrames_Type()
)
frAtmIwfConnOverSizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnOverSizedFrames.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnOverSizedFrames.setUnits("Frames")
_FrAtmIwfConnFailedAal5PduTranslate_Type = Counter32
_FrAtmIwfConnFailedAal5PduTranslate_Object = MibTableColumn
frAtmIwfConnFailedAal5PduTranslate = _FrAtmIwfConnFailedAal5PduTranslate_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 16),
    _FrAtmIwfConnFailedAal5PduTranslate_Type()
)
frAtmIwfConnFailedAal5PduTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnFailedAal5PduTranslate.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnFailedAal5PduTranslate.setUnits("PDUs")
_FrAtmIwfConnOverSizedSDUs_Type = Counter32
_FrAtmIwfConnOverSizedSDUs_Object = MibTableColumn
frAtmIwfConnOverSizedSDUs = _FrAtmIwfConnOverSizedSDUs_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 17),
    _FrAtmIwfConnOverSizedSDUs_Type()
)
frAtmIwfConnOverSizedSDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnOverSizedSDUs.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnOverSizedSDUs.setUnits("SDUs")
_FrAtmIwfConnCrcErrors_Type = Counter32
_FrAtmIwfConnCrcErrors_Object = MibTableColumn
frAtmIwfConnCrcErrors = _FrAtmIwfConnCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 18),
    _FrAtmIwfConnCrcErrors_Type()
)
frAtmIwfConnCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnCrcErrors.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnCrcErrors.setUnits("PDUs")
_FrAtmIwfConnSarTimeOuts_Type = Counter32
_FrAtmIwfConnSarTimeOuts_Object = MibTableColumn
frAtmIwfConnSarTimeOuts = _FrAtmIwfConnSarTimeOuts_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 19),
    _FrAtmIwfConnSarTimeOuts_Type()
)
frAtmIwfConnSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnSarTimeOuts.setStatus("current")
if mibBuilder.loadTexts:
    frAtmIwfConnSarTimeOuts.setUnits("PDUs")


class _FrAtmIwfConnectionDescriptorIndexNext_Type(Integer32):
    """Custom type frAtmIwfConnectionDescriptorIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrAtmIwfConnectionDescriptorIndexNext_Type.__name__ = "Integer32"
_FrAtmIwfConnectionDescriptorIndexNext_Object = MibScalar
frAtmIwfConnectionDescriptorIndexNext = _FrAtmIwfConnectionDescriptorIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 3),
    _FrAtmIwfConnectionDescriptorIndexNext_Type()
)
frAtmIwfConnectionDescriptorIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptorIndexNext.setStatus("current")
_FrAtmIwfConnectionDescriptorTable_Object = MibTable
frAtmIwfConnectionDescriptorTable = _FrAtmIwfConnectionDescriptorTable_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4)
)
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptorTable.setStatus("current")
_FrAtmIwfConnectionDescriptorEntry_Object = MibTableRow
frAtmIwfConnectionDescriptorEntry = _FrAtmIwfConnectionDescriptorEntry_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1)
)
frAtmIwfConnectionDescriptorEntry.setIndexNames(
    (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndex"),
)
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptorEntry.setStatus("current")


class _FrAtmIwfConnectionDescriptorIndex_Type(Integer32):
    """Custom type frAtmIwfConnectionDescriptorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrAtmIwfConnectionDescriptorIndex_Type.__name__ = "Integer32"
_FrAtmIwfConnectionDescriptorIndex_Object = MibTableColumn
frAtmIwfConnectionDescriptorIndex = _FrAtmIwfConnectionDescriptorIndex_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 1),
    _FrAtmIwfConnectionDescriptorIndex_Type()
)
frAtmIwfConnectionDescriptorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptorIndex.setStatus("current")
_FrAtmIwfConnDescriptorRowStatus_Type = RowStatus
_FrAtmIwfConnDescriptorRowStatus_Object = MibTableColumn
frAtmIwfConnDescriptorRowStatus = _FrAtmIwfConnDescriptorRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 2),
    _FrAtmIwfConnDescriptorRowStatus_Type()
)
frAtmIwfConnDescriptorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnDescriptorRowStatus.setStatus("current")


class _FrAtmIwfConnDeToClpMappingMode_Type(Integer32):
    """Custom type frAtmIwfConnDeToClpMappingMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2Const0", 2),
          ("mode2Const1", 3))
    )


_FrAtmIwfConnDeToClpMappingMode_Type.__name__ = "Integer32"
_FrAtmIwfConnDeToClpMappingMode_Object = MibTableColumn
frAtmIwfConnDeToClpMappingMode = _FrAtmIwfConnDeToClpMappingMode_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 3),
    _FrAtmIwfConnDeToClpMappingMode_Type()
)
frAtmIwfConnDeToClpMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnDeToClpMappingMode.setStatus("current")


class _FrAtmIwfConnClpToDeMappingMode_Type(Integer32):
    """Custom type frAtmIwfConnClpToDeMappingMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2Const0", 2),
          ("mode2Const1", 3))
    )


_FrAtmIwfConnClpToDeMappingMode_Type.__name__ = "Integer32"
_FrAtmIwfConnClpToDeMappingMode_Object = MibTableColumn
frAtmIwfConnClpToDeMappingMode = _FrAtmIwfConnClpToDeMappingMode_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 4),
    _FrAtmIwfConnClpToDeMappingMode_Type()
)
frAtmIwfConnClpToDeMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnClpToDeMappingMode.setStatus("current")


class _FrAtmIwfConnCongestionMappingMode_Type(Integer32):
    """Custom type frAtmIwfConnCongestionMappingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_FrAtmIwfConnCongestionMappingMode_Type.__name__ = "Integer32"
_FrAtmIwfConnCongestionMappingMode_Object = MibTableColumn
frAtmIwfConnCongestionMappingMode = _FrAtmIwfConnCongestionMappingMode_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 5),
    _FrAtmIwfConnCongestionMappingMode_Type()
)
frAtmIwfConnCongestionMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnCongestionMappingMode.setStatus("current")


class _FrAtmIwfConnEncapsulationMappingMode_Type(Integer32):
    """Custom type frAtmIwfConnEncapsulationMappingMode based on Integer32"""
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
        *(("translationMode", 2),
          ("translationModeAll", 3),
          ("transparentMode", 1))
    )


_FrAtmIwfConnEncapsulationMappingMode_Type.__name__ = "Integer32"
_FrAtmIwfConnEncapsulationMappingMode_Object = MibTableColumn
frAtmIwfConnEncapsulationMappingMode = _FrAtmIwfConnEncapsulationMappingMode_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 6),
    _FrAtmIwfConnEncapsulationMappingMode_Type()
)
frAtmIwfConnEncapsulationMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnEncapsulationMappingMode.setStatus("current")


class _FrAtmIwfConnEncapsulationMappings_Type(Bits):
    """Custom type frAtmIwfConnEncapsulationMappings based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("bPdus", 3),
          ("bridged802dot6", 2),
          ("bridgedPdus", 1),
          ("none", 0),
          ("otherRouted", 6),
          ("q933q2931", 8),
          ("routedIp", 4),
          ("routedOsi", 5),
          ("x25Iso8202", 7))
    )

_FrAtmIwfConnEncapsulationMappings_Type.__name__ = "Bits"
_FrAtmIwfConnEncapsulationMappings_Object = MibTableColumn
frAtmIwfConnEncapsulationMappings = _FrAtmIwfConnEncapsulationMappings_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 7),
    _FrAtmIwfConnEncapsulationMappings_Type()
)
frAtmIwfConnEncapsulationMappings.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnEncapsulationMappings.setStatus("current")


class _FrAtmIwfConnFragAndReassEnabled_Type(Integer32):
    """Custom type frAtmIwfConnFragAndReassEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FrAtmIwfConnFragAndReassEnabled_Type.__name__ = "Integer32"
_FrAtmIwfConnFragAndReassEnabled_Object = MibTableColumn
frAtmIwfConnFragAndReassEnabled = _FrAtmIwfConnFragAndReassEnabled_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 8),
    _FrAtmIwfConnFragAndReassEnabled_Type()
)
frAtmIwfConnFragAndReassEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnFragAndReassEnabled.setStatus("current")


class _FrAtmIwfConnArpTranslationEnabled_Type(Integer32):
    """Custom type frAtmIwfConnArpTranslationEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FrAtmIwfConnArpTranslationEnabled_Type.__name__ = "Integer32"
_FrAtmIwfConnArpTranslationEnabled_Object = MibTableColumn
frAtmIwfConnArpTranslationEnabled = _FrAtmIwfConnArpTranslationEnabled_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 9),
    _FrAtmIwfConnArpTranslationEnabled_Type()
)
frAtmIwfConnArpTranslationEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frAtmIwfConnArpTranslationEnabled.setStatus("current")
_FrAtmIwfVclTable_Object = MibTable
frAtmIwfVclTable = _FrAtmIwfVclTable_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 5)
)
if mibBuilder.loadTexts:
    frAtmIwfVclTable.setStatus("current")
_FrAtmIwfVclEntry_Object = MibTableRow
frAtmIwfVclEntry = _FrAtmIwfVclEntry_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 5, 1)
)
if mibBuilder.loadTexts:
    frAtmIwfVclEntry.setStatus("current")


class _FrAtmIwfVclCrossConnectIdentifier_Type(Integer32):
    """Custom type frAtmIwfVclCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrAtmIwfVclCrossConnectIdentifier_Type.__name__ = "Integer32"
_FrAtmIwfVclCrossConnectIdentifier_Object = MibTableColumn
frAtmIwfVclCrossConnectIdentifier = _FrAtmIwfVclCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 86, 1, 5, 1, 1),
    _FrAtmIwfVclCrossConnectIdentifier_Type()
)
frAtmIwfVclCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIwfVclCrossConnectIdentifier.setStatus("current")
_FrAtmIwfTraps_ObjectIdentity = ObjectIdentity
frAtmIwfTraps = _FrAtmIwfTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 2)
)
_FrAtmIwfTrapsPrefix_ObjectIdentity = ObjectIdentity
frAtmIwfTrapsPrefix = _FrAtmIwfTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 2, 0)
)
_FrAtmIwfConformance_ObjectIdentity = ObjectIdentity
frAtmIwfConformance = _FrAtmIwfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 3)
)
_FrAtmIwfGroups_ObjectIdentity = ObjectIdentity
frAtmIwfGroups = _FrAtmIwfGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 3, 1)
)
_FrAtmIwfCompliances_ObjectIdentity = ObjectIdentity
frAtmIwfCompliances = _FrAtmIwfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 86, 3, 2)
)
atmVclEntry.registerAugmentions(
    ("FR-ATM-PVC-SERVICE-IWF-MIB",
     "frAtmIwfVclEntry")
)
frAtmIwfVclEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Managed Objects groups

frAtmIwfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 86, 3, 1, 1)
)
frAtmIwfBasicGroup.setObjects(
      *(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndexNext"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrLastChange"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmLastChange"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptor"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedFrameTranslate"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedFrames"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedAal5PduTranslate"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedSDUs"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCrcErrors"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnSarTimeOuts"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnRowStatus"))
)
if mibBuilder.loadTexts:
    frAtmIwfBasicGroup.setStatus("current")

frAtmIwfConnectionDescriptorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 86, 3, 1, 2)
)
frAtmIwfConnectionDescriptorGroup.setObjects(
      *(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndexNext"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDeToClpMappingMode"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnClpToDeMappingMode"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCongestionMappingMode"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappingMode"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappings"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFragAndReassEnabled"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnArpTranslationEnabled"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDescriptorRowStatus"))
)
if mibBuilder.loadTexts:
    frAtmIwfConnectionDescriptorGroup.setStatus("current")

frAtmIwfAtmVclTableAugmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 86, 3, 1, 3)
)
frAtmIwfAtmVclTableAugmentGroup.setObjects(
    ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclCrossConnectIdentifier")
)
if mibBuilder.loadTexts:
    frAtmIwfAtmVclTableAugmentGroup.setStatus("current")


# Notification objects

frAtmIwfConnStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 86, 2, 0, 1)
)
frAtmIwfConnStatusChange.setObjects(
      *(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"),
        ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"))
)
if mibBuilder.loadTexts:
    frAtmIwfConnStatusChange.setStatus(
        "current"
    )


# Notifications groups

frAtmIwfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 86, 3, 1, 4)
)
frAtmIwfNotificationsGroup.setObjects(
    ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnStatusChange")
)
if mibBuilder.loadTexts:
    frAtmIwfNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

frAtmIwfEquipmentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 86, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmIwfEquipmentCompliance.setStatus(
        "current"
    )

frAtmIwfServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 86, 3, 2, 2)
)
if mibBuilder.loadTexts:
    frAtmIwfServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FR-ATM-PVC-SERVICE-IWF-MIB",
    **{"frAtmIwfMIB": frAtmIwfMIB,
       "frAtmIwfMIBObjects": frAtmIwfMIBObjects,
       "frAtmIwfConnIndexNext": frAtmIwfConnIndexNext,
       "frAtmIwfConnectionTable": frAtmIwfConnectionTable,
       "frAtmIwfConnectionEntry": frAtmIwfConnectionEntry,
       "frAtmIwfConnIndex": frAtmIwfConnIndex,
       "frAtmIwfConnAtmPort": frAtmIwfConnAtmPort,
       "frAtmIwfConnVpi": frAtmIwfConnVpi,
       "frAtmIwfConnVci": frAtmIwfConnVci,
       "frAtmIwfConnFrPort": frAtmIwfConnFrPort,
       "frAtmIwfConnDlci": frAtmIwfConnDlci,
       "frAtmIwfConnRowStatus": frAtmIwfConnRowStatus,
       "frAtmIwfConnAdminStatus": frAtmIwfConnAdminStatus,
       "frAtmIwfConnAtm2FrOperStatus": frAtmIwfConnAtm2FrOperStatus,
       "frAtmIwfConnAtm2FrLastChange": frAtmIwfConnAtm2FrLastChange,
       "frAtmIwfConnFr2AtmOperStatus": frAtmIwfConnFr2AtmOperStatus,
       "frAtmIwfConnFr2AtmLastChange": frAtmIwfConnFr2AtmLastChange,
       "frAtmIwfConnectionDescriptor": frAtmIwfConnectionDescriptor,
       "frAtmIwfConnFailedFrameTranslate": frAtmIwfConnFailedFrameTranslate,
       "frAtmIwfConnOverSizedFrames": frAtmIwfConnOverSizedFrames,
       "frAtmIwfConnFailedAal5PduTranslate": frAtmIwfConnFailedAal5PduTranslate,
       "frAtmIwfConnOverSizedSDUs": frAtmIwfConnOverSizedSDUs,
       "frAtmIwfConnCrcErrors": frAtmIwfConnCrcErrors,
       "frAtmIwfConnSarTimeOuts": frAtmIwfConnSarTimeOuts,
       "frAtmIwfConnectionDescriptorIndexNext": frAtmIwfConnectionDescriptorIndexNext,
       "frAtmIwfConnectionDescriptorTable": frAtmIwfConnectionDescriptorTable,
       "frAtmIwfConnectionDescriptorEntry": frAtmIwfConnectionDescriptorEntry,
       "frAtmIwfConnectionDescriptorIndex": frAtmIwfConnectionDescriptorIndex,
       "frAtmIwfConnDescriptorRowStatus": frAtmIwfConnDescriptorRowStatus,
       "frAtmIwfConnDeToClpMappingMode": frAtmIwfConnDeToClpMappingMode,
       "frAtmIwfConnClpToDeMappingMode": frAtmIwfConnClpToDeMappingMode,
       "frAtmIwfConnCongestionMappingMode": frAtmIwfConnCongestionMappingMode,
       "frAtmIwfConnEncapsulationMappingMode": frAtmIwfConnEncapsulationMappingMode,
       "frAtmIwfConnEncapsulationMappings": frAtmIwfConnEncapsulationMappings,
       "frAtmIwfConnFragAndReassEnabled": frAtmIwfConnFragAndReassEnabled,
       "frAtmIwfConnArpTranslationEnabled": frAtmIwfConnArpTranslationEnabled,
       "frAtmIwfVclTable": frAtmIwfVclTable,
       "frAtmIwfVclEntry": frAtmIwfVclEntry,
       "frAtmIwfVclCrossConnectIdentifier": frAtmIwfVclCrossConnectIdentifier,
       "frAtmIwfTraps": frAtmIwfTraps,
       "frAtmIwfTrapsPrefix": frAtmIwfTrapsPrefix,
       "frAtmIwfConnStatusChange": frAtmIwfConnStatusChange,
       "frAtmIwfConformance": frAtmIwfConformance,
       "frAtmIwfGroups": frAtmIwfGroups,
       "frAtmIwfBasicGroup": frAtmIwfBasicGroup,
       "frAtmIwfConnectionDescriptorGroup": frAtmIwfConnectionDescriptorGroup,
       "frAtmIwfAtmVclTableAugmentGroup": frAtmIwfAtmVclTableAugmentGroup,
       "frAtmIwfNotificationsGroup": frAtmIwfNotificationsGroup,
       "frAtmIwfCompliances": frAtmIwfCompliances,
       "frAtmIwfEquipmentCompliance": frAtmIwfEquipmentCompliance,
       "frAtmIwfServiceCompliance": frAtmIwfServiceCompliance}
)
