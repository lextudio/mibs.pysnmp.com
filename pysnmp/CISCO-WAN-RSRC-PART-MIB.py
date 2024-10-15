# SNMP MIB module (CISCO-WAN-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-RSRC-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWANRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125)
)
ciscoWANRsrcPartMIB.setRevisions(
        ("2002-09-14 00:00",
         "2002-03-06 00:00",
         "1999-10-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWANRsrcPartMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWANRsrcPartMIBObjects = _CiscoWANRsrcPartMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1)
)
_CwRsrcPartConfGrp_ObjectIdentity = ObjectIdentity
cwRsrcPartConfGrp = _CwRsrcPartConfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1)
)
_CwRsrcPartConfTable_Object = MibTable
cwRsrcPartConfTable = _CwRsrcPartConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwRsrcPartConfTable.setStatus("current")
_CwRsrcPartConfEntry_Object = MibTableRow
cwRsrcPartConfEntry = _CwRsrcPartConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1)
)
cwRsrcPartConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartID"),
)
if mibBuilder.loadTexts:
    cwRsrcPartConfEntry.setStatus("current")


class _CwRsrcPartID_Type(Unsigned32):
    """Custom type cwRsrcPartID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwRsrcPartID_Type.__name__ = "Unsigned32"
_CwRsrcPartID_Object = MibTableColumn
cwRsrcPartID = _CwRsrcPartID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 1),
    _CwRsrcPartID_Type()
)
cwRsrcPartID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwRsrcPartID.setStatus("current")


class _CwRsrcPartController_Type(Unsigned32):
    """Custom type cwRsrcPartController based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwRsrcPartController_Type.__name__ = "Unsigned32"
_CwRsrcPartController_Object = MibTableColumn
cwRsrcPartController = _CwRsrcPartController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 2),
    _CwRsrcPartController_Type()
)
cwRsrcPartController.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartController.setStatus("current")


class _CwRsrcPartEgrGuarPctBwConf_Type(Unsigned32):
    """Custom type cwRsrcPartEgrGuarPctBwConf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartEgrGuarPctBwConf_Type.__name__ = "Unsigned32"
_CwRsrcPartEgrGuarPctBwConf_Object = MibTableColumn
cwRsrcPartEgrGuarPctBwConf = _CwRsrcPartEgrGuarPctBwConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 3),
    _CwRsrcPartEgrGuarPctBwConf_Type()
)
cwRsrcPartEgrGuarPctBwConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartEgrGuarPctBwConf.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartEgrGuarPctBwConf.setUnits("0.0001 percentage")


class _CwRsrcPartEgrMaxPctBwConf_Type(Unsigned32):
    """Custom type cwRsrcPartEgrMaxPctBwConf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartEgrMaxPctBwConf_Type.__name__ = "Unsigned32"
_CwRsrcPartEgrMaxPctBwConf_Object = MibTableColumn
cwRsrcPartEgrMaxPctBwConf = _CwRsrcPartEgrMaxPctBwConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 4),
    _CwRsrcPartEgrMaxPctBwConf_Type()
)
cwRsrcPartEgrMaxPctBwConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartEgrMaxPctBwConf.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartEgrMaxPctBwConf.setUnits("0.0001 percentage")


class _CwRsrcPartIngGuarPctBwConf_Type(Unsigned32):
    """Custom type cwRsrcPartIngGuarPctBwConf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartIngGuarPctBwConf_Type.__name__ = "Unsigned32"
_CwRsrcPartIngGuarPctBwConf_Object = MibTableColumn
cwRsrcPartIngGuarPctBwConf = _CwRsrcPartIngGuarPctBwConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 5),
    _CwRsrcPartIngGuarPctBwConf_Type()
)
cwRsrcPartIngGuarPctBwConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartIngGuarPctBwConf.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIngGuarPctBwConf.setUnits("0.0001 percentage")


class _CwRsrcPartIngMaxPctBwConf_Type(Unsigned32):
    """Custom type cwRsrcPartIngMaxPctBwConf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartIngMaxPctBwConf_Type.__name__ = "Unsigned32"
_CwRsrcPartIngMaxPctBwConf_Object = MibTableColumn
cwRsrcPartIngMaxPctBwConf = _CwRsrcPartIngMaxPctBwConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 6),
    _CwRsrcPartIngMaxPctBwConf_Type()
)
cwRsrcPartIngMaxPctBwConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartIngMaxPctBwConf.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIngMaxPctBwConf.setUnits("0.0001 percentage")


class _CwRsrcPartEgrPctBwUsed_Type(Unsigned32):
    """Custom type cwRsrcPartEgrPctBwUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartEgrPctBwUsed_Type.__name__ = "Unsigned32"
_CwRsrcPartEgrPctBwUsed_Object = MibTableColumn
cwRsrcPartEgrPctBwUsed = _CwRsrcPartEgrPctBwUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 7),
    _CwRsrcPartEgrPctBwUsed_Type()
)
cwRsrcPartEgrPctBwUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartEgrPctBwUsed.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartEgrPctBwUsed.setUnits("0.0001 percentage")


class _CwRsrcPartIngPctBwUsed_Type(Unsigned32):
    """Custom type cwRsrcPartIngPctBwUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartIngPctBwUsed_Type.__name__ = "Unsigned32"
_CwRsrcPartIngPctBwUsed_Object = MibTableColumn
cwRsrcPartIngPctBwUsed = _CwRsrcPartIngPctBwUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 8),
    _CwRsrcPartIngPctBwUsed_Type()
)
cwRsrcPartIngPctBwUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartIngPctBwUsed.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIngPctBwUsed.setUnits("0.0001 percentage")


class _CwRsrcPartEgrPctBwAvail_Type(Unsigned32):
    """Custom type cwRsrcPartEgrPctBwAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartEgrPctBwAvail_Type.__name__ = "Unsigned32"
_CwRsrcPartEgrPctBwAvail_Object = MibTableColumn
cwRsrcPartEgrPctBwAvail = _CwRsrcPartEgrPctBwAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 9),
    _CwRsrcPartEgrPctBwAvail_Type()
)
cwRsrcPartEgrPctBwAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartEgrPctBwAvail.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartEgrPctBwAvail.setUnits("0.0001 percentage")


class _CwRsrcPartIngPctBwAvail_Type(Unsigned32):
    """Custom type cwRsrcPartIngPctBwAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwRsrcPartIngPctBwAvail_Type.__name__ = "Unsigned32"
_CwRsrcPartIngPctBwAvail_Object = MibTableColumn
cwRsrcPartIngPctBwAvail = _CwRsrcPartIngPctBwAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 10),
    _CwRsrcPartIngPctBwAvail_Type()
)
cwRsrcPartIngPctBwAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartIngPctBwAvail.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIngPctBwAvail.setUnits("0.0001 percentage")


class _CwRsrcPartVpiLo_Type(Unsigned32):
    """Custom type cwRsrcPartVpiLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwRsrcPartVpiLo_Type.__name__ = "Unsigned32"
_CwRsrcPartVpiLo_Object = MibTableColumn
cwRsrcPartVpiLo = _CwRsrcPartVpiLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 11),
    _CwRsrcPartVpiLo_Type()
)
cwRsrcPartVpiLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartVpiLo.setStatus("current")


class _CwRsrcPartVpiHigh_Type(Unsigned32):
    """Custom type cwRsrcPartVpiHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwRsrcPartVpiHigh_Type.__name__ = "Unsigned32"
_CwRsrcPartVpiHigh_Object = MibTableColumn
cwRsrcPartVpiHigh = _CwRsrcPartVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 12),
    _CwRsrcPartVpiHigh_Type()
)
cwRsrcPartVpiHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartVpiHigh.setStatus("current")


class _CwRsrcPartVciLo_Type(Unsigned32):
    """Custom type cwRsrcPartVciLo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwRsrcPartVciLo_Type.__name__ = "Unsigned32"
_CwRsrcPartVciLo_Object = MibTableColumn
cwRsrcPartVciLo = _CwRsrcPartVciLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 13),
    _CwRsrcPartVciLo_Type()
)
cwRsrcPartVciLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartVciLo.setStatus("current")


class _CwRsrcPartVciHigh_Type(Unsigned32):
    """Custom type cwRsrcPartVciHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwRsrcPartVciHigh_Type.__name__ = "Unsigned32"
_CwRsrcPartVciHigh_Object = MibTableColumn
cwRsrcPartVciHigh = _CwRsrcPartVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 14),
    _CwRsrcPartVciHigh_Type()
)
cwRsrcPartVciHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartVciHigh.setStatus("current")


class _CwRsrcPartGuarCon_Type(Unsigned32):
    """Custom type cwRsrcPartGuarCon based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_CwRsrcPartGuarCon_Type.__name__ = "Unsigned32"
_CwRsrcPartGuarCon_Object = MibTableColumn
cwRsrcPartGuarCon = _CwRsrcPartGuarCon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 15),
    _CwRsrcPartGuarCon_Type()
)
cwRsrcPartGuarCon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartGuarCon.setStatus("current")


class _CwRsrcPartMaxCon_Type(Unsigned32):
    """Custom type cwRsrcPartMaxCon based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_CwRsrcPartMaxCon_Type.__name__ = "Unsigned32"
_CwRsrcPartMaxCon_Object = MibTableColumn
cwRsrcPartMaxCon = _CwRsrcPartMaxCon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 16),
    _CwRsrcPartMaxCon_Type()
)
cwRsrcPartMaxCon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartMaxCon.setStatus("current")


class _CwRsrcPartUsedCon_Type(Unsigned32):
    """Custom type cwRsrcPartUsedCon based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_CwRsrcPartUsedCon_Type.__name__ = "Unsigned32"
_CwRsrcPartUsedCon_Object = MibTableColumn
cwRsrcPartUsedCon = _CwRsrcPartUsedCon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 17),
    _CwRsrcPartUsedCon_Type()
)
cwRsrcPartUsedCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartUsedCon.setStatus("current")


class _CwRsrcPartAvailCon_Type(Unsigned32):
    """Custom type cwRsrcPartAvailCon based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_CwRsrcPartAvailCon_Type.__name__ = "Unsigned32"
_CwRsrcPartAvailCon_Object = MibTableColumn
cwRsrcPartAvailCon = _CwRsrcPartAvailCon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 18),
    _CwRsrcPartAvailCon_Type()
)
cwRsrcPartAvailCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwRsrcPartAvailCon.setStatus("current")
_CwRsrcPartRowStatus_Type = RowStatus
_CwRsrcPartRowStatus_Object = MibTableColumn
cwRsrcPartRowStatus = _CwRsrcPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 1, 1, 19),
    _CwRsrcPartRowStatus_Type()
)
cwRsrcPartRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartRowStatus.setStatus("current")
_CwRsrcPartIlmiTable_Object = MibTable
cwRsrcPartIlmiTable = _CwRsrcPartIlmiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwRsrcPartIlmiTable.setStatus("current")
_CwRsrcPartIlmiEntry_Object = MibTableRow
cwRsrcPartIlmiEntry = _CwRsrcPartIlmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1)
)
cwRsrcPartIlmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartID"),
)
if mibBuilder.loadTexts:
    cwRsrcPartIlmiEntry.setStatus("current")


class _CwRsrcPartIlmiEnabled_Type(TruthValue):
    """Custom type cwRsrcPartIlmiEnabled based on TruthValue"""


_CwRsrcPartIlmiEnabled_Object = MibTableColumn
cwRsrcPartIlmiEnabled = _CwRsrcPartIlmiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 1),
    _CwRsrcPartIlmiEnabled_Type()
)
cwRsrcPartIlmiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiEnabled.setStatus("current")


class _CwRsrcPartSignallingVpi_Type(Integer32):
    """Custom type cwRsrcPartSignallingVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwRsrcPartSignallingVpi_Type.__name__ = "Integer32"
_CwRsrcPartSignallingVpi_Object = MibTableColumn
cwRsrcPartSignallingVpi = _CwRsrcPartSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 2),
    _CwRsrcPartSignallingVpi_Type()
)
cwRsrcPartSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartSignallingVpi.setStatus("current")


class _CwRsrcPartSignallingVci_Type(Integer32):
    """Custom type cwRsrcPartSignallingVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwRsrcPartSignallingVci_Type.__name__ = "Integer32"
_CwRsrcPartSignallingVci_Object = MibTableColumn
cwRsrcPartSignallingVci = _CwRsrcPartSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 3),
    _CwRsrcPartSignallingVci_Type()
)
cwRsrcPartSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartSignallingVci.setStatus("current")
_CwRsrcPartIlmiTrapEnable_Type = TruthValue
_CwRsrcPartIlmiTrapEnable_Object = MibTableColumn
cwRsrcPartIlmiTrapEnable = _CwRsrcPartIlmiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 4),
    _CwRsrcPartIlmiTrapEnable_Type()
)
cwRsrcPartIlmiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiTrapEnable.setStatus("current")


class _CwRsrcPartIlmiEstablishConPollIntvl_Type(Unsigned32):
    """Custom type cwRsrcPartIlmiEstablishConPollIntvl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CwRsrcPartIlmiEstablishConPollIntvl_Type.__name__ = "Unsigned32"
_CwRsrcPartIlmiEstablishConPollIntvl_Object = MibTableColumn
cwRsrcPartIlmiEstablishConPollIntvl = _CwRsrcPartIlmiEstablishConPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 5),
    _CwRsrcPartIlmiEstablishConPollIntvl_Type()
)
cwRsrcPartIlmiEstablishConPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiEstablishConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiEstablishConPollIntvl.setUnits("seconds")


class _CwRsrcPartIlmiCheckConPollIntvl_Type(Unsigned32):
    """Custom type cwRsrcPartIlmiCheckConPollIntvl based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwRsrcPartIlmiCheckConPollIntvl_Type.__name__ = "Unsigned32"
_CwRsrcPartIlmiCheckConPollIntvl_Object = MibTableColumn
cwRsrcPartIlmiCheckConPollIntvl = _CwRsrcPartIlmiCheckConPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 6),
    _CwRsrcPartIlmiCheckConPollIntvl_Type()
)
cwRsrcPartIlmiCheckConPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiCheckConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiCheckConPollIntvl.setUnits("seconds")


class _CwRsrcPartIlmiConPollInactFactor_Type(Unsigned32):
    """Custom type cwRsrcPartIlmiConPollInactFactor based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwRsrcPartIlmiConPollInactFactor_Type.__name__ = "Unsigned32"
_CwRsrcPartIlmiConPollInactFactor_Object = MibTableColumn
cwRsrcPartIlmiConPollInactFactor = _CwRsrcPartIlmiConPollInactFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 2, 1, 7),
    _CwRsrcPartIlmiConPollInactFactor_Type()
)
cwRsrcPartIlmiConPollInactFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwRsrcPartIlmiConPollInactFactor.setStatus("current")
_CwRsrcPartCtlrConfTable_Object = MibTable
cwRsrcPartCtlrConfTable = _CwRsrcPartCtlrConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cwRsrcPartCtlrConfTable.setStatus("current")
_CwRsrcPartCtlrConfEntry_Object = MibTableRow
cwRsrcPartCtlrConfEntry = _CwRsrcPartCtlrConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 3, 1)
)
cwRsrcPartCtlrConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartID"),
    (0, "CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartCtlrController"),
)
if mibBuilder.loadTexts:
    cwRsrcPartCtlrConfEntry.setStatus("current")


class _CwRsrcPartCtlrController_Type(Unsigned32):
    """Custom type cwRsrcPartCtlrController based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CwRsrcPartCtlrController_Type.__name__ = "Unsigned32"
_CwRsrcPartCtlrController_Object = MibTableColumn
cwRsrcPartCtlrController = _CwRsrcPartCtlrController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 3, 1, 1),
    _CwRsrcPartCtlrController_Type()
)
cwRsrcPartCtlrController.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwRsrcPartCtlrController.setStatus("current")
_CwRsrcPartCtlrRowStatus_Type = RowStatus
_CwRsrcPartCtlrRowStatus_Object = MibTableColumn
cwRsrcPartCtlrRowStatus = _CwRsrcPartCtlrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 1, 3, 1, 2),
    _CwRsrcPartCtlrRowStatus_Type()
)
cwRsrcPartCtlrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcPartCtlrRowStatus.setStatus("current")
_CwRsrcSvcAggrGrp_ObjectIdentity = ObjectIdentity
cwRsrcSvcAggrGrp = _CwRsrcSvcAggrGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2)
)
_CwRsrcSvcAggregateTable_Object = MibTable
cwRsrcSvcAggregateTable = _CwRsrcSvcAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwRsrcSvcAggregateTable.setStatus("current")
_CwRsrcSvcAggregateEntry_Object = MibTableRow
cwRsrcSvcAggregateEntry = _CwRsrcSvcAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1)
)
cwRsrcSvcAggregateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartID"),
)
if mibBuilder.loadTexts:
    cwRsrcSvcAggregateEntry.setStatus("current")


class _CwRsrcSvcAggrVpiLow_Type(Unsigned32):
    """Custom type cwRsrcSvcAggrVpiLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwRsrcSvcAggrVpiLow_Type.__name__ = "Unsigned32"
_CwRsrcSvcAggrVpiLow_Object = MibTableColumn
cwRsrcSvcAggrVpiLow = _CwRsrcSvcAggrVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 1),
    _CwRsrcSvcAggrVpiLow_Type()
)
cwRsrcSvcAggrVpiLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrVpiLow.setStatus("current")


class _CwRsrcSvcAggrVpiHigh_Type(Unsigned32):
    """Custom type cwRsrcSvcAggrVpiHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwRsrcSvcAggrVpiHigh_Type.__name__ = "Unsigned32"
_CwRsrcSvcAggrVpiHigh_Object = MibTableColumn
cwRsrcSvcAggrVpiHigh = _CwRsrcSvcAggrVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 2),
    _CwRsrcSvcAggrVpiHigh_Type()
)
cwRsrcSvcAggrVpiHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrVpiHigh.setStatus("current")


class _CwRsrcSvcAggrEgrPctBw_Type(Integer32):
    """Custom type cwRsrcSvcAggrEgrPctBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwRsrcSvcAggrEgrPctBw_Type.__name__ = "Integer32"
_CwRsrcSvcAggrEgrPctBw_Object = MibTableColumn
cwRsrcSvcAggrEgrPctBw = _CwRsrcSvcAggrEgrPctBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 3),
    _CwRsrcSvcAggrEgrPctBw_Type()
)
cwRsrcSvcAggrEgrPctBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrEgrPctBw.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrEgrPctBw.setUnits("percent")


class _CwRsrcSvcAggrIngPctBw_Type(Integer32):
    """Custom type cwRsrcSvcAggrIngPctBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwRsrcSvcAggrIngPctBw_Type.__name__ = "Integer32"
_CwRsrcSvcAggrIngPctBw_Object = MibTableColumn
cwRsrcSvcAggrIngPctBw = _CwRsrcSvcAggrIngPctBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 4),
    _CwRsrcSvcAggrIngPctBw_Type()
)
cwRsrcSvcAggrIngPctBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrIngPctBw.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrIngPctBw.setUnits("percent")


class _CwRsrcSvcAggrChanVADTolerance_Type(Integer32):
    """Custom type cwRsrcSvcAggrChanVADTolerance based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CwRsrcSvcAggrChanVADTolerance_Type.__name__ = "Integer32"
_CwRsrcSvcAggrChanVADTolerance_Object = MibTableColumn
cwRsrcSvcAggrChanVADTolerance = _CwRsrcSvcAggrChanVADTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 5),
    _CwRsrcSvcAggrChanVADTolerance_Type()
)
cwRsrcSvcAggrChanVADTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrChanVADTolerance.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrChanVADTolerance.setUnits("0.0001")


class _CwRsrcSvcAggrChanVADDutyCycle_Type(Integer32):
    """Custom type cwRsrcSvcAggrChanVADDutyCycle based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CwRsrcSvcAggrChanVADDutyCycle_Type.__name__ = "Integer32"
_CwRsrcSvcAggrChanVADDutyCycle_Object = MibTableColumn
cwRsrcSvcAggrChanVADDutyCycle = _CwRsrcSvcAggrChanVADDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 6),
    _CwRsrcSvcAggrChanVADDutyCycle_Type()
)
cwRsrcSvcAggrChanVADDutyCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrChanVADDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrChanVADDutyCycle.setUnits("0.01")
_CwRsrcSvcAggrRowStatus_Type = RowStatus
_CwRsrcSvcAggrRowStatus_Object = MibTableColumn
cwRsrcSvcAggrRowStatus = _CwRsrcSvcAggrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 1, 2, 1, 1, 7),
    _CwRsrcSvcAggrRowStatus_Type()
)
cwRsrcSvcAggrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwRsrcSvcAggrRowStatus.setStatus("current")
_CwRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
cwRsrcPartMIBConformance = _CwRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3)
)
_CwRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
cwRsrcPartMIBCompliances = _CwRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 1)
)
_CwRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
cwRsrcPartMIBGroups = _CwRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 2)
)

# Managed Objects groups

cwRsrcPartMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 2, 1)
)
cwRsrcPartMIBGroup.setObjects(
      *(("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartController"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartEgrGuarPctBwConf"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartEgrMaxPctBwConf"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIngGuarPctBwConf"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIngMaxPctBwConf"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartEgrPctBwAvail"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIngPctBwAvail"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartEgrPctBwUsed"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIngPctBwUsed"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartVpiLo"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartVpiHigh"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartVciLo"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartVciHigh"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartGuarCon"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartMaxCon"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartUsedCon"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartAvailCon"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartRowStatus"))
)
if mibBuilder.loadTexts:
    cwRsrcPartMIBGroup.setStatus("current")

cwRsrcPartIlmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 2, 2)
)
cwRsrcPartIlmiMIBGroup.setObjects(
      *(("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIlmiEnabled"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartSignallingVpi"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartSignallingVci"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIlmiTrapEnable"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIlmiEstablishConPollIntvl"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIlmiCheckConPollIntvl"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartIlmiConPollInactFactor"))
)
if mibBuilder.loadTexts:
    cwRsrcPartIlmiMIBGroup.setStatus("current")

cwRsrcPartMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 2, 3)
)
cwRsrcPartMappingGroup.setObjects(
    ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcPartCtlrRowStatus")
)
if mibBuilder.loadTexts:
    cwRsrcPartMappingGroup.setStatus("current")

cwRsrcSvcAggrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 2, 4)
)
cwRsrcSvcAggrGroup.setObjects(
      *(("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrVpiLow"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrVpiHigh"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrEgrPctBw"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrIngPctBw"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrChanVADTolerance"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrChanVADDutyCycle"),
        ("CISCO-WAN-RSRC-PART-MIB", "cwRsrcSvcAggrRowStatus"))
)
if mibBuilder.loadTexts:
    cwRsrcSvcAggrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwRsrcPartMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwRsrcPartMIBCompliance.setStatus(
        "deprecated"
    )

cwRsrcPartMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 125, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cwRsrcPartMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-RSRC-PART-MIB",
    **{"ciscoWANRsrcPartMIB": ciscoWANRsrcPartMIB,
       "ciscoWANRsrcPartMIBObjects": ciscoWANRsrcPartMIBObjects,
       "cwRsrcPartConfGrp": cwRsrcPartConfGrp,
       "cwRsrcPartConfTable": cwRsrcPartConfTable,
       "cwRsrcPartConfEntry": cwRsrcPartConfEntry,
       "cwRsrcPartID": cwRsrcPartID,
       "cwRsrcPartController": cwRsrcPartController,
       "cwRsrcPartEgrGuarPctBwConf": cwRsrcPartEgrGuarPctBwConf,
       "cwRsrcPartEgrMaxPctBwConf": cwRsrcPartEgrMaxPctBwConf,
       "cwRsrcPartIngGuarPctBwConf": cwRsrcPartIngGuarPctBwConf,
       "cwRsrcPartIngMaxPctBwConf": cwRsrcPartIngMaxPctBwConf,
       "cwRsrcPartEgrPctBwUsed": cwRsrcPartEgrPctBwUsed,
       "cwRsrcPartIngPctBwUsed": cwRsrcPartIngPctBwUsed,
       "cwRsrcPartEgrPctBwAvail": cwRsrcPartEgrPctBwAvail,
       "cwRsrcPartIngPctBwAvail": cwRsrcPartIngPctBwAvail,
       "cwRsrcPartVpiLo": cwRsrcPartVpiLo,
       "cwRsrcPartVpiHigh": cwRsrcPartVpiHigh,
       "cwRsrcPartVciLo": cwRsrcPartVciLo,
       "cwRsrcPartVciHigh": cwRsrcPartVciHigh,
       "cwRsrcPartGuarCon": cwRsrcPartGuarCon,
       "cwRsrcPartMaxCon": cwRsrcPartMaxCon,
       "cwRsrcPartUsedCon": cwRsrcPartUsedCon,
       "cwRsrcPartAvailCon": cwRsrcPartAvailCon,
       "cwRsrcPartRowStatus": cwRsrcPartRowStatus,
       "cwRsrcPartIlmiTable": cwRsrcPartIlmiTable,
       "cwRsrcPartIlmiEntry": cwRsrcPartIlmiEntry,
       "cwRsrcPartIlmiEnabled": cwRsrcPartIlmiEnabled,
       "cwRsrcPartSignallingVpi": cwRsrcPartSignallingVpi,
       "cwRsrcPartSignallingVci": cwRsrcPartSignallingVci,
       "cwRsrcPartIlmiTrapEnable": cwRsrcPartIlmiTrapEnable,
       "cwRsrcPartIlmiEstablishConPollIntvl": cwRsrcPartIlmiEstablishConPollIntvl,
       "cwRsrcPartIlmiCheckConPollIntvl": cwRsrcPartIlmiCheckConPollIntvl,
       "cwRsrcPartIlmiConPollInactFactor": cwRsrcPartIlmiConPollInactFactor,
       "cwRsrcPartCtlrConfTable": cwRsrcPartCtlrConfTable,
       "cwRsrcPartCtlrConfEntry": cwRsrcPartCtlrConfEntry,
       "cwRsrcPartCtlrController": cwRsrcPartCtlrController,
       "cwRsrcPartCtlrRowStatus": cwRsrcPartCtlrRowStatus,
       "cwRsrcSvcAggrGrp": cwRsrcSvcAggrGrp,
       "cwRsrcSvcAggregateTable": cwRsrcSvcAggregateTable,
       "cwRsrcSvcAggregateEntry": cwRsrcSvcAggregateEntry,
       "cwRsrcSvcAggrVpiLow": cwRsrcSvcAggrVpiLow,
       "cwRsrcSvcAggrVpiHigh": cwRsrcSvcAggrVpiHigh,
       "cwRsrcSvcAggrEgrPctBw": cwRsrcSvcAggrEgrPctBw,
       "cwRsrcSvcAggrIngPctBw": cwRsrcSvcAggrIngPctBw,
       "cwRsrcSvcAggrChanVADTolerance": cwRsrcSvcAggrChanVADTolerance,
       "cwRsrcSvcAggrChanVADDutyCycle": cwRsrcSvcAggrChanVADDutyCycle,
       "cwRsrcSvcAggrRowStatus": cwRsrcSvcAggrRowStatus,
       "cwRsrcPartMIBConformance": cwRsrcPartMIBConformance,
       "cwRsrcPartMIBCompliances": cwRsrcPartMIBCompliances,
       "cwRsrcPartMIBCompliance": cwRsrcPartMIBCompliance,
       "cwRsrcPartMIBComplianceRev1": cwRsrcPartMIBComplianceRev1,
       "cwRsrcPartMIBGroups": cwRsrcPartMIBGroups,
       "cwRsrcPartMIBGroup": cwRsrcPartMIBGroup,
       "cwRsrcPartIlmiMIBGroup": cwRsrcPartIlmiMIBGroup,
       "cwRsrcPartMappingGroup": cwRsrcPartMappingGroup,
       "cwRsrcSvcAggrGroup": cwRsrcSvcAggrGroup}
)
